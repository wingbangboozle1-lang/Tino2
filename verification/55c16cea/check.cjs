const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const { JSDOM, VirtualConsole } = require("../../.cache/test/node_modules/jsdom");

const root = path.resolve(__dirname, "../..");

function renderPage(relPath) {
  const vc = new VirtualConsole();
  const errors = [];
  vc.on("jsdomError", (e) => errors.push(e.message));
  const full = path.join(root, relPath);
  const dom = new JSDOM(fs.readFileSync(full, "utf8"), {
    runScripts: "outside-only",
    url: "https://example.org/Tino2/" + relPath,
    virtualConsole: vc
  });
  for (const script of dom.window.document.querySelectorAll("script")) {
    const src = script.getAttribute("src");
    const code = src ? fs.readFileSync(path.resolve(path.dirname(full), src), "utf8") : script.textContent;
    dom.window.eval(code);
  }
  assert.equal(errors.length, 0, `${relPath} jsdom errors: ${errors.join("; ")}`);
  return dom;
}

// 1. Ledger & model verification
const ledger = JSON.parse(fs.readFileSync(path.join(root, "qa/ledger.json"), "utf8"));
assert.equal(ledger.length, 84, "qa/ledger.json should have 84 entries");
for (const id of ["CF-04", "CF-05", "SF-09", "CA-05", "CA-06", "CA-07", "SF-04", "SF-05"]) {
  const entry = ledger.find((x) => x.id === id);
  assert(entry, `missing ledger entry ${id}`);
  assert.equal(entry.status, "verified", `${id} should be verified`);
  assert.equal(entry.checked, "2026-11-12", `${id} checked date should be 2026-11-12`);
}
assert(ledger.find((x) => x.id === "P19-12"), "preserved P19-12 entry from origin/main");
const cf04 = ledger.find((x) => x.id === "CF-04");
assert.match(cf04.value, /\$5,440.*\$5,800/);
const cf05 = ledger.find((x) => x.id === "CF-05");
assert.match(cf05.value, /\$2,770.*\$3,410/);
const sf09 = ledger.find((x) => x.id === "SF-09");
assert.match(sf09.value, /\$249.*\$0\.195/);

// 2. Questions & discovery page DOM + interactive filter checks
const qDom = renderPage("site/questions.html");
const qDoc = qDom.window.document;
assert.equal(qDoc.querySelectorAll(".q-group tbody tr").length, 24, "24 discovery questions rendered across groups A-D");
assert(!/\bsession\b|the brief/i.test(qDoc.body.textContent), "R-D4 internal wording removed from questions.html");
assert.match(qDoc.body.textContent, /\$5,800.*4BR/);
assert.match(qDoc.body.textContent, /\$249\/yr base \+ \$0\.195\/sq ft/);
const qStatus = qDoc.getElementById("qStatusFilter");
qStatus.value = "blocking";
qStatus.dispatchEvent(new qDom.window.Event("change"));
const visibleBlocking = [...qDoc.querySelectorAll(".q-group tbody tr")].filter(tr => tr.style.display !== "none").length;
assert.equal(visibleBlocking, 3, "blocking filter isolates 3 blocking questions");
assert(qDoc.getElementById("downloadChecklist"), "CSV discovery checklist download button present");
qDom.window.close();

// 3. Suggestions page DOM + interactive path selection checks
const sDom = renderPage("site/suggestions.html");
const sDoc = sDom.window.document;
assert(!/\bsession\b|the brief/i.test(sDoc.body.textContent), "R-D4 internal wording removed from suggestions.html");
assert.match(sDoc.body.textContent, /\$5,800.*4BR/);
assert.match(sDoc.body.textContent, /\$249\/yr base \+ \$0\.195\/sq ft/);
assert(sDoc.getElementById("dl-md") && sDoc.getElementById("dl-json"), "Markdown and JSON export buttons present");
const privSel = sDoc.getElementById("privacy-path-select");
assert(privSel, "Interactive privacy path selector present");
privSel.value = "Path A: Private analysis, public generic examples";
privSel.dispatchEvent(new sDom.window.Event("change", { bubbles: true }));
assert.match(sDoc.getElementById("summary-card").textContent, /Path A: Private analysis, public generic examples/);
const a05Sel = sDoc.querySelector('select[data-choice="A-05"]');
a05Sel.value = "Approve";
a05Sel.dispatchEvent(new sDom.window.Event("change", { bubbles: true }));
assert.match(sDoc.getElementById("summary-card").textContent, /A-05/);
sDom.window.close();

// 4. Decision Lab FY2027 selector check
const dDom = renderPage("site/decision.html");
const dDoc = dDom.window.document;
const rentSel = dDoc.getElementById("rentChoice");
assert(rentSel.querySelector('option[value="4BR_2027"]'), "Decision Lab exposes FY2027 4BR option");
assert(rentSel.querySelector('option[value="3BR_2027"]'), "Decision Lab exposes FY2027 3BR option");
const baseRentText = dDoc.querySelector("#strategy-cards .card:nth-child(2) .metric").textContent;
rentSel.value = "4BR_2027";
rentSel.dispatchEvent(new dDom.window.Event("change"));
const fy27RentText = dDoc.querySelector("#strategy-cards .card:nth-child(2) .metric").textContent;
const toNum = (s) => Number(s.replace(/[^0-9-]/g, ""));
assert(toNum(fy27RentText) < toNum(baseRentText), "FY2027 lower 4BR rent reduces rent-then-sell terminal wealth and widens selling's lead");
assert(dDoc.querySelector('#annual tr td.source a[href*="fmr2027"]'), "Annual table dynamically cites FY2027 HUD URL when 4BR_2027 selected");
dDom.window.close();

// 5. SF page + Sources date precedence + Review / Footer hygiene checks
const sfDom = renderPage("site/san-francisco.html");
assert.match(sfDom.window.document.body.textContent, /\$2,770/);
assert.match(sfDom.window.document.body.textContent, /\$249\/yr base \+ \$0\.195\/sq ft/);
sfDom.window.close();

const srcDom = renderPage("site/sources.html");
const srcHtml = srcDom.window.document.body.textContent;
assert(!/by one of the sessions/i.test(srcHtml), "R-D4 wording removed from sources.html");
const registerText = srcDom.window.document.getElementById("register").textContent;
assert(registerText.includes("12 Nov 2026 · checked"), "Sources register correctly surfaces 12 Nov 2026 checked entries");
assert(srcDom.window.document.querySelector("footer").textContent.includes("Last verified: 12 Nov 2026"), "Footer stamp updated to 12 Nov 2026");
srcDom.window.close();

const revDom = renderPage("site/review.html");
const revText = revDom.window.document.body.textContent;
assert(!/\bsession\b|audit note|the brief/i.test(revText), "R-D4 internal wording removed from review.html");
revDom.window.close();

// 6. R-D3 NOI expansion across updated pages
for (const page of ["site/decision.html", "site/properties.html", "site/san-francisco.html", "site/black-swan.html", "site/sources.html"]) {
  const dom = renderPage(page);
  assert.match(dom.window.document.body.textContent, /Net operating income \(NOI\)/, `${page} spells out Net operating income (NOI)`);
  dom.window.close();
}

console.log("PASS: 55c16cea verification checks passed across ledger, Q&A page, Suggestions path selector, Decision FY2027 sensitivity, SF Measure H, and R-D3/R-D4/R-D5 fixes.");
