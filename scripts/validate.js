#!/usr/bin/env node
"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");
const root = path.resolve(__dirname, "..");
global.window = global;
require(path.join(root, "site/data/sources.js"));
require(path.join(root, "site/data/model.js"));
require(path.join(root, "site/data/history.js"));
require(path.join(root, "site/data/scenarios.js"));
let checks = 0;
function ok(condition, message) {
  checks += 1;
  if (!condition) throw new Error(`Validation failed: ${message}`);
}
function near(actual, expected, tolerance, message) {
  ok(Number.isFinite(actual) && Math.abs(actual - expected) <= tolerance, `${message}: ${actual} != ${expected}`);
}

// Core model and source data.
near(MODEL.BASE.aValue + MODEL.BASE.bValue, 4900000, 0.001, "current real-estate total");
near(MODEL.estateRow(2026).headroom, 10100000, 0.001, "2026 real-estate-only headroom");
near(MODEL.seriesFor("A", 2027).assessed, 550540 * 1.02, 0.001, "Prop 13 assessment factoring");
near(MODEL.inheritanceValues(2026).primaryAssessed, 3100000 - 1044586, 0.001, "Prop 19 high-value formula");
near(MODEL.inheritanceValues(2026).allowance, 1044586, 0.001, "official current Prop 19 amount");
near(MODEL.seriesFor("B", 2026).assessed, 114250 * 1.02, 0.001, "Property B 2026 assessment scenario");
near(MODEL.sfAnnual(2026).grossRent, 7150 * 12, 0.001, "two-unit annual rent");
near(MODEL.sfAnnual(2026).fee, 118, 0.001, "two-unit Rent Board fee scenario");
near(MODEL.afterTaxPortfolioReturn(), 0.05, 1e-12, "after-tax portfolio return");
const baseDecision = MODEL.decision({...MODEL.BASE, inheritYear: 2040}, 10);
near(baseDecision.sell.initialNet, baseDecision.transfer.market * 0.94, 0.001, "immediate net sale");
near(baseDecision.sell.terminal, baseDecision.sell.initialNet * Math.pow(1.05, 10), 0.001, "portfolio terminal value");
near(baseDecision.live.gainExclusion, 250000, 0.001, "modeled primary-home exclusion");
near(baseDecision.rent.gainExclusion, 0, 0.001, "no rental home-sale exclusion");
ok(baseDecision.winner === "sell", "base-case financial winner");
ok(baseDecision.rent.firstYearCash > 0 && baseDecision.rent.firstYearCash < 5000, "base-case narrow rental margin");
const loss = MODEL.annualA(2041, "rent", {...MODEL.BASE, inheritYear: 2040, aRent4BR: 0});
ok(loss.afterTaxCash === loss.noi && loss.incomeTax === 0, "no tax refund for rental loss");
ok(MODEL.round10(12345) === 12350 && MODEL.round10(-12345) === -12340, "nearest-$10 rounding");
ok(MODEL.fmtMoney(null) === "—", "unknown values stay blank");
ok(Object.keys(SOURCES).length >= 35, "official source register coverage");
Object.entries(SOURCES).forEach(([key, source]) => {
  ok(source.url.startsWith("https://"), `${key} uses HTTPS`);
  ok(source.agency && source.title && source.note, `${key} has agency, title and note`);
});


// Privacy: published household history must already be rounded to the nearest $10.
[...MODEL.historyA, ...MODEL.historyB].forEach(r => {
  [r.tax, r.assessed].forEach(v => ok(v === null || v % 10 === 0, `household history value ${v} is a $10 multiple`));
});
ok(MODEL.BASE.aAssessed % 10 === 0 && MODEL.BASE.bAssessed2025 % 10 === 0, "base assessed inputs are $10 multiples");

