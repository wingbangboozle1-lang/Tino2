/*
 * Browser calculator — session 5a1bd5be.
 * Uses the same engine (src/engine.js) and inputs (src/inputs.js) as the page generator.
 * An input overrides the default only after the user changes it, so the untouched
 * calculator reproduces the published tables exactly. Nothing is stored or sent.
 */
(function () {
  'use strict';
  var E = window.Engine, I = window.ModelInputs, F = window.Fmt;
  var form = document.getElementById('calc');
  if (!E || !I || !F || !form) return;

  var NAME = { SELL: 'Sell and invest', RENT: 'Rent it out', LIVE: 'Live in it' };
  var CLS = { SELL: 'f-sell', RENT: 'f-rent', LIVE: 'f-live' };
  var controls = Array.prototype.slice.call(form.querySelectorAll('[data-key]'));
  controls.forEach(function (el) { el.setAttribute('data-initial', el.getAttribute('data-default')); });
  var scenario = {};      // overrides set by the scenario buttons

  function readInputs() {
    var p = I.defaults(), k;
    for (k in scenario) p[k] = scenario[k];
    controls.forEach(function (el) {
      var key = el.getAttribute('data-key'), kind = el.getAttribute('data-kind');
      var changed = el.value !== el.getAttribute('data-default');
      el.closest('.field').classList.toggle('changed', changed);
      if (!changed) return;
      var v = Number(el.value);
      if (!isFinite(v) || el.value === '') return;
      p[key] = kind === 'pct' ? v / 100 : v;
    });
    return p;
  }

  function setControl(key, value) {
    var el = form.querySelector('[data-key="' + key + '"]');
    if (!el) return;
    var kind = el.getAttribute('data-kind');
    el.value = kind === 'pct' ? String(Math.round(value * 1e6) / 1e4) : String(value);
    el.setAttribute('data-default', el.value);   // scenario values count as the new baseline
  }

  function row(label, value) { return '<tr><td>' + label + '</td><td>' + value + '</td></tr>'; }

  function render() {
    var p = readInputs(), s;
    try { s = E.simulate(p); } catch (e) { return; }
    var list = [['SELL', s.sell], ['RENT', s.rent], ['LIVE', s.live]];
    var max = Math.max.apply(null, list.map(function (x) { return Math.abs(x[1].wealthLiquid); })) || 1;
    document.getElementById('calc-title').textContent = 'Inherited in ' + s.inheritYear + ', measured in ' + s.endYear + ': ' + NAME[s.best] + ' is highest';
    document.getElementById('calc-bars').innerHTML = '<div class="bars">' + list.map(function (x) {
      return '<div class="bar' + (s.best === x[0] ? ' best' : '') + '"><div class="barlabel">' + NAME[x[0]] + '</div><div class="bartrack"><div class="barfill ' + CLS[x[0]] +
        '" style="width:' + (Math.abs(x[1].wealthLiquid) / max * 100).toFixed(1) + '%"></div></div><div class="barvalue">' + F.usd(x[1].wealthLiquid) + '</div></div>';
    }).join('') + '</div>';

    var beRent = E.breakEvenRent(p), beLive = E.breakEvenReturn(p, 'live'), beRentRet = E.breakEvenReturn(p, 'rent');
    var defl = s.deflator, y1l = s.live.years[0], y1r = s.rent.years[0];
    var html = '';
    html += row('Value of Property A in ' + s.inheritYear, F.usd(s.valueAtDeath));
    html += row('After tax in ' + s.endYear + ' — sell and invest', F.usd(s.sell.wealthLiquid));
    html += row('After tax in ' + s.endYear + ' — rent it out', F.usd(s.rent.wealthLiquid));
    html += row('After tax in ' + s.endYear + ' — live in it', F.usd(s.live.wealthLiquid));
    html += row('Highest, in 2026 dollars', F.usd(Math.max(s.sell.wealthLiquid, s.rent.wealthLiquid, s.live.wealthLiquid) / defl));
    html += row('Selling against renting', F.usdSigned(s.costOfRenting));
    html += row('Selling against living in it', F.usdSigned(s.costOfLiving));
    html += row('Yearly price of living in it', F.usd(s.costOfLivingPerYear));
    html += row('First-year property tax if an heir moves in', F.usd(y1l.propertyTax));
    html += row('First-year property tax if rented out', F.usd(y1r.propertyTax));
    html += row('First-year net cash — live in it', F.usd(y1l.cash));
    html += row('First-year net cash — rent it out', F.usd(y1r.cash));
    html += row('First-year return — sell and invest, before tax', F.usd(s.sell.firstYearReturn));
    html += row('Return below which renting beats selling', beRentRet === null ? 'none between 0% and 30%' : F.pct(beRentRet, 2));
    html += row('Return below which living in it beats selling', beLive === null ? 'none between 0% and 30%' : F.pct(beLive, 2));
    html += row('Rent at which renting matches selling (2026 dollars, a month)', beRent === null ? 'not reached' : F.usd(beRent));
    html += row('Federal estate exclusion in ' + s.inheritYear + (p.spouses === 2 ? ' (two)' : ''), F.usd(s.estate.shelter));
    html += row('Federal estate tax (Property A plus other assets entered)', F.usd(s.estate.tax));
    document.getElementById('calc-rows').innerHTML = html;
  }

  form.addEventListener('input', render);
  form.addEventListener('change', render);
  form.addEventListener('submit', function (e) { e.preventDefault(); });
  Array.prototype.forEach.call(form.querySelectorAll('[data-house]'), function (b) {
    b.addEventListener('click', function () {
      var h = I.SCENARIOS.house[b.getAttribute('data-house')];
      ['aGrowth', 'bGrowth', 'caHpiChange'].forEach(function (k) { scenario[k] = h[k]; setControl(k, h[k]); });
      render();
    });
  });
  Array.prototype.forEach.call(form.querySelectorAll('[data-returns]'), function (b) {
    b.addEventListener('click', function () {
      var r = I.SCENARIOS.returns[b.getAttribute('data-returns')];
      scenario.investReturn = r.investReturn; setControl('investReturn', r.investReturn);
      render();
    });
  });
  document.getElementById('calc-reset').addEventListener('click', function () {
    scenario = {};
    controls.forEach(function (el) { var v = el.getAttribute('data-initial'); el.value = v; el.setAttribute('data-default', v); });
    render();
  });
  render();
})();
