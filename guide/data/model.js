/* Fictional teaching inputs only. No household facts, records or results are used.
   These numbers are invented examples for demonstrating how the calculator works;
   they are not quotes, estimates or recommendations. Official links explain legal rules. */
(function () {
  const BASE = Object.freeze({
    startYear: 2026,
    aValue: 2000000, aAssessed: 600000,
    bValue: 1200000, bAssessed: 420000,
    aRate: 0.011, bRate: 0.012,
    appreciation: 0.035, assessmentGrowth: 0.02,
    expenseInflation: 0.03, rentGrowth: 0.03, sfRentGrowth: 0.016,
    portfolioNet: 0.05, saleCost: 0.055, vacancy: 0.07, management: 0.085,
    maintenanceA: 0.0075, maintenanceB: 0.0125,
    ordinaryTax: 0.30, capitalGainsTax: 0.361, primaryGainExclusion: 250000,
// Tax rates are simplified teaching assumptions. The 1% California surcharge above
// the statutory threshold is discussed separately and is not applied to this example.
    aRentMonthly: 4200, bRentMonthly: 4800,
    aWaterMonthly: 110, aSolarMonthlyCredit: 0,
    aInsuranceAnnual: 1800,
    bWaterMonthly: 240, bElectricMonthly: 80,
    bInsuranceAnnual: 2400,
    bFeeAnnual: 120,
    prop19Amount: 1044586,
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
