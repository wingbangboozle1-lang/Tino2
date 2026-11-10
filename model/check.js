#!/usr/bin/env node
/*
 * Checker — session 5a1bd5be.   Run:  node model/check.js
 *
 * Looks at every file the repository publishes (GitHub Pages serves the whole tree), not only model/.
 *  1. Internal links and fragments resolve.
 *  2. Privacy patterns (e-mail, phone, street address, parcel number, ZIP code).
 *  3. Dollar figures on the analysis pages of model/ are multiples of $10.
 *  4. Every table row in model/ carries an official source link or a link to the Flagged page.
 *  5. model/ loads nothing from other hosts, and links out only to official hosts.
 *
 * Findings inside model/ make the run fail. Findings in other sessions' files are reported
 * (counts only; matched text is never printed or stored) and are not changed.
 */
'use strict';
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const MODEL = path.join(ROOT, 'model');
const SKIP_DIRS = new Set(['.git', 'node_modules', '__pycache__']);
const TEXT_EXT = new Set(['.html', '.htm', '.md', '.js', '.json', '.jsonl', '.py', '.css', '.txt', '.yml', '.yaml', '.csv', '.svg']);

// Hosts accepted as official on model/ pages (government bodies, the legislature, Federal Reserve data).
const OFFICIAL = [/\.gov$/, /^leginfo\.legislature\.ca\.gov$/, /^(www\.)?sftreasurer\.org$/, /^fred\.stlouisfed\.org$/,
  /^(www\.)?govinfo\.gov$/];
const REPO_HOSTS = [/^github\.com$/, /^wingbangboozle1-lang\.github\.io$/];

function walk(dir, out) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (SKIP_DIRS.has(e.name)) continue;
    const full = path.join(dir, e.name);
    if (e.isDirectory()) walk(full, out);
    else out.push(full);
  }
  return out;
}
const rel = f => path.relative(ROOT, f).split(path.sep).join('/');
const area = f => { const r = rel(f); const i = r.indexOf('/'); return i < 0 ? '(root)' : r.slice(0, i) + '/'; };

function stripTags(html) {
  return html.replace(/<script[\s\S]*?<\/script>/gi, ' ').replace(/<style[\s\S]*?<\/style>/gi, ' ').replace(/<[^>]+>/g, ' ');
}

