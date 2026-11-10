// Run with:  node --test model/test/
'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const E = require('../src/engine.js');
const I = require('../src/inputs.js');

const near = (a, b, tol, msg) => assert.ok(Math.abs(a - b) <= tol, `${msg || ''} expected ${b}, got ${a}`);
const base = () => I.defaults();

test('round10 rounds to the nearest $10, both signs, no negative zero', () => {
  assert.equal(E.round10(1234.99), 1230);
  assert.equal(E.round10(1235), 1240);
  assert.equal(E.round10(-1235), -1240);
  assert.equal(E.round10(4.9), 0);
  assert.ok(Object.is(E.round10(-4.9), 0));
  assert.equal(E.round10(1044586), 1044590);
});

test('Prop 19 formula reproduces the Board of Equalization worked example', () => {
  // BOE FAQ: factored base year value 300,000; market value 1,500,000; amount 1,000,000 -> 500,000
  const r = E.prop19TaxableValue(300000, 1500000, 1000000);
  assert.equal(r.excluded, 1300000);
  assert.equal(r.excess, 200000);
  assert.equal(r.taxable, 500000);
});

test('Prop 19 formula reproduces the Santa Clara County Assessor example', () => {
  // Assessor page: 200,000 taxable value; 1,800,000 market value -> 800,000
  assert.equal(E.prop19TaxableValue(200000, 1800000, 1000000).taxable, 800000);
});

test('Prop 19: below the limit the old taxable value is kept in full', () => {
  const r = E.prop19TaxableValue(550540, 1500000, 1044586);
  assert.equal(r.excess, 0);
  assert.equal(r.taxable, 550540);
});

test('Prop 19: above the limit the exclusion is worth exactly rate x amount', () => {
  const p = base();
  const fmv = 3100000, fbyv = p.aAv2026, amt = p.prop19Amount2025;
  const withExcl = E.propertyTax(E.prop19TaxableValue(fbyv, fmv, amt).taxable, p.aRate, 0);
  const without = E.propertyTax(fmv, p.aRate, 0);
  near(without - withExcl, p.aRate * amt, 1e-6);
});

test('Prop 19 amount: adjusted on 16 February of odd years only', () => {
  assert.equal(E.prop19Adjustments(2026), 0);
  assert.equal(E.prop19Adjustments(2027), 1);
  assert.equal(E.prop19Adjustments(2028), 1);
  assert.equal(E.prop19Adjustments(2029), 2);
  assert.equal(E.prop19Adjustments(2045), 10);
  assert.equal(E.prop19Adjustments(2050), 12);
  assert.equal(E.prop19Amount(2026, 1044586, 0.05), 1044586);
  near(E.prop19Amount(2029, 1044586, 0.05), 1044586 * 1.05 * 1.05, 1e-6);
});

test('Prop 19 amount: the published 2025 figure is one year of index change on the 2023 figure', () => {
  // Board of Equalization letter 2025/009: 1,022,600 x 1.0215 = 1,044,586
  assert.equal(Math.round(1022600 * 1.0215), 1044586);
});

test('Brief figures agree with the official 2026-27 inflation factor (1.02)', () => {
  const p = base();
  near(p.aAv2025 * 1.02, p.aAv2026, 10, 'assessed value 2026');
});

test('Fixed charges are defined so that the 2025 bill is reproduced exactly', () => {
  const p = base();
  const fa = E.fixedCharges(p.aBill2025, p.aRate, p.aAv2025);
  const fb = E.fixedCharges(p.bBill2025, p.bRate, p.bAv2025);
  near(E.propertyTax(p.aAv2025, p.aRate, fa), p.aBill2025, 1e-9);
  near(E.propertyTax(p.bAv2025, p.bRate, fb), p.bBill2025, 1e-9);
  assert.ok(fa > 0 && fa < 2000, 'A fixed charges plausible: ' + fa);
  // San Francisco parcel taxes read on the Treasurer page add up to at least $829 for three units
  assert.ok(fb > 829 && fb < 2000, 'B fixed charges not below the official parcel taxes: ' + fb);
});