// Scenario engine: constant-rate baseline must reproduce the Decision lab exactly.
const SC = window.SCEN;
for (const Y of [2040, 2045, 2050]) {
  for (const H of [5, 10, 20]) {
    const lab = MODEL.decision({...MODEL.BASE, inheritYear: Y}, H, "4BR");
    const eng = SC.simulate(SC.buildPath(SC.SCENARIOS[0]), Y, H, "4BR");
    near(eng.sell, lab.sell.terminal, 0.01, `engine sell ${Y}/${H}`);
    near(eng.rent, lab.rent.terminal, 0.01, `engine rent ${Y}/${H}`);
    near(eng.live, lab.live.terminal, 0.01, `engine live ${Y}/${H}`);
    near(eng.sellLiq, lab.sell.terminalAfterLiquidation, 0.01, `engine liquidation-taxed sell ${Y}/${H}`);
  }
}
ok(SC.SCENARIOS.length === 12, "twelve scenarios");
SC.SCENARIOS.forEach(sc => ok(Boolean(SOURCES[sc.source]), `scenario ${sc.id} has an official source key`));
// History data integrity against the downloaded CSV.
const csv = fs.readFileSync(path.join(root, "research/data/fred_annual_2026-11-11.csv"), "utf8").trim().split("\n").slice(1).map(l => l.split(","));
ok(csv.length === window.HISTORY.rows.length, "history row count matches CSV");
csv.forEach((cells, i) => { ok(Number(cells[0]) === window.HISTORY.rows[i][0] && Number(cells[1]) === window.HISTORY.rows[i][1], `history row ${cells[0]} matches CSV`); });
near(SC.H[2025].cpi / SC.H[2024].cpi - 1, 321.943 / 313.689 - 1, 1e-12, "CPI 2025 change");
// Prop 19 formula against BOE letter 2026/026: new taxable value = factored base + (market - (factored base + cap)) when market exceeds the limit.
const tx = MODEL.inheritanceValues(2026);
near(tx.primaryAssessed, tx.carryForwardAssessed + (tx.market - (tx.carryForwardAssessed + 1044586)), 0.001, "BOE excess-amount formula");
// Deterministic Monte Carlo.
const mcA = SC.monteCarlo({paths: 200}), mcB = SC.monteCarlo({paths: 200});
near(mcA.summary[2045].p50.sell, mcB.summary[2045].p50.sell, 1e-9, "Monte Carlo is seeded and reproducible");
ok(mcA.summary[2045].sellBeatsRent > 0 && mcA.summary[2045].sellBeatsRent < 1, "Monte Carlo produces mixed outcomes");

// HTML syntax, internal links and source references.
const htmlFiles = [path.join(root, "index.html"), ...fs.readdirSync(path.join(root, "site")).filter(f => f.endsWith(".html")).map(f => path.join(root, "site", f))];
ok(htmlFiles.length === 9, "nine dashboard pages");
for (const file of htmlFiles) {
  const html = fs.readFileSync(file, "utf8");
  ok(html.includes('name="viewport"'), `${path.basename(file)} responsive viewport`);
  ok(html.includes('name="robots" content="noindex,nofollow,noarchive"'), `${path.basename(file)} privacy robots directive`);
  ok(!/@import|fonts\.googleapis|localhost|127\.0\.0\.1/.test(html), `${path.basename(file)} no external fonts or browser localhost dependency`);
  for (const match of html.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g)) {
    new vm.Script(match[1], {filename: path.basename(file)});
    checks += 1;
  }
  for (const match of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
    const ref = match[1];
    if (/^(?:https?:|mailto:|#|javascript:)/.test(ref) || ref.includes("${")) continue;
    const clean = ref.split("#")[0].split("?")[0];
    if (!clean) continue;
    const target = path.resolve(path.dirname(file), clean);
    ok(fs.existsSync(target), `${path.basename(file)} local reference ${ref}`);
  }
  for (const match of html.matchAll(/UI\.source\("([A-Za-z0-9]+)"/g)) {
    ok(Boolean(SOURCES[match[1]]), `${path.basename(file)} source key ${match[1]}`);
  }
}
const assets = ["assets/styles.css", "assets/app.js"];
assets.forEach(file => ok(fs.existsSync(path.join(root, file)), `${file} exists`));
new vm.Script(fs.readFileSync(path.join(root, "assets/app.js"), "utf8"), {filename: "app.js"}); checks += 1;
ok(fs.existsSync(path.join(root, ".nojekyll")), "GitHub Pages .nojekyll");
console.log(`PASS: ${checks} checks across ${htmlFiles.length} pages and ${Object.keys(SOURCES).length} official sources.`);
console.log(`Base case 2040→2050: sell ${MODEL.fmtMoney(baseDecision.sell.terminal)}, rent ${MODEL.fmtMoney(baseDecision.rent.terminal)}, live ${MODEL.fmtMoney(baseDecision.live.terminal)}.`);
