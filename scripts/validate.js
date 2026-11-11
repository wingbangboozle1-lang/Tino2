#!/usr/bin/env node
"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");
const root = path.resolve(__dirname, "..");
global.window = global;
require(path.join(root, "site/data/sources.js"));
require(path.join(root, "site/data/model.js"));
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
near(MODEL.seriesFor("A", 2027).assessed, 550537 * 1.02, 0.001, "Prop 13 assessment factoring");
near(MODEL.inheritanceValues(2026).primaryAssessed, 3100000 - 1044586, 0.001, "Prop 19 high-value formula");
near(MODEL.inheritanceValues(2026).allowance, 1044586, 0.001, "official current Prop 19 amount");
near(MODEL.seriesFor("B", 2026).assessed, 114248 * 1.02, 0.001, "Property B 2026 assessment scenario");
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
  for (const match of html.matchAll(/(?:UI\.source|src)\("([A-Za-z0-9]+)"/g)) {
    ok(Boolean(SOURCES[match[1]]), `${path.basename(file)} source key ${match[1]}`);
  }
}
// Black-swan scenario engine: assumptions stay inside sane bounds and the ranking is reproducible.
require(path.join(root, "site/data/scenarios.js"));
ok(SCENARIOS.DEFS.length === 7, "seven stress cases");
ok(SCENARIOS.INHERIT === 2045 && SCENARIOS.END === 2055, "transfer year and horizon");
const scenarioRows = SCENARIOS.runAll();
ok(scenarioRows.length === SCENARIOS.DEFS.length, "every case runs");
scenarioRows.forEach(({ def, result }) => {
  ok(["sell", "rent", "live"].includes(result.winner), `${def.id} has a winner`);
  ok(result.vAtInherit > 0 && result.sell.terminal > 0 && result.rent.terminal > 0 && result.live.terminal > 0, `${def.id} produces positive values`);
  ok(result.margin >= 0, `${def.id} margin is non-negative`);
  ok(def.sources.every(k => Boolean(SOURCES[k])), `${def.id} cites registered sources`);
  ok(result.live.housingAdjustedTerminal >= result.live.terminal, `${def.id} housing value is additive`);
  ok(result.fullTaxAtTransfer > result.primaryTaxAtTransfer, `${def.id} Prop 19 exclusion reduces tax`);
});
const stag = scenarioRows.find(r => r.def.id === "stagflation");
ok(stag.result.winner === "rent", "stagflation replay favours holding");
const baseRow = scenarioRows.find(r => r.def.id === "base").result;
near(baseRow.vAtInherit, MODEL.decision({ ...MODEL.BASE, inheritYear: 2045 }, 10).transfer.market, 1, "scenario engine matches the decision page value at 2045");
const refDecision = MODEL.decision({ ...MODEL.BASE, inheritYear: 2045 }, 10);
near(baseRow.sell.terminal, refDecision.sell.terminal, 1, "scenario engine matches the decision page sell terminal");
near(baseRow.rent.terminal, refDecision.rent.terminal, 1, "scenario engine matches the decision page rent terminal");
near(baseRow.live.terminal, refDecision.live.terminal, 1, "scenario engine matches the decision page live terminal");
near(baseRow.primaryTaxAtTransfer, refDecision.transfer.primaryTax, 0.5, "scenario engine matches the decision page Prop 19 tax");
const beHome = SCENARIOS.breakEvenHomeGrowth(SCENARIOS.DEFS[0]);
const bePort = SCENARIOS.breakEvenPortfolioReturn(SCENARIOS.DEFS[0]);
ok(beHome > 0.03 && beHome < 0.15, `break-even home growth is plausible: ${beHome}`);
ok(bePort > 0 && bePort < 0.10, `break-even portfolio return is plausible: ${bePort}`);
ok(SCENARIOS.quakeShock(0.10).hit > SCENARIOS.quakeShock(0.05).hit, "larger damage produces a larger hit");
ok(SCENARIOS.insuranceShock(0.12).rentDelta < SCENARIOS.insuranceShock(0.03).rentDelta, "faster premium growth costs more");
const expectation = SCENARIOS.expectation();
ok(expectation.sell > expectation.rent && expectation.sell > expectation.live, "weighted result favours selling");

const assets = ["assets/styles.css", "assets/app.js"];
assets.forEach(file => ok(fs.existsSync(path.join(root, file)), `${file} exists`));
new vm.Script(fs.readFileSync(path.join(root, "assets/app.js"), "utf8"), {filename: "app.js"}); checks += 1;
ok(fs.existsSync(path.join(root, ".nojekyll")), "GitHub Pages .nojekyll");
console.log(`PASS: ${checks} checks across ${htmlFiles.length} pages and ${Object.keys(SOURCES).length} official sources.`);
console.log(`Base case 2040→2050: sell ${MODEL.fmtMoney(baseDecision.sell.terminal)}, rent ${MODEL.fmtMoney(baseDecision.rent.terminal)}, live ${MODEL.fmtMoney(baseDecision.live.terminal)}.`);
