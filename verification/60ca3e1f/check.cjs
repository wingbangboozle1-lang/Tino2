#!/usr/bin/env node
/* Session 60ca3e1f — checks of what this session researched and published on 12 Nov 2026.

   Run from the repository root:
     python3 scripts/package-site.py
     node verification/60ca3e1f/check.cjs
   Part 7 renders the packaged page with jsdom (installed by the repo's own runtime test under
   .cache/test). If jsdom is not there, part 7 is reported as skipped, not as passed.

   What this script cannot do: open the official pages. The sandbox has no route to them, so the
   figures were read with the page-reading tool and typed in. Part 1 compares the typed figures with
   a second, separate reading of the same official page made about 35 minutes after the first.      */
const fs = require("fs"), path = require("path"), vm = require("vm");
const root = path.resolve(__dirname, "..", "..");
const read = f => fs.readFileSync(path.join(root, f), "utf8");
const results = [];
let failed = 0;
function ok(cond, label, detail) {
  results.push({ check: label, result: cond ? "pass" : "FAIL", ...(detail ? { detail } : {}) });
  if (!cond) { failed += 1; console.log("FAIL  " + label + (detail ? "  → " + detail : "")); }
}
const r10 = v => Math.round(v / 10) * 10;
const median = a => { const v = [...a].sort((x, y) => x - y), n = v.length; return n % 2 ? v[(n - 1) / 2] : (v[n / 2 - 1] + v[n / 2]) / 2; };
const section = t => console.log("\n" + t);

const survey = JSON.parse(read("research/60ca3e1f/insurance-survey-2026.json"));
const sens = JSON.parse(read("research/60ca3e1f/insurance-sensitivity.json"));

/* ---------- 1. second reading of one official page ---------- */
section("1. Typed figures against a second reading of the official page");
// Cupertino, 40-year-old home, $1,000,000 dwelling: first 25 rows of the result page as read again
// at about 05:05 UTC on 12 Nov 2026 (company, $2,500 deductible, $5,000 deductible; null = N/A).
const second = [
  ["Aegis Security Ins Co", 4082, 3608], ["Amica Mutual Ins Co", 3116, 2731], ["Armed Forces Ins Exch", 3268, 3028],
  ["ASI Select Ins Corp", 2911, 2654], ["California Automobile Ins Co (Mercury Group)", 1784, 1569],
  ["California Capital Ins Co (Auto Owners Group)", 1767, 1629], ["California Cas Indemnity Exch", 4135, 3656],
  ["CSAA Ins Exch", 2127, 1939], ["DB Ins Co. LTD (U.S. Branch)", 4202, 3722], ["Farmers Ins Exchange (Farmers Group)", 3659, 3438],
  ["Federal Ins Co (Chubb Group)", 4677, 4247], ["General Ins Co of Amer", 3415, 2962], ["Grange Ins Association", 6430, 5942],
  ["Homesite Ins Co of the Midwest", 2025, 1918], ["Horace Mann Ins Co", 3968, 3185], ["Horace Mann Prop & Cas Ins Co", 4739, 3803],
  ["Incline Cas Co", 2581, 2274], ["Integon National Ins Co", 2162, 1651], ["Interins Exch of the Automobile Club (AAA)", null, 3994],
  ["MAPFRE Ins Co", 2405, 2084], ["Metromile Ins Co", 4132, 3927], ["Nationwide Mutual Ins Co", 2690, 2240],
  ["Obsidian Pacific Ins Co", 2581, 2274], ["Pacific Specialty Ins Co", 1543, 1355], ["Privilege Underwriters Reciprocal Exch (PURE)", 4433, 3534]
];
const typed = survey.homeowners.cupertino_40y_1000000.rows;
let same = 0;
second.forEach(([c, a, b], i) => { if (typed[i].company === c && typed[i].deductible_2500 === a && typed[i].deductible_5000 === b) same += 1; });
ok(same === second.length, `second reading: ${same} of ${second.length} rows identical to the transcription (Cupertino, 40 years, $1,000,000)`);
ok(typed.find(r => r.deductible_2500 === 6430).company === "Grange Ins Association" && typed.find(r => r.deductible_2500 === 1543).company === "Pacific Specialty Ins Co",
  "lowest and highest premium belong to the insurers named on the page");

