/*
 * Every number the model uses, with where it came from — session 5a1bd5be.
 *
 * status:
 *   verified   = read on the official page listed in `src` (see facts.js for the wording)
 *   calculated = arithmetic on verified figures; the arithmetic is in `note`
 *   brief      = supplied by the owner in the project brief, rounded to $10; not checkable by me
 *   assumption = no official figure exists for this household; listed on the Flagged for Review page
 *
 * No personal identifiers. Brief figures are stored already rounded to the nearest $10.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.ModelInputs = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  // kind: usd = dollars, usdm = dollars per month, pct = fraction shown as %, year, int, choice
  var FIELDS = [
    // ---------------- timing
    { key: 'inheritYear', group: 'Timing', label: 'Year Property A is inherited', value: 2045, kind: 'choice',
      choices: [[2040, '2040'], [2045, '2045'], [2050, '2050']], status: 'brief', src: [],
      note: 'The brief gives a window of 2040 to 2050. 2045 is the middle of it.', flag: 'F-TIMING' },
    { key: 'horizon', group: 'Timing', label: 'Years followed after inheritance', value: 10, kind: 'choice',
      choices: [[5, '5 years'], [10, '10 years'], [20, '20 years']], status: 'assumption', src: [],
      note: 'Long enough for the home-sale exclusion (2 of 5 years) and to show compounding.', flag: 'F-HORIZON' },

    // ---------------- Property A
    { key: 'aValue2026', group: 'Property A (Cupertino)', label: 'Market value, November 2026', value: 3100000, kind: 'usd',
      status: 'brief', src: [], note: 'Owner estimate. No appraisal was supplied.', flag: 'F-VALUE-A' },
    { key: 'aAv2026', group: 'Property A (Cupertino)', label: 'Assessed value, 2026 roll', value: 550540, kind: 'usd',
      status: 'brief', src: ['B1'], note: 'Equals the 2025 value times the official 2026-27 factor of 1.02, so it is consistent with the State table.' },
    { key: 'aAv2025', group: 'Property A (Cupertino)', label: 'Assessed value, 2025 roll', value: 539740, kind: 'usd',
      status: 'brief', src: [], note: 'From the brief.' },
    { key: 'aBill2025', group: 'Property A (Cupertino)', label: 'Property tax bill, 2025', value: 7210, kind: 'usd',
      status: 'brief', src: [], note: 'From the brief. The 2026 bill was not supplied.' },
    { key: 'aRate', group: 'Property A (Cupertino)', label: 'Ad valorem tax rate', value: 0.011636, kind: 'pct', digits: 4,
      status: 'calculated', src: ['L2'],
      note: 'Sum of the FY2025-26 county summary rates for the agencies that serve most of Cupertino: 1.00000 + 0.03880 + 0.00240 + 0.00520 + 0.00560 + 0.03350 (elementary) + 0.04170 (high school) + 0.03110 (college) + 0.00140 (open space) + 0.00390 (water district). The parcel’s tax rate area was not looked up; FY2026-27 rates were not yet posted.',
      flag: 'F-RATE-A' },
    { key: 'aGrowth', group: 'Property A (Cupertino)', label: 'House price growth per year', value: 0.0429, kind: 'pct', digits: 2,
      status: 'calculated', src: ['H1'], note: 'FHFA index, San Jose metro, 10 years to Q2 2026: (558.75 / 367.05)^(1/10) − 1 = 4.29%. History, not a forecast.', flag: 'F-GROWTH' },
    { key: 'aInsurance', group: 'Property A (Cupertino)', label: 'Home insurance per year (2026 dollars)', value: 1500, kind: 'usd',
      status: 'brief', src: ['CDI'], note: 'Owner’s guess. The State’s comparison tool shows premiums only for hypothetical homes and says an exact premium needs a quote.', flag: 'F-INSURANCE' },
    { key: 'aMaintenance', group: 'Property A (Cupertino)', label: 'Maintenance and repairs per year (2026 dollars)', value: 6000, kind: 'usd',
      status: 'assumption', src: [], note: 'No official figure exists and no repair history was supplied. Set equal to the figure used by the dashboard already published in this repository so the two can be compared.', flag: 'F-MAINT' },
    { key: 'aUtilities', group: 'Property A (Cupertino)', label: 'Water and power per year if lived in (2026 dollars)', value: 1500, kind: 'usd',
      status: 'brief', src: ['N1'], note: 'Middle of the brief’s $100 to $150 a month for water. The solar bill credit in the brief is not counted after inheritance: the 20-year net-metering period will have run out for any system connected before April 2023.', flag: 'F-SOLAR' },
    { key: 'aRent2026', group: 'Property A (Cupertino)', label: 'Monthly rent if rented out (2026 dollars)', value: 6000, kind: 'usdm',
      status: 'assumption', src: ['HUD1'], note: 'No official rent exists for one house. HUD’s metro-wide benchmark for 2026 is $4,602 (3 bedrooms) and $5,010 (4 bedrooms), utilities included; the bedroom count was not supplied.', flag: 'F-RENT-A' },
    { key: 'aBuildingShare', group: 'Property A (Cupertino)', label: 'Share of value that is building (depreciable)', value: 0.30, kind: 'pct', digits: 0,
      status: 'assumption', src: ['D2'], note: 'Land cannot be depreciated. The IRS allows the split shown on the tax bill; the bill’s land and improvement lines were not supplied.', flag: 'F-SPLIT' },
    { key: 'landlordInsuranceFactor', group: 'Property A (Cupertino)', label: 'Landlord policy cost ÷ homeowner policy cost', value: 1.0, kind: 'num',
      status: 'assumption', src: [], note: 'No official ratio found. 1.0 means the same premium.', flag: 'F-INSURANCE' },
    { key: 'managementFee', group: 'Property A (Cupertino)', label: 'Property manager fee (share of rent)', value: 0, kind: 'pct', digits: 0,
      status: 'assumption', src: [], note: '0 means self-managed.', flag: 'F-MGMT' },
    { key: 'vacancy', group: 'Property A (Cupertino)', label: 'Vacancy (share of the year unrented)', value: 0.05, kind: 'pct', digits: 0,
      status: 'assumption', src: [], note: 'Applied to Property A when rented and to the freed unit in Property B.', flag: 'F-VACANCY' },

    // ---------------- Property B
    { key: 'bValue2026', group: 'Property B (San Francisco)', label: 'Market value, November 2026', value: 1800000, kind: 'usd',
      status: 'brief', src: [], note: 'Owner estimate.', flag: 'F-VALUE-B' },
    { key: 'bAv2025', group: 'Property B (San Francisco)', label: 'Assessed value, 2025 roll', value: 114250, kind: 'usd',
      status: 'brief', src: [], note: 'From the brief.' },
    { key: 'bBill2025', group: 'Property B (San Francisco)', label: 'Property tax bill, 2025', value: 2440, kind: 'usd',
      status: 'brief', src: [], note: 'From the brief.' },
    { key: 'bRate', group: 'Property B (San Francisco)', label: 'Ad valorem tax rate', value: 0.0118162182, kind: 'pct', digits: 4,
      status: 'verified', src: ['L1'], note: 'San Francisco secured rate for FY2026-27.' },
    { key: 'bGrowth', group: 'Property B (San Francisco)', label: 'House price growth per year', value: 0.0278, kind: 'pct', digits: 2,
      status: 'calculated', src: ['H2'], note: 'FHFA index, San Francisco metro division, 10 years to Q2 2026: (506.53 / 385.01)^(1/10) − 1 = 2.78%.', flag: 'F-GROWTH' },
    { key: 'bUnitRent2026', group: 'Property B (San Francisco)', label: 'Monthly rent for the unit the household would leave (2026 dollars)', value: 3580, kind: 'usdm',
      status: 'assumption', src: ['HUD2', 'R3'], note: 'Half of the $7,150 a month the brief reports for the two rented units, rounded to $10. HUD’s metro benchmark for 2026: $2,977 (1 bedroom), $3,604 (2 bedrooms).', flag: 'F-RENT-B' },
    { key: 'rentCapShare', group: 'Property B (San Francisco)', label: 'Yearly rent increase as a share of inflation', value: 0.60, kind: 'pct', digits: 0,
      status: 'verified', src: ['R3'], note: 'San Francisco’s allowed increase is 60% of Bay Area inflation. Applies only if the building is covered by the Rent Ordinance.', flag: 'F-RENTCONTROL' },

    { key: 'bMaintenance', group: 'Property B (San Francisco)', label: 'Maintenance and repairs per year (2026 dollars)', value: 9000, kind: 'usd',
      status: 'assumption', src: [], note: 'No official figure exists. Set equal to the figure used by the dashboard already published in this repository.', flag: 'F-MAINT' },
    { key: 'bHousingRent', group: 'Property B (San Francisco)', label: 'Monthly rent the household would pay elsewhere if B were sold', value: 3600, kind: 'usdm',
      status: 'assumption', src: ['HUD2'], note: 'HUD’s 2026 benchmark for a 2-bedroom home in the San Francisco area ($3,604), rounded to $10. The size of home the household needs was not supplied.', flag: 'F-RENT-B' },

    // ---------------- rules and economy
    { key: 'prop13Factor', group: 'Rules and economy', label: 'Yearly rise in assessed value', value: 0.02, kind: 'pct', digits: 2,
      status: 'verified', src: ['B1'], note: '2% is the legal maximum. The factor was below 2% in 11 of the 51 years in the State table (average of the last 20 years: 1.67%), so this slightly overstates future tax.', flag: 'F-PROP13' },
    { key: 'prop19Amount2025', group: 'Rules and economy', label: 'Proposition 19 amount, 16 Feb 2025 to 15 Feb 2027', value: 1044586, kind: 'usd', exact: true, fixed: true,
      status: 'verified', src: ['P9'], note: 'Adjusted on 16 February of every odd year.' },
    { key: 'caHpiChange', group: 'Rules and economy', label: 'California house price change used at each adjustment', value: 0.0583, kind: 'pct', digits: 2,
      status: 'calculated', src: ['H3', 'P9'], note: 'FHFA index, California, 10 years to Q2 2026: (974.97 / 553.43)^(1/10) − 1 = 5.83%. The State’s two adjustments so far were 2.26% and 2.15%.', flag: 'F-P19AMOUNT' },
    { key: 'inflation', group: 'Rules and economy', label: 'Inflation per year', value: 0.0286, kind: 'pct', digits: 2,
      status: 'calculated', src: ['CPI'], note: 'Consumer prices, San Francisco area, August 2006 to August 2026: (370.130 / 210.700)^(1/20) − 1 = 2.86%.', flag: 'F-INFLATION' },
    { key: 'investReturn', group: 'Rules and economy', label: 'Investment return per year', value: 0.08025, kind: 'pct', digits: 2,
      status: 'calculated', src: ['TSP'], note: 'Half Treasury fund (4.65% a year since 1987) and half S&P 500 index fund (11.40% a year since 1988), federal Thrift Savings Plan figures to October 2026. History, not a forecast.', flag: 'F-RETURN' },
    { key: 'sellCost', group: 'Rules and economy', label: 'Cost of selling a house (share of price)', value: 0.06, kind: 'pct', digits: 1,
      status: 'assumption', src: ['T1', 'T3'], note: 'Agent fees and closing costs have no official figure. Only the county transfer tax inside it is official: $1.10 per $1,000 (0.11%).', flag: 'F-SELLCOST' },
    { key: 'taxOrdinary', group: 'Rules and economy', label: 'Income tax on one more dollar of rent', value: 0.333, kind: 'pct', digits: 1,
      status: 'assumption', src: ['F2', 'C5'], note: 'Federal 24% plus California 9.3%. The heir household’s income was not supplied.', flag: 'F-TAXRATES' },
    { key: 'taxGain', group: 'Rules and economy', label: 'Tax on long-term gains', value: 0.281, kind: 'pct', digits: 1,
      status: 'assumption', src: ['I2', 'I4', 'C4', 'C5'], note: 'Federal 15% plus 3.8% net investment income tax plus California 9.3%. Large gains taken in one year would be taxed at up to 20% + 3.8% + 12.3% or more.', flag: 'F-TAXRATES' },
    { key: 'taxRecapture', group: 'Rules and economy', label: 'Tax on gain from depreciation taken', value: 0.381, kind: 'pct', digits: 1,
      status: 'assumption', src: ['I2', 'I4', 'C5'], note: 'Federal maximum 25% plus 3.8% plus California 9.3%.', flag: 'F-TAXRATES' },
    { key: 'homeSaleExclusion', group: 'Rules and economy', label: 'Home-sale gain excluded from tax', value: 500000, kind: 'choice',
      choices: [[500000, '$500,000 (joint return)'], [250000, '$250,000 (single)']],
      status: 'verified', src: ['I3'], note: 'Needs 2 years of ownership and 2 years of living there in the 5 years before the sale. Joint filing is assumed.', flag: 'F-FILING' },
    { key: 'depreciationYears', group: 'Rules and economy', label: 'Depreciation period for a rental house (years)', value: 27.5, kind: 'num', fixed: true,
      status: 'verified', src: ['D1'], note: 'Building only.' },

    // ---------------- estate tax
    { key: 'estateExclusion2026', group: 'Estate tax', label: 'Federal exclusion per person, 2026', value: 15000000, kind: 'usd', fixed: true,
      status: 'verified', src: ['F1', 'F3'], note: '' },
    { key: 'estateExclusion2027', group: 'Estate tax', label: 'Federal exclusion per person, 2027', value: 15480000, kind: 'usd', fixed: true,
      status: 'verified', src: ['F2'], note: '' },
    { key: 'estateIndexing', group: 'Estate tax', label: 'Yearly rise in the exclusion after 2027', value: 0.0253, kind: 'pct', digits: 2,
      status: 'calculated', src: ['F1', 'F2'], note: 'Average of the 14 yearly inflation adjustments in the IRS table (2011–2017, 2018–2025, 2026–2027); the 2018 and 2026 jumps were acts of Congress and are left out. Congress can change the exclusion at any time.', flag: 'F-ESTATE' },
    { key: 'estateRate', group: 'Estate tax', label: 'Federal estate tax rate above the exclusion', value: 0.40, kind: 'pct', digits: 0, fixed: true,
      status: 'verified', src: ['F6'], note: '' },
    { key: 'spouses', group: 'Estate tax', label: 'Exclusions available', value: 1, kind: 'choice',
      choices: [[1, 'One (single owner)'], [2, 'Two (married, portability elected)']],
      status: 'assumption', src: ['F1', 'F5'], note: 'The owner’s marital status was not supplied.', flag: 'F-ESTATE' },
    { key: 'otherEstateAssets', group: 'Estate tax', label: 'Other assets in the estate at death', value: 0, kind: 'usd',
      status: 'brief', src: [], note: 'The brief says “a considerable amount of money” without a figure. Enter [AMOUNT] to test it.', flag: 'F-ESTATE' }
  ];

  var SCENARIOS = {
    house: {
      low:  { label: 'Low', window: '20 years, 2006–2026 (includes the 2006–2012 fall)', aGrowth: 0.0287, bGrowth: 0.0254, caHpiChange: 0.0210 },
      mid:  { label: 'Middle', window: '10 years, 2016–2026', aGrowth: 0.0429, bGrowth: 0.0278, caHpiChange: 0.0583 },
      high: { label: 'High', window: '30 years, 1996–2026', aGrowth: 0.0575, bGrowth: 0.0553, caHpiChange: 0.0541 }
    },
    returns: {
      low:  { label: 'Treasuries', basis: 'Thrift Savings Plan G Fund, since April 1987', investReturn: 0.0465 },
      mid:  { label: 'Half and half', basis: 'Average of the two', investReturn: 0.08025 },
      high: { label: 'S&P 500 index', basis: 'Thrift Savings Plan C Fund, since January 1988', investReturn: 0.1140 }
    }
  };

  // Brief figures used only for the Property B table and for cross-checks (rounded to $10).
  var BRIEF = {
    bRentTwoUnits: 7150,          // $ per month, two rented units together
    bWaterMonthly: [330, 400],    // $ per month, all three units
    bPowerMonthly: [30, 70],      // $ per month
    bInsurance: 1500,             // $ per year, owner's guess
    aWaterMonthly: [100, 150],    // $ per month
    aSolarCreditMonthly: [10, 20] // $ per month credit reported by the owner
  };

  function defaults() {
    var p = {};
    FIELDS.forEach(function (f) { p[f.key] = f.value; });
    return p;
  }

  return { FIELDS: FIELDS, SCENARIOS: SCENARIOS, BRIEF: BRIEF, defaults: defaults };
});
