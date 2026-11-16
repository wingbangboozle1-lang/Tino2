const {JSDOM,VirtualConsole}=require('../.cache/test/node_modules/jsdom');
const fs=require('fs'),path=require('path'),assert=require('assert');
const root=path.resolve('_public');let count=0, rows=0;
// Repointed 16 Nov 2026 (session ec971900): this script scanned `_public/site`, which the
// publication manifest stopped packaging when the legacy dashboard was excluded, so it failed
// with a raw ENOENT. It now runs the same runtime and broken-local-link checks on the pages the
// manifest actually publishes. scripts/test-guide.cjs remains the stricter gate (source links and
// the $10 rule); this one is the fast check.
if(!fs.existsSync(root+'/guide'))throw new Error('_public is not built or is stale: run python3 scripts/package-site.py first');
for(const file of ['index.html',...fs.readdirSync(root+'/guide').filter(x=>x.endsWith('.html')).map(x=>'guide/'+x)]){
 const errors=[],vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push(e.message));
 const dom=new JSDOM(fs.readFileSync(root+'/'+file,'utf8'),{runScripts:'outside-only',url:'https://example.org/Tino2/'+file,virtualConsole:vc});
 for(const script of dom.window.document.querySelectorAll('script')) {
  try{dom.window.eval(script.src?fs.readFileSync(path.resolve(root,path.dirname(file),script.getAttribute('src')),'utf8'):script.textContent)}catch(e){errors.push(e.stack)}
 }
 assert.equal(errors.length,0,file+': '+errors.join('\n'));
 for(const tr of dom.window.document.querySelectorAll('tbody tr')){
  rows++; assert(tr.querySelector('a[href^="https://"]'),file+' row missing official source: '+tr.textContent.slice(0,90));
 }
 assert(dom.window.document.querySelector('nav'));
 for(const a of dom.window.document.querySelectorAll('a[href]')){
  const href=a.getAttribute('href');if(!href || /^(https?:|#|blob:)/.test(href))continue;
  assert(fs.existsSync(path.resolve(root,path.dirname(file),href.split('#')[0])),file+' broken '+href);
 }
 count++;dom.window.close();
}
console.log(`PASS: ${count} rendered pages; ${rows} rendered rows source-linked; no runtime errors or broken local links`);