test('Estate tax: published exclusions, 40% above, nothing below', () => {
  const p = base();
  assert.equal(E.estateExclusion(2026, p), 15000000);
  assert.equal(E.estateExclusion(2027, p), 15480000);
  near(E.estateExclusion(2028, p), 15480000 * (1 + p.estateIndexing), 1e-6);
  assert.equal(E.estateTax(15000000, 15000000, 0.4, 1).tax, 0);
  assert.equal(E.estateTax(16000000, 15000000, 0.4, 1).tax, 400000);
  assert.equal(E.estateTax(16000000, 15000000, 0.4, 2).tax, 0);
  assert.equal(E.estateTax(31000000, 15000000, 0.4, 2).tax, 400000);
});

test('Yearly series covers 2026 to 2050 and starts at the brief figures', () => {
  const p = base(), rows = E.yearlySeries(p);
  assert.equal(rows.length, 25);
  assert.equal(rows[0].year, 2026);
  assert.equal(rows[24].year, 2050);
  assert.equal(rows[0].aValue, p.aValue2026);
  assert.equal(rows[0].aAssessed, p.aAv2026);
  assert.equal(rows[0].prop19Amount, p.prop19Amount2025);
  near(rows[0].bAssessed, p.bAv2025 * 1.02, 1e-6);
  for (let i = 1; i < rows.length; i++) {
    near(rows[i].aAssessed / rows[i - 1].aAssessed, 1.02, 1e-12, 'Prop 13 2% step');
    assert.ok(rows[i].aLiveTaxable <= rows[i].aValue + 1e-6, 'excluded value never exceeds market value');
    assert.ok(rows[i].aLiveTaxable >= rows[i].aAssessed - 1e-6, 'never below the factored base year value');
    assert.ok(rows[i].aTaxOwner <= rows[i].aLiveTax && rows[i].aLiveTax <= rows[i].aFullTax);
  }
});

test('Account helper: level payment accumulates to the target', () => {
  const pay = E.levelPayment(1000000, 0.07, 10);
  const acct = E.runAccount(0, Array(10).fill(pay), 0.07);
  near(acct.balance, 1000000, 1e-6);
  near(E.levelPayment(1000, 0, 4), 250, 1e-12);
});

test('SELL: proceeds are value at death less selling cost, with no gains tax (stepped-up basis)', () => {
  const p = base(), s = E.simulate(p);
  near(s.sell.proceeds, s.valueAtDeath * (1 - p.sellCost), 1e-6);
  assert.equal(s.sell.saleTax, 0);
  near(s.sell.wealthHold, s.sell.proceeds * Math.pow(1 + p.investReturn, p.horizon), 1e-4);
  const growth = s.sell.wealthHold - s.sell.proceeds;
  near(s.sell.wealthLiquid, s.sell.proceeds + growth * (1 - p.taxGain), 1e-4);
});

test('Indifference: no costs, no taxes, no rent and equal growth rates give equal wealth', () => {
  const p = E.clone(base(), { sellCost: 0, taxGain: 0, taxOrdinary: 0, taxRecapture: 0, aInsurance: 0,
    aMaintenance: 0, aUtilities: 0, aRent2026: 0, bUnitRent2026: 0, aRate: 0, aBill2025: 0, investReturn: 0.05, aGrowth: 0.05 });
  const s = E.simulate(p);
  near(s.sell.wealthLiquid, s.live.wealthLiquid, 1e-3);
  near(s.sell.wealthLiquid, s.rent.wealthLiquid, 1e-3);
});

test('LIVE first-year cash equals the listed components', () => {
  const s = E.simulate(base()), y = s.live.years[0];
  near(y.cash, -(y.propertyTax + y.insurance + y.maintenance + y.utilities) + (y.unitRent - y.unitRentTax), 1e-6);
  near(y.taxableValue, s.prop19.taxable, 1e-6);
});

test('RENT: reassessed to full market value; depreciation on the building share over 27.5 years', () => {
  const p = base(), s = E.simulate(p), y = s.rent.years[0];
  near(y.taxableValue, s.valueAtDeath, 1e-6);
  near(y.depreciation, p.aBuildingShare * s.valueAtDeath / 27.5, 1e-6);
  near(y.noi, y.grossRent - y.propertyTax - y.insurance - y.maintenance - y.management, 1e-6);
  near(s.rent.accumulatedDepreciation, y.depreciation * p.horizon, 1e-6);
});

