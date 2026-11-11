/*
  Economic-scenario ("black swan") engine for Property A (inherited) and Property B (already owned).
  Not a forecast and not an appraisal. Historical windows are replayed from official-source index data in
  history.js (BLS CPI, FHFA house-price indexes, Treasury yields, OECD share prices, via FRED).
  Assumption-based scenarios are labelled as such. All dollar results are rounded to $10 only when displayed.
  The engine reproduces MODEL.decision() exactly when every rate is constant (checked by scripts/validate.js).
*/
(function (root) {
  const MODEL = root.MODEL;
  const HISTORY = root.HISTORY;
  const B = MODEL.BASE;
  const START = 2026, N = 50;               // paths cover 2026 .. 2076
  const BASELINE = { home: B.appreciation, cpi: 0.023, eq: 0.07, bond: 0.045 };
  const SPREAD = B.expenseInflation - 0.023; // cost and rent growth = CPI + 0.7 pt (= 3.0% in the base case)
  const EQ_WEIGHT = 0.6, DIVIDEND = 0.02, DRAG = B.portfolioTaxDrag;
  const SF_RATE_OFFICIAL = 0.0118162182;     // SF FY2026-27 combined ad valorem rate (Board of Supervisors minutes)
  const SF_UNIT_RENT_2026 = B.bRent1BR;      // HUD FY2026 SAFMR 1BR benchmark for the vacant owner-unit scenario

  // ---------- history helpers ----------
  const H = {};
  HISTORY.rows.forEach(r => { H[r[0]] = {}; HISTORY.columns.forEach((c, i) => { H[r[0]][c] = r[i]; }); });
  const g = (col, y) => (H[y] && H[y - 1] && H[y][col] != null && H[y - 1][col] != null) ? H[y][col] / H[y - 1][col] - 1 : null;
  function histYear(y) {
    const cpi = g("cpi", y);
    const home = g("sj", y) ?? g("ca", y) ?? cpi;      // fallback order: San Jose MSA, California, CPI
    const homeB = g("sf", y) ?? g("ca", y) ?? cpi;     // fallback order: SF metro division, California, CPI
    const eqPrice = g("eq", y);
    return { home, homeB, cpi, eq: eqPrice + DIVIDEND, bond: H[y].gs10 / 100, fallback: g("sj", y) == null };
  }
  function window_(a, b) { const out = []; for (let y = a; y <= b; y += 1) out.push(histYear(y)); return out; }
  function cagr(col, a, b) { return Math.pow(H[b][col] / H[a][col], 1 / (b - a)) - 1; }
  function total(col, a, b) { return H[b][col] / H[a][col] - 1; }

  // ---------- scenario catalogue ----------
  const SCENARIOS = [
    { id: "baseline", name: "Smooth baseline", kind: "Baseline", seq: [], fixedStart: null,
      analog: "Same constant rates as the Decision lab", params: "Home +3.5%/yr · CPI 2.3% · costs/rent CPI+0.7 pt · equities 7.0% · 10-yr 4.5%",
      note: "CBO (Feb 2026) projects ~2% PCE inflation from 2030 and a 10-yr yield of about 4.4% from 2031; home growth and equity return are household-model assumptions.", source: "cbo" },
    { id: "replay50", name: "Replay of the last 49 years", kind: "Official-data replay", seq: window_(1977, 2025), fixedStart: 2027,
      analog: "1977–2025 annual data replayed in order from 2027 (then baseline for 2076)", params: "San Jose-area home prices, CPI, Treasury yields and equity price index (+2.0 pt dividend assumption) exactly as recorded",
      note: "Real sequence incl. 1980s inflation, 1990s Bay Area bust, 2000 dot-com, 2008 crisis, 2021–23 inflation. Home growth averaged far above the baseline, so this is not a 'bad' case for homeowners.", source: "fredSJ" },
    { id: "stagflation", name: "1970s-style stagflation", kind: "Official-data replay", seq: window_(1973, 1982), fixedStart: null,
      analog: "1973–1982 CPI, yields and equity prices; home prices from FHFA California index (1976+), CPI before that", params: "Replayed annually",
      note: "CPI compounded about 8.7%/yr across 1972–1982 while equity prices compounded about 2.3%/yr: investors lose purchasing power. Prop 13 caps assessments at 2%, so property tax lags inflation, while insurance and utilities do not.", source: "fredCPI" },
    { id: "gfc", name: "2008-style housing and equity crash", kind: "Official-data replay", seq: window_(2006, 2012), fixedStart: null,
      analog: "2006–2012 CPI, yields, equities, San Jose-area home prices", params: "San Jose-area index fell about 26% 2006→2011; California index about 40%; US share-price index fell about 44% in 2008",
      note: "Hits the sell-and-reinvest option (equities) and the keep-the-house options (home value) at the same time.", source: "fredSJ" },
    { id: "bust90", name: "Early-1990s Bay Area bust", kind: "Official-data replay", seq: window_(1990, 1996), fixedStart: null,
      analog: "1990–1996 data", params: "San Jose-area index fell about 12.5% 1989→1994 while CPI rose about 3–4%/yr (real decline about 25%)",
      note: "Regional bust with healthy equity markets: favors having sold and diversified.", source: "fredSJ" },
    { id: "dotcom", name: "Equity-only crash (2000–2003 style)", kind: "Official-data replay", seq: window_(2000, 2003), fixedStart: null,
      analog: "2000–2003 data", params: "US share-price index fell about 26% 2000→2002; local home prices kept rising",
      note: "Tests the main risk of selling and investing: a market drawdown early in the reinvestment period.", source: "fredOECD" },
    { id: "infl2123", name: "2021–23 inflation spike", kind: "Official-data replay", seq: window_(2021, 2023), fixedStart: null,
      analog: "2021–2023 data", params: "CPI about 4.7% / 8.0% / 4.1% (annual averages), 30-yr mortgage rate 3.0%→6.8%",
      note: "Costs jump; Prop 13 assessments rise only 2% (or the CPI if lower); rents in rent-controlled SF are allowed only 60% of CPI.", source: "fredCPI" },
    { id: "lost", name: "Lost decades (flat nominal prices)", kind: "Assumption", seq: Array.from({ length: 15 }, () => ({ home: 0, homeB: 0, cpi: 0.005, eq: 0.03, bond: 0.015 })), fixedStart: null,
      analog: "Stylised; no official US data series supports this exact path", params: "15 years: home 0%, CPI 0.5%, equities 3.0%, 10-yr 1.5%",
      note: "Included because long deflation-like spells have occurred in other economies; flagged as an unverified assumption.", source: "fredSJ" },
    { id: "insurance", name: "Insurance and climate-cost shock", kind: "Assumption", seq: Array.from({ length: 10 }, (_, i) => ({ home: i < 5 ? -0.03 : BASELINE.home, homeB: i < 5 ? -0.03 : BASELINE.home, cpi: BASELINE.cpi, eq: BASELINE.eq, bond: BASELINE.bond, insExtra: 0.12 })), fixedStart: null,
      analog: "Stylised; premiums rising faster than CPI", params: "10 years: insurance +12 pt/yr above cost inflation; home prices −3%/yr for 5 years",
      note: "California regulators have approved large homeowners-insurance increases and insurer withdrawals; this path is an assumption, not a CDI forecast.", source: "insurance" },
    { id: "policyTax", name: "Property-tax regime change (assessments track market)", kind: "Assumption", seq: [], fixedStart: null, flags: { assessFollowsMarket: true },
      analog: "Hypothetical; no such measure is currently on the books", params: "From the shock year onward Property A and B are taxed on current market value",
      note: "The Nov 2026 'Save Prop 13' measure was a different proposal (see Sources → watchlist). This stresses the model's biggest hidden dependency: the 2% assessment cap.", source: "boeProp13" },
    { id: "noProp19", name: "Prop 19 inheritance relief repealed", kind: "Assumption", seq: [], fixedStart: null, flags: { noProp19: true },
      analog: "Hypothetical", params: "Living in Property A earns no assessment relief: full reassessment at inheritance",
      note: "Prop 19's parent-child exclusion was narrowed in 2021 and is itself subject to ballot-box and legislative change.", source: "boeProp19" },
    { id: "perfect", name: "Compound shock: stagflation → 2008-style crash + insurance shock", kind: "Official-data replay + assumption",
      seq: window_(1973, 1982).map((r, i) => ({ ...r, insExtra: 0.08 })).concat(window_(2006, 2012)), fixedStart: null,
      analog: "Back-to-back replays of 1973–82 and 2006–12 with +8 pt/yr insurance shock in the first decade", params: "17 consecutive stressed years",
      note: "A deliberately severe path; shows which strategy is least bad rather than most likely.", source: "fredCPI" }
  ];

  // ---------- path construction ----------
  function baselinePath() {
    const p = { home: [], homeB: [], cpi: [], eq: [], bond: [], insExtra: [] };
    for (let i = 0; i <= N; i += 1) { p.home.push(BASELINE.home); p.homeB.push(BASELINE.home); p.cpi.push(BASELINE.cpi); p.eq.push(BASELINE.eq); p.bond.push(BASELINE.bond); p.insExtra.push(0); }
    return p;
  }
  function buildPath(scenario, shockStart) {
    const p = baselinePath();
    const start = scenario.fixedStart || shockStart || 2042;
    scenario.seq.forEach((r, k) => {
      const i = start - START + k;
      if (i < 1 || i > N) return;
      p.home[i] = r.home; p.homeB[i] = r.homeB; p.cpi[i] = r.cpi; p.eq[i] = r.eq; p.bond[i] = r.bond; p.insExtra[i] = r.insExtra || 0;
    });
    p.flags = Object.assign({}, scenario.flags || {});
    p.shockStart = start;
    return p;
  }

  // ---------- derived series ----------
  function derive(path) {
    const flags = path.flags || {};
    const d = { cpiI: [1], mA: [B.aValue], mB: [B.bValue], fbA: [B.aAssessed], fbB: [B.bAssessed2025 * (1 + B.assessmentGrowth)], costI: [1], rentI: [1], insI: [1], sfg: [0], port: [0] };
    for (let i = 1; i <= N; i += 1) {
      d.cpiI.push(d.cpiI[i - 1] * (1 + path.cpi[i]));
      d.mA.push(d.mA[i - 1] * (1 + path.home[i]));
      d.mB.push(d.mB[i - 1] * (1 + path.homeB[i]));
      const f = Math.min(0.02, path.cpi[i]);
      d.fbA.push(d.fbA[i - 1] * (1 + f));
      d.fbB.push(d.fbB[i - 1] * (1 + f));
      const costG = Math.max(-0.5, path.cpi[i] + SPREAD);
      d.costI.push(d.costI[i - 1] * (1 + costG));
      d.rentI.push(d.rentI[i - 1] * (1 + costG));
      d.insI.push(d.insI[i - 1] * (1 + costG + (path.insExtra[i] || 0)));
      d.sfg.push(Math.min(0.07, Math.max(0, 0.6 * (path.cpi[i] + 0.004)))); // SF Rent Board: 60% of Bay Area CPI (official); 7% ceiling is from the Rent Ordinance and unverified here
      d.port.push(EQ_WEIGHT * path.eq[i] + (1 - EQ_WEIGHT) * path.bond[i] - DRAG);
    }
    d.flags = flags; d.shockStart = path.shockStart || START;
    return d;
  }
  function cap(d, year) { const steps = Math.max(0, Math.floor((year - START) / 2)); return B.prop19Amount * d.mA[Math.min(N, 2 * steps)] / d.mA[0]; }
  function follows(d, year) { return d.flags.assessFollowsMarket && year >= d.shockStart; }

  // ---------- strategy engine ----------
  function simulate(path, inheritYear, hold, rentChoice, opts) {
    const d = derive(path), o = opts || {};
    const Y = inheritYear - START, T = Y + hold;
    const MY = d.mA[Y];
    const fb = d.fbA[Y];
    const capY = cap(d, inheritYear);
    const useP19 = !d.flags.noProp19;
    const primaryAssessed = useP19 ? (MY <= fb + capY ? fb : MY - capY) : MY;
    const net = MY * (1 - B.saleCost);
    let sell = net;
    for (let t = Y + 1; t <= T; t += 1) sell *= 1 + d.port[t];
    const res = { rent: 0, live: 0, liveSF: 0 };
    const ladder = { rent: MY, live: primaryAssessed };
    const rentRent = (rentChoice === "3BR" ? B.aRent3BR : B.aRent4BR);
    const sfUnitStart = SF_UNIT_RENT_2026 * 12 * d.rentI[Y];
    let sfUnit = sfUnitStart;
    const yearly = [];
    let first = null;
    for (let t = Y + 1; t <= T; t += 1) {
      const yr = START + t;
      ladder.rent *= 1 + Math.min(0.02, path.cpi[t]); ladder.live *= 1 + Math.min(0.02, path.cpi[t]);
      const assessedRent = follows(d, yr) ? d.mA[t] : Math.min(ladder.rent, d.mA[t]);
      const assessedLive = follows(d, yr) ? d.mA[t] : Math.min(ladder.live, d.mA[t]);
      const water = B.aWaterMonthly * 12 * d.costI[t];
      const insurance = B.aInsuranceAnnual * d.insI[t];
      const maint = d.mA[t] * B.maintenanceA;
      const solar = B.aSolarMonthlyCredit * 12;
      const fixed = water + insurance + maint - solar;
      const taxRent = assessedRent * B.aRate, taxLive = assessedLive * B.aRate;
      const gross = rentRent * 12 * d.rentI[t];
      const collected = gross * (1 - B.vacancy);
      const noi = collected * (1 - B.management) - taxRent - fixed;
      const rentCash = noi - Math.max(0, noi) * B.ordinaryTax;
      const liveCash = -(taxLive + fixed);
      sfUnit *= 1 + d.sfg[t];
      const sfNet = sfUnit * (1 - B.vacancy) * (1 - B.management) * (1 - B.ordinaryTax);
      res.rent = res.rent * (1 + d.port[t]) + rentCash;
      res.live = res.live * (1 + d.port[t]) + liveCash;
      res.liveSF = res.liveSF * (1 + d.port[t]) + liveCash + sfNet;
      if (o.detail) yearly.push({ year: yr, market: d.mA[t], assessedRent, assessedLive, taxRent, taxLive, rentCash, liveCash, sfNet });
    }
    const amountRealized = d.mA[T] * (1 - B.saleCost);
    const gainBefore = Math.max(0, amountRealized - MY);
    const taxRentSale = gainBefore * B.capitalGainsTax;
    const exclusion = hold >= 2 ? Math.min(B.primaryGainExclusion, gainBefore) : 0;
    const taxLiveSale = Math.max(0, gainBefore - exclusion) * B.capitalGainsTax;
    const sellLiq = sell - Math.max(0, sell - net) * B.capitalGainsTax;
    const out = {
      inheritYear, endYear: START + T, marketAtInherit: MY, marketAtEnd: d.mA[T], deflator: d.cpiI[T], primaryAssessed, fullAssessed: MY, capUsed: capY,
      sell, sellLiq, rent: amountRealized - taxRentSale + res.rent, live: amountRealized - taxLiveSale + res.live, liveSF: amountRealized - taxLiveSale + res.liveSF,
      reserves: res, yearly
    };
    out.best = ["sell", "rent", "live", "liveSF"].reduce((a, k) => out[k] > out[a] ? k : a, "sell");
    out.bestLiq = ["sellLiq", "rent", "live", "liveSF"].reduce((a, k) => out[k] > out[a] ? k : a, "sellLiq");
    return out;
  }

  // ---------- Property B (already owned) ----------
  function sfSeries(path) {
    const d = derive(path), rows = [];
    for (let i = 0; i <= N; i += 1) {
      const yr = START + i;
      const assessed = follows(d, yr) ? d.mB[i] : Math.min(d.fbB[i], d.mB[i]);
      const tax = follows(d, yr) ? d.mB[i] * SF_RATE_OFFICIAL : assessed * B.bRate;
      let rent = B.bRentMonthly * 12;
      rows.push({ i, yr, market: d.mB[i], assessed, tax });
    }
    let rentIdx = 1;
    rows.forEach(r => {
      if (r.i > 0) rentIdx *= 1 + d.sfg[r.i];
      const gross = B.bRentMonthly * 12 * rentIdx;
      const vacancy = gross * B.vacancy, mgmt = (gross - vacancy) * B.management;
      const water = B.bWaterMonthly * 12 * d.costI[r.i], elec = B.bElectricMonthly * 12 * d.costI[r.i];
      const insurance = B.bInsuranceAnnual * d.insI[r.i], maint = r.market * B.maintenanceB, fee = B.bRentBoardFeeAnnual * d.costI[r.i];
      r.gross = gross; r.noi = gross - vacancy - mgmt - r.tax - water - elec - insurance - maint - fee; r.cpiIdx = d.costI[r.i];
    });
    return rows;
  }

  // ---------- Monte Carlo (seeded block bootstrap of 1977-2025 official data) ----------
  function mulberry32(a) { return function () { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
  const histVec = window_(1977, 2025);
  function geo(key) { return Math.exp(histVec.reduce((s, r) => s + Math.log(1 + r[key]), 0) / histVec.length) - 1; }
  function monteCarlo(opts) {
    const o = Object.assign({ paths: 2000, block: 5, seed: 20261111, adjust: true, inheritYears: [2040, 2045, 2050], hold: 10, rentChoice: "4BR" }, opts || {});
    const rnd = mulberry32(o.seed);
    const shift = o.adjust ? { home: BASELINE.home - geo("home"), homeB: BASELINE.home - geo("homeB"), cpi: BASELINE.cpi - geo("cpi"), eq: BASELINE.eq - geo("eq"), bond: BASELINE.bond - geo("bond") } : { home: 0, homeB: 0, cpi: 0, eq: 0, bond: 0 };
    const results = {}; o.inheritYears.forEach(y => { results[y] = { sell: [], sellLiq: [], rent: [], live: [], liveSF: [] }; });
    for (let k = 0; k < o.paths; k += 1) {
      const p = { home: [0], homeB: [0], cpi: [0], eq: [0], bond: [0], insExtra: [0], flags: {} };
      while (p.home.length <= N) {
        const s = Math.floor(rnd() * (histVec.length - o.block + 1));
        for (let j = 0; j < o.block && p.home.length <= N; j += 1) {
          const r = histVec[s + j];
          p.home.push(Math.max(-0.6, r.home + shift.home)); p.homeB.push(Math.max(-0.6, r.homeB + shift.homeB));
          p.cpi.push(Math.max(-0.05, r.cpi + shift.cpi)); p.eq.push(Math.max(-0.9, r.eq + shift.eq)); p.bond.push(Math.max(0, r.bond + shift.bond)); p.insExtra.push(0);
        }
      }
      o.inheritYears.forEach(y => { const r = simulate(p, y, o.hold, o.rentChoice); ["sell", "sellLiq", "rent", "live", "liveSF"].forEach(key => results[y][key].push(r[key])); });
    }
    const q = (arr, pr) => { const s = arr.slice().sort((a, b) => a - b); return s[Math.min(s.length - 1, Math.max(0, Math.floor(pr * (s.length - 1))))]; };
    const summary = {};
    o.inheritYears.forEach(y => {
      const R = results[y], n = R.sell.length;
      const share = (a, b) => R[a].filter((v, i) => v > R[b][i]).length / n;
      summary[y] = {
        n, p10: {}, p50: {}, p90: {}, mean: {},
        sellBeatsRent: share("sell", "rent"), sellLiqBeatsRent: share("sellLiq", "rent"), sellLiqBeatsLive: share("sellLiq", "live"), sellBeatsLive: share("sell", "live"), sellBeatsLiveSF: share("sell", "liveSF"), liveSFBeatsRent: share("liveSF", "rent"),
        bestCount: ["sell", "rent", "live", "liveSF"].reduce((m, key) => { m[key] = R.sell.filter((_, i) => ["sell", "rent", "live", "liveSF"].reduce((a, kk) => R[kk][i] > R[a][i] ? kk : a, "sell") === key).length / n; return m; }, {})
      };
      ["sell", "sellLiq", "rent", "live", "liveSF"].forEach(key => { summary[y].p10[key] = q(R[key], 0.1); summary[y].p50[key] = q(R[key], 0.5); summary[y].p90[key] = q(R[key], 0.9); summary[y].mean[key] = R[key].reduce((a, b) => a + b, 0) / n; });
    });
    return { options: o, shift, summary };
  }

  // ---------- calibration statistics from official data ----------
  function calibration() {
    return [
      { label: "CPI-U inflation, 1976–2025 (annualized)", value: cagr("cpi", 1976, 2025), assumption: BASELINE.cpi, series: "fredCPI" },
      { label: "CPI-U inflation, 1972–1982 (annualized)", value: cagr("cpi", 1972, 1982), assumption: null, series: "fredCPI" },
      { label: "CPI-U inflation, 2020–2025 (annualized)", value: cagr("cpi", 2020, 2025), assumption: null, series: "fredCPI" },
      { label: "San Jose-area home prices, 1976–2025 (annualized)", value: cagr("sj", 1976, 2025), assumption: BASELINE.home, series: "fredSJ" },
      { label: "San Francisco-area home prices, 1976–2025 (annualized)", value: cagr("sf", 1976, 2025), assumption: BASELINE.home, series: "fredSF" },
      { label: "California home prices, 1975–2025 (annualized)", value: cagr("ca", 1975, 2025), assumption: null, series: "fredCA" },
      { label: "San Jose-area home prices, 2019–2025 (annualized)", value: cagr("sj", 2019, 2025), assumption: BASELINE.home, series: "fredSJ" },
      { label: "San Jose-area home prices, 2024→2025", value: total("sj", 2024, 2025), assumption: null, series: "fredSJ" },
      { label: "San Jose-area home prices, 2006→2011 (peak to trough, year-end)", value: total("sj", 2006, 2011), assumption: null, series: "fredSJ" },
      { label: "California home prices, 2006→2011", value: total("ca", 2006, 2011), assumption: null, series: "fredCA" },
      { label: "San Jose-area home prices, 1989→1994", value: total("sj", 1989, 1994), assumption: null, series: "fredSJ" },
      { label: "US share-price index (price only), 1976–2025 (annualized)", value: cagr("eq", 1976, 2025), assumption: null, series: "fredOECD", note: "Excludes dividends" },
      { label: "US share-price index, 2007→2008", value: total("eq", 2007, 2008), assumption: null, series: "fredOECD" },
      { label: "US share-price index, 2000→2002", value: total("eq", 2000, 2002), assumption: null, series: "fredOECD" },
      { label: "US share-price index, 1972→1974", value: total("eq", 1972, 1974), assumption: null, series: "fredOECD" },
      { label: "US share-price index, 1972–1982 (annualized)", value: cagr("eq", 1972, 1982), assumption: null, series: "fredOECD" }
    ];
  }

  root.SCEN = { START, N, BASELINE, SPREAD, EQ_WEIGHT, DIVIDEND, SF_RATE_OFFICIAL, SF_UNIT_RENT_2026, SCENARIOS, H, buildPath, derive, simulate, sfSeries, monteCarlo, calibration, geo, histVec };
  if (typeof module !== "undefined" && module.exports) module.exports = root.SCEN;
})(typeof window !== "undefined" ? window : globalThis);
