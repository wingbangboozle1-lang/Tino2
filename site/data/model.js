/*
  Deterministic planning model, not an appraisal or tax return.
  Observed household inputs are separated from official law and derived projections.
  All displayed currency is rounded to the nearest $10 by fmtMoney().
*/
(function () {
  const A_RATE = 0.012; // hypothetical combined levy; actual parcel rate unverified
  const B_RATE = 0.0118162182; // carried-forward city ad valorem rate; direct charges excluded
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
    estateExclusion: 15000000,      // official, decedents dying in 2026 (IRS)
    estateExclusion2027: 15480000,  // official, decedents dying in 2027 (IRS IR-2026-133; Rev. Proc. 2026-35 sec. 3.44)
    estateIndex: 0.02               // assumption for 2028 onward only
  };

  // Private historical bill sequences are intentionally not distributed.
  const historyA = [];
  const historyB = [];

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
    return fmtMoney(value);
  }
  function fmtPct(value, digits = 1) {
    return (value * 100).toFixed(digits) + "%";
  }
  function futureValue(present, annualRate, years) {
    return present * Math.pow(1 + annualRate, years);
  }
  function prop19Steps(year) {
    // Adjustments take effect every second February 16: 2027, 2029, 2031, ...
    return Math.max(0, Math.floor((year - 2025) / 2));
  }
  function modelAllowance(year, config = BASE) {
    // BOE method, verified 2026-11-11 against Letters to Assessors 2023/012 and 2025/009:
    // every second February 16 the amount is multiplied by ONE calendar year's change in the FHFA
    // House Price Index for California (2023: x1.0226 for 2022; 2025: x1.0215 for 2024).
    // The other year's change is not applied, so the amount grows at about half the pace of home prices.
    // Future amounts are unknown; this scenario applies the model's home-price growth once per step.
    return config.prop19Amount * Math.pow(1 + config.appreciation, prop19Steps(year));
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
      // Conservative bound: also tax ALL portfolio growth above the invested principal at the capital-gain scenario rate
      // (the annual drag already taxes part of the return, so this deliberately double-counts to bracket the result).
      terminalAfterLiquidation: netImmediateSale * Math.pow(1 + portfolioReturn, horizon) - Math.max(0, netImmediateSale * (Math.pow(1 + portfolioReturn, horizon) - 1)) * config.capitalGainsTax,
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
    // 2026 and 2027 are official IRS amounts; later years index the 2027 amount by an assumed rate.
    const exclusion = year <= 2026 ? config.estateExclusion : futureValue(config.estateExclusion2027, config.estateIndex, year - 2027);
    const combined = a; // B is already owned by the heir, not the decedent.
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
    modelAllowance, prop19Steps, seriesFor, inheritanceValues, annualA, afterTaxPortfolioReturn,
    decision, sfAnnual, estateRow, historyChecks
  };
})();