// ---------------------------------------------------------------- 1. links
function attrs(html) {
  const out = [], re = /\b(href|src)\s*=\s*("([^"]*)"|'([^']*)')/gi;
  let m; while ((m = re.exec(html))) out.push({ attr: m[1].toLowerCase(), url: m[3] !== undefined ? m[3] : m[4] });
  return out;
}
function ids(html) {
  const s = new Set(), re = /\b(?:id|name)\s*=\s*("([^"]*)"|'([^']*)')/gi;
  let m; while ((m = re.exec(html))) s.add(m[2] !== undefined ? m[2] : m[3]);
  return s;
}
function checkLinks(files) {
  const broken = [], external = [];
  const cache = new Map();
  const read = f => { if (!cache.has(f)) cache.set(f, fs.readFileSync(f, 'utf8')); return cache.get(f); };
  for (const f of files.filter(x => /\.html?$/i.test(x))) {
    const html = read(f).replace(/<!--[\s\S]*?-->/g, '');
    for (const a of attrs(html)) {
      const u = a.url.trim();
      if (!u || /^(mailto:|tel:|javascript:|data:)/i.test(u)) continue;
      if (/\$\{|\{\{/.test(u)) continue;                       // template text inside a script
      if (/^(https?:)?\/\//i.test(u)) { external.push({ file: rel(f), attr: a.attr, url: u }); continue; }
      const [p0, frag] = u.split('#');
      const p = p0.split('?')[0];
      let target = f;
      if (p) {
        target = p.startsWith('/') ? path.join(ROOT, p.replace(/^\/Tino2\//, '/')) : path.resolve(path.dirname(f), decodeURIComponent(p));
        if (fs.existsSync(target) && fs.statSync(target).isDirectory()) target = path.join(target, 'index.html');
        if (!fs.existsSync(target)) { broken.push({ file: rel(f), url: u, why: 'file not found' }); continue; }
      }
      if (frag && /\.html?$/i.test(target)) {
        if (!ids(read(target)).has(decodeURIComponent(frag))) broken.push({ file: rel(f), url: u, why: 'fragment not found' });
      }
    }
  }
  return { broken, external };
}

// ---------------------------------------------------------------- 2. privacy patterns
const PRIVACY = [
  { key: 'email', label: 'E-mail address', re: /[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}/g,
    keep: m => !/\.(png|jpg|svg|css|js)$/i.test(m) },
  { key: 'phone', label: 'Phone-number-like string', re: /(?<![\d$.,-])\(?\b\d{3}\)?[-. ]\d{3}[-. ]\d{4}\b(?![\d,])/g },
  { key: 'street', label: 'Street-address-like string',
    re: /\b\d{2,5}\s+(?:[NSEW]\.?\s+)?[A-Z][a-z]+(?:\s[A-Z][a-z]+)?\s+(?:Street|St|Avenue|Ave|Boulevard|Blvd|Drive|Dr|Road|Rd|Way|Court|Ct|Lane|Ln|Place|Pl|Terrace|Ter|Circle|Cir)\b\.?/g },
  { key: 'parcel', label: 'Parcel-number-like string', re: /(?<![\d-])\d{3}-\d{2}-\d{3}(?![\d-])|\b(?:APN|Assessor'?s? Parcel(?: Number| No\.?)?|Block\/Lot)\b\s*[:#]?\s*[\dA-Z][\dA-Z -]{3,}/g },
  { key: 'zip', label: 'Five-digit number in the Bay Area ZIP range', re: /(?<![\d$.,#-])9[45]\d{3}(?![\d,.]\d|\d)/g },
  // A number within $5 of one of the brief's figures as published (rounded to $10) but not equal to it:
  // most likely the unrounded original. Only the rounded values are stored here.
  { key: 'unrounded', label: 'Number within $5 of a rounded brief figure (likely the unrounded original)', re: nearRounded([550540, 539740, 114250, 7210, 2440]) }
];
function nearRounded(values) {
  const alts = [];
  for (const v of values) for (let n = v - 5; n < v + 5; n++) {
    if (n === v) continue;
    const s = String(n);
    alts.push(s, s.replace(/(\d)(?=(\d{3})+$)/g, '$1,'), s.replace(/(\d)(?=(\d{3})+$)/g, '$1_'));
  }
  return new RegExp('(?<![\\d.,_])(?:' + Array.from(new Set(alts)).join('|') + ')(?![\\d_]|[.,]\\d)', 'g');
}
function checkPrivacy(files) {
  const perFile = [];
  for (const f of files) {
    if (!TEXT_EXT.has(path.extname(f).toLowerCase())) continue;
    let text = fs.readFileSync(f, 'utf8');
    if (/\.html?$/i.test(f)) text = stripTags(text.replace(/<!--[\s\S]*?-->/g, ' '));
    text = text.replace(/https?:\/\/[^\s"'<>)]+/g, ' ');       // official URLs often contain digit runs
    const counts = {};
    for (const p of PRIVACY) {
      const ms = (text.match(p.re) || []).filter(m => !p.keep || p.keep(m));
      if (ms.length) counts[p.key] = ms.length;
    }
    if (Object.keys(counts).length) perFile.push({ file: rel(f), area: area(f), counts });
  }
  return perFile;
}

// ---------------------------------------------------------------- 3. $10 rounding (model analysis pages)
function checkRounding(file) {
  const bad = [];
  const text = stripTags(fs.readFileSync(file, 'utf8'));
  const re = /\$\s?(\d[\d,]*(?:\.\d+)?)/g;
  let m;
  while ((m = re.exec(text))) {
    const v = Number(m[1].replace(/,/g, ''));
    if (!isFinite(v) || v < 10) continue;
    if (Math.abs(v / 10 - Math.round(v / 10)) > 1e-9) bad.push(m[0]);
  }
  return bad;
}

// ---------------------------------------------------------------- 4. sourced rows, 5. hosts (model pages)
function hostOf(u) { try { return new URL(u.startsWith('//') ? 'https:' + u : u).hostname.toLowerCase(); } catch (e) { return ''; } }
const isOfficial = h => OFFICIAL.some(r => r.test(h));
function checkRows(file) {
  const html = fs.readFileSync(file, 'utf8');
  const bad = []; let rows = 0;
  const tb = /<tbody[^>]*>([\s\S]*?)<\/tbody>/gi; let t;
  while ((t = tb.exec(html))) {
    const tr = /<tr[^>]*>([\s\S]*?)<\/tr>/gi; let r;
    while ((r = tr.exec(t[1]))) {
      rows++;
      const links = attrs(r[1]).filter(a => a.attr === 'href').map(a => a.url);
      const official = links.some(u => /^https:\/\//.test(u) && isOfficial(hostOf(u)));
      const flagged = links.some(u => /^flagged\.html#F-/.test(u));
      if (!official && !flagged) bad.push(stripTags(r[1]).replace(/\s+/g, ' ').trim().slice(0, 90));
    }
  }
  return { rows, bad };
}
function checkHosts(file) {
  const html = fs.readFileSync(file, 'utf8');
  const bad = [];
  const res = /<(script|link|img|iframe|source|video|audio)\b[^>]*>/gi; let m;
  while ((m = res.exec(html))) {
    for (const a of attrs(m[0])) {
      if (/^(https?:)?\/\//i.test(a.url) && !(m[1].toLowerCase() === 'link' && /rel\s*=\s*["']?(canonical)/i.test(m[0])))
        bad.push('external resource: ' + a.url);
    }
  }
  for (const a of attrs(html)) {
    if (a.attr !== 'href' || !/^(https?:)?\/\//i.test(a.url)) continue;
    const h = hostOf(a.url);
    if (!/^https:/.test(a.url)) bad.push('not https: ' + a.url);
    else if (!isOfficial(h) && !REPO_HOSTS.some(r => r.test(h))) bad.push('not an official host: ' + a.url);
  }
  return bad;
}

// ---------------------------------------------------------------- run
function run() {
  const files = walk(ROOT, []);
  const html = files.filter(f => /\.html?$/i.test(f));
  const modelHtml = html.filter(f => f.startsWith(MODEL + path.sep));
  const links = checkLinks(files);
  const privacy = checkPrivacy(files);
  const report = {
    filesScanned: files.length, htmlPages: html.length, modelPages: modelHtml.length,
    brokenLinks: links.broken, externalLinkCount: links.external.length,
    privacy, rounding: {}, rows: {}, hosts: {}, failures: []
  };
  const inModel = r => r.file.startsWith('model/');
  for (const b of links.broken.filter(inModel)) report.failures.push(`broken link in ${b.file}: ${b.url} (${b.why})`);
  for (const p of privacy.filter(inModel)) report.failures.push(`privacy pattern in ${p.file}: ${JSON.stringify(p.counts)}`);
  for (const f of modelHtml) {
    const name = rel(f);
    const rows = checkRows(f);
    report.rows[name] = rows.rows;
    for (const b of rows.bad) report.failures.push(`row without official source or flag in ${name}: ${b}`);
    const hosts = checkHosts(f);
    report.hosts[name] = hosts.length;
    for (const b of hosts) report.failures.push(`${name}: ${b}`);
    if (/model\/(index|decision|projections)\.html$/.test(name)) {
      const bad = checkRounding(f);
      report.rounding[name] = bad.length;
      for (const b of bad) report.failures.push(`figure not rounded to $10 in ${name}: ${b}`);
    }
  }
  return report;
}

function summarise(report) {
  const byArea = {};
  for (const p of report.privacy) {
    const a = byArea[p.area] || (byArea[p.area] = { files: 0 });
    a.files++;
    for (const k of Object.keys(p.counts)) a[k] = (a[k] || 0) + p.counts[k];
  }
  const brokenByArea = {};
  for (const b of report.brokenLinks) { const a = b.file.includes('/') ? b.file.split('/')[0] + '/' : '(root)'; brokenByArea[a] = (brokenByArea[a] || 0) + 1; }
  return { byArea, brokenByArea };
}

module.exports = { run, summarise, PRIVACY, ROOT };

if (require.main === module) {
  const report = run();
  const s = summarise(report);
  const totalRows = Object.values(report.rows).reduce((a, b) => a + b, 0);
  console.log(`Scanned ${report.filesScanned} files; ${report.htmlPages} HTML pages (${report.modelPages} under model/).`);
  console.log(`Internal links: ${report.brokenLinks.length} broken in the whole tree ${JSON.stringify(s.brokenByArea)}.`);
  for (const b of report.brokenLinks) console.log(`  - ${b.file} -> ${b.url} (${b.why})`);
  console.log(`model/: ${totalRows} table rows, each with an official source link or a Flagged link.`);
  console.log(`model/: figures not rounded to $10 on analysis pages: ${Object.values(report.rounding).reduce((a, b) => a + b, 0)}.`);
  console.log('Privacy patterns by area (counts only):');
  for (const a of Object.keys(s.byArea).sort()) console.log(`  ${a.padEnd(14)} ${JSON.stringify(s.byArea[a])}`);
  if (report.failures.length) {
    console.log(`\nFAILED: ${report.failures.length} finding(s) inside model/:`);
    for (const f of report.failures.slice(0, 60)) console.log('  - ' + f);
    process.exit(1);
  }
  console.log('\nOK: no findings inside model/.');
}
