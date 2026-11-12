// Session f344fcd1. Test only: what happens to the published ranking if the rent benchmark for
// Property A were lower or higher than the FY2026 HUD figure the model uses.
// Reads every input from the published model; no household figure is typed here.
global.window = global;
require('../../site/data/model.js');
const M = window.MODEL, r10 = v => Math.round(v / 10) * 10;
const out = [];
for (const year of [2040, 2045, 2050]) {
  for (const f of [0.9, 1.0, 1.1]) {
    const cfg = { ...M.BASE, inheritYear: year, aRent4BR: M.BASE.aRent4BR * f };
    const d = M.decision(cfg, 10, '4BR');
    out.push({ year, rentFactor: f, monthlyRent: r10(cfg.aRent4BR), sell: r10(d.sell.terminal), rent: r10(d.rent.terminal), live: r10(d.live.terminal), sellTaxedAtEnd: r10(d.sell.terminalAfterLiquidation) });
  }
}
for (const o of out) { o.sellAheadOfRent = o.sell - o.rent; o.sellAheadOfRentBothTaxed = o.sellTaxedAtEnd - o.rent; }
console.log(JSON.stringify(out, null, 1));
