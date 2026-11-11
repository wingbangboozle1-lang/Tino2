/* Hypothetical stress paths, not official forecasts or estimated probabilities. */
(function () {
  const paths = {
    baseline: {name:'Changing-cycle baseline', source:'blsCPI'},
    crisis: {name:'Early housing / equity crash', source:'investorRisk'},
    inflation: {name:'Stagflation and insurance squeeze', source:'blsCPI'},
    late: {name:'Late crash / sequence risk', source:'investorRisk'},
    disaster: {name:'Uninsured repair and rent interruption', source:'insuranceResidential'}
  };
  function rates(key, t) {
    const cycle=(t-1)%10;
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
    let market=transfer.market, assessed=market, liveAssessed=transfer.primaryAssessed;
    let portfolio=market*(1-c.saleCost), reserve=0, liveReserve=0, priceIndex=1;
    let rent=c.aRent4BR*12*Math.pow(1+c.rentGrowth,19);
    let water=c.aWaterMonthly*12*Math.pow(1+c.expenseInflation,19);
    let insurance=c.aInsuranceAnnual*Math.pow(1+c.expenseInflation,19);
    const rows=[];
    for(let t=1;t<=50;t++) {
      const r=rates(key,t);
      market*=1+r.home; assessed*=1+Math.min(0.02,Math.max(0,r.inflation));
      liveAssessed*=1+Math.min(0.02,Math.max(0,r.inflation));
      priceIndex*=1+r.inflation; rent*=1+r.rent; water*=1+r.inflation;
      insurance*=(1+r.inflation)*r.insuranceJump;
      const tax=assessed*c.aRate, maintenance=market*c.maintenanceA;
      const costs=water+insurance+maintenance+r.repair-c.aSolarMonthlyCredit*12;
      const noi=rent*(1-r.vacancy)*(1-c.management)-tax-costs;
      const cash=noi-Math.max(0,noi)*c.ordinaryTax;
      portfolio*=1+r.portfolio;
      // Start-of-year reserve earns return; year-end operating cash follows.
      reserve=reserve*(1+r.portfolio)+cash;
      liveReserve=liveReserve*(1+r.portfolio)-costs-liveAssessed*c.aRate;
      const realized=market*(1-c.saleCost);
      const rentalNet=realized-Math.max(0,realized-transfer.market)*c.capitalGainsTax;
      const liveNet=realized-Math.max(0,realized-transfer.market-c.primaryGainExclusion)*c.capitalGainsTax;
      rows.push({year:2045+t,...r,market,assessed,tax,insurance,water,maintenance,cash,priceIndex,
        sell:portfolio,rent:rentalNet+reserve,live:liveNet+liveReserve,
        realSell:portfolio/priceIndex,realRent:(rentalNet+reserve)/priceIndex,realLive:(liveNet+liveReserve)/priceIndex});
    }
    return rows;
  }
  window.STRESS={paths,rates,run};
})();
