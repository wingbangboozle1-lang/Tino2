/*
  Deterministic planning model, not an appraisal or tax return.
  Observed household inputs are separated from official law and derived projections.
  All displayed currency is rounded to the nearest $10 by fmtMoney().
*/
(function () {
  const A_RATE = 7210 / 539740; // household-derived effective rate, not an official TRA rate
  const B_RATE = 2440 / 114250; // household-derived effective rate, not the city ad valorem rate
  const BASE = {
    startYear: 2026,
    aValue: 3100000,
    aAssessed: 550540,
    bValue: 1800000,
    bAssessed2025: 114250,
    aRate: A_RATE,
    bRate: B_RATE,
    appreciation: 0.035,
    assessmentGrowth: 0.02,
    expenseInflation: 0.03,
    rentGrowth: 0.03,
    sfRentGrowth: 0.016,
    portfolioGross: 0.06,
    portfolioTaxDrag: 0.01,
    saleCost: 0.06,
    vacancy: 0.05,
    management: 0.08,
    maintenanceA: 0.005,
    maintenanceB: 0.01,
    ordinaryTax: 0.333,
    capitalGainsTax: 0.331,
    primaryGainExclusion: 250000,
    aRent4BR: 6390,
    aRent3BR: 5870,
    bRent1BR: 2730,
    bRent2BR: 3310,
    aWaterMonthly: 125,
    aSolarMonthlyCredit: 15,
    aInsuranceAnnual: 1500,
    bWaterMonthly: 365,
    bElectricMonthly: 50,
    bInsuranceAnnual: 1500,
    bRentMonthly: 7150,
    bRentBoardFeeAnnual: 118,
    prop19Amount: 1044586,
    estateExclusion: 15000000,
    estateIndex: 0.02
  };

  const historyA = [
    [2026, null, null, 550540, "+2%"],
    [2025, 7210, "+2.9%", 539740, "+2%"],
    [2024, 7000, "+1.2%", 529160, "+2%"],
    [2023, 6920, "+2.4%", 518790, "+2%"],
    [2022, 6760, "+1.4%", 508610, "+2%"],
    [2021, 6660, "+1.5%", 498640, "+1%"],
    [2020, 6570, null, 493530, "+2%"],
    [2019, 6570, "+2.8%", 483850, "+2%"],
    [2018, 6380, null, 474370, "+2%"],
    [2017, 6380, "-0.5%", 465070, "+2%"],
    [2016, 6410, "+4.6%", 455950, "+1.5%"],
    [2015, 6130, "+2.8%", 449100, "+2%"],
    [2014, 5970, null, 440310, "+0.5%"]
  ].map(([year, tax, taxChange, assessed, assessedChange]) => ({ year, tax, taxChange, assessed, assessedChange }));

  const historyB = [
    [2025, 2440, "+5.3%", 114250, "+2%"],
    [2024, 2320, "+6.2%", 112010, "+2%"],
    [2023, 2180, "+3.4%", 109810, "+2%"],
    [2022, 2110, "+2%", 107660, "+2%"],
    [2021, 2070, "-5.9%", 105600, "+1%"],
    [2020, 2200, "+3%", 104510, "+2%"],
    [2019, 2130, "+3.5%", 102470, "+2%"],
    [2018, 2060, "+18.4%", 100460, "+2%"],
    [2017, 1740, "+3.9%", 98490, "+2%"],
    [2016, 1680, "+1.6%", 96560, "+1.5%"]
  ].map(([year, tax, taxChange, assessed, assessedChange]) => ({ year, tax, taxChange, assessed, assessedChange }));

  function round10(value) {
    if (value === null || value === undefined || !Number.isFinite(value)) return null;
    return Math.round(value / 10) * 10;
  }
  function fmtMoney(value, options = {}) {
    const rounded = round10(value);
    if (rounded === null) return "—";
    const sign = rounded < 0 ? "−" : (options.sign && rounded > 0 ? "+" : "");
    return sign + "$" + Math.abs(rounded).toLocaleString("en-US", { maximumFractionDigits: 0 });
  }
  function fmtExact(value) {
    if (value === null || value === undefined || !Number.isFinite(value)) return "—";
    return "$" + value.toLocaleString("en-US", { maximumFractionDigits: 0 });
  }
  function fmtPct(value, digits = 1) {
    return (value * 100).toFixed(digits) + "%";
  }
  function futureValue(present, annualRate, years) {
    return present * Math.pow(1 + annualRate, years);
  }
  function modelAllowance(year, config = BASE) {
    // Explicit assumption only: the official post-February-2027 amount is not yet published.
    const periods = Math.max(0, Math.ceil((year - 2026) / 2));
    return config.prop19Amount * Math.pow(1.02, periods);
  }
  function seriesFor(property, year, config = BASE) {
    const n = year - config.startYear;
    const isA = property === "A";
    const market = futureValue(isA ? config.aValue : config.bValue, config.appreciation, n);
    const assessed = isA
      ? futureValue(config.aAssessed, config.assessmentGrowth, n)
      : futureValue(config.bAssessed2025, config.assessmentGrowth, n + 1);
    const rate = isA ? config.aRate : config.bRate;
    return { year, market, assessed, tax: assessed * rate, rate };
  }
  function inheritanceValues(year, config = BASE) {
    const current = seriesFor("A", year, config);
    const allowance = modelAllowance(year, config);
    const primaryAssessed = current.market <= current.assessed + allowance
      ? current.assessed
      : current.market - allowance;
    return {
      market: current.market,
      carryForwardAssessed: current.assessed,
      fullAssessed: current.market,
      primaryAssessed,
      allowance,
      primaryTax: primaryAssessed * config.aRate,
      fullTax: current.market * config.aRate,
      primarySavings: (current.market - primaryAssessed) * config.aRate
    };
  }
  function annualA(year, option, config = BASE, rentChoice = "4BR") {
    const n = year - config.startYear;
    const inherited = inheritanceValues(config.inheritYear || year, config);
    const transferYear = config.inheritYear || year;
    const yearsSinceTransfer = Math.max(0, year - transferYear);
    const market = seriesFor("A", year, config).market;
    const fullAssessmentAtTransfer = inherited.fullAssessed;
    const primaryAssessmentAtTransfer = inherited.primaryAssessed;
    const assessed = option === "live"
      ? futureValue(primaryAssessmentAtTransfer, config.assessmentGrowth, yearsSinceTransfer)
      : futureValue(fullAssessmentAtTransfer, config.assessmentGrowth, yearsSinceTransfer);
    const propertyTax = assessed * config.aRate;
    const water = config.aWaterMonthly * 12 * Math.pow(1 + config.expenseInflation, n);
    const solarCredit = config.aSolarMonthlyCredit * 12; // deliberately held flat: no tariff forecast
    const insurance = config.aInsuranceAnnual * Math.pow(1 + config.expenseInflation, n);
    const maintenance = market * config.maintenanceA;
    const operatingCost = propertyTax + water + insurance + maintenance - solarCredit;
    if (option === "live") {
      return { year, market, assessed, propertyTax, water, solarCredit, insurance, maintenance, grossRent: 0, vacancyCost: 0, managementCost: 0, noi: -operatingCost, incomeTax: 0, afterTaxCash: -operatingCost };
    }
    const monthlyRent = (rentChoice === "3BR" ? config.aRent3BR : config.aRent4BR) * Math.pow(1 + config.rentGrowth, n);
    const grossRent = monthlyRent * 12;
    const collected = grossRent * (1 - config.vacancy);
    const vacancyCost = grossRent * config.vacancy;
    const managementCost = collected * config.management;
    const noi = collected - managementCost - operatingCost;
    // No depreciation or passive-loss benefit is imputed without land/building and taxpayer facts.
    const incomeTax = Math.max(0, noi) * config.ordinaryTax;
    return { year, market, assessed, propertyTax, water, solarCredit, insurance, maintenance, grossRent, vacancyCost, managementCost, noi, incomeTax, afterTaxCash: noi - incomeTax };
  }
  function afterTaxPortfolioReturn(config = BASE) {
    return config.portfolioGross - config.portfolioTaxDrag;
  }
  function decision(config = BASE, horizon = 10, rentChoice = "4BR") {
    const transferYear = config.inheritYear;
    const inherited = inheritanceValues(transferYear, config);
    const netImmediateSale = inherited.market * (1 - config.saleCost);
    const portfolioReturn = afterTaxPortfolioReturn(config);
    const result = {};
    result.sell = {
      option: "Sell & reinvest",
      initialNet: netImmediateSale,
      firstYearTax: 0,
      firstYearCash: netImmediateSale * portfolioReturn,
      terminal: netImmediateSale * Math.pow(1 + portfolioReturn, horizon),
      cashReserve: 0,
      finalSale: 0,
      capitalGainsTax: 0
    };
    ["rent", "live"].forEach(option => {
      let cashReserve = 0;
      const yearly = [];
      for (let t = 1; t <= horizon; t += 1) {
        const row = annualA(transferYear + t, option, config, rentChoice);
        cashReserve = cashReserve * (1 + portfolioReturn) + row.afterTaxCash;
        yearly.push(row);
      }
      const finalMarket = seriesFor("A", transferYear + horizon, config).market;
      const amountRealized = finalMarket * (1 - config.saleCost);
      const gainBeforeExclusion = Math.max(0, amountRealized - inherited.market);
      const exclusion = option === "live" && horizon >= 2 ? Math.min(config.primaryGainExclusion, gainBeforeExclusion) : 0;
      const capitalGainsTax = Math.max(0, gainBeforeExclusion - exclusion) * config.capitalGainsTax;
      const finalSale = amountRealized - capitalGainsTax;
      result[option] = {
        option: option === "rent" ? "Rent, then sell" : "Live, then sell",
        initialNet: 0,
        firstYearTax: yearly[0].propertyTax,
        firstYearCash: yearly[0].afterTaxCash,
        firstYearNOI: yearly[0].noi,
        terminal: finalSale + cashReserve,
        cashReserve,
        finalSale,
        finalMarket,
        amountRealized,
        capitalGainsTax,
        gainExclusion: exclusion,
        yearly
      };
    });
    result.transfer = inherited;
    result.portfolioReturn = portfolioReturn;
    result.horizon = horizon;
    result.rentChoice = rentChoice;
    result.winner = ["sell", "rent", "live"].sort((a, b) => result[b].terminal - result[a].terminal)[0];
    return result;
  }
  function sfAnnual(year, config = BASE, includeReserves = true) {
    const n = year - config.startYear;
    const series = seriesFor("B", year, config);
    const grossRent = config.bRentMonthly * 12 * Math.pow(1 + config.sfRentGrowth, n);
    const vacancyCost = includeReserves ? grossRent * config.vacancy : 0;
    const managementCost = includeReserves ? grossRent * (1 - config.vacancy) * config.management : 0;
    const water = config.bWaterMonthly * 12 * Math.pow(1 + config.expenseInflation, n);
    const electricity = config.bElectricMonthly * 12 * Math.pow(1 + config.expenseInflation, n);
    const insurance = config.bInsuranceAnnual * Math.pow(1 + config.expenseInflation, n);
    const maintenance = series.market * config.maintenanceB;
    const fee = config.bRentBoardFeeAnnual * Math.pow(1 + config.expenseInflation, n);
    const noi = grossRent - vacancyCost - managementCost - series.tax - water - electricity - insurance - maintenance - fee;
    return { year, market: series.market, assessed: series.assessed, propertyTax: series.tax, grossRent, vacancyCost, managementCost, water, electricity, insurance, maintenance, fee, noi };
  }
  function estateRow(year, config = BASE) {
    const a = seriesFor("A", year, config).market;
    const b = seriesFor("B", year, config).market;
    const exclusion = futureValue(config.estateExclusion, config.estateIndex, year - config.startYear);
    const combined = a + b;
    return { year, a, b, combined, exclusion, headroom: Math.max(0, exclusion - combined), excess: Math.max(0, combined - exclusion) };
  }
  function historyChecks(history) {
    return history.map((row, index) => {
      const previous = history[index + 1];
      const computedTaxChange = previous && previous.tax && row.tax ? row.tax / previous.tax - 1 : null;
      const computedAssessmentChange = previous && previous.assessed && row.assessed ? row.assessed / previous.assessed - 1 : null;
      return { ...row, computedTaxChange, computedAssessmentChange };
    });
  }

  window.MODEL = {
    BASE, historyA, historyB, round10, fmtMoney, fmtExact, fmtPct, futureValue,
    modelAllowance, seriesFor, inheritanceValues, annualA, afterTaxPortfolioReturn,
    decision, sfAnnual, estateRow, historyChecks
  };
})();
