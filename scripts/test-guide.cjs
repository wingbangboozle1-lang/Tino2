/* Tests the public artifact as rendered. This file contains no household data. */
const {JSDOM,VirtualConsole}=require('../.cache/test/node_modules/jsdom');
const fs=require('fs'),path=require('path'),assert=require('assert');
const root=path.resolve('_public');
const pages=['index.html',...fs.readdirSync(path.join(root,'guide')).filter(f=>f.endsWith('.html')).map(f=>'guide/'+f)];
// Dollar amounts published exactly by a government body. Each was re-read on
// 13 Nov 2026 against the official page that publishes it; the passage and the
// URL are recorded in verification/b2418dfa/REPORT.md. These are published
// rates, not household figures, so they are shown exactly rather than mis-rounded.
const OFFICIAL_AMOUNTS=new Map([
 [249,'SFMTA Proposition H FY 2027-28 multifamily base amount'],
 [129,'SFMTA Proposition H FY 2027-28 single-family base amount'],
]);
const hosts=new Set(['www.boe.ca.gov','boe.ca.gov','asr.santaclaracounty.gov','www.irs.gov','www.sco.ca.gov','leginfo.legislature.ca.gov','www.sf.gov','sftreasurer.org','www.sfpuc.gov','www.sfmta.com','www.sfelections.org','www.cupertino.gov','www.pge.com','www.insurance.ca.gov','www.huduser.gov','www.fdic.gov','www.investor.gov','www.cbo.gov','www.bls.gov','fred.stlouisfed.org','pubs.usgs.gov','www.congress.gov','docs.github.com','www.cbo.gov','www.census.gov','www.freddiemac.com','www.cfpnet.com','www.sjwater.com','www.sfpuc.gov','www.sf.gov']);
let rows=0, checks=0;
const seenTitles=new Set(), seenH1s=new Set();
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
  check(amount%10===0||OFFICIAL_AMOUNTS.has(amount),file+' non-$10 dollar amount: '+match[0]);
 }
 check(!/\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b/i.test(text),file+' email in rendered text');
}
for(const file of pages){
 const dom=open(file);inspect(dom,file);
 const title=dom.window.document.querySelector('title').textContent.trim();
 const h1=dom.window.document.querySelector('h1').textContent.trim();
 check(title.length>0,file+' empty title');
 check(!seenTitles.has(title),'duplicate page title: '+title);seenTitles.add(title);
 check(h1.length>0,file+' empty h1');
 check(!seenH1s.has(h1),'duplicate page h1: '+h1);seenH1s.add(h1);
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
 if(file==='guide/questions.html'){
  const d=dom.window.document;
  const heads=[...d.querySelectorAll('thead th')].map(th=>th.textContent.trim());
  check(heads.includes('Answer already known from official sources'),'Questions register states the rule-level answer');
  check(heads.includes('Household answer'),'Questions register keeps the household answer separate');
  const table=[...d.querySelectorAll('table')].find(t=>[...t.querySelectorAll('thead th')].some(th=>th.textContent.trim()==='Answer already known from official sources'));
  check(Boolean(table),'Questions register table found');
  const rows=[...table.querySelectorAll('tbody tr')];
  check(rows.length===20,'Questions register has 20 rows, found '+rows.length);
  for(const tr of rows){
   const cells=[...tr.querySelectorAll(':scope > td')];
   const rule=cells[2].textContent.trim();
   check(rule.startsWith('Rule known'),'Every question states the rule already known: '+rule.slice(0,60));
   check(cells[3].textContent.trim().startsWith('\u2014'),'Household answer must stay blank: '+cells[3].textContent.trim());
   check(cells[5].textContent.trim().length>0,'Decision impact must be stated');
  }
  const ready=[...d.querySelectorAll('h2')].map(h=>h.textContent.trim());
  check(ready.some(h=>h.includes('Can a decision reasonably be made yet')),'Decision-readiness section present');
  check(d.body.textContent.includes('Answer: not yet'),'Decision-readiness verdict present');
  check(d.querySelectorAll('a[href="suggestions.html"]').length>0,'Readiness verdict links to the suggestions register');
 }
 if(file==='guide/property.html'){
  const d=dom.window.document;
  const table=[...d.querySelectorAll('table')].find(t=>[...t.querySelectorAll('thead th')].some(th=>th.textContent.includes('Official annual amount')));
  check(Boolean(table),'Proposition H schedule table found');
  const rows=[...table.querySelectorAll('tbody tr')];
  check(rows.length===5,'Proposition H schedule has 5 rows, found '+rows.length);
  for(const tr of rows){
   check(tr.querySelectorAll('a[href^="https://www.sfmta.com/"]').length>0,'Proposition H row without an official link');
   const cells=[...tr.querySelectorAll(':scope > td')];
   check(cells[3].textContent.includes('unverified'),'Proposition H amount for B must stay unverified');
  }
 }
 if(file==='guide/conditions.html'){
  const d=dom.window.document,C=dom.window.CONDITIONS,i=C.inflation,p13=C.prop13;
  check(d.querySelectorAll('#band-table tr').length===C.BANDS.length,'Every scenario band renders');
  check(d.querySelectorAll('#compound-table tr').length===4,'Compounding table renders');
  check(d.querySelectorAll('#breakeven-table tr').length===6,'Break-even table renders');
  check(d.querySelectorAll('#cost-table tr').length===4,'Cost-structure table renders');
  const ys=Object.keys(C.CPI_ANNUAL).map(Number).sort((a,b)=>a-b);
  const ch=[];for(let k=1;k<ys.length;k++)ch.push(C.CPI_ANNUAL[ys[k]]/C.CPI_ANNUAL[ys[k-1]]-1);
  const mean=ch.reduce((a,b)=>a+b,0)/ch.length;
  check(Math.abs(mean-i.mean)<1e-12,'CPI mean recomputes from the stored annual series');
  check(ch.length===i.count,'CPI change count matches the series');
  check(Math.abs(Math.min(...ch)-i.min)<1e-12 && Math.abs(Math.max(...ch)-i.max)<1e-12,'CPI range recomputes');
  check(ch.filter(x=>x>0.03).length===i.above(0.03),'Years above 3% recomputes');
  check(C.PROP13_FACTORS.length===51 && p13.count===51,'51 published assessment years');
  check(C.PROP13_FACTORS.filter(f=>Math.abs(f-1.02)<1e-9).length===40 && p13.atCap===40,'40 years at the 2% cap');
  check(C.PROP13_FACTORS.filter(f=>f<1).length===1,'Exactly one negative inflation year');
  const b=C.BANDS.find(x=>x.key==='high');
  check(Math.abs(C.project(b,24,0).inflationMultiple-Math.pow(1.04,24))<1e-9,'Band projection exponent 24y');
  check(Math.abs(C.project(b,50,0).inflationMultiple-Math.pow(1.04,50))<1e-9,'Band projection exponent 50y');
  check(C.round10(1234)===1230 && C.round10(-1236)===-1240,'round10 behaviour');
 }
 if(file==='guide/brief.html'){
  const d=dom.window.document,B=dom.window.BREAKEVEN;
  check(d.querySelectorAll('#boundary-body tr').length===B.GROWTH.length,'Boundary grid rows');
  check(d.querySelectorAll('#threshold-body tr').length===B.GROWTH.length,'Break-even rows');
  check(d.querySelectorAll('#sensitivity-body tr').length===B.GROWTH.length+B.RETURNS.length+1,'Sensitivity rows including reference');
  const g=0.035, low=B.evaluate(g,0,24), mid=B.evaluate(g,0.05,24);
  check(['sell','rent','live'].includes(low.winner) && ['sell','rent','live'].includes(mid.winner),'Boundary winners are valid labels');
  check(low.winner!=='sell','A zero portfolio return must not favour selling on these inputs');
  check(mid.winner==='sell','The middle case favours selling on these inputs');
  let sawSell=false, monotone=true;
  for(const r of B.RETURNS){const w=B.evaluate(g,r,24).winner; if(w==='sell')sawSell=true; else if(sawSell)monotone=false;}
  check(monotone,'Selling becomes dominant at higher returns and never reverts');
  const be=B.sellBreakeven(g,24);
  check(be.threshold!==null && B.evaluate(g,be.threshold,24).winner==='sell','Break-even point actually leads with selling');
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
