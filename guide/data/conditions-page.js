/* Renders the real-conditions tables. Every cell is either a published official
   statistic, arithmetic derived from one, or a clearly labelled scenario value.
   No household data is read or written. Nothing is uploaded or saved. */
(function () {
  'use strict';
  const C = window.CONDITIONS, M = window.MODEL, B = window.BREAKEVEN;
  const money = M.fmtMoney;
  const pct = (v, d) => (100 * v).toFixed(d === undefined ? 2 : d) + '%';
  const src = (key, label) => {
    const href = C.SRC[key];
    const text = label || key;
    return `<a href="${href}" rel="noopener noreferrer">${text} ↗</a>`;
  };
  const tr = xs => '<tr>' + xs.map((x, i) =>
    `<td${i === xs.length - 1 ? ' class="source"' : ' class="wrap"'}>${x}</td>`).join('') + '</tr>';
  const body = id => document.getElementById(id);

  /* --- scenario bands, generated from the data file so the page cannot drift --- */
  body('band-table').innerHTML = C.BANDS.map(b => {
    const p24 = C.project(b, 24, 0), p50 = C.project(b, 50, 0);
    return tr([
      `<strong>${b.label}</strong>`,
      pct(b.inflation, 1),
      '×' + p24.inflationMultiple.toFixed(2),
      '×' + p50.inflationMultiple.toFixed(2),
      b.key === 'prop13' ? 'Official cap used as a scenario' : 'Scenario, not a forecast',
      src('cpiHistory', 'Observed series')
    ]);
  }).join('');

  /* --- what compounding does, including the purchasing-power check --- */
  body('compound-table').innerHTML = [0.02, 0.026, 0.04, 0.07].map(r => {
    const g24 = Math.pow(1 + r, 24), g50 = Math.pow(1 + r, 50);
    return tr([
      pct(r, 1),
      '×' + g24.toFixed(2),
      '×' + g50.toFixed(2),
      money(1000000 / g24),
      src('cpiHistory', 'Arithmetic from the index')
    ]);
  }).join('');

  /* --- the rent break-even and cost-structure tables --- */
  const GROWTH = 0.035, YEAR = 2045, AFTER = 1;
  const be = B.rentBreakeven(GROWTH, YEAR, AFTER);
  const first = be.rows[0];
  const cs = B.costStructure(GROWTH, YEAR, AFTER);
  const share = (part, whole) => Math.round(100 * part / whole) + '%';

  const beRows = [
    ['Property tax on the reassessed value',
      money(first.propertyTax),
      'Computed on market value, not on the protected base. This is the line a rental cannot avoid if relief does not apply.'],
    ['Water, insurance and upkeep',
      money(first.otherCosts),
      'Upkeep tracks modeled market value, so it rises with price, not with the tax cap.'],
    ['Gross rent the model assumes',
      money(first.assumedMonthly) + ' per month',
      'An invented figure for 2046, grown from an invented 2026 rent.'],
    ['Gross rent the cost structure requires to break even',
      money(first.grossNeededMonthly) + ' per month',
      'Before financing and income tax. Computed from the same invented assumptions.'],
    ['The gap',
      share(first.grossNeededMonthly - first.assumedMonthly, first.assumedMonthly) + ' of assumed rent',
      'The rental is short by roughly this fraction before any mortgage or income tax is added.'],
    ['Same test expressed in today’s money',
      money(first.grossNeededMonthlyToday) + ' required vs ' + money(first.assumedMonthlyToday) + ' assumed',
      'Today’s-money figures remove assumed rent growth, so they can be compared with an actual rent roll.']
  ];
  body('breakeven-table').innerHTML = beRows.map(r =>
    tr([r[0], `<strong>${r[1]}</strong>`, r[2],
      src('prop13', 'Assessment rule') + ' · ' + src('rental', 'Rental tax rule')])).join('');

  const costRows = [
    ['Property tax', share(cs.live.propertyTax, cs.live.total), share(cs.rent.propertyTax, cs.rent.total),
      src('prop13', 'Prop 13 mechanics')],
    ['Maintenance and repairs', share(cs.live.maintenance, cs.live.total), share(cs.rent.maintenance, cs.rent.total),
      src('rental', 'Capital versus repair')],
    ['Water', share(cs.live.water, cs.live.total), share(cs.rent.water, cs.rent.total),
      src('water', 'Provider context')],
    ['Insurance', share(cs.live.insurance, cs.live.total), share(cs.rent.insurance, cs.rent.total),
      src('cdi', 'Premium context')]
  ];
  body('cost-table').innerHTML = costRows.map(tr).join('');
})();
