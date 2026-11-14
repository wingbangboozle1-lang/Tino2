(function(){
  const M=window.MODEL, S=window.STRESS, money=M.fmtMoney;
  const refs={
    blsCPI:'https://www.bls.gov/news.release/archives/cpi_01122023.htm',
    investorRisk:'https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/world-investor-week-2026-investor-bulletin',
    insuranceResidential:'https://pubs.usgs.gov/publication/fs20163020',
    bills:'https://www.treasurydirect.gov/marketable-securities/treasury-bills/',
    notes:'https://www.treasurydirect.gov/marketable-securities/treasury-notes/',
    pricing:'https://www.treasurydirect.gov/marketable-securities/understanding-pricing/'
  };
  const link=(url,label)=>`<a href="${url}" rel="noopener noreferrer">${label} ↗</a>`;
  const source=p=>link(refs[p.source],'Official risk context');
  const sourcePair=()=>link(refs.bills,'Treasury bills')+' · '+link(refs.notes,'Treasury notes')+' · '+link(refs.pricing,'Treasury pricing');
  const tr=xs=>'<tr>'+xs.map((x,i)=>`<td${i===xs.length-1?' class="source"':''}>${x}</td>`).join('')+'</tr>';
  const pct=x=>(100*x).toFixed(1)+'%';
  const pair=(a,b)=>`${money(a)} / ${money(b)}`;
  function render(){
    let results='',details='';
    for(const [key,p] of Object.entries(S.paths)){
      const rows=S.run(key),end=rows[rows.length-1];
      results+=tr([`<strong>${p.name}</strong>`,pair(end.sell,end.realSell),pair(end.rent,end.realRent),pair(end.live,end.realLive),source(p)]);
      const annual=rows.map(r=>tr([r.year,`${pct(r.home)} / ${pct(r.portfolio)} / ${pct(r.inflation)}`,money(r.market),pair(r.liveAssessed,r.assessed),pair(r.liveTax,r.tax),[r.water,r.insurance,r.maintenance,r.repair].map(money).join(' / '),money(r.cash),pair(r.sell,r.realSell),pair(r.rent,r.realRent),pair(r.live,r.realLive),source(p)])).join('');
      details+=`<details class="card"><summary>${p.name} · 50 annual rows</summary><div class="table-wrap"><table><thead><tr><th scope="col">Year</th><th scope="col">Home / portfolio / inflation</th><th scope="col">A market</th><th scope="col">Assessment · live / rent</th><th scope="col">Tax · live / rent</th><th scope="col">Water / insurance / maintenance / repair</th><th scope="col">After-tax rental cash</th><th scope="col">Sell · nominal / real</th><th scope="col">Rent · nominal / real</th><th scope="col">Live · nominal / real</th><th scope="col">Context only</th></tr></thead><tbody>${annual}</tbody></table></div></details>`;
    }
    document.getElementById('stress-results').innerHTML=results;
    document.getElementById('stress-years').innerHTML=details;

    const months=Number(document.getElementById('phase-months').value);
    const treasury=Number(document.getElementById('treasury-proxy').value);
    let summary='',windows='';
    for(const [key,p] of Object.entries(S.paths)){
      const rows=S.phased(key,months,treasury),end=rows[rows.length-1];
      summary+=tr([`<strong>${p.name}</strong><br>${months} months parked, ${pct(treasury)} flat proxy`,pair(end.immediate,end.realImmediate),pair(end.staged,end.realStaged),pair(end.difference,end.realDifference),source(p)+' · '+sourcePair()]);
      const indexes=key==='crisis'?[0,1,2,3,4,5]:key==='late'?[44,45,46,47,48,49]:[];
      for(const i of indexes){
        const r=rows[i];
        windows+=tr([`${p.name}<br>${r.year}`,pct(r.portfolioReturn),pct(r.treasuryProxy),pct(r.equityExposure),money(r.immediate),money(r.staged),money(r.difference),source(p)+' · '+sourcePair()]);
      }
    }
    document.getElementById('phase-summary').innerHTML=summary;
    document.getElementById('phase-years').innerHTML=windows;
  }
  document.getElementById('phase-months').addEventListener('change',render);
  document.getElementById('treasury-proxy').addEventListener('change',render);
  render();
})();
