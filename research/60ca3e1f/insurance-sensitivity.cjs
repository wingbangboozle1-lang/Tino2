#!/usr/bin/env node
/* Sensitivity of the published model to the insurance premium.
   Reads site/data/model.js unchanged and re-runs it with the premium replaced by figures from the
   California Department of Insurance 2026 survey (hypothetical $1,000,000-dwelling profiles; not quotes).
   Run from the repository root:  node research/60ca3e1f/insurance-sensitivity.cjs            */
const fs = require("fs"), path = require("path"), vm = require("vm");
const root = path.resolve(__dirname, "..", "..");
const sandbox = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(root, "site/data/model.js"), "utf8"), sandbox);
const M = sandbox.window.MODEL;
const survey = JSON.parse(fs.readFileSync(path.join(__dirname, "insurance-survey-2026.json"), "utf8"));
const r10 = v => Math.round(v / 10) * 10;
const fmt = v => (v < 0 ? "-$" : "$") + Math.abs(r10(v)).toLocaleString("en-US");

const cup = survey.homeowners.cupertino_40y_1000000.deductible_2500;
const cup70 = survey.homeowners.cupertino_70y_1000000.deductible_2500;
const sun = survey.homeowners.sunset_70y_1000000.deductible_2500;
const casesA = [
  ["no premium at all", 0],
  ["household estimate (model)", M.BASE.aInsuranceAnnual],
  ["survey lowest, 40-yr profile", cup.lowest],
  ["survey median, 40-yr profile", cup.median],
  ["survey median, 70-yr profile", cup70.median],
  ["survey highest, 40-yr profile", cup.highest],
];
const out = { generated_from: "site/data/model.js + insurance-survey-2026.json", propertyA: [], propertyB: [] };
console.log("PROPERTY A — 10-year result by inheritance year (all figures rounded to $10)");
for (const year of [2040, 2045, 2050]) {
  for (const [label, premium] of casesA) {
    const d = M.decision({ ...M.BASE, inheritYear: year, aInsuranceAnnual: premium }, 10, "4BR");
    const first = M.annualA(year + 1, "live", { ...M.BASE, inheritYear: year, aInsuranceAnnual: premium });
    const tenYear = d.live.yearly.reduce((s, r) => s + r.insurance, 0);
    const row = { inheritYear: year, case: label, premium2026: premium, firstYearPremium: r10(first.insurance),
      tenYearPremium: r10(tenYear), sell: r10(d.sell.terminal), rent: r10(d.rent.terminal), live: r10(d.live.terminal),
      sellAheadOfRent: r10(d.sell.terminal - d.rent.terminal), sellAheadOfLive: r10(d.sell.terminal - d.live.terminal),
      winner: d.winner };
    out.propertyA.push(row);
    console.log(`${year}  ${label.padEnd(30)} 2026 premium ${fmt(premium).padStart(7)}  first yr ${fmt(first.insurance).padStart(8)}  10 yrs ${fmt(tenYear).padStart(9)}  sell-rent ${fmt(row.sellAheadOfRent).padStart(11)}  sell-live ${fmt(row.sellAheadOfLive).padStart(11)}  winner ${d.winner}`);
  }
}
console.log("\nPROPERTY B — 2026 net operating income (model, with reserves)");
for (const [label, premium] of [["household estimate (model)", M.BASE.bInsuranceAnnual], ["survey lowest, 70-yr profile", sun.lowest], ["survey median, 70-yr profile", sun.median], ["survey highest, 70-yr profile", sun.highest]]) {
  const r = M.sfAnnual(2026, { ...M.BASE, bInsuranceAnnual: premium }, true);
  out.propertyB.push({ case: label, premium2026: premium, noi2026: r10(r.noi), insurance2026: r10(r.insurance) });
  console.log(`${label.padEnd(30)} premium ${fmt(premium).padStart(8)}  NOI ${fmt(r.noi).padStart(9)}`);
}
fs.writeFileSync(path.join(__dirname, "insurance-sensitivity.json"), JSON.stringify(out, null, 1) + "\n");

/* ---- Premium growth: the model grows every cost at 3% a year. The Department's statewide data
   (SB 824 workbook, all residential policy forms, as published) give earned premium and earned exposure by year. */
const state = { 2018: [8334249009, 11375891, 230138], 2019: [9044982611, 11839399, 244019], 2020: [10318255470, 12037936, 264159],
                2021: [11410952105, 12222318, 273978], 2022: [12804226026, 12463909, 295495], 2023: [14217212455, 12580970, 324973] };
