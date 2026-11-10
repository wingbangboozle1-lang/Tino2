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
ok(htmlFiles.length === 8, "eight dashboard pages");
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
