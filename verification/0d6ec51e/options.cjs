#!/usr/bin/env node
/*
  Session 0d6ec51e — strategies and rules the published model does not cover.

  A separately written calculation. It holds NO household figure: every input is read at run time
  from the published model (site/data/model.js, object MODEL.BASE). Legal parameters typed here are
  amounts published by a government body; each is listed in LAW below with its official page.

  Run:  node verification/0d6ec51e/options.cjs            (prints tables, writes options.json)
        node verification/0d6ec51e/options.cjs --check    (exit 1 if a self-check fails)
*/
const fs = require('fs'), path = require('path'), vm = require('vm');
const root = path.resolve(__dirname, '..', '..');
const sandbox = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(root, 'site/data/model.js'), 'utf8'), sandbox);
const M = sandbox.window.MODEL, B = M.BASE;

// Official parameters (not household data). Source pages are recorded in research/0d6ec51e/completeness-ledger.md.
const LAW = {
  recoveryYears: 27.5,            // IRS Pub. 527: residential rental property, straight line, 27.5 years
  recaptureFederalMax: 0.25,      // IRS Topic 409: unrecaptured section 1250 gain, maximum 25%
  capitalGainFederalMax: 0.20,    // IRS Topic 409: 20% top rate on net capital gain
  homeSaleExclusion: 250000,      // IRS Topic 701: up to $250,000 ($500,000 joint return)
  homeSaleYears: 2,               // IRS Topic 701: owned and used 24 months of the last 5 years
  estateTopRate: 0.40,            // IRS Form 706 instructions, Table A: over $1,000,000, 40% of the excess
  probate: [[100000, 0.04], [100000, 0.03], [800000, 0.02], [9000000, 0.01], [15000000, 0.005]] // Probate Code 10800, 10810
};

const r10 = v => Math.round(v / 10) * 10;
const H = 10;
const YEARS = [2040, 2045, 2050];
const cfg = T => ({ ...B, inheritYear: T });
const ret = M.afterTaxPortfolioReturn(B);

/* ---------- 1. Hold the house k years, then sell and invest to the same endpoint ---------- */
// mode: 'live' (heir's home, partial Prop 19 relief), 'rent' (full reassessment), 'empty' (full reassessment, no rent)
function holdThenSell(T, k, mode, opts = {}) {
  const c = cfg(T), inh = M.inheritanceValues(T, c);
  if (k === 0) {
    const net = inh.market * (1 - c.saleCost);
    return { atSale: net, terminal: net * Math.pow(1 + ret, H), taxAtSale: 0, reserveAtSale: 0 };
  }
  let reserve = 0;
  for (let t = 1; t <= k; t += 1) {
    const row = M.annualA(T + t, mode === 'empty' ? 'rent' : mode, c);
    let cash;
    if (mode === 'empty') cash = -(row.propertyTax + row.water + row.insurance + row.maintenance - row.solarCredit);
    else cash = row.afterTaxCash;
    if (opts.carryForward) {                 // pre-2021 rule: no reassessment on a parent-child transfer
      const assessedCF = inh.carryForwardAssessed * Math.pow(1 + c.assessmentGrowth, t);
      const saved = row.propertyTax - assessedCF * c.aRate;
      if (mode === 'rent') { const noi = row.noi + saved; cash = noi - Math.max(0, noi) * c.ordinaryTax; }
      else cash += saved;
    }
    reserve = reserve * (1 + ret) + cash;
  }
  const market = M.seriesFor('A', T + k, c).market;
  const realized = market * (1 - c.saleCost);
  const gain = Math.max(0, realized - inh.market);
  const excl = mode === 'live' && k >= LAW.homeSaleYears ? Math.min(LAW.homeSaleExclusion, gain) : 0;
  const tax = (gain - excl) * c.capitalGainsTax;
  const atSale = realized - tax + reserve;
  return { atSale, terminal: atSale * Math.pow(1 + ret, H - k), taxAtSale: tax, reserveAtSale: reserve, exclusion: excl };
}

