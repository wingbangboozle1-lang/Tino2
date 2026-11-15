/* Household inputs as supplied by the owner, every dollar rounded to the nearest $10.
   Owners are placeholders: Property A (Cupertino), Property B (San Francisco west side).
   Scenario knobs (growth, returns, tax rates) are labelled assumptions, not forecasts.
   Official sources explain rules and benchmarks; owner-stated figures are flagged. */
(function () {
  const BASE = Object.freeze({
    startYear: 2026,
    aValue: 3100000, aAssessed: 550540,          // owner-stated Nov 2026 value; 2026 factored base
    bValue: 1800000, bAssessed: 114250,          // owner-stated Nov 2026 value; 2025 factored base (latest supplied)
    aRate: 7210 / 539740,                        // implied from the 2025 bill ÷ assessed value; bill includes flat direct charges
    bRate: 2440 / 114250,                        // implied from the 2025 bill ÷ assessed value; bill includes flat direct charges
    appreciation: 0.035, assessmentGrowth: 0.02,
    expenseInflation: 0.03, rentGrowth: 0.03, sfRentGrowth: 0.016,
    portfolioNet: 0.05, saleCost: 0.055, vacancy: 0.07, management: 0.085,
    maintenanceA: 0.0075, maintenanceB: 0.0125,
    ordinaryTax: 0.30, capitalGainsTax: 0.361, primaryGainExclusion: 250000,
// capitalGainsTax = 20% federal top + 3.8% NIIT + 12.3% CA top + 1% CA Behavioral Health Services
// Tax on taxable income above $1,000,000 (R&TC §17043; FTB Form 540 line 62). CA components verified
// from the official FTB 2025 Form 540 rate schedules; capital gains taxed as ordinary income, no
// preferential rate. The 1% surcharge only applies above $1M and is not indexed.
// See guide/tax.html for the source-linked row and the Flagged page for the CA flag status.
    aRentMonthly: 6390, bRentMonthly: 7150,      // A: HUD small-area FMR 4BR benchmark, not a quote. B: owner-stated, two units.
    aWaterMonthly: 125, aSolarMonthlyCredit: 15, // owner ranges $100–$150 and a $10–$20 credit, midpoints
    aInsuranceAnnual: 2690,                      // CDI survey median (40y home, $1M cover, $2,500 ded) — not a quote
    bWaterMonthly: 365, bElectricMonthly: 50,    // owner ranges $330–$400 and $30–$70, midpoints
    bInsuranceAnnual: 3353,                      // CDI SF-Sunset survey median — wrong product for a 3-unit building; flagged proxy
    bFeeAnnual: 120,                             // invented placeholder; SF fees not verified
    // Official 2025–Feb 2027 allowance and 2026/2027 basic exclusions;
    // later amounts are hypothetical indexation, not published IRS/BOE figures.
    prop19Amount: 1044586,
    // Projection basis for carrying the allowance forward: the statutory adjustment
    // uses the FHFA California house-price change each other February 16 (BOE LTA
    // 2025/009). 2.86% is the 20-year CAGR of the FHFA San Jose-area HPI series on
    // FRED (2006 Q3–2026 Q2); it is a projection, not a published BOE figure.
    prop19Index: 0.0286,
    estateExclusion: 15000000, estateExclusion2027: 15480000, estateIndex: 0.02
  });

  function round10(value) {
    if (value === null || value === undefined || !Number.isFinite(value)) return null;
    return Math.sign(value) * Math.round(Math.abs(value) / 10) * 10;
  }
  function fmtMoney(value) {
    const rounded = round10(value);
    if (rounded === null) return '—';
    return (rounded < 0 ? '−' : '') + '$' + Math.abs(rounded).toLocaleString('en-US');
  }
  function futureValue(present, annualRate, years) {
    return present * Math.pow(1 + annualRate, years);
  }
  function prop19Steps(year) {
    // This annual illustration assumes transfer after the February 16 adjustment.
    return Math.max(0, Math.floor((year - 2025) / 2));
  }
  function modelAllowance(year, config = BASE) {
    // Enacted windows (BOE LTA 2025/009 enclosure, read 15 Nov 2026):
    // $1,000,000 for 16 Feb 2021 – 15 Feb 2023; $1,022,600 for 16 Feb 2023 –
    // 15 Feb 2025; $1,044,586 for 16 Feb 2025 – 15 Feb 2027. Later windows are
    // carried forward at the statutory index basis (config.prop19Index): a
    // projection of the biennial adjustment, not a published BOE figure.
    if (year < 2023) return 1000000;
    if (year < 2025) return 1022600;
    if (year <= 2026) return config.prop19Amount;
    return config.prop19Amount * Math.pow(1 + config.prop19Index, prop19Steps(year));
  }
  function seriesFor(property, year, config = BASE) {
    if (!['A', 'B'].includes(property) || year < config.startYear) throw new Error('Invalid property or year');
    const n = year - config.startYear;
    const isA = property === 'A';
    const market = futureValue(isA ? config.aValue : config.bValue, config.appreciation, n);
    const factoredBase = futureValue(isA ? config.aAssessed : config.bAssessed, config.assessmentGrowth, n);
    // A simplified decline-in-value proxy; actual lien-date value is determined by the assessor.
    const assessed = Math.min(factoredBase, market);
    const rate = isA ? config.aRate : config.bRate;
    return { year, market, factoredBase, assessed, tax: assessed * rate, rate };
  }
  function inheritanceValues(year, config = BASE) {
    const current = seriesFor('A', year, config);
    const allowance = modelAllowance(year, config);
    // This example's FBYV is below its market value. Exact treatment is fact-specific.
    const primaryAssessed = Math.min(current.market, Math.max(current.assessed, current.market - allowance));
    return {
      market: current.market, carryForwardAssessed: current.assessed,
      fullAssessed: current.market, primaryAssessed, allowance,
      primaryTax: primaryAssessed * config.aRate, fullTax: current.market * config.aRate,
      primarySavings: (current.market - primaryAssessed) * config.aRate
    };
  }
  function annualA(year, option, config = BASE) {
    if (!['live', 'rent'].includes(option)) throw new Error('Invalid holding option');
    const transferYear = config.inheritYear || year;
    if (year < transferYear) throw new Error('Holding costs start at transfer');
    const inherited = inheritanceValues(transferYear, config);
    const n = year - config.startYear, yearsSinceTransfer = year - transferYear;
    const market = seriesFor('A', year, config).market;
    const startingBase = option === 'live' ? inherited.primaryAssessed : inherited.fullAssessed;
    const factoredBase = futureValue(startingBase, config.assessmentGrowth, yearsSinceTransfer);
    const assessed = Math.min(factoredBase, market);
    const propertyTax = assessed * config.aRate;
    const water = futureValue(config.aWaterMonthly * 12, config.expenseInflation, n);
    const solarCredit = config.aSolarMonthlyCredit * 12; // zero in this example, not a finding
    const insurance = futureValue(config.aInsuranceAnnual, config.expenseInflation, n);
    const maintenance = market * config.maintenanceA;
    const operatingCost = propertyTax + water + insurance + maintenance - solarCredit;
    if (option === 'live') {
      return { year, market, factoredBase, assessed, propertyTax, water, solarCredit, insurance,
        maintenance, grossRent: 0, vacancyCost: 0, managementCost: 0, noi: -operatingCost,
        incomeTax: 0, afterTaxCash: -operatingCost };
    }
    const grossRent = futureValue(config.aRentMonthly * 12, config.rentGrowth, n);
    const vacancyCost = grossRent * config.vacancy;
    const collected = grossRent - vacancyCost;
    const managementCost = collected * config.management;
    const noi = collected - managementCost - operatingCost;
    // No depreciation or passive-loss benefit is invented without taxpayer-specific facts.
    const incomeTax = Math.max(0, noi) * config.ordinaryTax;
    return { year, market, factoredBase, assessed, propertyTax, water, solarCredit, insurance,
      maintenance, grossRent, vacancyCost, managementCost, noi, incomeTax, afterTaxCash: noi - incomeTax };
  }
  function decision(config = BASE, horizon = 10) {
    if (!Number.isInteger(horizon) || horizon < 1 || !Number.isInteger(config.inheritYear)) throw new Error('Invalid horizon or transfer year');
    const transferYear = config.inheritYear;
    const inherited = inheritanceValues(transferYear, config);
    // For the assumed FMV basis, immediate net sale proceeds produce no positive taxable gain.
    const initial = inherited.market * (1 - config.saleCost);
    const ret = config.portfolioNet;
    const result = {
      sell: { initialNet: initial, firstYearCash: initial * ret,
        terminal: futureValue(initial, ret, horizon) }
    };
    for (const option of ['rent', 'live']) {
      let cashReserve = 0;
      const yearly = [];
      for (let t = 1; t <= horizon; t += 1) {
        const row = annualA(transferYear + t, option, config);
        cashReserve = cashReserve * (1 + ret) + row.afterTaxCash;
        yearly.push(row);
      }
      const finalMarket = seriesFor('A', transferYear + horizon, config).market;
      const realized = finalMarket * (1 - config.saleCost);
      const gain = Math.max(0, realized - inherited.market);
      // A conditional illustration, not a determination of actual home-sale eligibility.
      const exclusion = option === 'live' && horizon >= 2 ? Math.min(config.primaryGainExclusion, gain) : 0;
      const capitalGainsTax = Math.max(0, gain - exclusion) * config.capitalGainsTax;
      const finalSale = realized - capitalGainsTax;
      result[option] = { initialNet: 0, firstYearCash: yearly[0].afterTaxCash,
        terminal: finalSale + cashReserve, cashReserve, finalSale, finalMarket,
        capitalGainsTax, gainExclusion: exclusion, yearly };
    }
    result.transfer = inherited;
    result.winner = ['sell', 'rent', 'live'].sort((a, b) => result[b].terminal - result[a].terminal)[0];
    return result;
  }
  function sfAnnual(year, config = BASE) {
    const n = year - config.startYear, series = seriesFor('B', year, config);
    const grossRent = futureValue(config.bRentMonthly * 12, config.sfRentGrowth, n);
    const vacancyCost = grossRent * config.vacancy;
    const managementCost = (grossRent - vacancyCost) * config.management;
    const water = futureValue(config.bWaterMonthly * 12, config.expenseInflation, n);
    const electricity = futureValue(config.bElectricMonthly * 12, config.expenseInflation, n);
    const insurance = futureValue(config.bInsuranceAnnual, config.expenseInflation, n);
    const maintenance = series.market * config.maintenanceB;
    const fee = futureValue(config.bFeeAnnual, config.expenseInflation, n);
    const noi = grossRent - vacancyCost - managementCost - series.tax - water - electricity - insurance - maintenance - fee;
    return { year, ...series, propertyTax: series.tax, grossRent, vacancyCost, managementCost, water, electricity, insurance, maintenance, fee, noi };
  }
  function estateRow(year, config = BASE) {
    const a = seriesFor('A', year, config).market;
    const b = seriesFor('B', year, config).market;
    const exclusion = year <= 2026 ? config.estateExclusion : futureValue(config.estateExclusion2027, config.estateIndex, year - 2027);
    // Only the fictional A is hypothesized as included; the heir's B is not automatically the donor's.
    return { year, a, b, combined: a, exclusion };
  }
  window.MODEL = { BASE, round10, fmtMoney, futureValue, prop19Steps, modelAllowance,
    seriesFor, inheritanceValues, annualA, decision, sfAnnual, estateRow };
})();