/* ---------- 2. internal consistency of the transcription ---------- */
section("2. Internal consistency of the transcription");
const lower = survey.homeowners_lower_amounts;
const p500 = lower.cupertino_40y_500000.rows, p750 = lower.cupertino_40y_750000.rows;
let mono = 0, comparable = 0, odd = [];
typed.forEach((r, i) => {
  const a = p500[i].deductible_2500, b = p750[i].deductible_2500, c = r.deductible_2500;
  if (p500[i].company !== r.company || p750[i].company !== r.company) odd.push("order " + r.company);
  if (a == null || b == null || c == null) return;
  comparable += 1;
  if (a < b && b < c) mono += 1; else odd.push(`${r.company} ${a}/${b}/${c}`);
});
ok(mono === comparable && comparable === 35, `every insurer's premium rises with the dwelling limit ($500,000 < $750,000 < $1,000,000): ${mono} of ${comparable}`, odd.join("; "));
let dedOk = 0, dedN = 0, dedOdd = [];
for (const [k, blk] of Object.entries(survey.homeowners)) for (const r of blk.rows) {
  if (r.deductible_2500 == null || r.deductible_5000 == null) continue;
  dedN += 1; if (r.deductible_5000 <= r.deductible_2500) dedOk += 1; else dedOdd.push(k + " " + r.company);
}
for (const [k, blk] of Object.entries(lower)) for (const r of blk.rows) {
  if (r.deductible_1000 == null || r.deductible_2500 == null) continue;
  dedN += 1; if (r.deductible_2500 <= r.deductible_1000) dedOk += 1; else dedOdd.push(k + " " + r.company);
}
ok(dedOk === dedN, `a higher deductible never costs more: ${dedOk} of ${dedN} insurer rows`, dedOdd.join("; "));
ok(Object.values(survey.homeowners).every(b => b.rows.length === b.companies_listed) && p500.length === 37 && p750.length === 37, "row counts equal the number of insurers listed on each page");

