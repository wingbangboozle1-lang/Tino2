#!/usr/bin/env node
/*
 * Site generator — session 5a1bd5be.   Run:  node model/build.js
 * Writes model/*.html from model/src (engine, inputs, sources, flags). Every figure on the
 * pages is computed here from those files; none is typed into the text by hand.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const E = require('./src/engine.js');
const I = require('./src/inputs.js');
const S = require('./src/sources.js');
const FL = require('./src/flags.js');
const Fmt = require('./src/format.js');
const L = require('./lib.js');
const P = require('./pages.js');

const OUT = __dirname;
const p0 = I.defaults();
const sim = over => E.simulate(E.clone(p0, over || {}));
const field = {};
I.FIELDS.forEach(f => { field[f.key] = f; });

// ---- integrity of the data files (fail the build rather than publish a gap)
const flagIds = new Set(FL.FLAGS.map(f => f.id));
for (const f of I.FIELDS) {
  for (const id of f.src) if (!S.byId[id]) throw new Error(`Input ${f.key}: unknown source ${id}`);
  if (f.flag && !flagIds.has(f.flag)) throw new Error(`Input ${f.key}: unknown flag ${f.flag}`);
  if ((f.status === 'assumption' || f.status === 'brief') && !f.flag && !f.src.length) throw new Error(`Input ${f.key}: needs a flag or a source`);
  if ((f.status === 'verified' || f.status === 'calculated') && !f.src.length) throw new Error(`Input ${f.key}: ${f.status} needs a source`);
}
for (const f of FL.FLAGS) for (const id of f.src) if (!S.byId[id]) throw new Error(`Flag ${f.id}: unknown source ${id}`);
const urls = new Set();
for (const s of S.SOURCES) {
  if (!/^https:\/\//.test(s.url)) throw new Error(`Source ${s.id}: URL must be https`);
  if (urls.has(s.url)) throw new Error(`Source ${s.id}: duplicate URL`);
  urls.add(s.url);
}

// ---- everything the pages need, computed once
const base = sim();
const ctx = {
  E, I, S, FL, Fmt, L, p0, sim, field, base,
  B: E.propertyB(p0, I.BRIEF),
  series: E.yearlySeries(p0),
  grid: E.grid(p0, I.SCENARIOS),
  beRent: E.breakEvenRent(p0),
  beLive: E.breakEvenReturn(p0, 'live'),
  beRentRet: E.breakEvenReturn(p0, 'rent'),
  real: (x, year) => x / Math.pow(1 + p0.inflation, year - E.BASE_YEAR),
  builtAt: new Date().toISOString().slice(0, 16).replace('T', ' ') + ' UTC'
};
try { ctx.report = require('./check.js').run(); ctx.reportSummary = require('./check.js').summarise(ctx.report); }
catch (e) { throw new Error('Tree scan failed: ' + e.message); }

const pages = P.build(ctx);
for (const file of Object.keys(pages)) fs.writeFileSync(path.join(OUT, file), pages[file]);

// machine-readable copy of the headline results, for anyone who wants to diff two builds
const r10 = Fmt.round10;
const out = {
  note: 'Model results, rounded to the nearest $10. Session 5a1bd5be.',
  defaults: { inheritYear: p0.inheritYear, horizon: p0.horizon, houseGrowthA: p0.aGrowth, investReturn: p0.investReturn, inflation: p0.inflation },
  cases: [2040, 2045, 2050].map(T => [10, 20].map(H => { const s = sim({ inheritYear: T, horizon: H });
    return { inheritYear: T, horizon: H, valueAtInheritance: r10(s.valueAtDeath), sell: r10(s.sell.wealthLiquid), live: r10(s.live.wealthLiquid), rent: r10(s.rent.wealthLiquid), best: s.best }; })).flat(),
  grid: ctx.grid.map(g => ({ house: g.house, returns: g.returns, sell: r10(g.sell), live: r10(g.live), rent: r10(g.rent), best: g.best })),
  breakEven: { rentPerMonth2026Dollars: r10(ctx.beRent), returnVersusLiving: Math.round(ctx.beLive * 1e4) / 1e4, returnVersusRenting: Math.round(ctx.beRentRet * 1e4) / 1e4 }
};
fs.writeFileSync(path.join(OUT, 'results.json'), JSON.stringify(out, null, 2) + '\n');
console.log(`Wrote ${Object.keys(pages).length} pages and results.json to ${path.relative(process.cwd(), OUT) || '.'}/`);
