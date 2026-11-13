/* Rendered tests for the public dashboard. Contains no household data.
   Opens every page in a DOM, runs its scripts, and checks structure, links,
   sources, rounding, privacy and the interactive behaviour. */
'use strict';
const { JSDOM, VirtualConsole } = require('../.cache/test/node_modules/jsdom');
const fs = require('fs');
const path = require('path');
const assert = require('assert');

const root = path.resolve('_public');
const pages = ['index.html', ...fs.readdirSync(path.join(root, 'guide'))
  .filter((f) => f.endsWith('.html'))
  .map((f) => 'guide/' + f)];

const hosts = new Set([
  'www.irs.gov', 'www.sco.ca.gov', 'www.boe.ca.gov', 'boe.ca.gov',
  'asr.santaclaracounty.gov', 'files.santaclaracounty.gov', 'sftreasurer.org',
  'www.sf.gov', 'www.sfmta.com', 'www.sfelections.org',
  'leginfo.legislature.ca.gov', 'www.ftb.ca.gov', 'www.insurance.ca.gov',
  'www.sjwater.com', 'www.sfpuc.gov', 'www.cupertino.gov', 'www.pge.com',
  'www.huduser.gov', 'fred.stlouisfed.org', 'www.cbo.gov',
  'www.federalreserve.gov', 'www.ssa.gov', 'pubs.usgs.gov',
  'www.congress.gov', 'www.fdic.gov', 'www.investor.gov', 'docs.github.com',
]);

let rows = 0;
let checks = 0;
function check(ok, msg) { checks += 1; assert(ok, msg); }

