(function(){
  var D = window.WHATIF_DATA; if (!D) return;
  var ids = ['wi-scenario','wi-horizon','wi-phase','wi-cash','wi-mu'];
  var els = ids.map(function(i){ return document.getElementById(i); });
  if (els.some(function(e){ return !e; })) return;
  function fmt(v){ if (v === null || v === undefined) return '—'; var s = Math.abs(v).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ','); return (v < 0 ? '−$' : '$') + s; }
  function refresh(){
    var key = els.map(function(e){ return e.value; }).join('|');
    var row = D[key];
    if (!row) return;
    document.querySelectorAll('[data-wi-path]').forEach(function(cell){
      cell.textContent = fmt(row[cell.getAttribute('data-wi-path')]);
    });
    var best = Object.keys(row).reduce(function(a,b){ return row[a] >= row[b] ? a : b; });
    var st = document.getElementById('wi-status');
    var lb = document.querySelector('[data-wi-label="' + best + '"]');
    if (st) st.textContent = 'Highest total under these controls: ' + (lb ? lb.textContent : best) + '. Illustrative example inputs; not a forecast.';
  }
  els.forEach(function(e){ e.addEventListener('change', refresh); });
  refresh();
})();
