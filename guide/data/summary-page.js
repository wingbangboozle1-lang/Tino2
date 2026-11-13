/* Summary page: fills the live headline cards from the model so the front page
   can never drift from the decision page. No data leaves the browser. */
(function () {
  'use strict';
  var M = window.MODEL;
  if (!M) return;
  var sellCard = document.getElementById('sum-sell-live');
  var bootEl = document.getElementById('boot-rent');
  var rentCard = document.getElementById('sum-rent');
  var liveCard = document.getElementById('sum-live');
  var be = document.getElementById('sum-breakeven');
  if (!sellCard) return;
  var r = M.compare(2045, 20, {});
  sellCard.textContent = M.fmtMoney(r.rows.sell.terminal);
  rentCard.textContent = M.fmtMoney(r.rows.rent.terminal);
  liveCard.textContent = M.fmtMoney(r.rows.live.terminalTotal);
  if (be) {
    var b = M.breakEven(2045, 20, 'rent', {});
    be.textContent = b.rate === null ? b.note : M.fmtPct(b.rate);
  }
}());
