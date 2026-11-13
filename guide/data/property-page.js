/* Year-jump for the projection table. No data leaves the page. */
(function () {
  'use strict';
  var sel = document.getElementById('p-jump');
  if (!sel) return;
  var wrap = sel.closest('.controls');
  var table = wrap && wrap.nextElementSibling;
  if (!table) return;
  function jump() {
    var year = sel.value;
    var rows = table.querySelectorAll('tbody tr');
    for (var i = 0; i < rows.length; i += 1) {
      if (rows[i].firstElementChild.textContent === year) {
        rows[i].scrollIntoView({ block: 'center' });
        rows[i].style.outline = '2px solid #296b50';
        return;
      }
    }
  }
  sel.addEventListener('change', jump);
}());