test('Sensitivity runs the right way', () => {
  const p = base();
  const a = E.simulate(p), b = E.simulate(E.clone(p, { investReturn: p.investReturn + 0.01 }));
  assert.ok(b.costOfLiving > a.costOfLiving, 'higher return makes living in A dearer');
  const c = E.simulate(E.clone(p, { aRent2026: p.aRent2026 + 1000 }));
  assert.ok(c.rent.wealthLiquid > a.rent.wealthLiquid, 'higher rent helps RENT');
  const d = E.simulate(E.clone(p, { aGrowth: p.aGrowth + 0.01 }));
  assert.ok(d.live.wealthLiquid - d.sell.wealthLiquid > a.live.wealthLiquid - a.sell.wealthLiquid, 'faster house growth helps LIVE relative to SELL');
});

test('Break-even rent and break-even return really are break-evens', () => {
  const p = base();
  const r = E.breakEvenRent(p);
  const s = E.simulate(E.clone(p, { aRent2026: r }));
  near(s.rent.wealthLiquid, s.sell.wealthLiquid, 1, 'rent break-even');
  for (const other of ['live', 'rent']) {
    const x = E.breakEvenReturn(p, other);
    const t = E.simulate(E.clone(p, { investReturn: x }));
    near(t.sell.wealthLiquid, t[other].wealthLiquid, 1, other + ' return break-even');
  }
});

test('Grid has nine cells and each names the highest strategy', () => {
  const g = E.grid(base(), I.SCENARIOS);
  assert.equal(g.length, 9);
  for (const c of g) {
    const max = Math.max(c.sell, c.live, c.rent);
    assert.equal(c[c.best.toLowerCase()], max);
  }
});

test('Scenario rates are the ones computed from the official index tables', () => {
  const cagr = (a, b, n) => Math.pow(b / a, 1 / n) - 1;
  const S = I.SCENARIOS.house;
  near(S.low.aGrowth, cagr(317.27, 558.75, 20), 5e-5);   // FHFA San Jose metro, 2006 Q2 -> 2026 Q2
  near(S.mid.aGrowth, cagr(367.05, 558.75, 10), 5e-5);
  near(S.high.aGrowth, cagr(104.42, 558.75, 30), 5e-5);
  near(S.low.bGrowth, cagr(306.74, 506.53, 20), 5e-5);   // FHFA San Francisco division
  near(S.mid.bGrowth, cagr(385.01, 506.53, 10), 5e-5);
  near(S.high.bGrowth, cagr(100.83, 506.53, 30), 5e-5);
  near(S.low.caHpiChange, cagr(643.96, 974.97, 20), 5e-5); // FHFA California
  near(S.mid.caHpiChange, cagr(553.43, 974.97, 10), 5e-5);
  near(S.high.caHpiChange, cagr(200.89, 974.97, 30), 5e-5);
  near(base().inflation, cagr(210.700, 370.130, 20), 5e-5); // BLS CPI-U San Francisco area, Aug 2006 -> Aug 2026
  near(base().estateIndexing, Math.pow((5.49 / 5.00) * (13.99 / 11.18) * (15.48 / 15.00), 1 / 14) - 1, 5e-5);
  near(I.SCENARIOS.returns.mid.investReturn, (0.0465 + 0.1140) / 2, 6e-5);
});

test('Property B today: net rent and the returns a sale would have to earn', () => {
  const p = base(), b = E.propertyB(p, I.BRIEF);
  assert.equal(b.rent, 85800);
  assert.equal(b.totalCosts, 2440 + 1500 + 365 * 12 + 50 * 12 + 9000);
  assert.equal(b.net, 85800 - b.totalCosts);
  near(b.saleNet, 1800000 * 0.94, 1e-6);
  near(b.taxMax, (1800000 * 0.94 - 114250) * p.taxGain, 1e-6);
  assert.ok(b.maxTax.toReplaceRent > b.noTax.toReplaceRent);
  near(b.noTax.toMatchEverything, (b.net + 3600 * 12 + 1800000 * p.bGrowth) / b.saleNet, 1e-12);
  near(b.taxIfReassessed, 1800000 * p.bRate + b.fixed, 1e-9);
});
