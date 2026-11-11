const {JSDOM,VirtualConsole}=require('../.cache/test/node_modules/jsdom');
const fs=require('fs'),path=require('path'),assert=require('assert');
const root=path.resolve('_public');let count=0, rows=0;
for(const file of ['index.html',...fs.readdirSync(root+'/site').filter(x=>x.endsWith('.html')).map(x=>'site/'+x)]){
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
