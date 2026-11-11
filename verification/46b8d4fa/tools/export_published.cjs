#!/usr/bin/env node
/*
  Session 46b8d4fa - verification helper (read-only with respect to the site).

  Renders every published page (index.html + site/*.html) with jsdom, exactly as
  scripts/runtime-test.cjs does, and writes what a visitor sees to a JSON file:
    - the base settings object the pages compute from (MODEL.BASE)
    - every rendered table (nearest heading, header cells, body cells, links per row)
    - every element that shows a dollar amount outside a table (cards, worked arithmetic)

  Output goes to .cache/46b8d4fa/published.json, which is git-ignored on purpose:
  this session does not copy household inputs into its own committed files.

  Usage:  npm install --prefix .cache/test jsdom --no-audit --no-fund
          node verification/46b8d4fa/tools/export_published.cjs
*/
const fs = require('fs');
const path = require('path');
const repo = path.resolve(__dirname, '..', '..', '..');
let JSDOM, VirtualConsole;
try { ({ JSDOM, VirtualConsole } = require(path.join(repo, '.cache/test/node_modules/jsdom'))); }
catch (e) { console.error('jsdom missing: run  npm install --prefix .cache/test jsdom --no-audit --no-fund'); process.exit(2); }

const files = ['index.html', ...fs.readdirSync(path.join(repo, 'site')).filter(f => f.endsWith('.html')).sort().map(f => 'site/' + f)];
const clean = s => s.replace(/\s+/g, ' ').trim();
const out = { generated: new Date().toISOString(), commit: null, base: null, pages: {} };
try { out.commit = require('child_process').execSync('git rev-parse HEAD', { cwd: repo }).toString().trim(); } catch (e) {}

for (const file of files) {
  const errors = [];
  const vc = new VirtualConsole(); vc.on('jsdomError', e => errors.push(String(e.message).slice(0, 300)));
  const dom = new JSDOM(fs.readFileSync(path.join(repo, file), 'utf8'), { runScripts: 'outside-only', url: 'https://example.org/Tino2/' + file, virtualConsole: vc });
  const doc = dom.window.document;
  for (const script of doc.querySelectorAll('script')) {
    try {
      const code = script.src ? fs.readFileSync(path.resolve(repo, path.dirname(file), script.getAttribute('src').split('?')[0]), 'utf8') : script.textContent;
      dom.window.eval(code);
    } catch (e) { errors.push(String(e.stack || e).slice(0, 300)); }
  }
  if (!out.base && dom.window.MODEL && dom.window.MODEL.BASE) out.base = JSON.parse(JSON.stringify(dom.window.MODEL.BASE));

  const headingFor = el => {
    // nearest preceding h1-h4 in document order
    let best = '';
    const all = [...doc.querySelectorAll('h1,h2,h3,h4,table')];
    for (const node of all) { if (node === el) break; if (/^H[1-4]$/.test(node.tagName)) best = clean(node.textContent); }
    return best;
  };
  const tables = [...doc.querySelectorAll('table')].map((t, i) => ({
    index: i,
    heading: headingFor(t),
    head: [...t.querySelectorAll('thead th')].map(th => clean(th.textContent)),
    rows: [...t.querySelectorAll('tbody tr')].map(tr => ({
      cells: [...tr.children].map(td => clean(td.textContent)),
      links: [...tr.querySelectorAll('a[href]')].map(a => a.getAttribute('href'))
    }))
  }));
  // text blocks outside tables that contain a dollar figure or a percentage
  const blocks = [];
  for (const el of doc.querySelectorAll('p,li,h1,h2,h3,h4,div,span,strong,td')) {
    if (el.closest('table') || el.closest('nav') || el.closest('script')) continue;
    if (el.children.length > 0 && [...el.children].some(c => /\$|%/.test(c.textContent))) continue; // keep leaf-most carriers
    const t = clean(el.textContent);
    if (t && /\$\s?\d|\d%/.test(t)) blocks.push(t);
  }
  const links = [...doc.querySelectorAll('a[href]')].map(a => ({ href: a.getAttribute('href'), text: clean(a.textContent).slice(0, 80) }));
  const controls = [...doc.querySelectorAll('select,input')].map(c => ({ id: c.id, value: c.value, options: c.tagName === 'SELECT' ? [...c.options].map(o => ({ value: o.value, text: clean(o.textContent) })) : undefined }));
  out.pages[file] = { title: doc.title, errors, tables, blocks: [...new Set(blocks)], links, controls, nav: [...doc.querySelectorAll('nav a[href]')].map(a => ({ href: a.getAttribute('href'), text: clean(a.textContent) })) };
  dom.window.close();
}

const dest = path.join(repo, '.cache', '46b8d4fa');
fs.mkdirSync(dest, { recursive: true });
fs.writeFileSync(path.join(dest, 'published.json'), JSON.stringify(out, null, 1));
const summary = Object.entries(out.pages).map(([f, p]) => `${f}: ${p.tables.length} tables, ${p.tables.reduce((a, t) => a + t.rows.length, 0)} rows, ${p.blocks.length} figure blocks, ${p.errors.length} runtime errors`);
console.log(summary.join('\n'));
console.log('base settings exported:', out.base ? Object.keys(out.base).length + ' keys' : 'NOT FOUND');
console.log('written (git-ignored):', path.relative(repo, path.join(dest, 'published.json')));
if (Object.values(out.pages).some(p => p.errors.length)) process.exit(1);