/* ---------- 2. Rental case with depreciation (the published model leaves it out) ---------- */
function rentWithDepreciation(T, buildingShare) {
  const c = cfg(T), inh = M.inheritanceValues(T, c);
  const dep = buildingShare * inh.market / LAW.recoveryYears;      // full-year amounts; mid-month convention ignored
  let reserve = 0, suspended = 0, taxSavedYearly = 0;
  for (let t = 1; t <= H; t += 1) {
    const row = M.annualA(T + t, 'rent', c);
    const taxable = row.noi - dep;
    const tax = Math.max(0, taxable) * c.ordinaryTax;
    if (taxable < 0) suspended += -taxable;                         // passive loss carried forward (no special allowance assumed)
    taxSavedYearly += row.incomeTax - tax;
    reserve = reserve * (1 + ret) + (row.noi - tax);
  }
  const market = M.seriesFor('A', T + H, c).market;
  const realized = market * (1 - c.saleCost);
  const taken = dep * H;
  const gainAboveBasis = Math.max(0, realized - inh.market);
  const recaptureRate = c.capitalGainsTax + (LAW.recaptureFederalMax - LAW.capitalGainFederalMax);
  const taxOnSale = gainAboveBasis * c.capitalGainsTax + taken * recaptureRate;
  const released = suspended * c.ordinaryTax;                        // suspended losses deductible in the year of sale
  const terminal = realized - taxOnSale + released + reserve;
  return { dep, taken, suspended, recaptureRate, taxOnSale, released, taxSavedYearly, terminal };
}

/* ---------- 3. Federal estate tax by amount of money in the estate ---------- */
function estateTax(year, money) {
  const row = M.estateRow(year, B);
  const over = Math.max(0, row.a + money - row.exclusion);
  return { year, a: row.a, exclusion: row.exclusion, money, over, tax: over * LAW.estateTopRate };
}

/* ---------- 4. Statutory probate compensation if the house is not held in the trust ---------- */
function probateFee(value) {
  let left = value, fee = 0;
  for (const [band, rate] of LAW.probate) { const part = Math.min(left, band); fee += part * rate; left -= part; if (left <= 0) break; }
  return fee;                                                         // above $25,000,000: set by the court, not computed
}

/* ---------- 5. Property B: yearly property tax avoided by keeping its assessed value ---------- */
function bAdvantage(year) {
  const s = M.seriesFor('B', year, B);
  return { year, market: s.market, assessed: s.assessed, taxNow: s.tax, taxIfReassessed: s.market * s.rate, saved: (s.market - s.assessed) * s.rate };
}

