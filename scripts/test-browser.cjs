/* End-to-end smoke test against the packaged public site; no external network is used. */
'use strict';
const {chromium}=require('../.cache/test/node_modules/playwright-core');
const executable=require('../.cache/test/node_modules/@sparticuz/chromium');
const fs=require('fs'),path=require('path'),http=require('http'),assert=require('assert/strict');
const root=path.resolve('_public');
// Navigation length is derived, not hardcoded: adding a reviewed page used to
// break this smoke test while the site itself was correct.
const navCount=fs.readdirSync(path.join(root,'site')).filter(f=>f.endsWith('.html')).length+1;
const mime={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.txt':'text/plain; charset=utf-8'};
const server=http.createServer((req,res)=>{
  const decoded=decodeURIComponent(new URL(req.url,'http://test').pathname);
  const f=path.resolve(root,'.'+(decoded==='/'?'/index.html':decoded));
  if(!f.startsWith(root+path.sep) || !fs.existsSync(f) || !fs.statSync(f).isFile()){res.writeHead(404).end();return;}
  res.setHeader('content-type',mime[path.extname(f)]||'application/octet-stream');
  fs.createReadStream(f).pipe(res);
});
(async()=>{
 let browser;
 try{
  await new Promise(resolve=>server.listen(0,'0.0.0.0',resolve));
  const origin=`http://127.0.0.1:${server.address().port}`;
  browser=await chromium.launch({executablePath:await executable.executablePath(),args:executable.args,headless:true});
  const context=await browser.newContext({viewport:{width:1440,height:900}});
  const page=await context.newPage(), errors=[],external=[];
  page.on('pageerror',e=>errors.push(e.message));
  page.on('request',r=>{if(!r.url().startsWith(origin+'/'))external.push(r.url());});
 // Every reviewed page is smoked, derived from the packaged tree so a new page
  // cannot be silently skipped. The published artifact is the dashboard (index.html
  // plus site/**), so the routes come from there, not from guide/.
  const routes=['/',...fs.readdirSync(path.join(root,'site')).filter(f=>f.endsWith('.html')).sort().map(f=>'/site/'+f)];
  for(const route of routes){
   const response=await page.goto(origin+route,{waitUntil:'networkidle'});
   assert.equal(response.status(),200,route);
   assert.equal(await page.locator('nav a').count(),navCount,route+' navigation');
   assert(await page.locator('h1').isVisible(),route+' heading');
   const broken=await page.locator('tbody tr').evaluateAll(rows=>rows.filter(r=>!r.querySelector('a[href^="https://"]')).length);
   assert.equal(broken,0,route+' source links');
   await page.addScriptTag({path:require.resolve('../.cache/test/node_modules/axe-core/axe.min.js')});
   const violations=await page.evaluate(async()=>{const r=await window.axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa']}});return r.violations.map(v=>v.id);});
   assert.deepEqual(violations,[],route+' WCAG automated violations');
  }
  await page.goto(origin+'/site/decision.html');
  await page.waitForSelector('#comparison tr');
  assert.equal(await page.locator('#years-a tr').count(),51);
  assert.equal(await page.locator('#years-b tr').count(),51);
  const first=await page.locator('#comparison').innerText();
  await page.selectOption('#transfer-year','2050');
  assert.notEqual(await page.locator('#comparison').innerText(),first,'transfer selector recalculates');
  await page.selectOption('#hold-years','50');
  assert((await page.locator('#winner').innerText()).includes('2100'),'horizon recalculates');
  await page.screenshot({path:'.cache/test/decision-desktop.png',fullPage:false});
  await page.goto(origin+'/site/stress.html');
  assert.equal(await page.locator('#stress-years details').count(),5);
  await page.locator('#stress-years details').first().locator('summary').click();
  assert.equal(await page.locator('#stress-years details[open] tbody tr').count(),50);
  await page.goto(origin+'/site/suggestions.html');
  await page.selectOption('[data-suggestion="S01"]','consider');
  await page.selectOption('[data-suggestion="PATH"]','privacy');
  await page.reload();
  assert.equal(await page.locator('[data-suggestion="S01"]').inputValue(),'consider');
  assert.equal(await page.locator('[data-suggestion="PATH"]').inputValue(),'privacy');
  const saved=await page.evaluate(()=>JSON.parse(localStorage.getItem('tino2-public-suggestions-v2')));
  assert.deepEqual(saved,{S01:'consider',PATH:'privacy'});
  await page.click('#clear-selections');
  assert.equal(await page.evaluate(()=>localStorage.getItem('tino2-public-suggestions-v2')),null);
  await page.setViewportSize({width:390,height:844});
  await page.goto(origin+'/');
  assert(await page.locator('.menu').isVisible());
  assert.equal(await page.locator('#navigation').isVisible(),false);
  await page.click('.menu');
  assert(await page.locator('#navigation').isVisible());
  assert.equal(await page.locator('.menu').getAttribute('aria-expanded'),'true');
  await page.click('.menu');
  const dimensions=await page.evaluate(()=>({width:document.documentElement.scrollWidth,viewport:innerWidth}));
  assert(dimensions.width<=dimensions.viewport+1,'mobile layout must not overflow');
  await page.screenshot({path:'.cache/test/overview-mobile.png',fullPage:false});
  const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});
  const fallback=await nojs.newPage();await fallback.goto(origin+'/site/properties.html');
  assert(await fallback.locator('#navigation').isVisible(),'mobile navigation works without JavaScript');
  assert(await fallback.locator('noscript').count()===1);
  assert((await fallback.locator('tbody tr').count())>0,'static rules remain available without JavaScript');
  // Some single-process headless builds terminate when a second context closes;
  // all contexts are closed together with the browser in the finally block.
  assert.deepEqual(errors,[],'browser errors');assert.deepEqual(external,[],'unexpected external requests');
  console.log('PASS: Chromium desktop/mobile, 10 pages, selectors, 50-year details, local-only selections, no-JS navigation, WCAG automated checks, and no external requests.');
 } finally {if(browser)await browser.close();server.close();}
})().catch(err=>{console.error(err);process.exitCode=1;});
