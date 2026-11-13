/* Privacy regression for the public dashboard.
   Compares the published artifact against the distinctive values used anywhere
   in the legacy material, so a household figure cannot silently reach the site.
   This is a limited collision scan, not proof of anonymisation. */
'use strict';
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('../.cache/test/node_modules/jsdom');

const root = path.resolve('_public');
const bad = [];

/* Distinctive record values that must never appear on the site. These are read
   from legacy data files at test time, never copied into this file. */
const legacySources = [
  'site/data/model.js',
  'docs/cupertino-model.md',
  'docs/executive-summary.md',
  'docs/sf-model.md',
];
const distinctive = new Set();
const RECORD = /\b\d{3},\d{3}\b|\b\d{2},\d{3}\b|\b7,150\b|\b3,100,000\b|\b1,800,000\b/g;

for (const rel of legacySources) {
  const p = path.resolve(rel);
  if (!fs.existsSync(p)) continue;
  const text = fs.readFileSync(p, 'utf8');
  for (const m of text.matchAll(RECORD)) distinctive.add(m[0].replace(/,/g, ''));
}
/* Values that legitimately appear because they are official published amounts. */
/* Official amounts published by a government source, so they cannot identify a
   household: IRS exclusion and home-sale amounts, and the BOE allowance. */
const ALLOWED = new Set(['1044586', '15480000', '15000000', '1000000',
  '250000', '500000', '480000', '7000']);

function hits(text) {
  const found = [];
  for (const m of text.matchAll(/\$?\s?(\d{1,3}(?:,\d{3})+)/g)) {
    const raw = m[1].replace(/,/g, '');
    if (ALLOWED.has(raw)) continue;
    if (!distinctive.has(raw)) continue;
    /* An explicit interval such as "2,990,000 - 3,100,000 band" is the
       intended way to publish a range; only point values are a leak. */
    const after = text.slice(m.index, m.index + 60);
    const before = text.slice(Math.max(0, m.index - 40), m.index);
    if (/band|range|&ndash;|–/.test(after + before)) continue;
    found.push(m[0]);
  }
  return found;
}

function inspect(file, text) {
  for (const h of hits(text)) bad.push(`${file}: distinctive legacy figure ${h}`);
  if (/\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b/i.test(text)) {
    bad.push(`${file}: email-like identifier`);
  }
  if (/\b\d{1,5}\s+[A-Z][A-Za-z]*(?:\s+[A-Z][A-Za-z]*){0,2}\s+(?:Street|St\.|Avenue|Ave\.|Road|Rd\.|Boulevard|Blvd\.)\b/i.test(text)) {
    bad.push(`${file}: street-address-like identifier`);
  }
  if (/\b\d{3}-\d{2}-\d{4}\b/.test(text)) bad.push(`${file}: national-id-like pattern`);
  if (/\bAPN\b|\bparcel\s+number\b\s*:?\s*\d/i.test(text)) bad.push(`${file}: parcel number`);
}

function walk(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const f = path.join(dir, e.name);
    if (e.isDirectory()) walk(f);
    else if (/\.(html|js|css|txt)$/.test(f)) {
      inspect(path.relative(root, f), fs.readFileSync(f, 'utf8'));
    }
  }
}
walk(root);

const pages = ['index.html', ...fs.readdirSync(root + '/guide')
  .filter((x) => x.endsWith('.html')).map((x) => 'guide/' + x)];

for (const file of pages) {
  const dom = new JSDOM(fs.readFileSync(path.join(root, file), 'utf8'), {
    runScripts: 'outside-only',
    url: 'https://example.org/Tino2/' + file,
  });
  for (const s of dom.window.document.querySelectorAll('script')) {
    const src = s.getAttribute('src');
    dom.window.eval(src
      ? fs.readFileSync(path.resolve(root, path.dirname(file), src), 'utf8')
      : s.textContent);
  }
  const doc = dom.window.document;
  for (const h of hits(doc.body.textContent)) {
    bad.push(`${file}: distinctive figure in rendered text ${h}`);
  }
  if (doc.querySelector('form,input[type=file],textarea,iframe')) {
    bad.push(`${file}: data input or embed present`);
  }
  if (doc.querySelector('script[src^="https:"],img[src^="https:"]')) {
    bad.push(`${file}: external automatic resource`);
  }
  /* No network calls and no storage of personal data. */
  const source = [...doc.querySelectorAll('script')]
    .map((s) => s.textContent).join('\n');
  if (/fetch\(|XMLHttpRequest|navigator\.sendBeacon/.test(source)) {
    bad.push(`${file}: inline script performs a network request`);
  }
  dom.window.close();
}

if (bad.length) {
  for (const b of Array.from(new Set(bad))) console.error('Privacy review required:', b);
  process.exit(1);
}
console.log('PASS: no distinctive legacy figure, identifier or external resource in the '
  + 'published artifact. This is not proof of anonymisation.');
