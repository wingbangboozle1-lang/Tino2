/*
  Black-swan / real-conditions scenario engine.

  Purpose: the eight-page dashboard carries one constant-rate planning line
  (3.5% home growth, 3% inflation). Real 50-year history is not constant, so this
  engine replays the *shape* of recorded stress episodes as explicit rate paths and
  re-runs the same three strategies (sell and reinvest, rent then sell, live then sell)
  through each path.

  Rules kept from the rest of the site:
    * every rate is a stated scenario assumption, never a forecast or an official figure;
    * historical anchors are cited to official sources on the page, separately from the assumptions;
    * no personal data, no parcel data, no inferred basis;
    * all displayed currency is rounded to the nearest $10 by MODEL.fmtMoney().

  Transfer year is the midpoint of the 2040-2050 window (2045) and the holding horizon
  is 10 years (to 2055), matching the decision page's default horizon.
*/
(function () {
  const M = window.MODEL;
  const B = M.BASE;
  const START = 2026;
  const INHERIT = 2045;
  const HORIZON = 10;
  const END = INHERIT + HORIZON;
  const PROP13_CAP = 0.02;

  function seg(list, year) {
    for (let i = 0; i < list.length; i += 1) {
      const s = list[i];
      if (year >= s[0] && year <= s[1]) return s[2];
    }
    return list[list.length - 1][2];
  }

  function paths(spec) {
    const p = { home: {}, cpi: {}, rent: {}, port: {}, ins: {} };
    for (let y = START; y <= END; y += 1) {
      p.home[y] = seg(spec.home, y);
      p.cpi[y] = seg(spec.cpi, y);
      p.rent[y] = seg(spec.rent, y);
      p.port[y] = seg(spec.port, y);
      p.ins[y] = seg(spec.ins, y);
    }
    return p;
  }

  function factor(rates, from, to) {
    let f = 1;
    for (let y = from + 1; y <= to; y += 1) f *= 1 + rates[y];
    return f;
  }

  function run(spec) {
    const p = paths(spec);
    const market = (y) => B.aValue * factor(p.home, START, y);
    // Prop 13 caps assessment growth at the lower of CPI and 2%.
    const assessedPre = {};
    assessedPre[START] = B.aAssessed;
    for (let y = START + 1; y <= END; y += 1) assessedPre[y] = assessedPre[y - 1] * (1 + Math.min(p.cpi[y], PROP13_CAP));

    const vAtInherit = market(INHERIT);
    const allowance = M.modelAllowance(INHERIT);
    const primaryStart = vAtInherit <= assessedPre[INHERIT] + allowance ? assessedPre[INHERIT] : vAtInherit - allowance;

    function assessedPath(start) {
      const out = {};
      out[INHERIT] = start;
      for (let y = INHERIT + 1; y <= END; y += 1) out[y] = out[y - 1] * (1 + Math.min(p.cpi[y], PROP13_CAP));
      return out;
    }

    const water = (y) => B.aWaterMonthly * 12 * factor(p.cpi, START, y);
    const insurance = (y) => B.aInsuranceAnnual * factor(p.ins, START, y);
    const rentAnnual = (y) => B.aRent4BR * 12 * factor(p.rent, START, y);

    function cash(year, assess, mode) {
      const mkt = market(year);
      const tax = assess[year] * B.aRate;
      const w = water(year);
      const ins = insurance(year);
      const solarCredit = B.aSolarMonthlyCredit * 12;
      const maintenance = mkt * B.maintenanceA;
      const operatingCost = tax + w + ins + maintenance - solarCredit;
      if (mode === "live") {
        return { year, market: mkt, assessed: assess[year], propertyTax: tax, water: w, insurance: ins, maintenance, grossRent: 0, noi: -operatingCost, incomeTax: 0, afterTax: -operatingCost };
      }
      const grossRent = rentAnnual(year);
      const collected = grossRent * (1 - B.vacancy);
      const noi = collected - collected * B.management - operatingCost;
      const incomeTax = Math.max(0, noi) * B.ordinaryTax;
      return { year, market: mkt, assessed: assess[year], propertyTax: tax, water: w, insurance: ins, maintenance, grossRent, noi, incomeTax, afterTax: noi - incomeTax };
    }

    function hold(mode) {
      const assess = assessedPath(mode === "live" ? primaryStart : vAtInherit);
      let reserve = 0;
      const rows = [];
      for (let y = INHERIT + 1; y <= END; y += 1) {
        const row = cash(y, assess, mode);
        reserve = reserve * (1 + p.port[y]) + row.afterTax;
        rows.push(row);
      }
      const finalMarket = market(END);
      const realized = finalMarket * (1 - B.saleCost);
      const gain = Math.max(0, realized - vAtInherit);
      const exclusion = mode === "live" ? Math.min(B.primaryGainExclusion, gain) : 0;
      const capitalGainsTax = Math.max(0, gain - exclusion) * B.capitalGainsTax;
      return {
        mode,
        terminal: reserve + realized - capitalGainsTax,
        reserve,
        finalMarket,
        realized,
        gain,
        exclusion,
        capitalGainsTax,
        rows,
        taxAtTransfer: assess[INHERIT] * B.aRate,
        firstRow: rows[0]
      };
    }

    // Live case with the housing service valued at the market rent the household would
    // otherwise pay. It is not cash: it is the avoided cost of equivalent housing.
    function liveHousingValue(holdResult) {
      const assess = assessedPath(primaryStart);
      let reserve = 0;
      for (let y = INHERIT + 1; y <= END; y += 1) {
        const row = cash(y, assess, "live");
        reserve = reserve * (1 + p.port[y]) + row.afterTax + rentAnnual(y);
      }
      return reserve + holdResult.realized - holdResult.capitalGainsTax;
    }

    const sellInitial = vAtInherit * (1 - B.saleCost);
    const sellTerminal = sellInitial * factor(p.port, INHERIT, END);
    const rent = hold("rent");
    const live = hold("live");
    const result = {
      id: spec.id,
      vAtInherit,
      allowance,
      assessedAtTransfer: assessedPre[INHERIT],
      primaryStart,
      fullTaxAtTransfer: vAtInherit * B.aRate,
      primaryTaxAtTransfer: primaryStart * B.aRate,
      sell: { mode: "sell", terminal: sellTerminal, initialNet: sellInitial, gain: 0, capitalGainsTax: 0 },
      rent,
      live,
      paths: p
    };
    live.housingAdjustedTerminal = liveHousingValue(live);
    const ranking = ["sell", "rent", "live"].sort((a, b) => result[b].terminal - result[a].terminal);
    result.winner = ranking[0];
    result.runnerUp = ranking[1];
    result.margin = result[ranking[0]].terminal - result[ranking[1]].terminal;
    return result;
  }

  /*
    Scenario register. `home`, `cpi`, `rent`, `port` and `ins` are annual rate paths
    in the form [firstYear, lastYear, rate]. `anchor` names the recorded episode that
    fixes the shape; `sources` are keys in site/data/sources.js.
  */
  const DEFS = [
    {
      id: "base",
      label: "Baseline planning case",
      shape: "Constant rates (the dashboard default)",
      anchor: "No episode is replayed. This is the arithmetic line the other cases are measured against.",
      sources: ["cboOutlook2026", "fedInflation", "investorRisk"],
      home: [[2026, END, 0.035]],
      cpi: [[2026, END, 0.03]],
      rent: [[2026, END, 0.03]],
      port: [[2026, END, 0.05]],
      ins: [[2026, END, 0.03]]
    },
    {
      id: "stagflation",
      label: "Stagflation replay",
      shape: "1973–82 shape: inflation 4.5% rising to 6.5%, home growth below inflation, portfolio return near zero in real terms",
      anchor: "CPI-U rose 11.0% (1974), 11.3% (1979), 13.5% (1980) and 10.3% (1981). The shape is replayed; the size is a design choice.",
      sources: ["blsCpiHistory", "boeProp13"],
      home: [[2026, 2030, 0.04], [2031, 2040, 0.045], [2041, END, 0.05]],
      cpi: [[2026, 2030, 0.045], [2031, 2035, 0.065], [2036, 2040, 0.05], [2041, END, 0.035]],
      rent: [[2026, END, 0.04]],
      port: [[2026, END, 0.02]],
      ins: [[2026, END, 0.055]]
    },
    {
      id: "gfc",
      label: "Great Recession replay at the transfer date",
      shape: "Home prices fall 5%, 9%, 7% and 4% in 2043–2046, then recover; equities −20% then −15%",
      anchor: "FHFA reported the national purchase-only index down 6.0% over the four quarters to 2008 Q3 and San Jose metro prices down 8.33% year over year. The 2043–2046 path here is a design choice of similar total depth.",
      sources: ["fhfaRelease2008", "fhfaHpi"],
      home: [[2026, 2042, 0.035], [2043, 2043, -0.05], [2044, 2044, -0.09], [2045, 2045, -0.07], [2046, 2046, -0.04], [2047, 2047, 0.01], [2048, END, 0.04]],
      cpi: [[2026, 2042, 0.03], [2043, 2043, 0.04], [2044, 2044, 0.01], [2045, 2045, -0.01], [2046, END, 0.03]],
      rent: [[2026, 2042, 0.03], [2043, 2043, 0.01], [2044, 2044, -0.02], [2045, 2045, -0.03], [2046, 2046, 0.01], [2047, END, 0.03]],
      port: [[2026, 2042, 0.05], [2043, 2043, -0.2], [2044, 2044, -0.15], [2045, 2046, 0.02], [2047, 2048, 0.1], [2049, END, 0.05]],
      ins: [[2026, END, 0.04]]
    },
    {
      id: "rateshock",
      label: "Rate and insurance shock at the transfer date",
      shape: "2045: home prices −6%, CPI 5%, equities −18%, premiums +5%; two years to recover",
      anchor: "CPI-U rose 8.0% in 2022, 4.1% in 2023 and 3.3% in the first half of 2026; the 30-year fixed stood at 2.98% in the week of 11 November 2021 and 7.18% in November 2026.",
      sources: ["blsCpiAnnual", "freddiePmms", "fairPlan"],
      home: [[2026, 2044, 0.035], [2045, 2045, -0.06], [2046, 2046, -0.03], [2047, 2047, 0.02], [2048, END, 0.035]],
      cpi: [[2026, 2044, 0.03], [2045, 2045, 0.05], [2046, 2046, 0.04], [2047, END, 0.03]],
      rent: [[2026, 2044, 0.03], [2045, 2045, 0.01], [2046, 2046, 0.02], [2047, END, 0.03]],
      port: [[2026, 2044, 0.05], [2045, 2045, -0.18], [2046, 2046, 0.04], [2047, END, 0.05]],
      ins: [[2026, END, 0.05]]
    },
    {
      id: "techbust",
      label: "Regional tech-cycle bust",
      shape: "2041–2043: home prices −8%, −7%, −2%; rents −4%, −5%, flat; local payrolls contract",
      anchor: "No official episode is replayed. The case tests what happens if regional employers contract while the household holds the property; rent levels come from the HUD benchmark.",
      sources: ["hudA", "fhfaHpi", "blsCpiAnnual"],
      home: [[2026, 2040, 0.04], [2041, 2041, -0.08], [2042, 2042, -0.07], [2043, 2043, -0.02], [2044, 2044, 0.02], [2045, END, 0.03]],
      cpi: [[2026, END, 0.028]],
      rent: [[2026, 2040, 0.03], [2041, 2041, -0.04], [2042, 2042, -0.05], [2043, 2043, 0], [2044, END, 0.03]],
      port: [[2026, 2040, 0.05], [2041, 2041, -0.15], [2042, 2042, -0.05], [2043, END, 0.05]],
      ins: [[2026, END, 0.035]]
    },
    {
      id: "insurance",
      label: "Insurance and climate repricing",
      shape: "Premiums +12% a year for ten years, then +7%; home growth 2.8%; CPI 3.2%",
      anchor: "California FAIR Plan exposure reached $773 billion at September 2026, 252% higher than September 2022, with 698,307 policies in force.",
      sources: ["fairPlan", "insurance"],
      home: [[2026, END, 0.028]],
      cpi: [[2026, END, 0.032]],
      rent: [[2026, END, 0.028]],
      port: [[2026, END, 0.05]],
      ins: [[2026, 2035, 0.12], [2036, END, 0.07]]
    },
    {
      id: "prolonged",
      label: "Lost decade (Japan-style)",
      shape: "Home growth 1% for 20 years, CPI 1.5%, rents 1%, portfolio 3%",
      anchor: "No official U.S. precedent is replayed here. This is a structure test for a 20-year nominal stagnation, not a forecast.",
      sources: ["cboOutlook2026", "investorRisk", "fedInflation"],
      home: [[2026, END, 0.01]],
      cpi: [[2026, END, 0.015]],
      rent: [[2026, END, 0.01]],
      port: [[2026, END, 0.03]],
      ins: [[2026, END, 0.035]]
    }
  ];

  function runAll(defs) {
    const out = (defs || DEFS).map((d) => ({ def: d, result: run(d) }));
    const baseSell = out[0].result.sell.terminal;
    out.forEach((o) => { o.delta = o.result.sell.terminal - baseSell; });
    return out;
  }

  /* Flat home-growth rate at which rent-then-sell catches sell-and-reinvest. */
  function breakEvenHomeGrowth(baseSpec) {
    let lo = -0.03;
    let hi = 0.15;
    for (let i = 0; i < 90; i += 1) {
      const mid = (lo + hi) / 2;
      const trial = { ...baseSpec, home: [[START, END, mid]] };
      const r = run(trial);
      if (r.rent.terminal > r.sell.terminal) hi = mid;
      else lo = mid;
    }
    return (lo + hi) / 2;
  }

  /* Flat after-tax portfolio return at which sell-and-reinvest stops winning. */
  function breakEvenPortfolioReturn(baseSpec) {
    let lo = 0.0;
    let hi = 0.15;
    for (let i = 0; i < 90; i += 1) {
      const mid = (lo + hi) / 2;
      const trial = { ...baseSpec, port: [[START, END, mid]] };
      const r = run(trial);
      if (r.rent.terminal < r.sell.terminal) hi = mid;
      else lo = mid;
    }
    return (lo + hi) / 2;
  }

  /* Premium-growth sensitivity: keep every other base path, change only insurance. */
  function insuranceShock(rate) {
    const spec = { ...DEFS[0], id: `ins-${rate}`, ins: [[START, END, rate]] };
    const r = run(spec);
    const base = run(DEFS[0]);
    return {
      rate,
      rentTerminal: r.rent.terminal,
      liveTerminal: r.live.terminal,
      sellTerminal: r.sell.terminal,
      rentDelta: r.rent.terminal - base.rent.terminal,
      liveDelta: r.live.terminal - base.live.terminal,
      firstYearPremium: r.rent.firstRow.insurance
    };
  }

  /* Uninsured damage at the transfer date: same absolute hit to every strategy. */
  function quakeShock(fraction) {
    const r = run(DEFS[0]);
    const loss = r.vAtInherit * fraction;
    const growth = factor(r.paths.port, INHERIT, END);
    const hit = loss * growth; // the part of the loss that would otherwise have compounded
    return {
      fraction,
      loss,
      hit,
      sellTerminal: r.sell.terminal - hit,
      rentTerminal: r.rent.terminal - hit,
      liveTerminal: r.live.terminal - hit
    };
  }

  function expectation(weights) {
    const rows = runAll();
    const w = weights || { base: 0.45, stagflation: 0.15, gfc: 0.1, rateshock: 0.1, techbust: 0.1, insurance: 0.05, prolonged: 0.05 };
    const total = Object.values(w).reduce((a, b) => a + b, 0);
    const acc = { sell: 0, rent: 0, live: 0 };
    rows.forEach((o) => {
      const weight = (w[o.def.id] || 0) / total;
      acc.sell += weight * o.result.sell.terminal;
      acc.rent += weight * o.result.rent.terminal;
      acc.live += weight * o.result.live.terminal;
    });
    return { weights: w, ...acc };
  }

  window.SCENARIOS = {
    START, INHERIT, END, HORIZON, DEFS, run, runAll, paths,
    breakEvenHomeGrowth, breakEvenPortfolioReturn, insuranceShock, quakeShock, expectation
  };
})();