/* ---------- 3. published figures against the transcription ---------- */
section("3. Figures in site/data against the transcription");
const sandbox = { window: {} };
vm.createContext(sandbox);
for (const f of ["site/data/sources.js", "site/data/model.js", "site/data/costs.js"]) vm.runInContext(read(f), sandbox);
const W = sandbox.window, C = W.COSTS, M = W.MODEL, S = W.SOURCES, INS = C.INSURANCE_SURVEY;
const rowsFor = p => {
  if (p.dwelling === 1000000) {
    const key = (p.place === "Cupertino" ? "cupertino" : "sunset") + "_" + p.age + "y_1000000";
    return survey.homeowners[key].rows.map(r => r.deductible_2500);
  }
  return lower["cupertino_40y_" + p.dwelling].rows.map(r => r.deductible_2500);
};
for (const p of INS.profiles) {
  const all = rowsFor(p), v = all.filter(x => x != null);
  const want = { listed: all.length, priced: v.length, lowest: Math.min(...v), median: median(v), highest: Math.max(...v), atOrBelow1500: v.filter(x => x <= 1500).length };
  const got = { listed: p.listed, priced: p.priced, lowest: p.lowest, median: p.median, highest: p.highest, atOrBelow1500: p.atOrBelow1500 };
  ok(JSON.stringify(want) === JSON.stringify(got), `survey row ${p.place} · ${p.age} years · $${p.dwelling.toLocaleString("en-US")}`, JSON.stringify(want) + " vs " + JSON.stringify(got));
  const note = S[p.src].note, money = n => "$" + n.toLocaleString("en-US");
  ok(note.includes(`${p.listed} insurers listed`) && note.includes(`${p.priced} show a premium`) && note.includes(`from ${money(p.lowest)} to ${money(p.highest)}`), `source note ${p.src} states the same counts and range`);
  ok(S[p.src].url === survey[p.dwelling === 1000000 ? "homeowners" : "homeowners_lower_amounts"][(p.place === "Cupertino" ? "cupertino" : "sunset") + "_" + p.age + "y_" + p.dwelling].url, `link of ${p.src} is the page the figures were read from`);
}
for (const q of INS.earthquake) {
  const e = survey.earthquake_single_family[q.place === "Cupertino" ? "cupertino" : "sunset"];
  ok(e.companies_listed === q.listed && e.rate_per_1000.priced === q.withRate && e.rate_per_1000.lowest === q.lowest && e.rate_per_1000.median === q.median && e.rate_per_1000.highest === q.highest && e.through_cea === q.throughCea && e.see_footnotes === q.footnotes && S[q.src].url === e.url,
    `earthquake row ${q.place}`);
}
const ledger = JSON.parse(read("qa/ledger.json"));
const L = id => ledger.find(e => e.id === id);
for (const id of ["INS-04", "INS-05", "INS-06", "INS-07", "INS-08", "INS-09", "ECO-01", "ECO-02", "ECO-03", "ECO-04", "P19-10"])
  ok(L(id) && L(id).status === "verified" && L(id).checked === "2026-11-12" && /^https:\/\//.test(L(id).url), `ledger entry ${id} present, dated 12 Nov 2026, with an https link`);
ok(read("site/data/ledger.js").includes('"id": "ECO-02"'), "site/data/ledger.js was regenerated from the ledger");
const vsrc = read("site/verification.html"), headings = [...vsrc.slice(vsrc.indexOf("const TOPICS"), vsrc.indexOf("];", vsrc.indexOf("const TOPICS"))).matchAll(/\["([a-z0-9-]+)",\s*"/g)].map(m => m[1]);
const orphan = [...new Set(ledger.map(e => e.topic))].filter(t => !headings.includes(t));
ok(orphan.length === 0, `every ledger topic has a heading on the Verified facts page (${headings.length} headings)`, orphan.join(", "));

/* ---------- 4. the model is unchanged and the sensitivity table is reproducible ---------- */
section("4. Model inputs unchanged; sensitivity reproducible");
const B = M.BASE;
ok(B.aInsuranceAnnual === 1500 && B.bInsuranceAnnual === 1500 && B.expenseInflation === 0.03 && B.appreciation === 0.035, "model inputs unchanged: $1,500 for each property, costs +3%, home prices +3.5%");
const published = { 2040: [7683290, 6249830, 5135780], 2045: [9125340, 7395620, 6068080], 2050: [10838040, 8752170, 7164510] };
for (const y of [2040, 2045, 2050]) {
  const d = M.decision({ ...B, inheritYear: y }, 10, "4BR");
  ok(r10(d.sell.terminal) === published[y][0] && r10(d.rent.terminal) === published[y][1] && r10(d.live.terminal) === published[y][2], `base case ${y} equals the figures on the landing page`);
  const plain = C.insuranceCase(M, y, 1500), device = C.insuranceCase(M, y, 1500, B.expenseInflation);
  ok(device && Math.abs(plain.sellAheadOfRent - device.sellAheadOfRent) < 1e-6 && Math.abs(plain.sellAheadOfLive - device.sellAheadOfLive) < 1e-6, `growth device at 3% reproduces the model exactly (${y})`);
}
const byCase = (year, label) => sens.propertyA.find(r => r.inheritYear === year && r.case === label);
const cup = a => INS.profiles.find(p => p.place === "Cupertino" && p.age === 40 && p.dwelling === a);
const pairs = [["household estimate (model)", 1500], ["survey median, 40-yr profile, $500,000 dwelling", cup(500000).median], ["survey median, 40-yr profile, $750,000 dwelling", cup(750000).median],
  ["survey median, 40-yr profile", cup(1000000).median], ["survey highest, 40-yr profile", cup(1000000).highest]];
let agree = 0, total = 0, allSell = true;
for (const y of [2040, 2045, 2050]) for (const [label, premium] of pairs) {
  const a = C.insuranceCase(M, y, premium), b = byCase(y, label);
  total += 1; if (b && r10(a.sellAheadOfRent) === b.sellAheadOfRent && r10(a.sellAheadOfLive) === b.sellAheadOfLive && r10(a.firstYear) === b.firstYearPremium) agree += 1;
  if (a.winner !== "sell") allSell = false;
}
const g = INS.statewide.growth;
for (const y of [2040, 2045, 2050]) for (const [label, premium] of [["$1,500 at statewide pace", 1500], ["survey median at statewide pace", cup(1000000).median]]) {
  const a = C.insuranceCase(M, y, premium, g), b = sens.growth.find(r => r.inheritYear === y && r.case === label);
  total += 1; if (a && b && r10(a.sellAheadOfRent) === b.sellAheadOfRent && r10(a.firstYear) === b.firstYearPremium) agree += 1;
  if (!a || a.winner !== "sell") allSell = false;
}
ok(agree === total, `page helper and research script agree on ${agree} of ${total} model runs`);
ok(allSell, "selling first is the best plan in every one of those runs");
const noi = p => r10(M.sfAnnual(B.startYear, { ...B, bInsuranceAnnual: p }, true).noi);
ok(noi(1500) === 49010 && noi(3191) === 47320 && noi(10384) === 40130, "Property B net operating income at the three premiums");
ok(noi(1500) - noi(2500) === 1000, "Property B: one more dollar of premium is one dollar less net income");

/* ---------- 5. arithmetic on the official series ---------- */
section("5. Arithmetic on the official series");
ok(Math.abs(g - 0.0905) < 0.00005, `statewide average premium growth 2018–2023 = ${(g * 100).toFixed(2)}% a year`);
const hpi = Math.pow(621.1 / 438.0, 1 / 10) - 1, cpi = Math.pow(416.5 / 331.8, 1 / 10) - 1;
ok(Math.abs(hpi - 0.0355) < 0.0001, `CBO national home-price index 2026–2036 = ${(hpi * 100).toFixed(2)}% a year (shown as about 3.6%)`);
ok(Math.abs(cpi - 0.023) < 0.0001, `CBO CPI-U 2026–2036 = ${(cpi * 100).toFixed(2)}% a year`);
ok(W.MODEL.BASE.appreciation === 0.035 && Math.abs(hpi - 0.035) < 0.001, "the model's 3.5% is within 0.1 point of that projection");
// FAIR Plan: the file's own year-over-year percentages must agree with the counts that were typed in.
const fair = { "ZIP 95014 · Property A": [155, -31, 133, 79, 7], "ZIP 94122 · Property B": [-12, 40, 286, 59, 19], "California": [12, 21, 40, 38, 7] };
for (const row of INS.fairPlan.rows) {
  const pub = fair[row.label]; let good = 0;
  for (let i = 1; i < row.counts.length; i += 1) if (Math.round((row.counts[i] / row.counts[i - 1] - 1) * 100) === pub[i]) good += 1;
  ok(good === 4, `FAIR Plan ${row.label}: the four published yearly changes match the counts`);
}
ok(S.fairPlanZip.note.includes("74, 51, 119, 213, 227") && S.fairPlanZip.note.includes("15, 21, 81, 129, 154"), "FAIR Plan source note carries the same counts");

/* ---------- 6. blanks stay blank; no personal data; rounding ---------- */
section("6. Blanks, privacy and rounding");
const page = read("site/operating-costs.html");
ok(/<td class="wrap">Property A premium<\/td><td class="wrap">—<\/td>/.test(page) && /<td class="wrap">Property B premium<\/td><td class="wrap">—<\/td>/.test(page), "both premium cells are still blank on the Operating costs page");
const mine = ["research/60ca3e1f/insurance.md", "research/60ca3e1f/economic-baseline.md", "research/60ca3e1f/build_insurance_survey.py", "research/60ca3e1f/insurance-sensitivity.cjs",
  "verification/60ca3e1f/REPORT.md", "verification/60ca3e1f/check.cjs"].filter(f => fs.existsSync(path.join(root, f)));
const personal = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}|\b\d{1,5}\s+[A-Z][a-z]+\s+(Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Way|Court|Ct|Lane|Ln|Boulevard|Blvd)\b|\bAPN\b|\b\d{3}-\d{2}-\d{3,4}\b/;
const hits = mine.filter(f => personal.test(read(f).replace(/1-\d{3}-\d{3}-\d{4}/g, "")));
ok(hits.length === 0, `no e-mail address, street address or parcel number in the ${mine.length} files this session wrote`, hits.join(", "));
const official = new Set();
for (const e of ledger) for (const t of [e.value, e.evidence, e.notes || ""]) for (const m of String(t).matchAll(/\$(\d{1,3}(?:,\d{3})+|\d+)(?!\.\d)/g)) official.add(+m[1].replace(/,/g, ""));
const bad = [];
for (const f of ["research/60ca3e1f/insurance.md", "research/60ca3e1f/economic-baseline.md", "verification/60ca3e1f/REPORT.md"].filter(f => fs.existsSync(path.join(root, f))))
  for (const m of read(f).matchAll(/\$(\d{1,3}(?:,\d{3})+|\d{4,})(?!\.\d)(?![\d,])/g)) { const v = +m[1].replace(/,/g, ""); if (v >= 1000 && v % 10 && !official.has(v)) bad.push(f + " " + m[0]); }
ok(bad.length === 0, "every dollar figure of $1,000 or more in this session's notes is a multiple of $10 or an official amount in the ledger", bad.join("; "));

/* ---------- 7. the rendered page ---------- */
section("7. Rendered Operating costs page (jsdom)");
let rendered = "skipped";
try {
  const { JSDOM, VirtualConsole } = require(path.join(root, ".cache/test/node_modules/jsdom"));
  const pub = path.join(root, "_public"), file = "site/operating-costs.html";
  const errors = [], vc = new VirtualConsole(); vc.on("jsdomError", e => errors.push(e.message));
  const dom = new JSDOM(fs.readFileSync(path.join(pub, file), "utf8"), { runScripts: "outside-only", url: "https://example.org/Tino2/" + file, virtualConsole: vc });
  for (const s of dom.window.document.querySelectorAll("script")) {
    try { dom.window.eval(s.src ? fs.readFileSync(path.resolve(pub, path.dirname(file), s.getAttribute("src")), "utf8") : s.textContent); } catch (e) { errors.push(e.message); }
  }
  const doc = dom.window.document, text = doc.body.textContent.replace(/\s+/g, " ");
  ok(errors.length === 0, "page scripts run without an error", errors.join("; "));
  const rows = [...doc.querySelectorAll("tbody tr")];
  ok(rows.length > 0 && rows.every(r => r.querySelector('a[href^="https://"]')), `all ${rows.length} table rows carry an https link`);
  const rowTexts = rows.map(tr => [...tr.children].map(c => c.textContent.replace(/\s+/g, " ").trim()).join(" "));
  for (const needle of ["$500,000 to rebuild 35 of 37 $790 $1,380 $3,371 20 of 35", "$750,000 to rebuild 35 of 37 $1,167 $2,020 $4,901 4 of 35", "$1,000,000 to rebuild 35 of 37 $1,543 $2,690 $6,430 0 of 35",
    "$1,500 $2,710 $1,433,470 $1,729,720 $2,085,880 Sell", "$2,690 $4,860 $1,451,090 $1,750,150 $2,109,560 Sell", "$6,430 $11,610 $1,506,460 $1,814,350 $2,183,980 Sell",
    "rising 9.05% a year instead of 3% $1,500 $8,490 $1,479,210 $1,808,790 $2,220,120 Sell", "$3,190 $47,320", "$10,384 $40,130", "$1.15 $3.10 $15.00 13 8", "$1.13 $3.29 $15.00 13 8",
    "74 51 119 213 227 3.1 times", "15 21 81 129 154 10.3 times", "265,909 320,572 449,832 621,234 665,673 2.5 times"]) {
    ok(rowTexts.some(t => t.includes(needle)), `rendered table row shows: ${needle}`);
  }
  ok(text.includes("none of them is the premium for either property"), "rendered page says that no figure is the premium for either property");
  ok(!/\bNaN\b|undefined|Missing source/.test(text), "no NaN, undefined or missing-source marker in the rendered page");
  rendered = "checked";
} catch (e) {
  if (/Cannot find module/.test(e.message)) console.log("SKIPPED part 7: jsdom is not installed under .cache/test (run node scripts/runtime-test.cjs setup first)");
  else { ok(false, "rendered-page check could not run", e.message); }
}

const passed = results.filter(r => r.result === "pass").length;
const summary = { session: "60ca3e1f", date: "2026-11-12", checks: results.length, passed, failed, renderedPage: rendered, results };
fs.writeFileSync(path.join(__dirname, "check-results.json"), JSON.stringify(summary, null, 1) + "\n");
console.log(`\n${failed ? "FAIL" : "PASS"}: ${passed} of ${results.length} checks passed; rendered page ${rendered}. Results written to verification/60ca3e1f/check-results.json`);
process.exit(failed ? 1 : 0);
