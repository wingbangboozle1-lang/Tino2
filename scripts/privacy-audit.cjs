/* Privacy regression for the public artifact. No private values are printed or copied.
   This is a limited collision/pattern scan, not proof of anonymization. */
'use strict';
const fs=require('fs'),path=require('path'),{JSDOM}=require('../.cache/test/node_modules/jsdom');
const root=path.resolve('_public'), bad=[];
const legacyPath=path.resolve('site/data/model.js');
let distinctive=new Set();
if(fs.existsSync(legacyPath)){
  // Legacy files remain public in the repository; they are not part of the artifact.
  global.window={};require(legacyPath);
  const m=global.window.MODEL;
  distinctive=new Set([...m.historyA,...m.historyB].map(x=>x.assessed).filter(x=>x>=50000).map(String));
  for(const k of ['aValue','aAssessed','bValue','bAssessed2025','bRentMonthly']){
    if(Number.isFinite(m.BASE[k])) distinctive.add(String(m.BASE[k]));
  }
}
function rawCollision(text){return (text.match(/\b[\d,]+\b/g)||[]).map(x=>x.replaceAll(',','')).some(x=>distinctive.has(x));}
function dollarCollision(text){return [...text.matchAll(/\$\s*([\d,]+)/g)].map(x=>x[1].replaceAll(',','')).some(x=>distinctive.has(x));}
function inspectText(file,text){
  if(rawCollision(text))bad.push(file+': distinctive legacy numeric token');
  if(/\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b/i.test(text))bad.push(file+': email-like identifier');
  if(/\b\d{1,5}\s+[A-Z][A-Za-z]*(?:\s+[A-Z][A-Za-z]*){0,2}\s+(?:Street|St\.|Avenue|Ave\.|Road|Rd\.|Boulevard|Blvd\.)\b/i.test(text))bad.push(file+': street-address-like identifier');
}
function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){
  const f=path.join(dir,e.name);if(e.isDirectory())walk(f);else if(/\.(html|js|css|txt)$/.test(f))inspectText(path.relative(root,f),fs.readFileSync(f,'utf8'));
}}
walk(root);
const pages=['index.html',...fs.readdirSync(root+'/guide').filter(x=>x.endsWith('.html')).map(x=>'guide/'+x)];
for(const file of pages){
  const dom=new JSDOM(fs.readFileSync(path.join(root,file),'utf8'),{runScripts:'outside-only',url:'https://example.org/Tino2/'+file});
  for(const s of dom.window.document.querySelectorAll('script'))dom.window.eval(fs.readFileSync(path.resolve(root,path.dirname(file),s.getAttribute('src')),'utf8'));
  if(dollarCollision(dom.window.document.body.textContent))bad.push(file+': legacy number in rendered dollars');
  if(dom.window.document.querySelector('form,input,textarea,iframe,script[src^="https:"],img[src^="https:"]'))bad.push(file+': input or external automatic resource');
  dom.window.close();
}
if(bad.length){for(const b of bad)console.error('Privacy review required:',b);process.exit(1);}
console.log('PASS: no distinctive legacy input/history tokens or common identifiers in the packaged source or default rendered dollar values. This is not proof of anonymity.');
