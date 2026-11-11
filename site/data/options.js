/* Options the three-way comparison leaves out (session 0d6ec51e, 11 Nov 2026).
   Every household input comes from MODEL.BASE; nothing is typed here except amounts published by a
   government body, each with its source key. An independently written calculation of the same figures
   is kept in the repository (verification/0d6ec51e/options.cjs) and compared by scripts/validate.js. */
(function () {
  const M = window.MODEL, B = M.BASE;
  const LAW = {
    recoveryYears: 27.5,          // irsPub527
    recaptureExtra: 0.05,         // irsTopic409: 25% maximum on depreciation gain instead of the 20% the model's rate contains
    estateTopRate: 0.40,          // irs706: Table A, over $1,000,000
    withholding: 1 / 30,          // ftb593: 3 1/3% of the sales price
    probateBands: [[100000, 0.04], [100000, 0.03], [800000, 0.02], [9000000, 0.01], [15000000, 0.005]] // prob10800, prob10810
  };
  const HORIZON = 10;
  const cfg = year => ({ ...B, inheritYear: year });
  const ret = M.afterTaxPortfolioReturn(B);
  const grow = (value, years) => value * Math.pow(1 + ret, years);

  // Hold the house for `years`, sell, invest the proceeds until the same endpoint as "sell at once".
  function holdThenSell(year, years, mode) {
    const sellNow = M.decision(cfg(year), HORIZON).sell.terminal;
    if (years === 0) return { terminal: sellNow, vsSellNow: 0, exclusionUsed: 0 };
    const config = mode === "empty" ? { ...cfg(year), aRent4BR: 0 } : cfg(year);
    const side = M.decision(config, years, "4BR")[mode === "live" ? "live" : "rent"];
    const terminal = grow(side.terminal, HORIZON - years);
    return { terminal, vsSellNow: terminal - sellNow, exclusionUsed: side.gainExclusion || 0 };
  }

  // Rental case with the depreciation deduction, its tax at sale, and losses carried to the sale.
  function rentWithDepreciation(year, buildingShare) {
    const d = M.decision(cfg(year), HORIZON), rent = d.rent;
    const deduction = d.transfer.market * buildingShare / LAW.recoveryYears;
    let reserve = 0, carried = 0, saved = 0;
    rent.yearly.forEach(row => {
      const taxable = row.noi - deduction;
      const tax = taxable > 0 ? taxable * B.ordinaryTax : 0;
      if (taxable < 0) carried -= taxable;
      saved += row.incomeTax - tax;
      reserve = reserve * (1 + ret) + row.noi - tax;
    });
    const extraTaxAtSale = deduction * HORIZON * (B.capitalGainsTax + LAW.recaptureExtra);
    const released = carried * B.ordinaryTax;
    const terminal = rent.finalSale - extraTaxAtSale + released + reserve;
    return { deduction, saved, carried, extraTaxAtSale, released, terminal, published: rent.terminal, change: terminal - rent.terminal, sellLead: d.sell.terminal - terminal };
  }

  // The pre-2021 rule: a child keeps the parent's assessed value whatever the use of the house.
  function oldRule(year) {
    const d = M.decision(cfg(year), HORIZON);
    const run = side => {
      let reserve = 0;
      side.yearly.forEach((row, index) => {
        const kept = d.transfer.carryForwardAssessed * Math.pow(1 + B.assessmentGrowth, index + 1) * B.aRate;
        const noi = row.noi + row.propertyTax - kept;
        const tax = side === d.rent && noi > 0 ? noi * B.ordinaryTax : 0;
        reserve = reserve * (1 + ret) + noi - tax;
      });
      return side.finalSale + reserve;
    };
    const rent = run(d.rent), live = run(d.live);
    return { sell: d.sell.terminal, sellTaxedAtEnd: d.sell.terminalAfterLiquidation, rentNow: d.rent.terminal, rent, liveNow: d.live.terminal, live,
      firstTaxNow: d.rent.yearly[0].propertyTax, firstTaxOld: d.transfer.carryForwardAssessed * (1 + B.assessmentGrowth) * B.aRate,
      sellLeadNow: d.sell.terminal - d.rent.terminal, sellLead: d.sell.terminal - rent, sellLeadEqualTerms: d.sell.terminalAfterLiquidation - rent };
  }

  // Federal estate tax when the estate holds Property A plus an amount of money.
  function estate(year, money) {
    const row = M.estateRow(year, B);
    const over = Math.max(0, row.a + money - row.exclusion);
    return { year, propertyA: row.a, exclusion: row.exclusion, startsAt: Math.max(0, row.exclusion - row.a), money, over, tax: over * LAW.estateTopRate, official: year <= 2027 };
  }

  // Statutory compensation in a probate (applies only if the house is not held by the trustee).
  function probate(value) {
    let left = value, fee = 0;
    LAW.probateBands.forEach(([band, rate]) => { const part = Math.max(0, Math.min(left, band)); fee += part * rate; left -= part; });
    return fee;
  }

  // Property B: yearly property tax avoided while its assessed value is kept.
  function propertyB(year) {
    const s = M.seriesFor("B", year, B);
    return { year, market: s.market, assessed: s.assessed, tax: s.tax, taxAtMarket: s.market * s.rate, avoided: (s.market - s.assessed) * s.rate };
  }

  const withholdingAtSale = year => M.inheritanceValues(year, cfg(year)).market * LAW.withholding;

  window.OPTIONS = { LAW, HORIZON, holdThenSell, rentWithDepreciation, oldRule, estate, probate, propertyB, withholdingAtSale };
})();