console.log("\nSTATEWIDE — earned premium per earned exposure (calculated from the two official columns)");
const avg = {};
for (const y of Object.keys(state)) { const [p, e, a] = state[y]; avg[y] = p / e; console.log(`${y}  ${fmt(p / e).padStart(7)}  avg Coverage A $${a.toLocaleString("en-US")}  premium per $1,000 of Coverage A ${(p / e / a * 1000).toFixed(2)}`); }
const g = Math.pow(avg[2023] / avg[2018], 1 / 5) - 1;
const gA = Math.pow(state[2023][2] / state[2018][2], 1 / 5) - 1;
console.log(`growth 2018 -> 2023: premium per exposure ${((avg[2023] / avg[2018] - 1) * 100).toFixed(1)}% total, ${(g * 100).toFixed(2)}% a year; average Coverage A ${(gA * 100).toFixed(2)}% a year`);
out.statewide = { averagePremiumPerExposure: Object.fromEntries(Object.entries(avg).map(([k, v]) => [k, Math.round(v)])), growthPerYear: +(g * 100).toFixed(2), coverageAGrowthPerYear: +(gA * 100).toFixed(2) };

/* Re-run the model with insurance alone growing at g instead of 3%. The model reads aInsuranceAnnual once per
   year-row, so a config whose aInsuranceAnnual returns premium(year)/1.03^n makes the model's own formula land on the
   intended premium. The first block proves the device: at 3% it must reproduce the published result exactly. */
function decisionWithGrowth(year, premium2026, growth) {
  const seq = []; for (const _ of ["rent", "live"]) for (let t = 1; t <= 10; t += 1) seq.push(year + t);
  let i = 0;
  const cfg = new Proxy({ ...M.BASE, inheritYear: year }, { get(target, key) {
    if (key !== "aInsuranceAnnual") return target[key];
    const n = seq[i++] - target.startYear;
    return premium2026 * Math.pow(1 + growth, n) / Math.pow(1 + target.expenseInflation, n);
  } });
  const d = M.decision(cfg, 10, "4BR");
  if (i !== seq.length) throw new Error("model read the premium " + i + " times, expected " + seq.length);
  return d;
}
console.log("\nPROPERTY A — insurance alone growing faster than the model's 3% (premium starts at the model's $1,500 in 2026)");
out.growth = [];
for (const year of [2040, 2045, 2050]) {
  const base = M.decision({ ...M.BASE, inheritYear: year }, 10, "4BR");
  const check = decisionWithGrowth(year, 1500, 0.03);
  if (Math.abs(check.rent.terminal - base.rent.terminal) > 1e-6 || Math.abs(check.live.terminal - base.live.terminal) > 1e-6) throw new Error("device does not reproduce the model");
  for (const [label, p0, gr] of [["model: $1,500 at 3%", 1500, 0.03], ["$1,500 at statewide pace", 1500, g], ["survey median at statewide pace", cup.median, g]]) {
    const d = decisionWithGrowth(year, p0, gr);
    const row = { inheritYear: year, case: label, growth: +(gr * 100).toFixed(2), firstYearPremium: r10(d.live.yearly[0].insurance), tenthYearPremium: r10(d.live.yearly[9].insurance),
      tenYearPremium: r10(d.live.yearly.reduce((s, r) => s + r.insurance, 0)), sellAheadOfRent: r10(d.sell.terminal - d.rent.terminal), sellAheadOfLive: r10(d.sell.terminal - d.live.terminal), winner: d.winner };
    out.growth.push(row);
    console.log(`${year}  ${label.padEnd(32)} yr1 ${fmt(row.firstYearPremium).padStart(8)}  yr10 ${fmt(row.tenthYearPremium).padStart(8)}  10 yrs ${fmt(row.tenYearPremium).padStart(9)}  sell-rent ${fmt(row.sellAheadOfRent).padStart(11)}  sell-live ${fmt(row.sellAheadOfLive).padStart(11)}  winner ${d.winner}`);
  }
}
console.log("\nPREMIUM PATH by year (rounded to $10)");
out.path = [];
for (const y of [2026, 2030, 2035, 2040, 2045, 2050, 2055, 2060]) {
  const n = y - 2026; const row = { year: y, est3: r10(1500 * 1.03 ** n), estG: r10(1500 * (1 + g) ** n), med3: r10(cup.median * 1.03 ** n), medG: r10(cup.median * (1 + g) ** n), sun3: r10(sun.median * 1.03 ** n), sunG: r10(sun.median * (1 + g) ** n) };
  out.path.push(row);
  console.log(`${y}  $1,500@3% ${fmt(row.est3).padStart(8)}  $1,500@${(g * 100).toFixed(1)}% ${fmt(row.estG).padStart(8)}  A median@3% ${fmt(row.med3).padStart(8)}  A median@${(g * 100).toFixed(1)}% ${fmt(row.medG).padStart(9)}  B median@3% ${fmt(row.sun3).padStart(8)}  B median@${(g * 100).toFixed(1)}% ${fmt(row.sunG).padStart(9)}`);
}
fs.writeFileSync(path.join(__dirname, "insurance-sensitivity.json"), JSON.stringify(out, null, 1) + "\n");
