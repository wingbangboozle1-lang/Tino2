/* Entirely synthetic example paths, not official forecasts or estimated probabilities. */
(function () {
  const paths = {
    baseline: {name:'Changing-cycle baseline', source:'blsCPI'},
    crisis: {name:'Early deep crash (stylized)', source:'investorRisk'},
    inflation: {name:'Stagflation and insurance squeeze', source:'blsCPI'},
    late: {name:'Late crash / sequence risk', source:'investorRisk'},
    disaster: {name:'Uninsured repair and rent interruption', source:'insuranceResidential'}
  };
  function rates(key, t) {
    // Keep the same multiset of underlying rates for the early/late pair.
    const cycle=(key==='crisis'||key==='late') && t>=48 ? t-48 : (t-1)%10;
    let r={home: [0.04,0.05,0.02,-0.04,0,0.06,0.04,0.03,0.04,0.03][cycle],
      portfolio:[0.08,0.10,0.03,-0.12,0.02,0.13,0.07,0.05,0.06,0.06][cycle],
      inflation:[0.025,0.03,0.04,0.035,0.02,0.025,0.03,0.025,0.02,0.025][cycle],
      rent:0.025,vacancy:0.05,insuranceJump:1,repair:0};
    if ((key==='crisis' && t<=3)||(key==='late' && t>=48)) {
      const i=key==='crisis'?t-1:t-48;
      Object.assign(r,{home:[-0.25,-0.10,0.04][i],portfolio:[-0.35,-0.10,0.12][i],rent:-0.05,vacancy:0.20});
    }
    if(key==='inflation' && t<=5) Object.assign(r,{home:0,portfolio:0.01,inflation:0.08,rent:0.02,insuranceJump:t===1?2:1});
    if(key==='disaster' && t===10) Object.assign(r,{home:-0.15,vacancy:1,insuranceJump:2,repair:250000});
    return r;
  }
  function run(key) {
    if(!paths[key]) throw new Error('Unknown stress path');
    const c={...MODEL.BASE,inheritYear:2045}, transfer=MODEL.inheritanceValues(2045,c);
    let market=transfer.market, factoredBase=market, liveFactoredBase=transfer.primaryAssessed;
    let portfolio=market*(1-c.saleCost), reserve=0, liveReserve=0, priceIndex=1;
    let rent=c.aRentMonthly*12*Math.pow(1+c.rentGrowth,19);
    let water=c.aWaterMonthly*12*Math.pow(1+c.expenseInflation,19);
    let insurance=c.aInsuranceAnnual*Math.pow(1+c.expenseInflation,19);
    const rows=[];
    for(let t=1;t<=50;t++) {
      const r=rates(key,t);
      market*=1+r.home;
      // Keep the factored base even during a decline-in-value year, so it can recover later.
      factoredBase*=1+Math.min(0.02,Math.max(0,r.inflation));
      liveFactoredBase*=1+Math.min(0.02,Math.max(0,r.inflation));
      const assessed=Math.min(factoredBase,market), liveAssessed=Math.min(liveFactoredBase,market);
      priceIndex*=1+r.inflation; rent*=1+r.rent; water*=1+r.inflation;
      insurance*=(1+r.inflation)*r.insuranceJump;
      const tax=assessed*c.aRate, maintenance=market*c.maintenanceA;
      const costs=water+insurance+maintenance+r.repair-c.aSolarMonthlyCredit*12;
      const noi=rent*(1-r.vacancy)*(1-c.management)-tax-costs;
      const cash=noi-Math.max(0,noi)*c.ordinaryTax;
      portfolio*=1+r.portfolio;
      // The rent an owner avoids by occupying the home. It follows the same modelled rent path
      // as the renting option, scaled by the ratio of the chosen imputed rent to the modelled
      // rent, so setting the imputed rent to zero removes the credit entirely.
      const liveAvoided=rent*(MODEL.imputedRent(c)/c.aRentMonthly);
      // Start-of-year reserve earns return; year-end operating cash follows.
      reserve=reserve*(1+r.portfolio)+cash;
      liveReserve=liveReserve*(1+r.portfolio)-costs-liveAssessed*c.aRate+liveAvoided;
      const realized=market*(1-c.saleCost);
      // Endpoint convention, shared with the published monthly engine and with model.js: a
      // path still holding the house at the endpoint is worth the house at its market value
      // plus the cash it accumulated. No sale is assumed and no gain tax is charged on a
      // sale that is not modelled.
      const rentalNet=realized-Math.max(0,realized-transfer.market)*c.capitalGainsTax;
      // The illustrative residence exclusion is not available before two years of use.
      const liveExclusion=t>=2?c.primaryGainExclusion:0;
      const liveNet=realized-Math.max(0,realized-transfer.market-liveExclusion)*c.capitalGainsTax;
      rows.push({year:2045+t,...r,market,factoredBase,liveFactoredBase,assessed,liveAssessed,tax,liveTax:liveAssessed*c.aRate,insurance,water,maintenance,cash,priceIndex,
        sell:portfolio,rent:market+reserve,live:market+liveReserve,
        realSell:portfolio/priceIndex,realRent:(market+reserve)/priceIndex,realLive:(market+liveReserve)/priceIndex});
    }
    return rows;
  }
  function phased(key, parkingMonths=24, treasuryRate=0.03) {
    if(!paths[key]) throw new Error('Unknown stress path');
    if(![24,36].includes(parkingMonths)) throw new Error('Parking period must be 24 or 36 months');
    if(![0.01,0.03,0.05].includes(treasuryRate)) throw new Error('Treasury proxy must be 1%, 3%, or 5%');
    const rows=run(key), initial=MODEL.inheritanceValues(2045).market*(1-MODEL.BASE.saleCost);
    let immediate=initial, staged=initial;
    const waitYears=parkingMonths/12;
    return rows.map((r,i)=>{
      const t=i+1;
      // One illustrative 12-month phase-in follows the selected waiting period.
      // A 3M–2Y ladder's actual maturities, yields, taxes and prices are not modeled.
      const equityExposure=t<=waitYears?0:t===waitYears+1?0.5:1;
      immediate*=1+r.portfolio;
      staged*=((1-equityExposure)*(1+treasuryRate)+equityExposure*(1+r.portfolio));
      return {year:r.year,portfolioReturn:r.portfolio,treasuryProxy:treasuryRate,equityExposure,
        immediate,staged,realImmediate:immediate/r.priceIndex,realStaged:staged/r.priceIndex,
        difference:staged-immediate,realDifference:(staged-immediate)/r.priceIndex};
    });
  }
  window.STRESS={paths,rates,run,phased};
})();
