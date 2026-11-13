/* Build-time snapshot. Runs the same model the browser runs, so the static
   HTML tables and the interactive tables cannot disagree. No record data. */
'use strict';
const fs = require('fs');
const path = require('path');
const MODEL = require(path.join(__dirname, '..', 'guide', 'data', 'model.js'));
const out = {};

const TRANSFER = 2045;
const HORIZON = 20;

/* Projections 2026-2076. */
out.projection = MODEL.projection({}).years;

/* Transfer comparison at three candidate years. */
out.transfers = [2040, 2045, 2050].map((y) => {
  const t = MODEL.transfer(MODEL.settings({}), y);
  const pre = MODEL.seriesA(MODEL.settings({}), y);
  return {
    year: y, market: t.market, carryForward: t.carryForward,
    allowance: t.allowance, cap: t.cap, primaryAssessed: t.primaryAssessed,
    fullAssessed: t.fullAssessed, taxLive: t.taxLive, taxRent: t.taxRent,
    taxNoTransfer: pre.tax, savings: t.savingsYear1
  };
});

/* Base-case comparison at the three transfer years, two horizons. */
out.comparisons = [];
[2040, 2045, 2050].forEach((y) => {
  [10, 20, 30, 50].forEach((h) => {
    const r = MODEL.compare(y, h, {});
    out.comparisons.push({
      year: y, horizon: h, best: r.best,
      sell: r.rows.sell.terminal, rent: r.rows.rent.terminal,
      live: r.rows.live.terminalTotal,
      rentY1: r.rows.rent.year1Cash, liveY1: r.rows.live.year1Cash,
      sfExtra: r.rows.live.sfExtra
    });
  });
});

/* Sensitivity and break-even at the 20-year horizon. */
out.breakEven = [2040, 2045, 2050].map((y) => ({
  year: y,
  rent: MODEL.breakEven(y, 20, 'rent', {}),
  live: MODEL.breakEven(y, 20, 'live', {})
}));
out.sensitivity = MODEL.sensitivity(TRANSFER, HORIZON, {});

/* Held-property annual detail at the base case. */
const base = MODEL.compare(TRANSFER, HORIZON, {});
out.holdRent = base.rows.rent.years;
out.holdLive = base.rows.live.years;
out.baseTransfer = base.transfer;

/* San Francisco building, 20 years. */
out.sf = MODEL.sfTable({}, 20);

/* Stress paths: 30-year and 50-year endpoints plus three-quarter marks. */
out.stress = {};
Object.keys(MODEL.PATHS).forEach((key) => {
  const rows = MODEL.runPath(key, {}, TRANSFER, 50);
  out.stress[key] = {
    title: MODEL.PATHS[key].title,
    note: MODEL.PATHS[key].note,
    rows: rows
  };
});

/* Estate-tax headroom at each candidate transfer year. */
out.estate = [2027, 2040, 2045, 2050, 2060, 2076].map((y) => {
  const e = MODEL.estate({}, y);
  return { year: y, exclusion: e.exclusion, aValue: e.aValue, headroom: e.headroom };
});

/* Operating cost build-up, first full year after a 2045 transfer. */
const c = MODEL.settings({});
const t = MODEL.transfer(c, TRANSFER);
out.aYearOne = {
  live: MODEL.holdA(c, t, TRANSFER + 1, 'live'),
  rent: MODEL.holdA(c, t, TRANSFER + 1, 'rent')
};
out.bYearOne = out.sf[0];

fs.writeFileSync(path.join(__dirname, 'data', 'snapshot.json'),
  JSON.stringify(out, null, 1));
console.log('wrote scripts/data/snapshot.json (no household data)');

/* ------------------------------------------------------------------ *
 * Real-condition analysis from published series (qa/series.json).     *
 * ------------------------------------------------------------------ */
const ECO = require(path.join(__dirname, '..', 'guide', 'data', 'stats.js'));
const series = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'qa', 'series.json'), 'utf8'));

const cpi = {};                 /* consumer price level, 1975 = 1 */
let level = 1;
cpi[1975] = 1;
series.boe_inflation_factor.rows.forEach((r) => {
  level *= 1 + r[1] / 100;
  cpi[parseInt(r[0], 10)] = level;
});

function asSeries(key) {
  return series[key].rows.map((r) => ({ year: r[0], value: r[1] }));
}
const scc = asSeries('hpi_santa_clara_county');
const sfHpi = asSeries('hpi_san_francisco_county');

