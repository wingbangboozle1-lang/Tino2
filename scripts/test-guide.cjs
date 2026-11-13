/* Tests the public artifact as rendered. This file contains no household data. */
const {JSDOM,VirtualConsole}=require('../.cache/test/node_modules/jsdom');
const fs=require('fs'),path=require('path'),assert=require('assert');
const root=path.resolve('_public');
const pages=['index.html',...fs.readdirSync(path.join(root,'guide')).filter(f=>f.endsWith('.html')).map(f=>'guide/'+f)];
const hosts=new Set(['www.boe.ca.gov','boe.ca.gov','asr.santaclaracounty.gov','www.irs.gov','www.sco.ca.gov','leginfo.legislature.ca.gov','www.sf.gov','sftreasurer.org','www.sfpuc.gov','www.sfmta.com','www.sfelections.org','www.cupertino.gov','www.pge.com','www.insurance.ca.gov','www.huduser.gov','www.fdic.gov','www.investor.gov','www.cbo.gov','www.bls.gov','fred.stlouisfed.org','pubs.usgs.gov','www.congress.gov','docs.github.com','www.cbo.gov','www.census.gov','www.freddiemac.com','www.cfpnet.com','www.sjwater.com','www.sfpuc.gov','www.sf.gov','fred.stlouisfed.org']);
let rows=0, checks=0;
function check(ok,msg){checks++;assert(ok,msg);}
function open(file){
 const errors=[],vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push(e.message));
 const dom=new JSDOM(fs.readFileSync(path.join(root,file),'utf8'),{url:'https://example.org/Tino2/'+file,runScripts:'outside-only',virtualConsole:vc});
 for(const script of dom.window.document.querySelectorAll('script')){
  try {
   const src=script.getAttribute('src');
   check(!src || !/^(?:https?:)?\/\//i.test(src),file+' external script forbidden');
   dom.window.eval(src?fs.readFileSync(path.resolve(root,path.dirname(file),src),'utf8'):script.textContent);
  } catch(e){errors.push(e.stack||String(e));}
 }
 check(errors.length===0,file+' runtime error: '+errors.join('\n'));
 return dom;
}
function inspect(dom,file){
 const doc=dom.window.document;
 check(Boolean(doc.querySelector('nav[aria-label]')),file+' accessible navigation missing');
 check(doc.querySelector('h1')!==null,file+' missing heading');
 const navCount=doc.querySelectorAll('nav a').length;
 check(navCount===new Set(fs.readdirSync(path.join(root,'guide')).filter(f=>f.endsWith('.html'))).size+1,file+' incomplete navigation: '+navCount);
 check(doc.querySelector('meta[name=referrer][content=no-referrer]')!==null,file+' referrer policy missing');
 check(!doc.querySelector('form,input,textarea,iframe'),file+' unexpected data input or embed');
 for(const th of doc.querySelectorAll('thead th')) check(th.getAttribute('scope')==='col',file+' missing column scope');
 check(doc.body.textContent.toLowerCase().includes('public'),file+' lacks public warning');
 for(const tr of doc.querySelectorAll('tbody tr')){
  rows++;
  const links=[...tr.querySelectorAll('a[href^="https://"]')];
  const heads=tr.closest('table').querySelectorAll('thead tr:last-child th');
  check(tr.querySelectorAll(':scope > td').length===heads.length,file+' mismatched table cells: '+tr.textContent.slice(0,100));
  check(links.length>0,file+' row without source: '+tr.textContent.slice(0,100));
  check(links.some(a=>hosts.has(new URL(a.href).hostname)),file+' row without approved agency source');
 }
 for(const el of doc.querySelectorAll('a[href],script[src],link[rel="stylesheet"][href]')){
  const href=el.getAttribute('href')||el.getAttribute('src');
  if(!href||href.startsWith('#')) continue;
  if(/^https?:/.test(href)) {check(href.startsWith('https://'),file+' insecure link');continue;}
  check(!/^(?:mailto:|tel:|javascript:|data:)/i.test(href),file+' disallowed link');
  const target=path.resolve(root,path.dirname(file),decodeURIComponent(href.split('#')[0].split('?')[0]));
  check(target.startsWith(root+path.sep) && fs.existsSync(target),file+' broken local target '+href);
 }
 // Published currency amounts are rounded to ten dollars. This is not an anonymization test.
 const text=doc.body.textContent;
 for(const match of text.matchAll(/\$\s*(\d{1,3}(?:,\d{3})+|\d+)(?![\d,])/g)){
  const amount=Number(match[1].replace(/,/g,''));
  check(amount%10===0,file+' non-$10 dollar amount: '+match[0]);
 }
 check(!/\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b/i.test(text),file+' email in rendered text');
}
for(const file of pages){
 const dom=open(file);inspect(dom,file);
 if(file==='guide/decision.html'){
  const d=dom.window.document;
  const before=d.getElementById('comparison').textContent;
  d.getElementById('transfer-year').value='2050';d.getElementById('transfer-year').dispatchEvent(new dom.window.Event('change'));
  check(d.getElementById('comparison').textContent!==before,'Changing transfer year must change the comparison');
  check(d.querySelectorAll('#years-a tr').length===51 && d.querySelectorAll('#years-b tr').length===51,'Both annual tables must cover 51 calendar years');
  const M=dom.window.MODEL,c={...M.BASE,inheritYear:2045},a=M.inheritanceValues(2045,c),d10=M.decision(c,10);
  check(Math.abs(a.primaryAssessed-Math.max(a.carryForwardAssessed,a.market-a.allowance))<1e-6,'Prop 19 example formula');
  check(Math.abs(d10.sell.terminal-a.market*(1-c.saleCost)*Math.pow(1+c.portfolioNet,10))<1e-6,'Sale proceeds compounding');
  check(M.estateRow(2026,{...c,bValue:c.bValue*10}).combined===c.aValue,'Already-owned B is excluded from donor estate example');
  check(M.fmtMoney(125)==='$130' && M.fmtMoney(-125)==='−$130' && M.fmtMoney(null)==='—','Rounding and unknown handling');
  check(!Number.isNaN(d10.rent.terminal)&&!Number.isNaN(d10.live.terminal),'Finite strategy results');
  inspect(dom,file+' (changed controls)');
 }
 if(file==='guide/stress.html'){
  const S=dom.window.STRESS,d=dom.window.document;
  check(Object.keys(S.paths).length===5,'Five stress paths');
  for(const k of Object.keys(S.paths)){
   const r=S.run(k);check(r.length===50 && r[0].year===2046 && r[49].year===2095,'50-year path '+k);
   check(r.every(x=>['sell','rent','live','realSell','realRent','realLive'].every(v=>Number.isFinite(x[v]))),'Finite stress path '+k);
   check(r.every(x=>x.assessed<=x.market && x.assessed<=x.factoredBase && x.liveAssessed<=x.market),'Stress decline-in-value proxy '+k);
   check(r.every(x=>Math.abs(x.realSell*x.priceIndex-x.sell)<1e-6),'Stress real/nominal reconciliation '+k);
  }
  const early=S.run('crisis').at(-1),late=S.run('late').at(-1);
  check(Math.abs(early.sell-late.sell)<1e-6,'Early and late examples contain same portfolio returns');
  check(Math.abs(early.rent-late.rent)>1,'Cash flow sequencing changes rental outcome');
  check(S.run('crisis')[0].assessed===S.run('crisis')[0].market,'Early crash models a temporary decline in assessment');
  check(d.querySelectorAll('#stress-years tbody tr').length===250,'All stress annual rows rendered');
 }
 if(file==='guide/suggestions.html'){
  const d=dom.window.document,sel=d.querySelector('[data-suggestion="S01"]');
  sel.value='consider';sel.dispatchEvent(new dom.window.Event('change'));
  check(JSON.parse(dom.window.localStorage.getItem('tino2-public-suggestions-v2')).S01==='consider','Suggestion saves status only');
  const pathSel=d.querySelector('[data-suggestion="PATH"]');pathSel.value='privacy';pathSel.dispatchEvent(new dom.window.Event('change'));
  check(JSON.parse(dom.window.localStorage.getItem('tino2-public-suggestions-v2')).PATH==='privacy','Path saves locally');
  d.getElementById('clear-selections').click();check(!dom.window.localStorage.getItem('tino2-public-suggestions-v2'),'Clear removes local marks');
 }
 dom.window.close();
}
console.log(`PASS: ${pages.length} rendered pages, ${rows} source-linked table rows, ${checks} checks; controls and model invariants verified.`);
