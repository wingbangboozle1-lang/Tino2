/* Renders the decision-boundary tables. Invented inputs only; nothing is saved. */
(function () {
  'use strict';
  const B = window.BREAKEVEN, M = window.MODEL, C = window.CONDITIONS;
  const money = M.fmtMoney;
  const pct = (v, d) => (100 * v).toFixed(d === undefined ? 1 : d) + '%';
  const tag = w => `<span class="tag${w === 'sell' ? ' on' : ''}">${B.LABELS[w]}</span>`;
  const tr = (xs, last) => '<tr>' + xs.map((x, i) =>
    `<td${i === xs.length - 1 ? ' class="source"' : ' class="wrap"'}>${x}</td>`).join('') + '</tr>';
  const ctx = C.SRC;

  function render() {
    const year = Number(document.getElementById('be-year').value);
    const horizon = Number(document.getElementById('be-horizon').value);

    /* grid: rows are growth, columns are return */
    document.getElementById('boundary-head').innerHTML =
      '<tr><th scope="col">Home-price growth</th>' +
      B.RETURNS.map(r => `<th scope="col">${pct(r, 0)} return</th>`).join('') +
      '<th scope="col">Context only</th></tr>';
    document.getElementById('boundary-body').innerHTML = B.grid(horizon, year).map(row =>
      '<tr><td class="wrap"><strong>' + pct(row.growth) + '</strong></td>' +
      row.cells.map(c => `<td class="wrap">${tag(c.winner)}</td>`).join('') +
      `<td class="source"><a href="${ctx.prop13}" rel="noopener noreferrer">Assessment mechanics ↗</a></td>` +
      '</tr>').join('');

    /* break-even return per growth assumption */
    document.getElementById('threshold-body').innerHTML = B.GROWTH.map(g => {
      const be = B.sellBreakeven(g, horizon, year);
      const text = be.threshold === null
        ? 'Selling never leads in the tested range'
        : be.threshold === 0
          ? 'Selling leads at every return tested'
          : 'about ' + pct(be.threshold);
      const interp = be.threshold === null || be.threshold === 0
        ? 'The ranking does not depend on the portfolio return here.'
        : be.threshold <= 0.04
          ? 'A modest net return is enough for selling to lead.'
          : 'Selling needs a strong net return to lead.';
      return tr([pct(g), '<strong>' + text + '</strong>', interp,
        `<a href="${ctx.prop13}" rel="noopener noreferrer">Assessment mechanics ↗</a>`]);
    }).join('');

    /* single-axis sensitivity */
    const s = B.sensitivity(horizon, year);
    document.getElementById('sensitivity-body').innerHTML = s.rows.map(r =>
      tr([r.axis, pct(r.value), tag(r.winner),
        r.flips ? '<strong>Yes</strong> — this input can change the answer'
          : 'No — the answer holds',
        `<a href="${ctx.pmms}" rel="noopener noreferrer">Market context ↗</a>`])).join('')
      + tr(['Both at the middle of the range (3.5% growth, 5% return)', '—',
        tag(s.baseWinner), 'Reference case for the rows above',
        `<a href="${ctx.cbo}" rel="noopener noreferrer">Baseline context ↗</a>`]);
  }

  document.querySelectorAll('#be-year,#be-horizon').forEach(el =>
    el.addEventListener('change', render));
  render();
})();