/* ---------- run ---------- */
const out = { generated: 'from site/data/model.js; no household figure typed in this script', horizonYears: H, portfolioReturn: ret, checks: [], delay: [], carryForward: [], depreciation: [], estate: [], probate: [], propertyB: [] };
let failed = 0;
function check(name, mine, published) {
  const ok = Math.abs(mine - published) < 0.5;
  if (!ok) failed += 1;
  out.checks.push({ name, mine: r10(mine), published: r10(published), ok });
}
for (const T of YEARS) {
  const d = M.decision(cfg(T), H);
  check(`${T}: sell now equals published sell`, holdThenSell(T, 0, 'rent').terminal, d.sell.terminal);
  check(`${T}: rent ${H} years equals published rent`, holdThenSell(T, H, 'rent').terminal, d.rent.terminal);
  check(`${T}: live ${H} years equals published live`, holdThenSell(T, H, 'live').terminal, d.live.terminal);
  check(`${T}: depreciation at 0% building share equals published rent`, rentWithDepreciation(T, 0).terminal, d.rent.terminal);
  for (const k of [0, 1, 2, 3, 5, 7, 10]) {
    const live = holdThenSell(T, k, 'live'), rent = holdThenSell(T, k, 'rent'), empty = holdThenSell(T, k, 'empty');
    out.delay.push({ inherit: T, yearsHeld: k, live: r10(live.terminal), rent: r10(rent.terminal), empty: r10(empty.terminal),
      liveVsSellNow: r10(live.terminal - d.sell.terminal), rentVsSellNow: r10(rent.terminal - d.sell.terminal), emptyVsSellNow: r10(empty.terminal - d.sell.terminal),
      homeSaleExclusionUsed: r10(live.exclusion || 0) });
  }
  const inh = M.inheritanceValues(T, cfg(T));
  const cfRent = holdThenSell(T, H, 'rent', { carryForward: true }), cfLive = holdThenSell(T, H, 'live', { carryForward: true });
  const first = M.annualA(T + 1, 'rent', cfg(T));
  out.carryForward.push({ inherit: T, sell: r10(d.sell.terminal), sellTaxedAtEnd: r10(d.sell.terminalAfterLiquidation),
    rentCurrentLaw: r10(d.rent.terminal), rentCarryForward: r10(cfRent.terminal), liveCurrentLaw: r10(d.live.terminal), liveCarryForward: r10(cfLive.terminal),
    firstYearTaxCurrentLawRent: r10(first.propertyTax), firstYearTaxCarryForward: r10(inh.carryForwardAssessed * (1 + B.assessmentGrowth) * B.aRate),
    sellMinusRent: r10(d.sell.terminal - cfRent.terminal), sellTaxedMinusRent: r10(d.sell.terminalAfterLiquidation - cfRent.terminal) });
  for (const share of [0.2, 0.3, 0.4]) {
    const x = rentWithDepreciation(T, share);
    out.depreciation.push({ inherit: T, buildingShare: share, yearlyDeduction: r10(x.dep), incomeTaxSavedOverHold: r10(x.taxSavedYearly), lossesCarriedToSale: r10(x.suspended),
      extraTaxAtSale: r10(x.taken * x.recaptureRate), valueOfReleasedLosses: r10(x.released), recaptureRate: Math.round(x.recaptureRate * 1000) / 1000,
      rentWithDepreciation: r10(x.terminal), rentPublished: r10(d.rent.terminal), change: r10(x.terminal - d.rent.terminal), sellStillAheadBy: r10(d.sell.terminal - x.terminal) });
  }
}
for (const year of [2027, 2040, 2045, 2050]) for (const money of [2500000, 5000000, 10000000, 15000000, 20000000, 25000000]) {
  const e = estateTax(year, money);
  out.estate.push({ year, propertyA: r10(e.a), exclusion: r10(e.exclusion), exclusionOfficial: year <= 2027, money, over: r10(e.over), tax: r10(e.tax), taxShareOfMoney: money ? Math.round(e.tax / money * 1000) / 10 : 0 });
}
for (const year of [2026, 2040, 2045, 2050]) {
  const v = M.seriesFor('A', year, B).market, f = probateFee(v);
  out.probate.push({ year, value: r10(v), each: r10(f), both: r10(2 * f) });
  const b = bAdvantage(year);
  out.propertyB.push({ year, market: r10(b.market), assessed: r10(b.assessed), taxNow: r10(b.taxNow), taxIfReassessed: r10(b.taxIfReassessed), saved: r10(b.saved) });
}
// arithmetic self-checks that do not depend on the model
check('probate schedule on $1,000,000 is $23,000', probateFee(1000000), 23000);
check('probate schedule on $10,000,000 is $113,000', probateFee(10000000), 113000);
check('estate tax is zero at the exclusion', estateTax(2027, M.estateRow(2027, B).exclusion - M.estateRow(2027, B).a).tax, 0);

fs.writeFileSync(path.join(__dirname, 'options.json'), JSON.stringify(out, null, 1) + '\n');
const fm = v => (v < 0 ? '-' : '') + '$' + Math.abs(v).toLocaleString('en-US');
console.log('Self-checks:'); out.checks.forEach(c => console.log(` ${c.ok ? 'PASS' : 'FAIL'}  ${c.name}  mine ${fm(c.mine)}  published ${fm(c.published)}`));
console.log('\nHold k years, then sell and invest (difference from selling at once):');
out.delay.forEach(d => console.log(` ${d.inherit} k=${String(d.yearsHeld).padStart(2)}  live ${fm(d.liveVsSellNow).padStart(12)}  rent ${fm(d.rentVsSellNow).padStart(12)}  empty ${fm(d.emptyVsSellNow).padStart(12)}`));
console.log('\nNo reassessment for a child (pre-2021 rule restored):'); out.carryForward.forEach(d => console.log(' ' + JSON.stringify(d)));
console.log('\nDepreciation in the rental case:'); out.depreciation.forEach(d => console.log(' ' + JSON.stringify(d)));
console.log('\nEstate tax by money:'); out.estate.forEach(d => console.log(` ${d.year} excl ${fm(d.exclusion)} A ${fm(d.propertyA)} money ${fm(d.money)} -> tax ${fm(d.tax)} (${d.taxShareOfMoney}%)`));
console.log('\nProbate:'); out.probate.forEach(d => console.log(' ' + JSON.stringify(d)));
console.log('\nProperty B:'); out.propertyB.forEach(d => console.log(' ' + JSON.stringify(d)));
console.log(failed ? `\nFAIL: ${failed} self-check(s)` : `\nPASS: ${out.checks.length} self-checks`);
if (process.argv.includes('--check') && failed) process.exit(1);
