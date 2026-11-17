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
      ['Property A · synthetic starting market / assessment',`${money(c.aValue)} / ${money(c.aAssessed)}`,'Invented teaching inputs, not a valuation, tax record or estimate of a real property.',src('tax')],
      ['Property B · synthetic starting market / assessment',`${money(c.bValue)} / ${money(c.bAssessed)}`,'Invented teaching inputs. This example is separate from Property A; actual title and estate inclusion are private facts.',src('tax')],
      ['Both · home growth / assessment growth',`${pct(growth)} / ${pct(c.assessmentGrowth)}`,'Scenario rates; the 2% cap is not a guaranteed actual increase. Assessment is capped at modeled market value.',src('tax')],
      ['Property A · synthetic effective tax-rate assumption',pct(c.aRate),'Invented example ratio, not a parcel rate or tax-bill calculation.',src('tax')],
      ['Property B · synthetic effective tax-rate assumption',pct(c.bRate,4),'Invented example ratio, not a parcel rate or tax-bill calculation.',src('sfTax')],
      ['Property A · synthetic rent / vacancy / management',`${money(c.aRentMonthly)} per month / ${pct(c.vacancy)} / ${pct(c.management)}`,'Rent is a fabricated model input, not a HUD benchmark, quote or lawful-rent determination. Vacancy applies to gross rent. No property-management cost is charged on the rental path, because the published reference model charges none — a known omission, published on the Flagged page.',src('rent')],
      ['Rent the living path avoids',`${money(d.imputedRentMonthly)} per month`,'The living path is credited the rent an owner does not pay while occupying the home, at the same growth rate as the rent it replaces. It is an assumption you can change, not a valuation of the home to you.',src('rent')],
      ['Property A · synthetic water / insurance / maintenance',`${money(c.aWaterMonthly)} monthly / ${money(c.aInsuranceAnnual)} yearly / ${pct(c.maintenanceA)} of market value yearly`,'Invented costs, not household bills, a tariff result, a survey match or an insurance quote. Water and insurance grow at a scenario rate.',src('water','Utility context')+' · '+src('insurance','Insurance context')],
      ['Property B · synthetic rent / water / electricity / insurance',`${money(c.bRentMonthly)} monthly / ${money(c.bWaterMonthly)} monthly / ${money(c.bElectricMonthly)} monthly / ${money(c.bInsuranceAnnual)} yearly`,'All values are fabricated model inputs, not a rent roll, lease, bill, quote or description of real unit occupancy.',src('sf','Rent-rule context')+' · '+src('sfWater','Utility context')],
      ['B · maintenance / reserves / annual fee',`${pct(c.maintenanceB)} of value / ${pct(c.vacancy)} vacancy / ${pct(c.management)} management / ${money(c.bFeeAnnual)} yearly`,'Maintenance rates are assumptions. The annual fee is an unverified placeholder. Utilities grow 3%. Vacancy applies to gross rent, management after vacancy.',src('rent')],
      ['Sale cost / portfolio return',`${pct(c.saleCost)} / ${pct(ret)} annual net proxy`,'Invented assumptions, not quotes or forecasts. No additional portfolio liquidation tax.',src('invest')],
      ['Income / capital-gain tax rates',`${pct(c.ordinaryTax)} / ${pct(c.capitalGainsTax)}`,'Flat combined scenario rates; no rental depreciation, recapture, loss benefit or taxpayer-specific brackets.',src('rent')],
      ['Primary-residence exclusion',`${money(c.primaryGainExclusion)} assumed at endpoint`,'Assumes the use and other requirements are met; real eligibility is not automatic.',src('residence')],
      ['Prop 19 amount at transfer',money(d.transfer.allowance),'Enacted windows through 15 Feb 2027 are published; later windows are carried forward at the statutory index basis (a projection, not a published BOE figure). Assumes the transfer is after the February 16 adjustment.',src('boe')]
    ];
    document.getElementById('assumptions').innerHTML=assumptions.map(tr).join('');
    const sameYear=[
      ['Basis at the transfer (date-of-death value)',money(d.transfer.market),'The inherited home takes its basis at fair market value on the date of death — the IRS general rule.',src('irs')],
      ['Sale price modeled at the transfer date',money(d.transfer.market),'The sale closes in the same tax year as the inheritance, before any modeled growth.',src('irs')],
      ['Selling costs at the modeled rate',money(d.transfer.market*c.saleCost),'A share of price; a negotiated assumption, not a statutory rate.',src('invest')],
      ['Taxable gain in the same tax year',money(0),'Price minus basis is zero by construction in this model, so there is no gain for the government to tax in the sale year.',src('irs')],
      ['Capital-gains tax at the modeled rate',money(0),'No gain, no tax, when basis equals the sale price. Each later year adds potential gain.',src('irs')],
      ['Net proceeds available to invest',money(d.sell.initialNet),'What the sell path actually starts with, after sale costs.',src('invest')],
      ['Value at the end of the selected horizon if invested',money(d.sell.terminal),'The sell row of the comparison below, on the selected horizon and return assumption.',src('invest')]
    ];
    const sameEl=document.getElementById('same-year-sale');
    if(sameEl) sameEl.innerHTML=sameYear.map(tr).join('');
    const names={sell:'Sell and reinvest',rent:'Rent it out',live:'Live in it'};
    document.getElementById('winner').innerHTML=`<h3>On these inputs: ${names[d.winner]} leads.</h3><p>Synthetic example inputs are used; scenario rates are assumptions, not forecasts. This is a calculation, not tax or legal advice. The transfer is modeled in ${y} and the comparison ends in ${y+horizon}. Change assumptions and review the omitted costs before drawing conclusions.</p>`;
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
