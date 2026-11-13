/* Interactive comparison. Runs entirely in the browser; nothing is sent or stored. */
(function () {
  'use strict';
  var M = window.MODEL;
  if (!M) return;

  var ids = ['c-transfer', 'c-horizon', 'c-home', 'c-port', 'c-rent'];
  var els = {};
  ids.forEach(function (id) { els[id] = document.getElementById(id); });
  var result = document.getElementById('live-result');
  var compare = document.getElementById('live-compare');
  if (!result || !compare || !els['c-transfer']) return;

  function render() {
    var cfg = {
      homeGrowth: Number(els['c-home'].value),
      portfolio: Number(els['c-port'].value),
      a: { rentMonth: Number(els['c-rent'].value) }
    };
    var year = Number(els['c-transfer'].value);
    var horizon = Number(els['c-horizon'].value);
    var r = M.compare(year, horizon, cfg);
    var rows = r.rows;
    var sell = rows.sell.terminal;
    var values = {
      sell: sell,
      rent: rows.rent.terminal,
      live: rows.live.terminalTotal
    };
    var best = r.best;

    result.innerHTML =
      '<div class="eyebrow" style="color:#d1e8b1">Result for a ' + year +
      ' transfer, held ' + horizon + ' years</div>' +
      '<h2>' + (best === 'sell' ? 'Selling leads' :
        best === 'rent' ? 'Renting leads' : 'Living in leads') + '</h2>' +
      '<p>Ending value: sell ' + M.fmtMoney(values.sell) +
      ' &middot; rent ' + M.fmtMoney(values.rent) +
      ' &middot; live ' + M.fmtMoney(values.live) + '</p>' +
      '<p class="tiny">Basis resets at death, so the sale pays no gain tax. ' +
      'Cash flows are reinvested at ' + M.fmtPct(cfg.portfolio - M.BASE.fee) +
      ' net. The live-in figure includes rent from the San Francisco third unit.</p>';

    var labels = {
      sell: 'Sell A and invest',
      rent: 'Keep A and rent it',
      live: 'Keep A and live in it'
    };
    var first = {
      sell: rows.sell.proceeds * (cfg.portfolio - M.BASE.fee),
      rent: rows.rent.year1Cash,
      live: rows.live.year1Cash
    };
    var src = 'https://www.irs.gov/taxtopics/tc701';
    compare.innerHTML = ['sell', 'rent', 'live'].map(function (k) {
      var diff = values[k] - sell;
      return '<tr><td>' + labels[k] + '</td>' +
        '<td class="number">' + M.fmtMoney(first[k]) + '</td>' +
        '<td class="number">' + M.fmtMoney(values[k]) + '</td>' +
        '<td class="number">' + (k === 'sell' ? '—' : M.fmtMoney(diff)) + '</td>' +
        '<td><a href="' + src + '" rel="noopener noreferrer">IRS Topic 701 ↗</a></td></tr>';
    }).join('');
  }

  ids.forEach(function (id) {
    if (els[id]) els[id].addEventListener('change', render);
  });
  render();
}());
