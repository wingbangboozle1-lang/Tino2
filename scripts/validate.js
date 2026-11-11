#!/usr/bin/env node
"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");
const root = path.resolve(__dirname, "..");
global.window = global;
require(path.join(root, "site/data/sources.js"));
require(path.join(root, "site/data/costs.js"));
require(path.join(root, "site/data/model.js"));
require(path.join(root, "site/data/history.js"));
require(path.join(root, "site/data/history-engine.js"));
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
near(MODEL.estateRow(2026).headroom, 11900000, 0.001, "2026 real-estate-only headroom");
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
ok(baseDecision.rent.firstYearCash > 0 && baseDecision.rent.firstYearCash < 20000, "base-case narrow rental margin");
const loss = MODEL.annualA(2041, "rent", {...MODEL.BASE, inheritYear: 2040, aRent4BR: 0});
ok(loss.afterTaxCash === loss.noi && loss.incomeTax === 0, "no tax refund for rental loss");
ok(MODEL.round10(12345) === 12350 && MODEL.round10(-12345) === -12340, "nearest-$10 rounding");
ok(MODEL.fmtMoney(null) === "—", "unknown values stay blank");
ok(Object.keys(SOURCES).length >= 35, "official source register coverage");
Object.entries(SOURCES).forEach(([key, source]) => {
  ok(source.url.startsWith("https://"), `${key} uses HTTPS`);
  ok(source.agency && source.title && source.note, `${key} has agency, title and note`);
});

// Recorded-data engine (site/black-swan.html): constant-rate baseline must reproduce the Decision lab exactly.
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
ok(SC.SCENARIOS.length === 12, "twelve recorded-data scenarios");
SC.SCENARIOS.forEach(sc => ok(Boolean(SOURCES[sc.source]), `scenario ${sc.id} has a source key`));
const csv = fs.readFileSync(path.join(root, "research/data/fred_annual_2026-11-11.csv"), "utf8").trim().split("\n").slice(1).map(l => l.split(","));
ok(csv.length === window.HISTORY.rows.length, "history row count matches the FRED CSV");
csv.forEach((cells, i) => ok(window.HISTORY.columns.every((c, j) => (cells[j] === "" ? window.HISTORY.rows[i][j] === null : Number(cells[j]) === window.HISTORY.rows[i][j])), `history row ${cells[0]} matches the FRED CSV`));
near(SC.H[2025].cpi / SC.H[2024].cpi - 1, 321.943 / 313.689 - 1, 1e-12, "CPI 2025 change");
const mcA = SC.monteCarlo({paths: 200}), mcB = SC.monteCarlo({paths: 200});
near(mcA.summary[2045].p50.sell, mcB.summary[2045].p50.sell, 1e-9, "Monte Carlo is seeded and reproducible");
ok(mcA.summary[2045].sellBeatsRent > 0 && mcA.summary[2045].sellBeatsRent < 1, "Monte Carlo produces mixed outcomes");
near(MODEL.modelAllowance(2026), 1044586, 1e-9, "Prop 19 amount in the current BOE period");
near(MODEL.modelAllowance(2030), 1044586 * Math.pow(1.035, 2), 1e-6, "Prop 19 amount: one year of growth per biennial step (BOE LTA 2023/012, 2025/009)");
near(MODEL.modelAllowance(2040), 1044586 * Math.pow(1.035, 7), 1e-6, "Prop 19 amount: seven biennial steps by 2040");
near(MODEL.estateRow(2027).exclusion, 15480000, 1e-9, "official 2027 federal basic exclusion (IRS IR-2026-133)");
near(MODEL.estateRow(2026).exclusion, 15000000, 1e-9, "official 2026 federal basic exclusion");

// HTML syntax, internal links and source references.
const htmlFiles = [path.join(root, "index.html"), ...fs.readdirSync(path.join(root, "site")).filter(f => f.endsWith(".html")).map(f => path.join(root, "site", f))];
ok(htmlFiles.length === 15, "fifteen dashboard pages");
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

