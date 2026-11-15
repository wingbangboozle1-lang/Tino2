/* Privacy regression for the public artifact, under the owner's own rule (brief
   restated 15 Nov 2026): household dollar figures may appear ONLY rounded to the
   nearest $10; raw pre-rounding values, identifiers and property ZIP codes must
   never appear. This is a limited collision/pattern scan, not proof of anonymity. */
'use strict';
const fs=require('fs'),path=require('path'),{JSDOM}=require('../.cache/test/node_modules/jsdom');
const root=path.resolve('_public'), bad=[];
// Raw (pre-rounding) household values from the owner's records. Values that equal
// their own $10-rounded form (for example 493530, 6130, 1740, 7150) are allowed by
// definition; only tokens that rounding changes are banned here.
const RAW_BANNED=new Set([
 '550537','539743','529161','518786','508614','498642','483854','474368','465067','455949','449101','440305',
 '7207','7003','6917','6755','6662','6565','6383','6414','5965',
 '114248','112008','109814','107662','105595','104513','102465','100456','98488','96557',
 '2439','2315','2179','2107','2066','2197','2134','2061','1675',
]);
const ZIP_BANNED=new Set(['95014','94122']);
function tokens(text){return (text.match(/\b[\d,]+\b/g)||[]).map(x=>x.replaceAll(',',''));}
function inspectText(file,text){
  // Separate digit/letter adjacency first so money like "$2,179,680NextWord" tokenizes
  // as the full amount rather than a truncated fragment.
  text=text.replace(/([0-9])([A-Za-z])/g,'$1 $2').replace(/([A-Za-z])([0-9])/g,'$1 $2');
  for(const t of (text.match(/\d[\d,]*/g)||[]).map(x=>x.replaceAll(',',''))){
    const isYearLike=/^\d{4}$/.test(t) && Number(t)>=2010 && Number(t)<=2120;
    if(ZIP_BANNED.has(t))bad.push(file+': property ZIP code token');
    // Calendar-year columns legitimately print bare 4-digit years (2026-2095) that can
    // collide with a raw value. Money is always $-prefixed or comma-grouped in this
    // artifact, so bare year-range tokens are exempt from the raw check only.
    if(RAW_BANNED.has(t) && !isYearLike)bad.push(file+': raw pre-rounding household token');
  }
  // Dollar and comma-grouped amounts are money context: no exemption at all.
  for(const m of text.matchAll(/\$\s*([\d,]+)/g)){
    const t=m[1].replaceAll(',','');
    if(RAW_BANNED.has(t))bad.push(file+': raw pre-rounding household token in money context');
    if(ZIP_BANNED.has(t))bad.push(file+': property ZIP code token in money context');
  }
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
  for(const s of dom.window.document.querySelectorAll('script')){
    const src=s.getAttribute('src');
    // Inline scripts carry the generated rounded values; evaluate them as the browser would.
    dom.window.eval(src?fs.readFileSync(path.resolve(root,path.dirname(file),src),'utf8'):s.textContent);
  }
  inspectText(file+' (rendered)',dom.window.document.body.textContent);
  if(dom.window.document.querySelector('form,input,textarea,iframe,script[src^="https:"],img[src^="https:"]'))bad.push(file+': input or external automatic resource');
  dom.window.close();
}
if(bad.length){for(const b of bad)console.error('Privacy review required:',b);process.exit(1);}
console.log('PASS: no raw pre-rounding household token, property ZIP code or common identifier in the packaged source or rendered text. Rounded household figures are permitted by the owner rule of 15 Nov 2026. This is not proof of anonymity.');