function open(file) {
  const errors = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', (e) => errors.push(e.message));
  const dom = new JSDOM(fs.readFileSync(path.join(root, file), 'utf8'), {
    url: 'https://example.org/Tino2/' + file,
    runScripts: 'outside-only',
    virtualConsole: vc,
  });
  for (const script of dom.window.document.querySelectorAll('script')) {
    try {
      const src = script.getAttribute('src');
      check(!src || !/^(?:https?:)?\/\//i.test(src), file + ' external script forbidden');
      dom.window.eval(src
        ? fs.readFileSync(path.resolve(root, path.dirname(file), src), 'utf8')
        : script.textContent);
    } catch (e) { errors.push(e.stack || String(e)); }
  }
  check(errors.length === 0, file + ' runtime error: ' + errors.join('\n'));
  return dom;
}

function inspect(dom, file) {
  const doc = dom.window.document;
  check(Boolean(doc.querySelector('nav[aria-label]')), file + ' navigation missing');
  check(doc.querySelector('h1') !== null, file + ' missing heading');
  check(doc.querySelectorAll('nav a').length === 12, file + ' incomplete navigation');
  check(doc.querySelector('meta[name=referrer][content=no-referrer]') !== null,
    file + ' referrer policy missing');
  check(!doc.querySelector('form,input,textarea,iframe'),
    file + ' unexpected data input or embed');

  for (const th of doc.querySelectorAll('thead th')) {
    check(th.getAttribute('scope') === 'col', file + ' missing column scope');
  }
  check(doc.body.textContent.toLowerCase().includes('anonymised'),
    file + ' lacks the anonymity notice');

  for (const tr of doc.querySelectorAll('tbody tr')) {
    rows += 1;
    const cells = tr.querySelectorAll(':scope > td');
    const heads = tr.closest('table').querySelectorAll('thead tr:last-child th');
    check(cells.length === heads.length,
      file + ' mismatched table cells: ' + tr.textContent.slice(0, 80));
    const links = [...tr.querySelectorAll('a[href^="https://"]')];
    check(links.length > 0, file + ' row without source: ' + tr.textContent.slice(0, 80));
    check(links.some((a) => hosts.has(new URL(a.href).hostname)),
      file + ' row without an approved agency source: ' + tr.textContent.slice(0, 60));
  }

  for (const el of doc.querySelectorAll('a[href],script[src],link[rel="stylesheet"][href]')) {
    const href = el.getAttribute('href') || el.getAttribute('src');
    if (!href || href.startsWith('#')) continue;
    if (/^https?:/.test(href)) { check(href.startsWith('https://'), file + ' insecure link'); continue; }
    check(!/^(?:mailto:|tel:|javascript:|data:)/i.test(href), file + ' disallowed link');
    const target = path.resolve(root, path.dirname(file),
      decodeURIComponent(href.split('#')[0].split('?')[0]));
    check(target.startsWith(root + path.sep) && fs.existsSync(target),
      file + ' broken local target ' + href);
  }

  // Every published dollar amount must be a multiple of $10 or an official one.
  const OFFICIAL = new Set([1044586, 59]);
  const text = doc.body.textContent;
  for (const m of text.matchAll(/\$\s?(\d{1,3}(?:,\d{3})+|\d+)(?![.,]?\d)(?![MB])\b/g)) {
    const amount = Number(m[1].replace(/,/g, ''));
    if (OFFICIAL.has(amount)) continue;
    check(amount % 10 === 0, file + ' non-$10 dollar amount: ' + m[0]);
  }
  check(!/\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b/i.test(text), file + ' email in text');
  check(!/\b\d{1,5}\s+[A-Z][A-Za-z]*(?:\s+[A-Z][A-Za-z]*){0,2}\s+(?:Street|Avenue|Road|Boulevard|Drive|Lane|Court)\b/.test(text),
    file + ' street-address-like text');
}

for (const file of pages) {
  const dom = open(file);
  inspect(dom, file);

  if (file === 'index.html') {
    const d = dom.window.document;
    check(/^\$\d{1,3}(?:,\d{3})+$/.test(d.getElementById('sum-sell-live').textContent),
      'the summary page fills the sell figure from the model');
    check(d.getElementById('sum-sell-live').textContent
      === d.getElementById('sum-sell-live').textContent.trim(), 'clean figure text');
  }

  if (file === 'guide/decision.html') {
    const d = dom.window.document;
    const before = d.getElementById('live-compare').textContent;
    d.getElementById('c-transfer').value = '2050';
    d.getElementById('c-transfer').dispatchEvent(new dom.window.Event('change'));
    check(d.getElementById('live-compare').textContent !== before,
      'changing the transfer year must change the comparison');
    d.getElementById('c-home').value = '0.07';
    d.getElementById('c-home').dispatchEvent(new dom.window.Event('change'));
    check(d.getElementById('live-result').textContent.includes('leads'),
      'the result card must name a leading option');
    const M = dom.window.MODEL;
    check(M.fmtMoney(125) === '$130' && M.fmtMoney(-125) === '−$130',
      'rounding and sign handling');
    const r = M.compare(2045, 20, {});
    check(Math.abs(r.rows.sell.terminal - r.rows.sell.terminal) < 1e-9, 'finite result');
    inspect(dom, file + ' (changed controls)');
  }

  if (file === 'guide/property.html') {
    const d = dom.window.document;
    const jump = d.getElementById('p-jump');
    check(Boolean(jump), 'the projection jump control exists');
    const table = jump.closest('.controls').nextElementSibling;
    check(table.querySelectorAll('tbody tr').length === 51,
      'the projection table must cover 2026-2076');
  }

  if (file === 'guide/suggestions.html') {
    const d = dom.window.document;
    const sel = d.querySelector('[data-suggestion="S01"]');
    sel.value = 'adopt';
    sel.dispatchEvent(new dom.window.Event('change'));
    const saved = JSON.parse(dom.window.localStorage.getItem('tino2-public-suggestions-v3'));
    check(saved.S01 === 'adopt', 'a suggestion records only its status');
    d.getElementById('clear-selections').click();
    check(!dom.window.localStorage.getItem('tino2-public-suggestions-v3'),
      'clearing removes the local marks');
  }

  if (file === 'guide/stress.html') {
    const M = dom.window.MODEL;
    for (const key of Object.keys(M.PATHS)) {
      const r = M.runPath(key, {}, 2045, 50);
      check(r.length === 50 && r[0].year === 2046 && r[49].year === 2095,
        '50-year path ' + key);
      check(r.every((x) => ['sell', 'rent', 'live', 'realSell', 'realRent', 'realLive']
        .every((v) => Number.isFinite(x[v]))), 'finite path ' + key);
      check(r.every((x) => Math.abs(x.realSell * x.priceIndex - x.sell) < 1e-6),
        'real and nominal reconcile on ' + key);
    }
  }

  dom.window.close();
}

console.log(`PASS: ${pages.length} rendered pages, ${rows} source-linked table rows, `
  + `${checks} checks; controls, rounding and privacy verified.`);
