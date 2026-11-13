/* Decision model for the public guide.
   Every published amount is rounded to $10 by fmtMoney before display.
   No personal record is stored here: the two property values are rounded to
   $1,000 and every tax and cost figure is either a published official amount
   or a stated planning assumption (see docs/projections.md). */
(function (root) {
  'use strict';

  var BASE = {
    start: 2026,
    end: 2076,
    /* Property A: Cupertino home, anticipated trust inheritance. */
    a: {
      market: 3100000, assessed: 550000, rate: 0.01335,
      waterMonth: 130, electricMonth: -10, insuranceYear: 2200,
      insuranceGrowth: 0.038, maintenance: 0.0075, rentMonth: 6500,
      vacancy: 0.05, management: 0.08,
      landShare: 0.20
    },
    /* Property B: San Francisco three-unit building, already owned. */
    b: {
      market: 1800000, assessed: 116500, rate: 0.0118162182,
      rentTwo: 7150, rentThird: 2770, waterMonth: 360, electricMonth: 50,
      insuranceYear: 3600, maintenance: 0.0100, vacancy: 0.04,
      management: 0.05, landShare: 0.35, parcelFixed: 830, rentFee: 177
    },
    /* Economy. */
    inflation: 0.023, homeGrowth: 0.036, rentGrowth: 0.023,
    insuranceGrowth: 0.038, assessmentGrowth: 0.02, sfRentGrowth: 0.016,
    portfolio: 0.050, fee: 0.005,
    ordinaryTax: 0.30, capGainsTax: 0.28, recaptureTax: 0.25,
    saleCost: 0.06, exclusion: 250000, depreciationYears: 27.5,
    /* Official amounts. */
    prop19: 1044586, prop19Steps2026: 0,
    estate2026: 15000000, estate2027: 15480000, estateIndex: 0.023,
    hpiCA: 0.036, homeownersExemption: 7000
  };

  var A_LABEL = 'Property A · Cupertino home';
  var B_LABEL = 'Property B · San Francisco building';

  function round10(v) {
    if (v === null || v === undefined || !isFinite(v)) return null;
    return Math.sign(v) * Math.round(Math.abs(v) / 10) * 10;
  }
  function fmtMoney(v) {
    var r = round10(v);
    if (r === null) return '—';
    return (r < 0 ? '−' : '') + '$' + Math.abs(r).toLocaleString('en-US');
  }
  function fmtPct(v, dp) { return (v * 100).toFixed(dp === undefined ? 1 : dp) + '%'; }
  function fv(p, r, n) { return p * Math.pow(1 + r, n); }

  /* Evaluate an option at a transfer year and horizon. `cfg` overrides BASE. */
  function settings(cfg) {
    var c = {};
    for (var k in BASE) c[k] = BASE[k];
    c.a = Object.assign({}, BASE.a, (cfg && cfg.a) || {});
    c.b = Object.assign({}, BASE.b, (cfg && cfg.b) || {});
    for (var j in (cfg || {})) {
      if (j !== 'a' && j !== 'b') c[j] = cfg[j];
    }
    return c;
  }

  /* ---------- property series ---------- */
  function seriesA(c, year) {
    var n = year - c.start;
    var market = fv(c.a.market, c.homeGrowth, n);
    var factored = fv(c.a.assessed, c.assessmentGrowth, n);
    var assessed = Math.min(factored, market);
    return {
      year: year, market: market, factored: factored, assessed: assessed,
      tax: assessed * c.a.rate
    };
  }
  function seriesB(c, year) {
    var n = year - c.start;
    var market = fv(c.b.market, c.homeGrowth, n);
    var factored = fv(c.b.assessed, c.assessmentGrowth, n);
    var assessed = Math.min(factored, market);
    return {
      year: year, market: market, factored: factored, assessed: assessed,
      tax: assessed * c.b.rate + c.b.parcelFixed
    };
  }

  /* Proposition 19 allowance in force for a transfer in `year`.
     The $1,000,000 amount steps every second 16 February on one year of the
     FHFA California index. Later steps are a planning assumption. */
  function allowance(c, year, hpi) {
    var g = hpi === undefined ? c.hpiCA : hpi;
    var steps = Math.max(0, Math.floor((year - 2025) / 2));
    return c.prop19 * Math.pow(1 + g, steps);
  }

  /* Values at the date of transfer. */
  function transfer(c, year) {
    var pre = seriesA(c, year);
    var allow = allowance(c, year);
    var cap = pre.assessed + allow;
    var primary = Math.min(pre.market, pre.assessed + Math.max(0, pre.market - cap));
    return {
      year: year,
      market: pre.market,
      carryForward: pre.assessed,
      allowance: allow,
      cap: cap,
      primaryAssessed: primary,
      fullAssessed: pre.market,
      taxLive: primary * c.a.rate,
      taxRent: pre.market * c.a.rate,
      savingsYear1: (pre.market - primary) * c.a.rate
    };
  }

  /* Post-transfer assessed value for a holding option. */
  function assessedAfter(c, t, year, option) {
    var base = option === 'live' ? t.primaryAssessed : t.fullAssessed;
    var factored = fv(base, c.assessmentGrowth, year - t.year);
    return Math.min(factored, seriesA(c, year).market);
  }

  /* Annual operating figures for A while it is held. */
  function holdA(c, t, year, option) {
    var n = year - c.start;
    var market = seriesA(c, year).market;
    var assessed = assessedAfter(c, t, year, option);
    var propTax = assessed * c.a.rate;
    var hoex = option === 'live' ? c.homeownersExemption * c.a.rate : 0;
    var water = fv(c.a.waterMonth * 12, c.inflation, n);
    var electric = c.a.electricMonth * 12; /* solar credit held flat in real terms */
    var insurance = fv(c.a.insuranceYear, c.a.insuranceGrowth, n);
    var maintenance = market * c.a.maintenance;
    var opex = propTax - hoex + water + electric + insurance + maintenance;
    var out = {
      year: year, market: market, assessed: assessed, propTax: propTax,
      hoex: hoex, water: water, electric: electric, insurance: insurance,
      maintenance: maintenance, opex: opex,
      rent: 0, collected: 0, managementCost: 0, noi: -opex,
      depreciation: 0, taxable: 0, incomeTax: 0, afterTax: -opex
    };
    if (option === 'rent') {
      out.rent = fv(c.a.rentMonth * 12, c.rentGrowth, n);
      out.collected = out.rent * (1 - c.a.vacancy);
      out.managementCost = out.collected * c.a.management;
      out.noi = out.collected - out.managementCost - opex;
      out.depreciation = (t.market * (1 - c.a.landShare)) / c.depreciationYears;
      out.afterTax = out.noi;
    }
    return out;
  }

  /* Tax on a terminal sale. */
  function saleTax(c, option, buyPrice, sellPrice, accumulatedDep, excluded) {
    var gross = sellPrice * (1 - c.saleCost);
    var gain = Math.max(0, gross - buyPrice + accumulatedDep);
    if (option === 'rent') {
      var recapture = Math.min(gain, accumulatedDep);
      return {
        gross: gross, gain: gain, recapture: recapture,
        tax: recapture * c.recaptureTax + Math.max(0, gain - recapture) * c.capGainsTax
      };
    }
    var useExclusion = excluded === undefined ? true : excluded;
    var taxable = Math.max(0, gain - (useExclusion ? c.exclusion : 0));
    return { gross: gross, gain: gain, recapture: 0, tax: taxable * c.capGainsTax };
  }

  /* ---------- strategy comparison ---------- */
  function compare(transferYear, horizon, cfg) {
    var c = settings(cfg);
    var t = transfer(c, transferYear);
    var rNet = c.portfolio - c.fee;
    var rows = {};

    /* 1. Sell A and invest the net proceeds. Basis resets at death, so the
       gain is nil and no capital-gains tax is modelled at the sale. */
    var proceeds = t.market * (1 - c.saleCost);
    var sellTerminal = fv(proceeds, rNet, horizon);
    var sellTaxDue = Math.max(0, sellTerminal - proceeds) * c.capGainsTax;
    rows.sell = {
      key: 'sell', label: 'Sell A and invest',
      proceeds: proceeds,
      year1Cash: proceeds * rNet,
      firstYearOperating: 0,
      terminalPreTax: sellTerminal,
      terminalTax: sellTaxDue,
      terminal: sellTerminal - sellTaxDue,
      detail: 'Net of 6% sale costs; no gain tax because basis resets at death.'
    };

    /* 2 and 3. Hold A. Cash flows are reinvested at the same net return. */
    ['rent', 'live'].forEach(function (option) {
      var reserve = 0, basis = 0, dep = 0, carry = 0, firstYear = 0;
      var years = [];
      for (var i = 1; i <= horizon; i += 1) {
        var y = transferYear + i;
        var h = holdA(c, t, y, option);
        var tax = 0;
        if (option === 'rent') {
          var taxable = h.noi - h.depreciation - carry;
          if (taxable < 0) { carry = -taxable; tax = 0; }
          else { carry = 0; tax = Math.max(0, taxable) * c.ordinaryTax; }
          dep += h.depreciation;
          basis = t.market;
        }
        var flow = (option === 'rent' ? h.noi - tax : -h.opex);
        if (i === 1) firstYear = flow;
        reserve = reserve * (1 + rNet) + flow;
        years.push({
          year: y, market: h.market, assessed: h.assessed, opex: h.opex,
          propTax: h.propTax, rent: h.rent, noi: h.noi, incomeTax: tax,
          flow: flow, reserve: reserve
        });
      }
      var exitYear = transferYear + horizon;
      var exitMarket = seriesA(c, exitYear).market;
      var st = saleTax(c, option, t.market, exitMarket, dep, true);
      var reserveGainTax = Math.max(0, reserve) * 0; /* reserve already after tax */
      rows[option] = {
        key: option,
        label: option === 'rent' ? 'Keep A and rent it' : 'Keep A and live in it',
        proceeds: 0,
        year1Cash: firstYear,
        terminalPreTax: st.gross + reserve,
        terminalTax: st.tax + reserveGainTax,
        terminal: st.gross - st.tax + reserve,
        detail: option === 'rent'
          ? 'Full reassessment at transfer, depreciation shield, 25% recapture at exit.'
          : 'Proposition 19 relief, no rent, $250,000 home-sale exclusion at exit.',
        years: years,
        sale: st,
        assessedAtTransfer: option === 'live' ? t.primaryAssessed : t.fullAssessed
      };
    });

    /* The San Francisco third unit is only rentable if the household lives in
       A rather than occupying that unit. */
    var sfExtraYear1 = c.b.rentThird * 12 * (1 - c.b.vacancy) *
      (1 - c.b.management) - c.b.rentThird * 12 * (1 - c.b.vacancy) *
      (1 - c.b.management) * c.ordinaryTax;
    var sfExtra = 0;
    for (var j = 1; j <= horizon; j += 1) {
      var flowJ = fv(sfExtraYear1, c.sfRentGrowth, j + (transferYear - c.start));
      sfExtra = sfExtra * (1 + rNet) + flowJ;
    }
    sfExtra -= Math.max(0, sfExtra) * 0.20;
    rows.live.sfExtra = sfExtra;
    rows.live.terminalTotal = rows.live.terminal + sfExtra;

    var best = 'sell';
    ['rent', 'live'].forEach(function (k) {
      var v = k === 'live' ? rows.live.terminalTotal : rows[k].terminal;
      var bv = best === 'live' ? rows.live.terminalTotal : rows[best].terminal;
      if (v > bv) best = k;
    });

    return {
      config: c, transfer: t, horizon: horizon, transferYear: transferYear,
      rows: rows, best: best,
      rNet: rNet,
      sfExtraYear1: sfExtraYear1
    };
  }

  /* ---------- projections ---------- */
  function projection(cfg) {
    var c = settings(cfg);
    var out = { years: [], estate: [] };
    for (var y = c.start; y <= c.end; y += 1) {
      var a = seriesA(c, y);
      var b = seriesB(c, y);
      var n = y - c.start;
      out.years.push({
        year: y,
        aMarket: a.market, aAssessed: a.assessed, aTax: a.tax,
        aRate: a.assessed / a.market,
        bMarket: b.market, bAssessed: b.assessed, bTax: b.tax,
        bRate: b.assessed / b.market,
        inflationIndex: fv(1, c.inflation, n)
      });
    }
    for (var e = c.start; e <= c.end; e += 1) {
      var excl = e >= 2027
        ? fv(c.estate2027, c.estateIndex, e - 2027)
        : fv(c.estate2026, c.estateIndex, e - 2026);
      out.estate.push({ year: e, exclusion: excl, aValue: seriesA(c, e).market });
    }
    return out;
  }

  /* Property A property tax and assessment at the transfer, both ways. */
  function transferTable(cfg) {
    var c = settings(cfg);
    var rows = [];
    [2040, 2045, 2050].forEach(function (y) {
      var t = transfer(c, y);
      var s = seriesA(c, y);
      rows.push({
        year: y, market: t.market, carryForward: t.carryForward,
        allowance: t.allowance, cap: t.cap, primaryAssessed: t.primaryAssessed,
        fullAssessed: t.fullAssessed, taxLive: t.taxLive, taxRent: t.taxRent,
        taxNoTransfer: s.tax, savings: t.savingsYear1
      });
    });
    return rows;
  }

  /* San Francisco building, year by year, at a stated occupancy. */
  function sfTable(cfg, horizonYears) {
    var c = settings(cfg);
    var rows = [];
    var years = horizonYears || 20;
    for (var y = c.start; y <= c.start + years; y += 1) {
      var n = y - c.start;
      var b = seriesB(c, y);
      var rent2 = fv(c.b.rentTwo * 12, c.sfRentGrowth, n);
      var rent3 = fv(c.b.rentThird * 12, c.sfRentGrowth, n);
      var gross = rent2 + rent3;
      var collected = gross * (1 - c.b.vacancy);
      var mgmt = collected * c.b.management;
      var water = fv(c.b.waterMonth * 12, c.inflation, n);
      var electric = fv(c.b.electricMonth * 12, c.inflation, n);
      var insurance = fv(c.b.insuranceYear, c.insuranceGrowth, n);
      var maintenance = b.market * c.b.maintenance;
      var fee = fv(c.b.rentFee, c.inflation, n);
      var noi = collected - mgmt - b.tax - water - electric - insurance - maintenance - fee;
      rows.push({
        year: y, market: b.market, assessed: b.assessed, tax: b.tax,
        gross: gross, water: water, electric: electric, insurance: insurance,
        maintenance: maintenance, noi: noi
      });
    }
    return rows;
  }

  /* ---------- stress paths ---------- */
  var PATHS = {
    stagflation: {
      title: '1970s stagflation',
      inflation: [0.09, 0.06, 0.07, 0.11, 0.09, 0.06, 0.07, 0.06, 0.07, 0.05],
      home: [0.05, 0.07, 0.12, 0.14, 0.10, 0.08, 0.06, 0.10, 0.13, 0.10],
      portfolio: [-0.03, 0.08, 0.02, -0.15, -0.27, 0.20, 0.13, 0.02, 0.05, 0.13],
      note: 'Costs compound at 9-11% while a balanced portfolio loses money in real terms.'
    },
    ca_crash: {
      title: 'California housing bust',
      inflation: [0.06, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03],
      home: [-0.01, -0.06, -0.05, -0.02, -0.01, 0.01, 0.02],
      portfolio: [0.05, 0.13, 0.07, 0.05, 0.01, 0.16, 0.15],
      note: 'Six consecutive years without a price gain; the county index took about a decade to recover.'
    },
    gfc: {
      title: 'Financial crisis',
      inflation: [0.04, 0.01, 0.03, 0.02, 0.03, 0.02],
      home: [-0.05, -0.12, -0.09, -0.02, -0.01, 0.03],
      portfolio: [0.05, -0.37, 0.26, 0.15, 0.02, 0.16],
      note: 'A one-year portfolio loss near 37% while the house also fell.'
    },
    rate_shock: {
      title: 'Rate shock',
      inflation: [0.08, 0.04, 0.03],
      home: [0.02, -0.04, -0.02],
      portfolio: [-0.13, 0.20, 0.12],
      note: 'Bonds and shares fall together as inflation rises to 8%.'
    },
    disaster: {
      title: 'Uninsured earthquake',
      inflation: [0.023],
      home: [0.0],
      portfolio: [0.05],
      note: 'One $600,000 loss in year 11 with double insurance afterwards.',
      repair: 600000, hitYear: 11
    }
  };

  /* Run an explicit annual-rate path. rates[i] = {inflation, home, portfolio}
     for year (transferYear + i + 1). Shared by the named scenarios and by the
     historical bootstrap, so both use identical arithmetic. */
  function runDraw(rates, cfg, transferYear, extra) {
    var c = settings(cfg);
    var T = transferYear || 2045;
    var ex = extra || {};
    var t = transfer(c, T);
    var market = t.market;
    var priceIndex = 1;
    var rent = fv(c.a.rentMonth * 12, c.rentGrowth, T - c.start);
    var water = fv(c.a.waterMonth * 12, c.inflation, T - c.start);
    var insurance = fv(c.a.insuranceYear, c.a.insuranceGrowth, T - c.start);
    var depStep = (t.market * (1 - c.a.landShare)) / c.depreciationYears;
    var sellBook = t.market * (1 - c.saleCost);
    var rentReserve = 0, liveReserve = 0, rentCarry = 0, accDep = 0;
    var rows = [];
    for (var i = 0; i < rates.length; i += 1) {
      var r = rates[i];
      var infl = r.inflation, port = r.portfolio;
      market *= 1 + r.home;
      priceIndex *= 1 + infl;
      rent *= 1 + Math.min(infl + 0.002, c.rentGrowth + 0.01);
      water *= 1 + infl;
      insurance *= 1 + infl;
      if (ex.hitYear === i + 1) insurance *= 2;
      var liveAssessed = Math.min(fv(t.primaryAssessed, c.assessmentGrowth, i + 1), market);
      var rentAssessed = Math.min(fv(t.fullAssessed, c.assessmentGrowth, i + 1), market);
      var maintenance = market * c.a.maintenance;
      var common = water + c.a.electricMonth * 12 + insurance + maintenance;
      if (ex.repair && ex.hitYear === i + 1) common += ex.repair;
      var liveOpex = liveAssessed * c.a.rate - c.homeownersExemption * c.a.rate + common;
      var rentOpex = rentAssessed * c.a.rate + common;
      var noi = rent * (1 - c.a.vacancy) * (1 - c.a.management) - rentOpex;
      accDep += depStep;
      var taxable = noi - depStep - rentCarry;
      var rentTax = 0;
      if (taxable > 0) { rentTax = taxable * c.ordinaryTax; rentCarry = 0; }
      else { rentCarry = -taxable; }
      sellBook *= 1 + port;
      rentReserve = rentReserve * (1 + port) + noi - rentTax;
      liveReserve = liveReserve * (1 + port) - liveOpex;
      var gross = market * (1 - c.saleCost);
      var sellGain = Math.max(0, sellBook - t.market * (1 - c.saleCost));
      var rentGain = Math.max(0, gross - t.market + accDep);
      var recap = Math.min(rentGain, accDep);
      var rentEnd = gross - (recap * c.recaptureTax +
        Math.max(0, rentGain - recap) * c.capGainsTax) + rentReserve;
      var liveGain = Math.max(0, gross - t.market);
      var liveEnd = gross - Math.max(0, liveGain - c.exclusion) * c.capGainsTax + liveReserve;
      rows.push({
        year: T + i + 1, market: market, priceIndex: priceIndex,
        liveAssessed: liveAssessed, rentAssessed: rentAssessed,
        inflation: infl, home: r.home, portfolio: port,
        sell: sellBook - sellGain * c.capGainsTax,
        rent: rentEnd, live: liveEnd,
        realSell: (sellBook - sellGain * c.capGainsTax) / priceIndex,
        realRent: rentEnd / priceIndex,
        realLive: liveEnd / priceIndex
      });
    }
    return rows;
  }

  function runPath(key, cfg, transferYear, horizon) {
    var c = settings(cfg);
    var T = transferYear || 2045;
    var H = horizon || 30;
    var path = PATHS[key];
    var rNet = c.portfolio - c.fee;
    var rates = [];
    for (var i = 0; i < H; i += 1) {
      rates.push({
        inflation: i < path.inflation.length ? path.inflation[i] : c.inflation,
        home: i < path.home.length ? path.home[i] : c.homeGrowth,
        portfolio: i < path.portfolio.length ? path.portfolio[i] : rNet
      });
    }
    return runDraw(rates, cfg, T, path);
  }


  /* Break-even: the home growth rate at which holding A beats selling A,
     holding the other assumptions fixed. */
  function breakEven(transferYear, horizon, option, cfg) {
    /* The comparison is not always monotone in home growth, so scan the whole
       range and report the highest rate at which holding overtakes selling. */
    function gap(g) {
      var c = settings(Object.assign({}, cfg || {}, { homeGrowth: g }));
      var r = compare(transferYear, horizon, c);
      var hold = option === 'live' ? r.rows.live.terminalTotal : r.rows[option].terminal;
      return hold - r.rows.sell.terminal;
    }
    var grid = [], i, g;
    for (i = -4; i <= 28; i += 1) {
      g = i * 0.005;
      grid.push({ g: g, gap: gap(g) });
    }
    var crossings = [];
    for (i = 1; i < grid.length; i += 1) {
      if ((grid[i].gap > 0) !== (grid[i - 1].gap > 0)) {
        var lo = grid[i - 1].g, hi = grid[i].g;
        for (var k = 0; k < 40; k += 1) {
          var mid = (lo + hi) / 2;
          if ((gap(mid) > 0) === (grid[i - 1].gap > 0)) lo = mid; else hi = mid;
        }
        crossings.push({ rate: mid, holdAbove: grid[i].gap > 0 });
      }
    }
    var holdAtTop = grid[grid.length - 1].gap > 0;
    var holdAtBottom = grid[0].gap > 0;
    if (!crossings.length) {
      return { rate: null, crossings: 0, hold: holdAtTop,
        note: holdAtTop ? 'holding leads at every rate scanned (−2% to 14%)'
                        : 'selling leads at every rate scanned (−2% to 14%)' };
    }
    var top = crossings[crossings.length - 1];
    return {
      rate: top.rate, crossings: crossings.length, hold: holdAtTop,
      nonMonotone: crossings.length > 1,
      note: null
    };
  }


  /* Sensitivity grid: which option leads. */
  function sensitivity(transferYear, horizon, cfg) {
    var homes = [0.02, 0.03, 0.04, 0.05, 0.06];
    var ports = [0.03, 0.04, 0.05, 0.06, 0.07];
    var grid = [];
    homes.forEach(function (hg) {
      var row = { homeGrowth: hg, cells: [] };
      ports.forEach(function (p) {
        var c = settings(Object.assign({}, cfg || {}, { homeGrowth: hg, portfolio: p }));
        var r = compare(transferYear, horizon, c);
        row.cells.push({
          portfolio: p,
          sell: r.rows.sell.terminal,
          rent: r.rows.rent.terminal,
          live: r.rows.live.terminalTotal,
          best: r.best
        });
      });
      grid.push(row);
    });
    return { homeGrowth: homes, portfolio: ports, grid: grid };
  }

  /* Inheritance-tax thresholds compared with a projected transfer value. */
  function estate(cfg, transferYear) {
    var c = settings(cfg);
    var t = transfer(c, transferYear || 2045);
    var excl = transferYear >= 2027
      ? fv(c.estate2027, c.estateIndex, transferYear - 2027)
      : fv(c.estate2026, c.estateIndex, transferYear - 2026);
    return {
      exclusion: excl,
      aValue: t.market,
      headroom: excl - t.market,
      aShare: t.market / excl
    };
  }

  var MODEL = {
    BASE: BASE,
    PATHS: PATHS,
    settings: settings,
    round10: round10,
    fmtMoney: fmtMoney,
    fmtPct: fmtPct,
    fv: fv,
    seriesA: seriesA,
    seriesB: seriesB,
    allowance: allowance,
    transfer: transfer,
    assessedAfter: assessedAfter,
    holdA: holdA,
    saleTax: saleTax,
    compare: compare,
    projection: projection,
    transferTable: transferTable,
    sfTable: sfTable,
    runPath: runPath,
    runDraw: runDraw,
    breakEven: breakEven,
    sensitivity: sensitivity,
    estate: estate,
    labels: { a: A_LABEL, b: B_LABEL }
  };

  root.MODEL = MODEL;
  if (typeof module !== 'undefined' && module.exports) module.exports = MODEL;
}(typeof window !== 'undefined' ? window : globalThis));
