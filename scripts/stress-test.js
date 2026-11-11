'use strict';
const assert=require('node:assert/strict');
global.window=global;
require('../site/data/model.js');require('../site/data/stress.js');
assert.equal(MODEL.estateRow(2026).combined,3100000);
assert.equal(MODEL.estateRow(2026).headroom,11900000);
assert.equal(MODEL.estateRow(2026,{...MODEL.BASE,bValue:999999999}).headroom,11900000);
assert.equal(MODEL.historyA.length+MODEL.historyB.length,0);
for(const key of Object.keys(STRESS.paths)){
 const rows=STRESS.run(key);assert.equal(rows.length,50);
 assert.equal(rows[0].year,2046);assert.equal(rows.at(-1).year,2095);
 for(const r of rows){
  for(const k of ['sell','rent','live','tax','realSell']) assert(Number.isFinite(r[k]));
  assert(Math.abs(r.realSell*r.priceIndex-r.sell)<0.001);
 }
}
assert.equal(STRESS.rates('crisis',1).portfolio,-0.35);
assert.equal(STRESS.rates('late',48).home,-0.25);
assert.equal(STRESS.rates('disaster',10).repair,250000);
assert.equal(STRESS.rates('disaster',10).vacancy,1);
assert.equal(STRESS.rates('inflation',1).insuranceJump,2);
assert.equal(STRESS.rates('inflation',2).insuranceJump,1);
console.log('PASS: 50-year paths, estate ownership, privacy, real-dollar and shock tests');
