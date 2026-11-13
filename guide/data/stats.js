/* Empirical baselines computed from the published series in qa/series.json.
   Used for the "real economic conditions" section: what 50-year windows in the
   actual record looked like, versus a straight-line projection. */
(function (root) {
  'use strict';

  function annualise(first, last, years) {
    return Math.pow(last / first, 1 / years) - 1;
  }

  /* Rolling 30-year real growth windows for a nominal index deflated by CPI. */
  function windows(series, cpi, window) {
    var out = [];
    for (var i = 0; i + window < series.length; i += 1) {
      var a = series[i], b = series[i + window];
      var ca = cpi[a.year], cb = cpi[b.year];
      if (!a || !b) continue;
      var nominal = annualise(a.value, b.value, window);
      var real = annualise(a.value / ca, b.value / cb, window);
      out.push({ start: a.year, end: b.year, nominal: nominal, real: real });
    }
    return out;
  }

  function stats(values) {
    if (!values.length) return null;
    var s = values.slice().sort(function (a, b) { return a - b; });
    function q(p) { return s[Math.min(s.length - 1, Math.floor(p * (s.length - 1)))]; }
    var mean = s.reduce(function (a, b) { return a + b; }, 0) / s.length;
    var sd = Math.sqrt(s.reduce(function (a, b) { return a + (b - mean) * (b - mean); }, 0) / s.length);
    return {
      n: s.length, min: s[0], p10: q(0.10), median: q(0.5), mean: mean,
      p90: q(0.90), max: s[s.length - 1], sd: sd
    };
  }

  function deflate(rows, cpi, base) {
    var baseCpi = cpi[base];
    return rows.map(function (r) {
      return { year: r.year, real: r.value / (cpi[r.year] || baseCpi) };
    });
  }

  /* Downside runs: worst peak-to-trough fall and longest run without a new high. */
  function drawdown(series) {
    var peak = -Infinity, peakYear = null, worst = 0, worstFrom = null, worstTo = null;
    var lastHigh = null, longest = 0, longestFrom = null;
    series.forEach(function (p) {
      if (p.value >= peak) {
        peak = p.value; peakYear = p.year;
        if (lastHigh !== null) longest = Math.max(longest, p.year - lastHigh);
        lastHigh = p.year;
      }
      var dd = p.value / peak - 1;
      if (dd < worst) { worst = dd; worstFrom = peakYear; worstTo = p.year; }
    });
    var final = series[series.length - 1];
    var yearsSinceHigh = lastHigh === null ? 0 : final.year - lastHigh;
    return {
      worstFall: worst, from: worstFrom, to: worstTo,
      longestFlat: Math.max(longest, yearsSinceHigh), sinceHigh: yearsSinceHigh
    };
  }

  var ECO = {
    annualise: annualise,
    windows: windows,
    stats: stats,
    drawdown: drawdown,
    deflate: deflate
  };

  root.ECO = ECO;
  if (typeof module !== 'undefined' && module.exports) module.exports = ECO;
}(typeof window !== 'undefined' ? window : globalThis));