// Options page (session 0d6ec51e): the published engine must agree with the independently written
// calculation kept in verification/0d6ec51e/, and must reproduce the Decision page at its end points.
require(path.join(root, "site/data/options.js"));
const optRef = JSON.parse(fs.readFileSync(path.join(root, "verification/0d6ec51e/options.json"), "utf8"));
const r10 = v => Math.round(v / 10) * 10;
ok(optRef.checks.every(c => c.ok), "independent calculation passes its own self-checks");
optRef.delay.forEach(d => ["live", "rent", "empty"].forEach(mode =>
  near(r10(OPTIONS.holdThenSell(d.inherit, d.yearsHeld, mode).terminal), d[mode], 0.001, `hold ${d.yearsHeld}y then sell (${mode}) ${d.inherit}`)));
optRef.depreciation.forEach(d => near(r10(OPTIONS.rentWithDepreciation(d.inherit, d.buildingShare).terminal), d.rentWithDepreciation, 0.001, `rental with depreciation ${d.inherit} at ${d.buildingShare}`));
optRef.carryForward.forEach(d => { const x = OPTIONS.oldRule(d.inherit); near(r10(x.rent), d.rentCarryForward, 0.001, `old-rule rent ${d.inherit}`); near(r10(x.live), d.liveCarryForward, 0.001, `old-rule live ${d.inherit}`); });
optRef.estate.forEach(d => near(r10(OPTIONS.estate(d.year, d.money).tax), d.tax, 0.001, `estate tax ${d.year} at ${d.money}`));
optRef.probate.forEach(d => near(r10(OPTIONS.probate(MODEL.seriesFor("A", d.year).market)), d.each, 0.001, `probate fee ${d.year}`));
optRef.propertyB.forEach(d => near(r10(OPTIONS.propertyB(d.year).avoided), d.saved, 0.001, `Property B tax avoided ${d.year}`));
for (const Y of [2040, 2045, 2050]) {
  const lab = MODEL.decision({ ...MODEL.BASE, inheritYear: Y }, 10);
  near(OPTIONS.holdThenSell(Y, 10, "rent").terminal, lab.rent.terminal, 0.01, `ten-year rent equals the Decision page ${Y}`);
  near(OPTIONS.holdThenSell(Y, 10, "live").terminal, lab.live.terminal, 0.01, `ten-year live equals the Decision page ${Y}`);
  near(OPTIONS.rentWithDepreciation(Y, 0).terminal, lab.rent.terminal, 0.01, `no depreciation equals the Decision page ${Y}`);
  ok(OPTIONS.holdThenSell(Y, 2, "live").vsSellNow < 0 && OPTIONS.holdThenSell(Y, 1, "empty").vsSellNow < OPTIONS.holdThenSell(Y, 1, "rent").vsSellNow, `waiting costs money ${Y}`);
  ok(OPTIONS.oldRule(Y).sellLead > 0 && OPTIONS.oldRule(Y).sellLead < OPTIONS.oldRule(Y).sellLeadNow, `old rule narrows but does not reverse the lead ${Y}`);
}
near(OPTIONS.probate(1000000), 23000, 1e-6, "Probate Code schedule on $1,000,000");
near(OPTIONS.estate(2027, 0).startsAt, 15480000 - MODEL.seriesFor("A", 2027).market, 1e-6, "money at which estate tax starts in 2027");
near(OPTIONS.estate(2027, OPTIONS.estate(2027, 0).startsAt + 1000000).tax, 400000, 1e-6, "40% on the first $1,000,000 above the exclusion");

const assets = ["assets/styles.css", "assets/app.js"];
assets.forEach(file => ok(fs.existsSync(path.join(root, file)), `${file} exists`));
new vm.Script(fs.readFileSync(path.join(root, "assets/app.js"), "utf8"), {filename: "app.js"}); checks += 1;
ok(fs.existsSync(path.join(root, "_config.yml")), "GitHub Pages publication exclusions");
console.log(`PASS: ${checks} checks across ${htmlFiles.length} pages and ${Object.keys(SOURCES).length} official sources.`);
console.log(`Base case 2040→2050: sell ${MODEL.fmtMoney(baseDecision.sell.terminal)}, rent ${MODEL.fmtMoney(baseDecision.rent.terminal)}, live ${MODEL.fmtMoney(baseDecision.live.terminal)}.`);
