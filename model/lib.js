/*
 * Page-building helpers — session 5a1bd5be. Used only by build.js (Node).
 * Every table goes through table(): it refuses to emit a row that has neither an
 * official source nor a Flagged-for-Review entry, so an unsourced row cannot be published.
 */
'use strict';
const S = require('./src/sources.js');
const FL = require('./src/flags.js');
const Fmt = require('./src/format.js');

const flagIds = new Set(FL.FLAGS.map(f => f.id));

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

const SHORT = [
  [/^Internal Revenue Service/, 'IRS'], [/Government Publishing Office/, 'U.S. Code'],
  [/^California Legislative Information/, 'California Codes'], [/State Controller/, 'State Controller'],
  [/Franchise Tax Board/, 'Franchise Tax Board'], [/Board of Equalization/, 'Board of Equalization'],
  [/Santa Clara County Assessor/, 'Santa Clara Assessor'], [/Controller-Treasurer/, 'Santa Clara County'],
  [/Clerk-Recorder/, 'Santa Clara Recorder'], [/San Francisco Treasurer/, 'SF Treasurer'],
  [/Assessor-Recorder/, 'SF Assessor-Recorder'], [/Rent Board/, 'SF Rent Board'],
  [/Public Utilities Commission/, 'CPUC'], [/Department of Insurance/, 'Dept. of Insurance'],
  [/Housing and Urban Development/, 'HUD'], [/Federal Housing Finance Agency/, 'FHFA index'],
  [/Bureau of Labor Statistics/, 'BLS index'], [/Thrift Investment Board/, 'Thrift Savings Plan'],
  [/Secretary of State/, 'Secretary of State'], [/U\.S\. Congress/, 'Congress.gov']
];
function shortName(id) {
  const s = S.byId[id];
  if (!s) throw new Error('Unknown source id: ' + id);
  for (const [re, name] of SHORT) if (re.test(s.publisher)) return name;
  return s.publisher;
}
/** Link(s) to the official page(s). */
function src(ids) {
  return (ids || []).map(id => {
    const s = S.byId[id];
    if (!s) throw new Error('Unknown source id: ' + id);
    return `<a href="${esc(s.url)}" rel="noopener" title="${esc(s.publisher + ' — ' + s.title)}">${esc(shortName(id))}</a>`;
  }).join(' · ');
}
function flagLink(id, text) {
  if (!flagIds.has(id)) throw new Error('Unknown flag id: ' + id);
  return `<a class="flaglink" href="flagged.html#${id}">${esc(text || 'Flagged')}</a>`;
}

const STATUS = {
  verified: ['Verified', 'Read on the official page linked in this row.'],
  calculated: ['Calculated', 'Arithmetic on verified figures; the working is on the Method page.'],
  brief: ['From the brief', 'Supplied by the owner; not checked against public records, to avoid handling the address.'],
  assumption: ['Assumption', 'No official figure exists. Listed on the Flagged for Review page.'],
  unverified: ['Unverified', 'No official figure was retrieved. Left blank and flagged.'],
  model: ['Model result', 'Output of the model from the inputs listed on the Method page.'],
  question: ['Open question', 'Needs a fact only the family or their adviser has.'],
  caution: ['Caution', 'A limit on how far these pages can be relied on.']
};
function chip(status) {
  const s = STATUS[status];
  if (!s) throw new Error('Unknown status: ' + status);
  return `<span class="chip chip-${status}" title="${esc(s[1])}">${s[0]}</span>`;
}

/**
 * table({ caption, head: [..], num: [column indexes right-aligned], rows: [{ c: [..], status, src: [..], flag, cls }], note, id })
 * Adds "Status" and "Source" columns. Cells are HTML (already escaped by the caller where needed).
 */
function table(t) {
  const num = new Set(t.num || []);
  const head = t.head.concat(['Status', 'Source']);
  const body = t.rows.map((r, i) => {
    const hasSrc = r.src && r.src.length, hasFlag = !!r.flag;
    if (!hasSrc && !hasFlag) throw new Error(`Row ${i} of "${t.caption}" has neither a source nor a flag`);
    if ((r.status === 'verified' || r.status === 'calculated') && !hasSrc) throw new Error(`Row ${i} of "${t.caption}": ${r.status} needs a source`);
    if ((r.status === 'assumption' || r.status === 'unverified' || r.status === 'brief' || r.status === 'question' || r.status === 'caution') && !hasFlag) throw new Error(`Row ${i} of "${t.caption}": ${r.status} needs a flag`);
    if (r.c.length !== t.head.length) throw new Error(`Row ${i} of "${t.caption}" has ${r.c.length} cells, expected ${t.head.length}`);
    const cells = r.c.map((c, j) => j === 0 ? `<th scope="row">${c}</th>` : `<td${num.has(j) ? ' class="num"' : ''}>${c === null || c === undefined ? '' : c}</td>`).join('');
    const source = [hasSrc ? src(r.src) : '', hasFlag ? flagLink(r.flag) : ''].filter(Boolean).join(' · ');
    return `<tr${r.id ? ` id="${r.id}"` : ''}${r.cls ? ` class="${r.cls}"` : ''}>${cells}<td>${chip(r.status)}</td><td class="srccell">${source}</td></tr>`;
  }).join('\n');
  return `<div class="tablewrap"${t.id ? ` id="${t.id}"` : ''}><table>
<caption>${t.caption}</caption>
<thead><tr>${head.map((h, j) => `<th scope="col"${num.has(j) ? ' class="num"' : ''}>${h}</th>`).join('')}</tr></thead>
<tbody>
${body}
</tbody></table></div>${t.note ? `\n<p class="tablenote">${t.note}</p>` : ''}`;
}

