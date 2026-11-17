/* Depreciation, recapture and the home-sale exclusion — a separate teaching engine.
   Synthetic example inputs only. No household record, value, rent, bill or parcel
   figure is used by this file. It reuses the public comparison model's synthetic
   property example so the two pages describe the same fictional house, and adds
   only the rental-tax arithmetic the comparison model deliberately omits.
   Rules are quoted from official IRS publications; each is linked on the page. */
(function () {
  var M = window.MODEL;
  var RECOVERY_YEARS = 27.5;          // Pub. 527, GDS recovery period for residential rental property
  var UNRECAPTURED_RATE = 0.25;       // IRS Topic 409: maximum 25% rate on unrecaptured section 1250 gain
  var EXCLUSION = { single: 250000, joint: 500000 };  // Pub. 523: $250,000 / $500,000 married filing jointly
  var TRANSFER_YEAR = 2045;
  // Mid-month convention (Pub. 527): property placed in service in the first month of
  // a year and disposed of in the last month of a year is treated as in service for
  // 11.5 months of each of those two years. Full years in between take a full year.
  var MID_MONTH_FRACTION = 11.5 / 12;

  var PATTERNS = [
    { key: 'rent_all', label: 'Rent it out the whole time, then sell',
      blurb: 'Never a main home. No home-sale exclusion; depreciation taken every year.' },
    { key: 'live_all', label: 'Live in it the whole time, then sell',
      blurb: 'A main home throughout. No depreciation; the exclusion applies to the gain.' },
    { key: 'live_then_rent', label: 'Live in it two years, rent it, then sell',
      blurb: 'Rental use comes after the last qualified use, so it is not nonqualified use — but the exclusion can still fail the residence test.' },
    { key: 'rent_then_live', label: 'Rent it out, move in for the last two years, then sell',
      blurb: 'Eligible for the exclusion, but the earlier rental years are nonqualified use and part of the gain is carved out.' }
  ];
  var YEARS = [5, 10, 20, 30];
  var SHARES = [0.70, 0.80, 0.90];
  var FILINGS = [{ key: 'single', limit: EXCLUSION.single, label: 'Single · $250,000' },
                 { key: 'joint', limit: EXCLUSION.joint, label: 'Married filing jointly · $500,000' }];
  var CG_RATES = [0.15, 0.20];
  var IMPUTED_RENTS = [0, 2500, 5000, 7500];
  var RESIDENCE_YEARS_MIXED = 2;   // the mixed patterns use two years of occupancy

  function occupancy(pattern, years) {
    var out = [];
    for (var y = 1; y <= years; y++) {
      if (pattern === 'rent_all') out.push('rent');
      else if (pattern === 'live_all') out.push('live');
      else if (pattern === 'live_then_rent') out.push(y <= RESIDENCE_YEARS_MIXED ? 'live' : 'rent');
      else out.push(y <= years - RESIDENCE_YEARS_MIXED ? 'rent' : 'live');
    }
    return out;
  }

  /* Straight-line MACRS over 27.5 years with the mid-month convention.
     Pub. 527: a mid-month convention is used for all residential rental property, and
     in the first year you can claim depreciation only for the number of months the
     property is in use. Where the property is placed in service and disposed of in the
     same year it is excepted property and no depreciation is allowed. */
  function depreciationSchedule(buildingBasis, rentalYears) {
    var annual = buildingBasis / RECOVERY_YEARS;
    var rows = [], total = 0;
    if (rentalYears >= 2) {
      for (var i = 1; i <= rentalYears; i++) {
        var fraction = (i === 1 || i === rentalYears) ? MID_MONTH_FRACTION : 1;
        var amount = annual * fraction;
        total += amount;
        rows.push({ year: i, fraction: fraction, amount: amount, cumulative: total });
      }
    }
    return { rows: rows, total: total, annual: annual,
             excepted: rentalYears < 2,
             note: rentalYears < 2
               ? 'Placed in service and disposed of in the same year, so the property is excepted from MACRS in this example.'
               : 'Year 1 and the disposal year each take ' + (MID_MONTH_FRACTION * 12).toFixed(1) + ' months of a full year under the mid-month convention.' };
  }

  function patternFacts(pattern, years) {
    var modes = occupancy(pattern, years);
    var rentalYears = modes.filter(function (m) { return m === 'rent'; }).length;
    var residenceYears = years - rentalYears;
    // Section 121 residence test: lived in the home for at least 24 months of the 5 years
    // ending on the date of sale. Occupancy outside that window does not count.
    var residenceInWindow = 0;
    for (var i = 0; i < modes.length; i++) {
      if (modes[i] === 'live' && (i + 1) > years - 5) residenceInWindow++;
    }
    var eligible = residenceInWindow >= 2 && years >= 2;
    // Section 121(b)(5): nonqualified use is a period after 2008 when the owner did not use
    // the property as a main home, ignoring any part of the 5-year window after the last
    // qualified use. Rental before the last qualified use counts; rental after it does not.
    var nonuseYears = 0;
    if (pattern === 'rent_then_live') nonuseYears = rentalYears;
    var nonuseFactor = eligible && nonuseYears > 0 ? nonuseYears / years : 0;
    return { modes: modes, rentalYears: rentalYears, residenceYears: residenceYears,
             residenceInWindow: residenceInWindow, eligible121: eligible,
             nonuseYears: nonuseYears, nonuseFactor: nonuseFactor };
  }

  function marketValue(year, config) {
    var n = year - config.startYear;
    return config.aValue * Math.pow(1 + config.appreciation, n);
  }

  /* The arithmetic of Worksheet 3 in Pub. 523, kept as one function so the page can run
     the two worked examples the IRS publishes and the synthetic scenarios with the same
     code. Nonqualified-use years are the post-2008 years of non-residence that fall
     before the last qualified use; days are counted here as whole years. */
  function worksheet3(input) {
    var adjustedBasis = input.basis - input.depreciation;
    var gain = input.salePrice - adjustedBasis;                       // Worksheet 2, line 7
    var unrecaptured = Math.max(0, Math.min(input.depreciation, gain)); // Section A, step 2
    var netGain = Math.max(0, gain - unrecaptured);                    // Section A, step 3
    var factor = input.ownedYears > 0 ? input.nonuseYears / input.ownedYears : 0; // Section B, step 4
    var nonqualified = netGain * factor;                               // Section B, step 5
    var eligible = Math.max(0, netGain - nonqualified);                // Section C
    var exclusion = Math.min(eligible, input.exclusionLimit);          // Section D
    return { adjustedBasis: adjustedBasis, gain: gain, unrecaptured: unrecaptured,
             netGain: netGain, factor: factor, nonqualified: nonqualified,
             eligible: eligible, exclusion: exclusion,
             taxable: Math.max(0, eligible - exclusion) };
  }

  /* One path: the same fictional house, held under one occupancy pattern, then sold. */
  function evaluate(options) {
    var o = options || {};
    var config = Object.assign({}, M.BASE, { inheritYear: o.transferYear || TRANSFER_YEAR });
    var transferYear = config.inheritYear;
    var years = o.years || 10;
    var share = o.share === undefined ? 0.8 : o.share;
    var filing = o.filing || 'single';
    var cgRate = o.cgRate === undefined ? 0.20 : o.cgRate;
    var pattern = o.pattern || 'rent_all';

    var facts = patternFacts(pattern, years);
    var saleYear = transferYear + years;
    var basis = marketValue(transferYear, config);          // assumed date-of-death value basis
    var buildingBasis = basis * share;
    var landBasis = basis - buildingBasis;
    var saleValue = marketValue(saleYear, config);
    var netProceeds = saleValue * (1 - config.saleCost);

    var dep = depreciationSchedule(buildingBasis, facts.rentalYears);
    var accumulated = dep.total;
    var adjustedBasis = basis - accumulated;
    var exclusionLimit = facts.eligible121 ? EXCLUSION[filing] : 0;
    var ws = worksheet3({
      basis: basis, depreciation: accumulated, salePrice: netProceeds,
      ownedYears: years, nonuseYears: facts.nonuseYears, exclusionLimit: exclusionLimit
    });
    var totalGain = ws.gain;
    var unrecaptured = ws.unrecaptured;
    var remainder = ws.netGain;
    var nonqualifiedGain = ws.nonqualified;
    var exclusionUsed = ws.exclusion;
    var taxableCapital = ws.taxable;
    var taxUnrecaptured = unrecaptured * UNRECAPTURED_RATE;
    var taxCapital = taxableCapital * cgRate;
    var afterTaxProceeds = netProceeds - taxUnrecaptured - taxCapital;

    var annualRows = [], cumulativeCash = 0, cumulativeShield = 0, suspended = 0, depIndex = 0;
    for (var i = 0; i < years; i++) {
      var year = transferYear + i + 1;
      var mode = facts.modes[i];
      var row = M.annualA(year, mode, config);
      var noi = mode === 'rent' ? row.noi : 0;
      var housingCost = mode === 'live' ? -row.noi : 0;   // for a residence year, noi is the negative of the operating cost
      var depreciation = (mode === 'rent' && depIndex < dep.rows.length) ? dep.rows[depIndex].amount : 0;
      if (mode === 'rent') depIndex++;
      var taxable = Math.max(0, noi - depreciation);
      var tax = taxable * config.ordinaryTax;
      // Passive-activity limits can suspend a rental loss; the suspended part is shown, not credited.
      var unusedDepreciation = Math.max(0, depreciation - Math.max(0, noi));
      suspended += unusedDepreciation;
      var shield = Math.min(depreciation, Math.max(0, noi)) * config.ordinaryTax;
      cumulativeShield += shield;
      var afterTaxCash = noi - housingCost - tax;
      cumulativeCash += afterTaxCash;
      annualRows.push({ year: year, mode: mode, noi: noi, housingCost: housingCost,
                        depreciation: depreciation, taxable: taxable, tax: tax,
                        shield: shield, unusedDepreciation: unusedDepreciation,
                        afterTaxCash: afterTaxCash, cumulativeCash: cumulativeCash });
    }

    return {
      pattern: pattern, years: years, share: share, filing: filing, cgRate: cgRate,
      transferYear: transferYear, saleYear: saleYear,
      rentalYears: facts.rentalYears, residenceYears: facts.residenceYears,
      residenceInWindow: facts.residenceInWindow, eligible121: facts.eligible121,
      nonuseFactor: facts.nonuseFactor, nonuseYears: facts.nonuseYears,
      basis: basis, buildingBasis: buildingBasis, landBasis: landBasis,
      saleValue: saleValue, netProceeds: netProceeds,
      annualDepreciation: dep.annual, depreciationRows: dep.rows,
      depreciationNote: dep.note, depreciationExcepted: dep.excepted,
      accumulatedDepreciation: accumulated, adjustedBasis: adjustedBasis,
      totalGain: totalGain, unrecaptured: unrecaptured, remainder: remainder,
      nonqualifiedGain: nonqualifiedGain, exclusionLimit: exclusionLimit,
      exclusionUsed: exclusionUsed, taxableCapital: taxableCapital,
      taxUnrecaptured: taxUnrecaptured, taxCapital: taxCapital,
      federalTax: taxUnrecaptured + taxCapital,
      afterTaxProceeds: afterTaxProceeds,
      annual: annualRows, cumulativeCash: cumulativeCash,
      cumulativeShield: cumulativeShield, suspendedDepreciation: suspended,
      total: cumulativeCash + afterTaxProceeds
    };
  }

  /* Imputed rent: the rent the household does not have to pay because it lives in the
     house. Public housing economists call this imputed rent; this site credits it only
     when the reader asks it to, because it is a preference, not a cash flow. */
  function imputedRent(options, monthlyRent) {
    var o = Object.assign({}, options);
    var config = Object.assign({}, M.BASE, { inheritYear: o.transferYear || TRANSFER_YEAR });
    var years = o.years || 10;
    var live = evaluate(Object.assign({}, o, { pattern: 'live_all' }));
    var rent = evaluate(Object.assign({}, o, { pattern: 'rent_all' }));
    var residenceYears = Math.max(1, live.residenceYears);
    var factor = 0;
    for (var i = 0; i < residenceYears; i++) factor += Math.pow(1 + config.rentGrowth, i);
    var needed = rent.total - live.total;
    var breakevenMonthly = needed / (12 * factor);
    var monthly = monthlyRent || 0;
    var cumulativeImputed = monthly * 12 * factor;
    return {
      monthly: monthly, factor: factor, residenceYears: residenceYears,
      cumulativeImputed: cumulativeImputed, needed: needed,
      breakevenMonthly: breakevenMonthly,
      liveTotal: live.total, rentTotal: rent.total,
      liveWithImputed: live.total + cumulativeImputed,
      rentTotalAfterTax: rent.total,
      gap: rent.total - (live.total + cumulativeImputed)
    };
  }

  window.TAXREALISM = {
    RECOVERY_YEARS: RECOVERY_YEARS, UNRECAPTURED_RATE: UNRECAPTURED_RATE,
    EXCLUSION: EXCLUSION, TRANSFER_YEAR: TRANSFER_YEAR, MID_MONTH_FRACTION: MID_MONTH_FRACTION,
    PATTERNS: PATTERNS, YEARS: YEARS, SHARES: SHARES, FILINGS: FILINGS,
    CG_RATES: CG_RATES, IMPUTED_RENTS: IMPUTED_RENTS,
    evaluate: evaluate, imputedRent: imputedRent, occupancy: occupancy,
    depreciationSchedule: depreciationSchedule, patternFacts: patternFacts,
    marketValue: marketValue, worksheet3: worksheet3,
    money: function (v) { return M.fmtMoney(v); },
    pct: function (v) { return (v * 100).toFixed(1).replace(/\.0$/, '') + '%'; }
  };
})();
