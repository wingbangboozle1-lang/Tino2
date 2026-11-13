/* Decision-boundary analysis on top of the invented teaching model.
   The point of this module is NOT to produce a bigger number. It is to find the
   conditions under which the ranking between strategies flips, so a reader can see
   which unknown facts actually matter. No household data is used. */
(function () {
  'use strict';
  const M = window.MODEL;

  /* Growth and return values the comparison page exposes, plus the observed
     inflation evidence, so a reader can see where the real conditions sit. */
  const GROWTH = Object.freeze([0, 0.01, 0.02, 0.03, 0.035, 0.04, 0.05, 0.06, 0.07]);
  const RETURNS = Object.freeze([0, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.10]);
  const LABELS = Object.freeze({ sell: 'Sell', rent: 'Rent', live: 'Live' });

  function config(growth, ret, year) {
    return Object.assign({}, M.BASE, {
      inheritYear: year || 2045,
      appreciation: growth,
      portfolioNet: ret
    });
  }
  function evaluate(growth, ret, horizon, year) {
    return M.decision(config(growth, ret, year), horizon);
  }

  /* Full grid: which strategy leads for each growth/return pair. */
  function grid(horizon, year) {
    return GROWTH.map(g => ({
      growth: g,
      cells: RETURNS.map(r => {
        const d = evaluate(g, r, horizon, year);
        return { ret: r, winner: d.winner, sell: d.sell.terminal, rent: d.rent.terminal, live: d.live.terminal };
      })
    }));
  }

  /* The portfolio return at which "sell and reinvest" STARTS winning, for a given
     home-growth rate. Searched at 0.1 percentage point resolution over 0-20%.
     Returns null when sell already wins at a zero return (no threshold below 20%),
     and null when sell never wins in the range. */
  function sellBreakeven(growth, horizon, year) {
    let first = null, everSell = false, winsAtZero = null;
    for (let r = 0; r <= 0.2001; r += 0.001) {
      const w = evaluate(growth, r, horizon, year).winner;
      if (r === 0) winsAtZero = w === 'sell';
      if (w === 'sell') {
        everSell = true;
        if (first === null) first = r;
      }
    }
    if (!everSell) return { threshold: null, note: 'sell never leads in the tested range' };
    if (winsAtZero) return { threshold: 0, note: 'sell leads even at a zero portfolio return' };
    return { threshold: first, note: 'sell leads at or above this return' };
  }

  /* Which single assumption, moved across its range, changes the leading strategy. */
  function sensitivity(horizon, year) {
    const base = { growth: 0.035, ret: 0.05 };
    const baseWinner = evaluate(base.growth, base.ret, horizon, year).winner;
    const rows = [];
    for (const g of GROWTH) {
      const w = evaluate(g, base.ret, horizon, year).winner;
      rows.push({ axis: 'Home-price growth', value: g, winner: w, flips: w !== baseWinner });
    }
    for (const r of RETURNS) {
      const w = evaluate(base.growth, r, horizon, year).winner;
      rows.push({ axis: 'Portfolio return', value: r, winner: w, flips: w !== baseWinner });
    }
    return { baseWinner, rows };
  }

  /* Contribution of each year to the holding strategies, so a reader can see whether
     the result depends on a handful of early years (sequence risk). */
  function yearlyContribution(horizon, year) {
    const d = evaluate(0.035, 0.05, horizon, year);
    const out = { transferYear: year, horizon, rent: [], live: [] };
    for (const option of ['rent', 'live']) {
      let acc = 0;
      for (const row of d[option].yearly) {
        acc = acc * 1.05 + row.afterTaxCash;
        out[option].push({ year: row.year, afterTaxCash: row.afterTaxCash, running: acc });
      }
    }
    return out;
  }

  /* --- The most decision-relevant test in the whole model ---

     Under full reassessment, the rented property pays property tax on market value
     rather than on the protected base. That single line can exceed the rent. This
     function finds, for each year after transfer, the gross monthly rent that would
     be needed for the rental to break even BEFORE financing and income tax, and
     compares it with the rent the invented example assumes.

     It divides by assumed rent growth to express the answer in today's money, which
     is the number a reader can compare with an actual rent roll. */
  function rentBreakeven(growth, year, yearsAfter) {
    const c = config(growth, 0.05, year);
    const d = M.decision(c, Math.max(1, yearsAfter));
    const rows = [];
    for (const row of d.rent.yearly) {
      const fixedCosts = row.propertyTax + row.water + row.insurance + row.maintenance;
      const keepPerGrossDollar = (1 - c.vacancy) * (1 - c.management);
      const grossNeeded = fixedCosts / keepPerGrossDollar;
      const actualGross = row.grossRent;
      rows.push({
        year: row.year,
        propertyTax: row.propertyTax,
        otherCosts: row.water + row.insurance + row.maintenance,
        fixedCosts,
        grossNeededAnnual: grossNeeded,
        grossNeededMonthly: grossNeeded / 12,
        grossNeededMonthlyToday: (grossNeeded / 12) / Math.pow(1 + c.rentGrowth, yearsAfter),
        assumedMonthly: actualGross / 12,
        assumedMonthlyToday: (actualGross / 12) / Math.pow(1 + c.rentGrowth, yearsAfter),
        shortfallRatio: grossNeeded / actualGross,
        noi: row.noi
      });
    }
    return {
      config: c,
      rows,
      firstYear: rows[0],
      assessment: d.transfer
    };
  }

  /* Where the annual operating cost of each holding strategy actually goes.
     This is the table that explains the result above. */
  function costStructure(growth, year, yearsAfter) {
    const c = config(growth, 0.05, year);
    const d = M.decision(c, Math.max(1, yearsAfter));
    const out = {};
    for (const option of ['rent', 'live']) {
      const row = d[option].yearly[yearsAfter - 1];
      const total = row.propertyTax + row.water + row.insurance + row.maintenance;
      out[option] = {
        year: row.year,
        propertyTax: row.propertyTax,
        water: row.water,
        insurance: row.insurance,
        maintenance: row.maintenance,
        total,
        assessed: row.assessed,
        market: row.market,
        propertyTaxShare: row.propertyTax / total,
        maintenanceShare: row.maintenance / total
      };
    }
    return out;
  }

  window.BREAKEVEN = {
    GROWTH, RETURNS, LABELS,
    evaluate, grid, sellBreakeven, sensitivity, yearlyContribution,
    rentBreakeven, costStructure
  };
})();
