/*
 * Number formatting shared by the page generator and the browser calculator — session 5a1bd5be.
 * usd() applies the project rule: every dollar figure in the analysis is rounded to the nearest $10.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.Fmt = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';
  var MINUS = '\u2212';

  function group(n) {
    var s = String(Math.abs(Math.round(n))), out = '';
    while (s.length > 3) { out = ',' + s.slice(-3) + out; s = s.slice(0, -3); }
    return s + out;
  }
  function round10(x) { var s = x < 0 ? -1 : 1; return s * Math.round(Math.abs(x) / 10) * 10 + 0; }

  /** Dollars rounded to the nearest $10. */
  function usd(x) {
    if (x === null || x === undefined || !isFinite(x)) return '';
    var r = round10(x);
    return (r < 0 ? MINUS : '') + '$' + group(r);
  }
  /** Same, with an explicit plus sign for gains. */
  function usdSigned(x) {
    if (x === null || x === undefined || !isFinite(x)) return '';
    var r = round10(x);
    return (r < 0 ? MINUS : r > 0 ? '+' : '') + '$' + group(r);
  }
  /** Exact dollars, for official figures quoted on reference pages (e.g. $1,044,586). */
  function usdExact(x, cents) {
    if (x === null || x === undefined || !isFinite(x)) return '';
    var neg = x < 0, a = Math.abs(x);
    if (cents) {
      var whole = Math.floor(a + 1e-9), c = Math.round((a - whole) * 100);
      if (c === 100) { whole += 1; c = 0; }
      return (neg ? MINUS : '') + '$' + group(whole) + '.' + (c < 10 ? '0' : '') + c;
    }
    return (neg ? MINUS : '') + '$' + group(a);
  }
  /** Millions with one decimal, for chart labels only ($6.9M). */
  function usdM(x) { return (x < 0 ? MINUS : '') + '$' + (Math.abs(x) / 1e6).toFixed(1) + 'M'; }
  function pct(x, digits) {
    if (x === null || x === undefined || !isFinite(x)) return '';
    var d = digits === undefined ? 1 : digits;
    var s = (Math.abs(x) * 100).toFixed(d);
    return (x < 0 && Number(s) !== 0 ? MINUS : '') + s + '%';
  }

  return { usd: usd, usdSigned: usdSigned, usdExact: usdExact, usdM: usdM, pct: pct, round10: round10, MINUS: MINUS };
});
