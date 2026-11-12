const assert = require('node:assert/strict');
const fs = require('node:fs');
const {JSDOM} = require('../../.cache/test/node_modules/jsdom');
const doc = new JSDOM(fs.readFileSync('index.html', 'utf8')).window.document;
assert.match(doc.querySelector('#recommendation-title').textContent, /Base-case leader/);
assert.match(doc.querySelector('#recommendation-copy').parentElement.textContent, /No estate-tax allocation/);
const rows = [...doc.querySelectorAll('#suggestions tbody tr')];
assert.equal(rows.length, 4);
for (const row of rows) {
  assert.equal(row.cells.length, 5);
  assert.match(row.cells[4].querySelector('a').href, /^https:\/\//);
  assert.ok(row.cells[3].textContent.length > 30);
}
assert.match(doc.querySelector('#suggestions').textContent, /not approved changes/);
console.log('PASS: conditional recommendation, estate-tax caveat, four source-linked review-gated suggestions');
