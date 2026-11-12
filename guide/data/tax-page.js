(function(){
  const M=window.MODEL, reference='https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts';
  document.getElementById('estate-projections').innerHTML=[2028,2030,2035,2040,2045,2050,2060,2076].map(year=>`<tr><td>${year}</td><td>${M.fmtMoney(M.futureValue(M.BASE.estateExclusion2027,M.BASE.estateIndex,year-2027))} <span class="tag">scenario</span></td><td class="empty">— unknown</td><td class="source"><a href="${reference}" rel="noopener noreferrer">IRS 2027 base, not a forecast ↗</a></td></tr>`).join('');
})();