function windowStats(list, win) {
  const w = ECO.windows(list, cpi, win).filter((x) => isFinite(x.real));
  return {
    window: win,
    n: w.length,
    real: ECO.stats(w.map((x) => x.real)),
    nominal: ECO.stats(w.map((x) => x.nominal))
  };
}

out.eco = {
  cpiAnnual: ECO.stats(Object.keys(cpi).filter((y) => +y > 1975)
    .map((y) => ({ y: +y })).map((o) => cpi[o.y] / cpi[o.y - 1] - 1)),
  cpiWindows: [20, 30].map((win) => {
    const list = [];
    for (let y = 1975; y + win <= 2025; y += 1) list.push(ECO.annualise(cpi[y], cpi[y + win], win));
    return { window: win, stats: ECO.stats(list) };
  }),
  scc50: {
    from: scc[0].year, to: scc[scc.length - 1].year,
    nominal: ECO.annualise(scc[0].value, scc[scc.length - 1].value, 50),
    real: ECO.annualise(scc[0].value / cpi[1975], scc[scc.length - 1].value / cpi[2025], 50)
  },
  sf50: {
    from: sfHpi[0].year, to: sfHpi[sfHpi.length - 1].year,
    nominal: ECO.annualise(sfHpi[0].value, sfHpi[sfHpi.length - 1].value, 50)
  },
  sccWindows: [20, 30].map((w) => windowStats(scc, w)),
  sfWindows: [20, 30].map((w) => windowStats(sfHpi, w)),
  sccDrawdown: ECO.drawdown(scc),
  sfDrawdown: ECO.drawdown(sfHpi),
  cpiSeries: Object.keys(cpi).map(Number).sort((a, b) => a - b)
    .map((y) => ({ year: y, cpi: cpi[y] }))
};

/* --------------------------------------------------------------- *
 * Historical bootstrap: resample the actual joint record of annual *
 * inflation and house-price change in consecutive five-year blocks. *
 * --------------------------------------------------------------- */
function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const rand = mulberry32(20261113);
const annual = [];
for (let y = 1976; y <= 2025; y += 1) {
  const i = scc.findIndex((p) => p.year === y);
  if (i <= 0) continue;
  annual.push({ year: y, inflation: cpi[y] / cpi[y - 1] - 1, home: scc[i].value / scc[i - 1].value - 1 });
}

const B = MODEL.BASE;
const realNet = (1 + B.portfolio) / (1 + B.inflation) - 1 - B.fee;
const PATH_YEARS = 30;
const DRAWS = 2000;
const sims = [];
for (let d = 0; d < DRAWS; d += 1) {
  const draws = [];
  while (draws.length < PATH_YEARS) {
    const start = Math.floor(rand() * (annual.length - 5));
    for (let k = 0; k < 5 && draws.length < PATH_YEARS; k += 1) draws.push(annual[start + k]);
  }
  const rates = draws.map((yr) => ({
    inflation: yr.inflation,
    home: yr.home,
    portfolio: (1 + realNet) * (1 + yr.inflation) - 1
  }));
  const rows = MODEL.runDraw(rates, {}, 2045);
  const last = rows[rows.length - 1];
  sims.push({ realSell: last.realSell, realRent: last.realRent, realLive: last.realLive, idx: rows[rows.length - 1].priceIndex });
}

out.bootstrap = {
  draws: DRAWS, years: PATH_YEARS,
  source: 'annual California CPI change (BOE LTA 2026/002) and Santa Clara County house-price change (FHFA via FRED), 1976-2025, resampled in consecutive five-year blocks; portfolio is a constant 5.0% nominal return less 0.5% fee, so its real return moves with the sampled inflation',
  real: {
    sell: ECO.stats(sims.map((s) => s.realSell)),
    rent: ECO.stats(sims.map((s) => s.realRent)),
    live: ECO.stats(sims.map((s) => s.realLive))
  },
  rentLeads: sims.filter((s) => s.realRent > s.realSell).length / sims.length,
  liveLeads: sims.filter((s) => s.realLive > s.realSell).length / sims.length
};
fs.writeFileSync(path.join(__dirname, 'data', 'snapshot.json'), JSON.stringify(out, null, 1));
console.log('wrote scripts/data/snapshot.json (no household data)');
