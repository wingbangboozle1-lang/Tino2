/* Only invented inputs. The controls never save or transmit data. */
(function(){
  const M=window.MODEL, B=M.BASE, money=M.fmtMoney;
  const ref={
    boe:'https://www.boe.ca.gov/prop19/',
    tax:'https://boe.ca.gov/proptaxes/pdf/lta25023.pdf',
    irs:'https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances',
    rent:'https://www.irs.gov/publications/p527',
    residence:'https://www.irs.gov/taxtopics/tc701',
    insurance:'https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/',
    water:'https://www.cupertino.gov/Residents/Utilities/Water',
    sfWater:'https://www.sfpuc.gov/sites/default/files/accounts-and-services/Rates_Schedule_Water_Sewer_2026-7.pdf',
    sfTax:'https://sftreasurer.org/property/secured-property-taxes',
    invest:'https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/world-investor-week-2026-investor-bulletin',
    sf:'https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit'
  };
  const src=(key,label='Official context only')=>`<a href="${ref[key]}" rel="noopener noreferrer">${label} ↗</a>`;
  const tr=xs=>'<tr>'+xs.map((x,i)=>`<td${i===xs.length-1?' class="source"':''}>${x}</td>`).join('')+'</tr>';
  const pct=(x,maximumFractionDigits=2)=>(100*x).toLocaleString('en-US',{maximumFractionDigits})+'%';
  function render(){
    const y=Number(document.getElementById('transfer-year').value), horizon=Number(document.getElementById('hold-years').value);
    const growth=Number(document.getElementById('home-growth').value), ret=Number(document.getElementById('portfolio-return').value);
    const c={...B,inheritYear:y,appreciation:growth,portfolioNet:ret};
    const d=M.decision(c,horizon);
    const assumptions=[
      ['A · starting market / assessment',`${money(c.aValue)} / ${money(c.aAssessed)}`,'Invented 2026 values; no appraisal or bill.',src('tax')],
      ['B · starting market / assessment',`${money(c.bValue)} / ${money(c.bAssessed)}`,'Invented 2026 values; B is already owned, not inherited.',src('tax')],
      ['Both · home growth / assessment growth',`${pct(growth)} / ${pct(c.assessmentGrowth)}`,'Scenario rates; the 2% cap is not a guaranteed actual increase. Assessment is capped at modeled market value.',src('tax')],
      ['A · assumed ad valorem rate',pct(c.aRate),'Invented combined rate; excludes direct and supplemental charges.',src('tax')],
      ['B · ad valorem rate',pct(c.bRate,8),'The 2026–27 SF secured rate is held constant as a future scenario; excludes direct charges.',src('sfTax')],
      ['A · rent / vacancy / management',`${money(c.aRentMonthly)} per month / ${pct(c.vacancy)} / ${pct(c.management)}`,'Invented 2026 rent; 3% annual growth. Vacancy applies to gross rent; management applies after vacancy.',src('rent')],
      ['A · water / insurance / maintenance',`${money(c.aWaterMonthly)} monthly / ${money(c.aInsuranceAnnual)} yearly / ${pct(c.maintenanceA)} of market value yearly`,'Invented 2026 costs; water and insurance grow 3% a year. Solar credit and electricity expense are zero in this example, not verified.',src('water','Water context')+' · '+src('insurance','Insurance context')],
      ['B · rent / water / electricity / insurance',`${money(c.bRentMonthly)} monthly / ${money(c.bWaterMonthly)} monthly / ${money(c.bElectricMonthly)} monthly / ${money(c.bInsuranceAnnual)} yearly`,'Invented 2026 amounts. Rent is the combined amount from two rented units; the owner-available unit is not rented. 1.6% annual rent growth is only a continuing scenario.',src('sf','Rent-rule context')+' · '+src('sfWater','Utility context')],
      ['B · maintenance / reserves / annual fee',`${pct(c.maintenanceB)} of value / ${pct(c.vacancy)} vacancy / ${pct(c.management)} management / ${money(c.bFeeAnnual)} yearly`,'Invented 2026 amounts; annual fee and utilities grow 3%. Vacancy applies to gross rent, management after vacancy.',src('rent')],
      ['Sale cost / portfolio return',`${pct(c.saleCost)} / ${pct(ret)} annual net proxy`,'Invented assumptions, not quotes or forecasts. No additional portfolio liquidation tax.',src('invest')],
      ['Income / capital-gain tax rates',`${pct(c.ordinaryTax)} / ${pct(c.capitalGainsTax)}`,'Flat combined scenario rates; no rental depreciation, recapture, loss benefit or taxpayer-specific brackets.',src('rent')],
      ['Primary-residence exclusion',`${money(c.primaryGainExclusion)} assumed at endpoint`,'Assumes the use and other requirements are met; real eligibility is not automatic.',src('residence')],
      ['Prop 19 amount at transfer',money(d.transfer.allowance),'Official 2025–27 base, followed by hypothetical biennial growth. Assumes the transfer is after the February 16 adjustment; future allowances are unknown.',src('boe')]
    ];
    document.getElementById('assumptions').innerHTML=assumptions.map(tr).join('');
    const names={sell:'Sell and reinvest',rent:'Rent then sell',live:'Live then sell'};
    document.getElementById('winner').innerHTML=`<h3>In this fictional setup: ${names[d.winner]} leads.</h3><p>That is a calculation for invented assumptions, not advice or a personalized result. The transfer is modeled in ${y} and the comparison ends in ${y+horizon}. Change assumptions and review the omitted costs before drawing conclusions.</p>`;
    document.getElementById('comparison').innerHTML=['sell','rent','live'].map(k=>{
      const a=d[k], cash=k==='sell'?`${money(a.firstYearCash)} portfolio change (not a distribution)`:money(a.firstYearCash);
      return tr([`<strong>${names[k]}</strong>`,money(a.initialNet),cash,`<strong>${money(a.terminal)}</strong>`,src(k==='sell'?'invest':k==='rent'?'rent':'boe','Rule / risk context')]);
    }).join('');
    let arows='', brows='';
    for(let year=2026;year<=2076;year++){
      const pre=M.seriesFor('A',year,c);
      let assessment,taxes,cost;
      if(year<y){ assessment=money(pre.assessed)+' (before transfer)';taxes=money(pre.tax)+' (before transfer)';cost='— not modeled before transfer'; }
      else{
        const l=M.annualA(year,'live',c),r=M.annualA(year,'rent',c);
        const operating=x=>x.propertyTax+x.water+x.insurance+x.maintenance-x.solarCredit;
        assessment=money(l.assessed)+' / '+money(r.assessed);
        taxes=money(l.propertyTax)+' / '+money(r.propertyTax);
        cost=money(operating(l))+' / '+money(operating(r));
      }
      arows+=tr([year,money(pre.market),assessment,taxes,cost,src('boe','Assessment rules')+' · '+src('water','Water context')]);
      const b=M.sfAnnual(year,c);
      brows+=tr([year,money(b.market)+' / '+money(b.assessed),money(b.propertyTax),money(b.grossRent),[b.water,b.electricity,b.insurance,b.maintenance].map(money).join(' / '),money(b.noi),src('sfTax','Tax context')+' · '+src('sf','Rent context')]);
    }
    document.getElementById('years-a').innerHTML=arows;
    document.getElementById('years-b').innerHTML=brows;
  }
  document.querySelectorAll('.controls select').forEach(el=>el.addEventListener('change',render));
  render();
})();
