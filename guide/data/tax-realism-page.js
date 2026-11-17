/* Renders the depreciation, recapture and exclusion page. Synthetic example only.
   No input box, no storage of anything, no network request. Every published row
   carries the official rule it was computed from. */
(function () {
  const T = window.TAXREALISM, M = window.MODEL, money = T.money;
  const ref = {
    p527: 'https://www.irs.gov/publications/p527',
    p946: 'https://www.irs.gov/publications/p946',
    p523: 'https://www.irs.gov/publications/p523',
    p544: 'https://www.irs.gov/publications/p544',
    tc409: 'https://www.irs.gov/taxtopics/tc409',
    i1040sd: 'https://www.irs.gov/instructions/i1040sd',
    i4797: 'https://www.irs.gov/instructions/i4797',
    ftb540: 'https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html',
    niit: 'https://www.irs.gov/taxtopics/tc559',
    basis: 'https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances'
  };
  const src = (key, label) => `<a href="${ref[key]}" rel="noopener noreferrer">${label} ↗</a>`;
  const tr = xs => '<tr>' + xs.map((x, i) => `<td${i === xs.length - 1 ? ' class="source"' : ' class="wrap"'}>${x}</td>`).join('') + '</tr>';
  const pct = (x, digits = 1) => (100 * x).toFixed(digits).replace(/\.0+$/, '') + '%';
  const val = id => document.getElementById(id).value;

  function controls() {
    return {
      pattern: val('tr-pattern'), years: Number(val('tr-years')),
      share: Number(val('tr-share')), filing: val('tr-filing'),
      cgRate: Number(val('tr-rate'))
    };
  }

  function summary(r) {
    const rows = [
      ['Market value at the transfer, and the assumed basis', money(r.basis),
        'Assumed date-of-death value basis, the IRS general rule for inherited property. A trust that is not includible in the estate may not get it.', src('basis', 'IRS · inherited basis')],
      ['Building share of that value (land is not depreciable)', `${money(r.buildingBasis)} · land ${money(r.landBasis)} · ${pct(r.share, 0)}`,
        'Land is never depreciable; the split is an appraisal question, and the IRS allows an assessed-value ratio where values are uncertain.', src('p527', 'IRS · Pub. 527')],
      ['Sale value and net proceeds', `${money(r.saleValue)} · ${money(r.netProceeds)}`,
        `Sold at the end of year ${r.years} in the synthetic example; selling costs use the comparison page's invented rate.`, src('p544', 'IRS · Pub. 544')],
      ['Depreciation taken over the rental years', money(r.accumulatedDepreciation),
        `Straight line over 27.5 years with the mid-month convention, on the building only, for ${r.rentalYears} rental year(s). ${r.depreciationNote}`, src('p527', 'IRS · Pub. 527')],
      ['Adjusted basis at the sale', money(r.adjustedBasis),
        'Basis is reduced by depreciation allowed or allowable, whether or not it was claimed.', src('p527', 'IRS · Pub. 527')],
      ['Total gain', money(r.totalGain),
        'Net proceeds less adjusted basis.', src('p544', 'IRS · Pub. 544')],
      ['Unrecaptured section 1250 gain — taxed at a maximum 25%', money(r.unrecaptured),
        'The part of the gain that comes from depreciation. The IRS states a maximum 25% rate on it.', src('tc409', 'IRS · Topic 409')],
      ['Gain left after the depreciation is taken out', money(r.remainder),
        'Pub. 523 Worksheet 3, Section A, step 3: everything above this point is capital gain, not recapture.', src('p523', 'IRS · Pub. 523')],
      ['Gain allocated to nonqualified use', money(r.nonqualifiedGain),
        `Factor ${pct(r.nonuseFactor, 0)} = ${r.nonuseYears} non-residence year(s) before the last qualified use, divided by ${r.years} years owned.`, src('p523', 'IRS · Pub. 523')],
      ['Home-sale exclusion applied', money(r.exclusionUsed),
        r.eligible121
          ? `Eligible: lived in for ${r.residenceInWindow} of the last 5 years, the 24-month test is met, limit ${money(r.exclusionLimit)}.`
          : 'Not eligible: the 24-month residence test inside the 5 years before the sale is not met in this pattern.', src('p523', 'IRS · Pub. 523')],
      ['Capital gain left to tax', money(r.taxableCapital),
        `Charged at the selected federal rate of ${pct(r.cgRate, 0)}. California, which the guide records as taxing capital gains as ordinary income, is not included here.`, src('tc409', 'IRS · Topic 409') + ' · ' + src('ftb540', 'FTB · Form 540')],
      ['Federal tax on the sale', money(r.federalTax),
        `25% of the recaptured depreciation plus ${pct(r.cgRate, 0)} of the taxable capital gain. Form 4797 carries the recapture.`, src('i4797', 'IRS · Form 4797')],
      ['After-tax proceeds', money(r.afterTaxProceeds),
        'Net proceeds less the two taxes. Neither the 3.8% net investment income tax nor any state tax is included.', src('i1040sd', 'IRS · Schedule D') + ' · ' + src('niit', 'IRS · Topic 559')],
      ['Depreciation that never produced a deduction this year', money(r.suspendedDepreciation),
        'Rental loss beyond the income it can offset is shown but not credited; passive-activity limits decide when it can be used.', src('p527', 'IRS · Pub. 527')]
    ];
    document.getElementById('tr-summary').innerHTML = rows.map(tr).join('');
  }

  function schedule(r) {
    const rows = r.depreciationRows.map(row => [
      `Rental year ${row.year}`, money(row.amount), money(row.cumulative),
      money(r.basis - row.cumulative),
      row.year === 1 || row.year === r.rentalYears
        ? 'Mid-month convention: 11.5 months of a full year.'
        : 'A full year of straight-line depreciation over 27.5 years.',
      src('p946', 'IRS · Pub. 946, Table A-6')
    ]);
    if (!rows.length) {
      rows.push(['No rental years', money(0), money(0), money(r.basis),
        'Nothing was placed in service for the production of income in this pattern.', src('p527', 'IRS · Pub. 527')]);
    }
    document.getElementById('tr-schedule').innerHTML = rows.map(tr).join('');
  }

  function annual(r) {
    document.getElementById('tr-annual').innerHTML = r.annual.map(row => [
      String(row.year),
      row.mode === 'rent' ? 'Rented' : 'Lived in',
      row.mode === 'rent' ? money(row.noi) : '−' + money(row.housingCost).replace('−', ''),
      money(row.depreciation), money(row.taxable), money(row.tax), money(row.afterTaxCash),
      row.mode === 'rent'
        ? 'Net operating income is reduced by depreciation before tax in this illustration.'
        : 'A residence year produces no rental income and no depreciation.',
      src('p527', 'IRS · Pub. 527')
    ]).map(tr).join('');
  }

  function patterns(opts) {
    document.getElementById('tr-patterns').innerHTML = T.PATTERNS.map(p => {
      const r = T.evaluate(Object.assign({}, opts, { pattern: p.key }));
      return [
        p.label,
        r.eligible121 ? `Yes — ${r.residenceInWindow} of the last 5 years` : 'No',
        pct(r.nonuseFactor, 0),
        money(r.accumulatedDepreciation),
        money(r.taxUnrecaptured),
        money(r.exclusionUsed),
        money(r.taxableCapital),
        money(r.federalTax),
        p.blurb,
        src('p523', 'IRS · Pub. 523')
      ];
    }).map(tr).join('');
  }

  function imputed(opts) {
    const monthly = Number(val('tr-rent'));
    document.getElementById('tr-imputed').innerHTML = T.YEARS.map(y => {
      const r = T.imputedRent(Object.assign({}, opts, { years: y }), monthly);
      return [
        `${y} years`,
        money(r.rentTotal - r.liveTotal),
        money(r.breakevenMonthly) + ' per month',
        money(r.cumulativeImputed),
        r.gap > 0 ? money(r.gap) + ' still short' : money(-r.gap) + ' ahead',
        `Renting returns ${money(r.rentTotal)} after tax over ${y} years; living there returns ${money(r.liveTotal)} before any rent is credited. The rent avoided is a preference, not a cash flow, and this site credits it only when asked.`,
        src('p527', 'IRS · Pub. 527')
      ];
    }).map(tr).join('');
  }

  function render() {
    const opts = controls();
    const r = T.evaluate(opts);
    document.getElementById('tr-readout').textContent =
      `${r.rentalYears} rental year(s), ${r.residenceYears} lived-in year(s) of ${r.years} owned; ` +
      `${r.eligible121 ? 'eligible' : 'not eligible'} for the home-sale exclusion; ` +
      `recapture ${money(r.unrecaptured)} taxed at 25%, capital gain ${money(r.taxableCapital)} taxed at ${pct(r.cgRate, 0)}.`;
    summary(r); schedule(r); annual(r); patterns(opts); imputed(opts);
  }

  for (const id of ['tr-pattern', 'tr-years', 'tr-share', 'tr-filing', 'tr-rate', 'tr-rent']) {
    const el = document.getElementById(id);
    if (el) el.addEventListener('change', render);
  }
  render();
})();
