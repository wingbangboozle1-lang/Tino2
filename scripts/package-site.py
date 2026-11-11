"""Allowlist public output: never ship legacy research or private tax histories.

Privacy check (session f16e6e34, 2026-11-11): this script holds NO household data.
An earlier version stored four private amounts as unsalted SHA-256 hashes. Hashes of 4- and 6-digit
numbers can be reversed by trying every number, so the hashes re-published the amounts; they were
removed. The check is now a rule: any dollar amount of $1,000 or more in the published files must be
a multiple of $10 unless it is an official published figure listed in qa/ledger.json.
The same rule is applied to the pages as rendered by qa/tools/gate.cjs.
"""
from pathlib import Path
import json, re, shutil, sys

root = Path(__file__).resolve().parents[1]
out = root / '_public'
if out.exists():
    shutil.rmtree(out)
out.mkdir()
shutil.copy2(root / 'index.html', out / 'index.html')
(out / 'assets').mkdir()
for name in ['styles.css', 'app.js']:
    shutil.copy2(root / 'assets' / name, out / 'assets' / name)
shutil.copytree(root / 'site', out / 'site')
(out / '.nojekyll').touch()
(out / 'robots.txt').write_text('User-agent: *\nDisallow: /\n')


def official_amounts():
    """Whole-dollar figures that appear in the verification ledger are official and may be exact."""
    allowed = set()
    ledger = root / 'qa' / 'ledger.json'
    if ledger.exists():
        for entry in json.loads(ledger.read_text()):
            for field in ('value', 'evidence', 'notes'):
                for m in re.finditer(r'(?<![\d.])(\d{1,3}(?:,\d{3})+|\d{4,})(?![\d,]*\d)', str(entry.get(field, ''))):
                    allowed.add(int(m.group(1).replace(',', '')))
    return allowed


MONEY = re.compile(r'\$\s?(\d{1,3}(?:,\d{3})+|\d{4,})(?:\.(\d{1,2}))?(?![\d,]*\d)')
allowed = official_amounts()
problems = []
for p in sorted(out.rglob('*')):
    if p.suffix not in ('.html', '.js'):
        continue
    if p.name == 'ledger.js':          # generated from the official ledger itself
        continue
    for m in MONEY.finditer(p.read_text(encoding='utf-8')):
        value = int(m.group(1).replace(',', ''))
        if value >= 1000 and value % 10 != 0 and value not in allowed:
            problems.append(f'{p.relative_to(out)}: {m.group(0)}')
if problems:
    print('FAIL: dollar amounts that are neither rounded to $10 nor official figures:')
    for line in problems[:40]:
        print('  ' + line)
    sys.exit(1)
print('Packaged canonical site only; legacy material excluded. Rounding rule passed (no household data in the check).')
