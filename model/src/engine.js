/*
 * Projection and decision engine — session 5a1bd5be.
 *
 * Pure functions, no dependencies, no I/O. The same file runs in Node (build + tests)
 * and in the browser (interactive calculator), so the published tables and the
 * calculator cannot drift apart.
 *
 * Money is carried unrounded inside the engine. Rounding to the nearest $10
 * (project rule) happens only when a figure is displayed: see round10().
 *
 * No personal identifiers appear in this file. Property A = the house expected to be
 * inherited (Cupertino). Property B = the heir household's present home (San Francisco).
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.Engine = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  var BASE_YEAR = 2026;      // all "2026 dollars" inputs are stated for this year
  var LAST_YEAR = 2050;      // end of the projection window asked for in the brief

  function pow(g, n) { return Math.pow(1 + g, n); }

  /** Round to the nearest $10 for display (project rule). Half rounds away from zero. */
  function round10(x) {
    if (!isFinite(x)) return x;
    var s = x < 0 ? -1 : 1;
    return s * Math.round(Math.abs(x) / 10) * 10 + 0; // "+ 0" turns -0 into 0
  }

  // ---------------------------------------------------------------- property tax
  /** Market value of a property in calendar year `year`. */
  function marketValue(value2026, growth, year) {
    return value2026 * pow(growth, year - BASE_YEAR);
  }

  /**
   * Taxable (assessed) value while ownership does not change:
   * the Proposition 13 factored base year value, compounded by `factor` (max 2%).
   */
  function factoredBaseYearValue(av, avYear, factor, year) {
    return av * pow(factor, year - avYear);
  }

  /**
   * Charges on the bill that do not depend on assessed value (parcel taxes, direct
   * charges). Derived, not read from a bill: bill - rate x assessed value.
   */
  function fixedCharges(bill, rate, av) { return bill - rate * av; }

  /** Annual bill = ad valorem rate x taxable value + fixed charges. */
  function propertyTax(taxableValue, rate, fixed) { return taxableValue * rate + fixed; }

  /**
   * Proposition 19 "$1 million" amount in force for a transfer in `year`
   * (after 16 February of that year). The Board of Equalization adjusts it on
   * 16 February of every odd year by ONE year's change in the FHFA California
   * house price index. $1,044,586 applies from 16 Feb 2025 to 15 Feb 2027.
   */
  function prop19Adjustments(year) {
    return year >= 2027 ? Math.floor((year - 2027) / 2) + 1 : 0;
  }
  function prop19Amount(year, amount2025, caHpiChange) {
    return amount2025 * pow(caHpiChange, prop19Adjustments(year));
  }

  /**
   * New taxable value when a child inherits the parent's principal residence and
   * makes it the child's own principal residence within one year (BOE formula):
   *   excluded amount = factored base year value + adjusted $1M amount
   *   if market value <= excluded amount: taxable value stays the factored base year value
   *   else: taxable value = factored base year value + (market value - excluded amount)
   */
  function prop19TaxableValue(fbyv, fmv, amount) {
    var excluded = fbyv + amount;
    var excess = Math.max(0, fmv - excluded);
    return { excluded: excluded, excess: excess, taxable: fbyv + excess };
  }

  // ---------------------------------------------------------------- federal estate tax
  /** Basic exclusion amount projected from the published 2026 and 2027 figures. */
  function estateExclusion(year, p) {
    if (year <= 2026) return p.estateExclusion2026;
    return p.estateExclusion2027 * pow(p.estateIndexing, year - 2027);
  }

  /**
   * Simplified federal estate tax: 40% of the part of the taxable estate above the
   * exclusion. Ignores deductions, lifetime gifts and the lower brackets that the
   * unified credit absorbs. `spouses` = 2 models a full portability election.
   */
  function estateTax(taxableEstate, exclusion, rate, spouses) {
    var shelter = exclusion * (spouses === 2 ? 2 : 1);
    return { shelter: shelter, over: Math.max(0, taxableEstate - shelter), tax: rate * Math.max(0, taxableEstate - shelter) };
  }

  // ---------------------------------------------------------------- yearly series before inheritance
  function yearlySeries(p) {
    var rows = [];
    var fixedA0 = fixedCharges(p.aBill2025, p.aRate, p.aAv2025);
    var fixedB0 = fixedCharges(p.bBill2025, p.bRate, p.bAv2025);
    for (var y = BASE_YEAR; y <= LAST_YEAR; y++) {
      var infl2025 = pow(p.inflation, y - 2025);
      var aFmv = marketValue(p.aValue2026, p.aGrowth, y);
      var aAv = factoredBaseYearValue(p.aAv2026, 2026, p.prop13Factor, y);
      var aFixed = fixedA0 * infl2025;
      var amount = prop19Amount(y, p.prop19Amount2025, p.caHpiChange);
      var p19 = prop19TaxableValue(aAv, aFmv, amount);
      var bFmv = marketValue(p.bValue2026, p.bGrowth, y);
      var bAv = factoredBaseYearValue(p.bAv2025, 2025, p.prop13Factor, y);
      var bFixed = fixedB0 * infl2025;
      var excl = estateExclusion(y, p);
      rows.push({
        year: y,
        aValue: aFmv, aAssessed: aAv, aFixed: aFixed,
        aTaxOwner: propertyTax(aAv, p.aRate, aFixed),
        prop19Amount: amount, prop19Adjustments: prop19Adjustments(y),
        aLiveTaxable: p19.taxable, aLiveTax: propertyTax(p19.taxable, p.aRate, aFixed),
        aFullTax: propertyTax(aFmv, p.aRate, aFixed),
        bValue: bFmv, bAssessed: bAv, bFixed: bFixed,
        bTaxOwner: propertyTax(bAv, p.bRate, bFixed),
        estateExclusion: excl, estateHeadroom: excl - aFmv
      });
    }
    return rows;
  }

  // ---------------------------------------------------------------- investment account helper
  /**
   * Every strategy's yearly net cash is paid into (or drawn from) one investment
   * account earning `r`. Cash arrives at the end of each year; `opening` is invested
   * at the start of the first year. A negative balance means money taken out of the
   * household's other investments, so the cost of carrying a house includes the
   * growth that money would have earned.
   */
  function runAccount(opening, flows, r) {
    var bal = opening, contrib = opening, path = [];
    for (var k = 0; k < flows.length; k++) {
      bal = bal * (1 + r) + flows[k];
      contrib += flows[k];
      path.push(bal);
    }
    return { balance: bal, contributed: contrib, path: path };
  }
  /** Balance after tax on the growth, at one flat rate; symmetric for negative balances. */
  function accountAfterTax(acct, taxRate) {
    return acct.contributed + (acct.balance - acct.contributed) * (1 - taxRate);
  }

  // ---------------------------------------------------------------- the three strategies
  /**
   * Simulate SELL, LIVE and RENT for Property A.
   * T = year of inheritance (death treated as 1 January of T), H = years followed.
   * Everything about Property B that is the same in all three strategies is left out,
   * because it cancels in the comparison. The one thing that differs is included:
   * if the heir household moves into A, the unit it leaves in B can be rented.
   */
  function simulate(p) {
    var T = p.inheritYear, H = p.horizon;
    var fixedA0 = fixedCharges(p.aBill2025, p.aRate, p.aAv2025);
    var valueT = marketValue(p.aValue2026, p.aGrowth, T);
    var valueEnd = marketValue(p.aValue2026, p.aGrowth, T + H);
    var fbyvT = factoredBaseYearValue(p.aAv2026, 2026, p.prop13Factor, T);
    var amountT = prop19Amount(T, p.prop19Amount2025, p.caHpiChange);
    var p19 = prop19TaxableValue(fbyvT, valueT, amountT);
    var deflator = pow(p.inflation, T + H - BASE_YEAR);

    // ---- SELL: sell at the date-of-death value, invest the net proceeds
    var sellCosts = valueT * p.sellCost;
    var sellNet = valueT - sellCosts;
    var sellGain = sellNet - valueT;               // basis = value at death, so this is <= 0
    var sellTax = Math.max(0, sellGain) * p.taxGain; // 0; a loss is not credited (conservative)
    var sellAcct = runAccount(sellNet - sellTax, zeros(H), p.investReturn);
    var sell = {
      name: 'SELL', years: [],
      proceeds: sellNet - sellTax, saleCosts: sellCosts, saleTax: sellTax,
      account: sellAcct,
      wealthHold: sellAcct.balance,
      wealthLiquid: accountAfterTax(sellAcct, p.taxGain),
      firstYearCash: 0,
      firstYearReturn: (sellNet - sellTax) * p.investReturn
    };
    for (var k0 = 0; k0 < H; k0++) sell.years.push({ year: T + k0, cash: 0, balance: sellAcct.path[k0] });

    // ---- LIVE: move in within one year, claim the Proposition 19 exclusion
    var live = { name: 'LIVE', years: [], taxableValue0: p19.taxable, excluded: p19.excluded, excess: p19.excess };
    var liveFlows = [];
    var unitRentT = p.bUnitRent2026 * 12 * pow(p.inflation, T - BASE_YEAR);
    for (var k = 0; k < H; k++) {
      var y = T + k, infl = pow(p.inflation, y - BASE_YEAR);
      var tv = p19.taxable * pow(p.prop13Factor, k);
      var tax = propertyTax(tv, p.aRate, fixedA0 * pow(p.inflation, y - 2025));
      var ins = p.aInsurance * infl, maint = p.aMaintenance * infl, util = p.aUtilities * infl;
      var unitGross = unitRentT * pow(p.inflation * p.rentCapShare, k) * (1 - p.vacancy);
      var unitNet = unitGross * (1 - p.taxOrdinary);
      var cash = -(tax + ins + maint + util) + unitNet;
      liveFlows.push(cash);
      live.years.push({ year: y, taxableValue: tv, propertyTax: tax, insurance: ins, maintenance: maint,
        utilities: util, unitRent: unitGross, unitRentTax: unitGross - unitNet, cash: cash });
    }
    var liveAcct = runAccount(0, liveFlows, p.investReturn);
    for (var k1 = 0; k1 < H; k1++) live.years[k1].balance = liveAcct.path[k1];
    var liveSaleNet = valueEnd * (1 - p.sellCost);
    var liveGain = liveSaleNet - valueT;
    var liveSaleTax = Math.max(0, liveGain - p.homeSaleExclusion) * p.taxGain;
    live.account = liveAcct;
    live.houseValueEnd = valueEnd;
    live.saleNet = liveSaleNet; live.saleTax = liveSaleTax;
    live.wealthHold = liveAcct.balance + valueEnd;
    live.wealthLiquid = accountAfterTax(liveAcct, p.taxGain) + liveSaleNet - liveSaleTax;
    live.firstYearCash = liveFlows[0];

    // ---- RENT: keep A as a rental; no exclusion, reassessed to market value
    var rent = { name: 'RENT', years: [], taxableValue0: valueT };
    var rentFlows = [], carry = 0, dep = p.aBuildingShare * valueT / p.depreciationYears, accDep = 0;
    for (var k2 = 0; k2 < H; k2++) {
      var y2 = T + k2, infl2 = pow(p.inflation, y2 - BASE_YEAR);
      var tv2 = valueT * pow(p.prop13Factor, k2);
      var tax2 = propertyTax(tv2, p.aRate, fixedA0 * pow(p.inflation, y2 - 2025));
      var gross = p.aRent2026 * 12 * infl2 * (1 - p.vacancy);
      var ins2 = p.aInsurance * p.landlordInsuranceFactor * infl2, maint2 = p.aMaintenance * infl2;
      var mgmt = gross * p.managementFee;
      var noi = gross - tax2 - ins2 - maint2 - mgmt;
      var taxable = noi - dep, incomeTax = 0;
      if (taxable < 0) { carry += -taxable; }
      else { var used = Math.min(carry, taxable); carry -= used; incomeTax = (taxable - used) * p.taxOrdinary; }
      accDep += dep;
      var cash2 = noi - incomeTax;
      rentFlows.push(cash2);
      rent.years.push({ year: y2, taxableValue: tv2, propertyTax: tax2, grossRent: gross, insurance: ins2,
        maintenance: maint2, management: mgmt, noi: noi, depreciation: dep, taxableIncome: taxable,
        incomeTax: incomeTax, suspendedLoss: carry, cash: cash2 });
    }
    var rentAcct = runAccount(0, rentFlows, p.investReturn);
    for (var k3 = 0; k3 < H; k3++) rent.years[k3].balance = rentAcct.path[k3];
    var rentSaleNet = valueEnd * (1 - p.sellCost);
    var rentGain = rentSaleNet - (valueT - accDep);
    var rentTaxableGain = Math.max(0, rentGain - carry);
    var recapture = Math.min(accDep, rentTaxableGain);
    var rentSaleTax = recapture * p.taxRecapture + (rentTaxableGain - recapture) * p.taxGain;
    rent.account = rentAcct;
    rent.houseValueEnd = valueEnd;
    rent.depreciationPerYear = dep; rent.accumulatedDepreciation = accDep; rent.suspendedLossEnd = carry;
    rent.saleNet = rentSaleNet; rent.saleTax = rentSaleTax;
    rent.wealthHold = rentAcct.balance + valueEnd;
    rent.wealthLiquid = accountAfterTax(rentAcct, p.taxGain) + rentSaleNet - rentSaleTax;
    rent.firstYearCash = rentFlows[0];

    // ---- estate tax at T (same in all three strategies)
    var excl = estateExclusion(T, p);
    var estate = estateTax(valueT + p.otherEstateAssets, excl, p.estateRate, p.spouses);

    var list = [sell, live, rent];
    var best = list.slice().sort(function (a, b) { return b.wealthLiquid - a.wealthLiquid; })[0];
    return {
      inputs: p, inheritYear: T, horizon: H, endYear: T + H,
      valueAtDeath: valueT, valueEnd: valueEnd, fbyvAtDeath: fbyvT, prop19Amount: amountT,
      prop19: p19, deflator: deflator,
      sell: sell, live: live, rent: rent, best: best.name,
      costOfLiving: sell.wealthLiquid - live.wealthLiquid,
      costOfRenting: sell.wealthLiquid - rent.wealthLiquid,
      costOfLivingPerYear: levelPayment(sell.wealthLiquid - live.wealthLiquid, p.investReturn, H),
      estate: { exclusion: excl, taxableEstate: valueT + p.otherEstateAssets, shelter: estate.shelter,
        over: estate.over, tax: estate.tax, headroom: estate.shelter - valueT }
    };
  }

  // ---------------- Property B: keep or sell (today's figures)
  function mid(range) { return (range[0] + range[1]) / 2; }
  /**
   * Property B as it stands in 2026. `b` holds the brief's monthly figures.
   * The tax on a sale cannot be computed: purchase price, improvements and depreciation
   * already claimed are unknown. Two bounds are returned instead: no tax at all, and tax
   * on everything above the assessed value (a floor for the basis only if the building
   * was bought, never inherited, and never improved).
   */
  function propertyB(p, b) {
    var rent = b.bRentTwoUnits * 12;
    var costs = { propertyTax: p.bBill2025, insurance: b.bInsurance, water: mid(b.bWaterMonthly) * 12,
      power: mid(b.bPowerMonthly) * 12, maintenance: p.bMaintenance };
    var totalCosts = costs.propertyTax + costs.insurance + costs.water + costs.power + costs.maintenance;
    var net = rent - totalCosts;
    var housing = p.bHousingRent * 12;
    var growth = p.bValue2026 * p.bGrowth;
    var saleNet = p.bValue2026 * (1 - p.sellCost);
    var taxMax = Math.max(0, saleNet - p.bAv2025) * p.taxGain;
    var fixed = fixedCharges(p.bBill2025, p.bRate, p.bAv2025);
    function need(proceeds) { return { proceeds: proceeds, toReplaceRent: net / proceeds,
      toReplaceRentAndHome: (net + housing) / proceeds, toMatchEverything: (net + housing + growth) / proceeds }; }
    return { rent: rent, costs: costs, totalCosts: totalCosts, net: net, netYield: net / p.bValue2026,
      housing: housing, growth: growth, saleNet: saleNet, saleCosts: p.bValue2026 * p.sellCost,
      taxMax: taxMax, noTax: need(saleNet), maxTax: need(saleNet - taxMax),
      taxIfReassessed: propertyTax(p.bValue2026, p.bRate, fixed), fixed: fixed };
  }

  function zeros(n) { var a = []; for (var i = 0; i < n; i++) a.push(0); return a; }

  /** Equal end-of-year payment that grows to `future` after n years at rate r. */
  function levelPayment(future, r, n) {
    if (n <= 0) return 0;
    if (Math.abs(r) < 1e-12) return future / n;
    return future * r / (Math.pow(1 + r, n) - 1);
  }

  function clone(p, over) {
    var q = {}, k;
    for (k in p) if (Object.prototype.hasOwnProperty.call(p, k)) q[k] = p[k];
    for (k in over) if (Object.prototype.hasOwnProperty.call(over, k)) q[k] = over[k];
    return q;
  }

  /** Solve f(x) = 0 on [lo, hi] by bisection; null if the sign does not change. */
  function bisect(f, lo, hi) {
    var flo = f(lo), fhi = f(hi);
    if (!isFinite(flo) || !isFinite(fhi) || flo * fhi > 0) return null;
    for (var i = 0; i < 200; i++) {
      var mid = (lo + hi) / 2, fm = f(mid);
      if (flo * fm <= 0) { hi = mid; fhi = fm; } else { lo = mid; flo = fm; }
    }
    return (lo + hi) / 2;
  }

  /** Monthly rent for A (2026 dollars) at which RENT ends level with SELL. */
  function breakEvenRent(p) {
    return bisect(function (x) {
      var s = simulate(clone(p, { aRent2026: x }));
      return s.rent.wealthLiquid - s.sell.wealthLiquid;
    }, 0, 200000);
  }

  /** Investment return at which SELL ends level with `other` ('live' or 'rent'). */
  function breakEvenReturn(p, other) {
    return bisect(function (x) {
      var s = simulate(clone(p, { investReturn: x }));
      return s.sell.wealthLiquid - s[other].wealthLiquid;
    }, 0, 0.30);
  }

  /** Apply a named house-price scenario and a named return scenario to the inputs. */
  function withScenario(p, scenarios, house, ret) {
    var h = scenarios.house[house], r = scenarios.returns[ret];
    return clone(p, { aGrowth: h.aGrowth, bGrowth: h.bGrowth, caHpiChange: h.caHpiChange, investReturn: r.investReturn });
  }

  /** 3 x 3 table: house-price scenario by investment-return scenario. */
  function grid(p, scenarios) {
    var out = [];
    Object.keys(scenarios.house).forEach(function (h) {
      Object.keys(scenarios.returns).forEach(function (r) {
        var s = simulate(withScenario(p, scenarios, h, r));
        out.push({ house: h, returns: r, sell: s.sell.wealthLiquid, live: s.live.wealthLiquid,
          rent: s.rent.wealthLiquid, best: s.best, costOfLiving: s.costOfLiving, costOfRenting: s.costOfRenting });
      });
    });
    return out;
  }

  return {
    BASE_YEAR: BASE_YEAR, LAST_YEAR: LAST_YEAR,
    round10: round10, marketValue: marketValue, factoredBaseYearValue: factoredBaseYearValue,
    fixedCharges: fixedCharges, propertyTax: propertyTax,
    prop19Adjustments: prop19Adjustments, prop19Amount: prop19Amount, prop19TaxableValue: prop19TaxableValue,
    estateExclusion: estateExclusion, estateTax: estateTax,
    yearlySeries: yearlySeries, runAccount: runAccount, accountAfterTax: accountAfterTax,
    simulate: simulate, levelPayment: levelPayment, clone: clone, bisect: bisect,
    breakEvenRent: breakEvenRent, breakEvenReturn: breakEvenReturn, propertyB: propertyB,
    withScenario: withScenario, grid: grid
  };
});