const NAV = [
  ['index.html', 'Summary'], ['decision.html', 'Decision'], ['projections.html', 'Projections'],
  ['taxes.html', 'Taxes'], ['costs.html', 'Running costs'], ['process.html', 'Inheritance steps'],
  ['law.html', 'Law watch'], ['compare.html', 'Why pages differ'], ['sources.html', 'Sources'],
  ['flagged.html', 'Flagged'], ['method.html', 'Method']
];

function page(file, title, lead, body, opts) {
  opts = opts || {};
  const nav = NAV.map(([f, l]) => `<a href="${f}"${f === file ? ' aria-current="page"' : ''}>${l}</a>`).join('');
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive">
<meta name="description" content="${esc(opts.description || title)}">
<title>${esc(title)} · Inheritance model</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap topin">
    <a class="brand" href="index.html"><span class="mark" aria-hidden="true">A·B</span><span>Inheritance model<small>Property A (Cupertino) · Property B (San Francisco)</small></span></a>
    <nav aria-label="Pages">${nav}</nav>
  </div>
</header>
<main id="main" class="wrap">
<p class="crumb"><a href="../index.html">Repository home page</a> › Model › ${esc(title)}</p>
<h1>${title}</h1>
${lead ? `<p class="lead">${lead}</p>` : ''}
${body}
</main>
<footer class="foot">
  <div class="wrap">
    <p><strong>No personal information.</strong> People appear only as [OWNER], [HEIR] and [TRUSTEE]; properties only as A and B. The pages contain no names, addresses, parcel numbers or contact details.</p>
    <p><strong>Not advice.</strong> A planning model. Laws quoted were read on official pages on ${S.READ}; they change. Take the questions on the <a href="flagged.html">Flagged</a> page to an estate-planning attorney and a tax preparer before acting.</p>
    <p class="small">Pages generated by <code>model/build.js</code> from <code>model/src/</code>; checked by <code>model/check.js</code> and <code>model/test/</code>. Session 5a1bd5be. Dollar figures in the analysis are rounded to the nearest $10.</p>
  </div>
</footer>
${opts.scripts || ''}
</body>
</html>
`;
}

/** Horizontal bars comparing a few amounts (pure HTML/CSS, readable without CSS). */
function bars(items, opts) {
  opts = opts || {};
  const max = Math.max.apply(null, items.map(i => Math.abs(i.value))) || 1;
  return `<div class="bars"${opts.id ? ` id="${opts.id}"` : ''}>` + items.map(i =>
    `<div class="bar${i.best ? ' best' : ''}"><div class="barlabel">${i.label}</div><div class="bartrack"><div class="barfill ${i.cls || ''}" style="width:${(Math.abs(i.value) / max * 100).toFixed(1)}%"></div></div><div class="barvalue">${Fmt.usd(i.value)}</div></div>`
  ).join('') + '</div>';
}

/** Small line chart as inline SVG, with a text alternative. */
function lineChart(c) {
  const W = 760, H = 320, L = 64, R = 16, T = 16, B = 36;
  const xs = c.years, x0 = xs[0], x1 = xs[xs.length - 1];
  const all = [].concat.apply([], c.series.map(s => s.values));
  const ymax = c.ymax || Math.max.apply(null, all) * 1.05;
  const X = x => L + (x - x0) / (x1 - x0) * (W - L - R);
  const Y = v => T + (1 - v / ymax) * (H - T - B);
  const step = c.ystep || niceStep(ymax);
  let grid = '';
  for (let v = 0; v <= ymax + 1e-9; v += step) {
    grid += `<line x1="${L}" x2="${W - R}" y1="${Y(v).toFixed(1)}" y2="${Y(v).toFixed(1)}" class="grid"/><text x="${L - 8}" y="${(Y(v) + 4).toFixed(1)}" text-anchor="end" class="tick">${Fmt.usdM(v)}</text>`;
  }
  let xt = '';
  for (const x of xs) if ((x - x0) % 4 === 0) xt += `<text x="${X(x).toFixed(1)}" y="${H - B + 18}" text-anchor="middle" class="tick">${x}</text>`;
  const lines = c.series.map((s, i) => {
    const pts = s.values.map((v, k) => `${X(xs[k]).toFixed(1)},${Y(v).toFixed(1)}`).join(' ');
    return `<polyline points="${pts}" class="line l${i + 1}"/>`;
  }).join('');
  const legend = c.series.map((s, i) => `<span class="key"><span class="swatch s${i + 1}"></span>${esc(s.name)}</span>`).join('');
  return `<figure class="chart"><svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(c.title)}"><title>${esc(c.title)}</title>${grid}${xt}${lines}</svg>
<figcaption>${legend}<br><span class="small">${c.caption || ''}</span></figcaption></figure>`;
}
function niceStep(max) {
  const raw = max / 5, mag = Math.pow(10, Math.floor(Math.log10(raw)));
  for (const m of [1, 2, 2.5, 5, 10]) if (raw <= m * mag) return m * mag;
  return 10 * mag;
}

module.exports = { esc, src, flagLink, chip, table, page, bars, lineChart, shortName, STATUS, NAV };
