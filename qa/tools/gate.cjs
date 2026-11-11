#!/usr/bin/env node
/* Publication gate (session f16e6e34). Runs on the packaged site in _public, on the pages AS RENDERED.
   It holds no household data: every rule is structural.
     R1 rounding     every dollar amount of $1,000 or more is a multiple of $10, unless it is an official
                     published figure found in qa/ledger.json or in a source note of site/data/sources.js
     R2 identifiers  no e-mail address, street address, parcel number or SSN pattern
     R3 links        every internal link resolves; every external link is https
     R4 row sources  every table body row carries an https link
     R5 scripts      no page throws while rendering
   Usage: python3 scripts/package-site.py && node qa/tools/gate.cjs   (exit code 1 on any error) */
const fs = require('fs'), path = require('path');
const repo = path.resolve(__dirname, '..', '..');
const { JSDOM, VirtualConsole } = require(path.join(repo, '.cache/test/node_modules/jsdom'));
const root = path.join(repo, '_public');
if (!fs.existsSync(root)) { console.error('Run python3 scripts/package-site.py first.'); process.exit(2); }

const allowed = new Set();
const grab = text => { for (const m of String(text).matchAll(/(?<![\d.])(\d{1,3}(?:,\d{3})+|\d{4,})(?![\d,]*\d)/g)) allowed.add(Number(m[1].replace(/,/g, ''))); };
for (const e of JSON.parse(fs.readFileSync(path.join(repo, 'qa/ledger.json'), 'utf8'))) { grab(e.value); grab(e.evidence); grab(e.notes || ''); }

const MONEY = /\$\s?(\d{1,3}(?:,\d{3})+|\d{4,})(?:\.(\d{1,2}))?(?![\d,]*\d)/g;
const EMAIL = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/g;
const SSN = /(?<![\d-])\d{3}-\d{2}-\d{4}(?![\d-])/g;
const APN = /(?<![\d-])\d{3}-\d{2}-\d{3}(?![\d-])/g;
const STREET = /\b\d{2,5}\s+(?:[NSEW]\.?\s+)?(?:\d{1,2}(?:st|nd|rd|th)|[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+(?:Street|St|Avenue|Ave|Boulevard|Blvd|Drive|Dr|Road|Rd|Lane|Ln|Way|Court|Ct|Place|Pl|Terrace|Circle)\b\.?/g;

const pages = ['index.html', ...fs.readdirSync(path.join(root, 'site')).filter(f => f.endsWith('.html')).sort().map(f => 'site/' + f)];
const report = { checked: new Date().toISOString().slice(0, 10), pages: [], errors: [], warnings: [], totals: { pages: 0, rows: 0, rowsWithOwnSource: 0, rowsWithContextLinkOnly: 0, amounts: 0, officialExactAmounts: 0, internalLinks: 0, externalLinks: 0 } };
const err = (page, rule, detail) => report.errors.push({ page, rule, detail });
const warn = (page, rule, detail) => report.warnings.push({ page, rule, detail });

for (const file of pages) {
  const scriptErrors = [], vc = new VirtualConsole(); vc.on('jsdomError', e => scriptErrors.push(e.message));
  const dom = new JSDOM(fs.readFileSync(path.join(root, file), 'utf8'), { runScripts: 'outside-only', url: 'https://example.org/Tino2/' + file, virtualConsole: vc });
  const doc = dom.window.document;
  for (const s of doc.querySelectorAll('script')) {
    try { dom.window.eval(s.src ? fs.readFileSync(path.resolve(root, path.dirname(file), s.getAttribute('src')), 'utf8') : s.textContent); }
    catch (e) { scriptErrors.push(e.message); }
  }
  scriptErrors.forEach(m => err(file, 'R5 scripts', m.slice(0, 200)));
  const page = { file, rows: 0, rowsWithContextLinkOnly: 0, amounts: 0, links: 0 };
  // R4 — row sources
  for (const tr of doc.querySelectorAll('tbody tr')) {
    page.rows += 1;
    const links = [...tr.querySelectorAll('a[href^="https://"]')];
    if (!links.length) err(file, 'R4 row sources', tr.textContent.replace(/\s+/g, ' ').slice(0, 100));
    else if (links.every(a => /Calculated value|Framework only/.test(a.textContent))) page.rowsWithContextLinkOnly += 1;
  }
  // R3 — links
  for (const a of doc.querySelectorAll('a[href]')) {
    const href = a.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('blob:')) continue;
    if (/^https:\/\//.test(href)) { report.totals.externalLinks += 1; continue; }
    if (/^http:\/\//.test(href)) { err(file, 'R3 links', 'not https: ' + href); continue; }
    if (/^mailto:/.test(href)) { err(file, 'R2 identifiers', 'mailto link ' + href); continue; }
    report.totals.internalLinks += 1;
    if (!fs.existsSync(path.resolve(root, path.dirname(file), href.split('#')[0].split('?')[0]))) err(file, 'R3 links', 'broken internal link ' + href);
  }
  // text as a reader sees it
  doc.querySelectorAll('script,style').forEach(n => n.remove());
  const text = doc.body.textContent.replace(/\s+/g, ' ');
  for (const m of text.matchAll(MONEY)) {
    page.amounts += 1;
    const value = Number(m[1].replace(/,/g, ''));
    if (value >= 1000 && value % 10 !== 0) {
      if (allowed.has(value)) report.totals.officialExactAmounts += 1;
      else err(file, 'R1 rounding', m[0] + '  …' + text.slice(Math.max(0, m.index - 50), m.index + 30));
    }
  }
  for (const m of text.matchAll(EMAIL)) err(file, 'R2 identifiers', 'e-mail address pattern');
  for (const m of text.matchAll(SSN)) err(file, 'R2 identifiers', 'SSN pattern');
  for (const m of text.matchAll(APN)) err(file, 'R2 identifiers', 'parcel-number pattern');
  for (const m of text.matchAll(STREET)) warn(file, 'R2 identifiers', 'possible street address: ' + m[0]);
  report.pages.push(page);
  report.totals.pages += 1; report.totals.rows += page.rows; report.totals.rowsWithContextLinkOnly += page.rowsWithContextLinkOnly; report.totals.amounts += page.amounts;
  dom.window.close();
}
report.totals.rowsWithOwnSource = report.totals.rows - report.totals.rowsWithContextLinkOnly;
fs.writeFileSync(path.join(repo, 'qa/gate-report.json'), JSON.stringify(report, null, 1) + '\n');
const t = report.totals;
console.log(`${report.errors.length ? 'FAIL' : 'PASS'}: ${t.pages} rendered pages · ${t.rows} table rows (${t.rowsWithOwnSource} with their own official link, ${t.rowsWithContextLinkOnly} calculated rows with a context link only) · ${t.amounts} dollar amounts checked (${t.officialExactAmounts} official exact figures) · ${t.internalLinks} internal and ${t.externalLinks} external links · ${report.errors.length} errors · ${report.warnings.length} warnings`);
report.errors.slice(0, 25).forEach(e => console.log('  ERROR', e.page, e.rule, e.detail));
report.warnings.slice(0, 10).forEach(e => console.log('  WARN ', e.page, e.rule, e.detail));
process.exit(report.errors.length ? 1 : 0);
