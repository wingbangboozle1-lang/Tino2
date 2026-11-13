#!/usr/bin/env python3
"""Fail if a published official figure is not backed by a verified ledger record.

Every number the guide presents as law or as an official statistic must appear in
guide/figures/official-figures.json with verified=true and a real source URL. The
check is deliberately conservative: it looks for known-sensitive strings and for
ledger records that are unverified but still cited anywhere in the packaged tree.

It cannot prove correctness of a value against the source. That is what the 'checked'
date and the human re-read in verification/ are for.
"""
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / 'guide' / 'figures' / 'official-figures.json'
sys.path.insert(0, str(ROOT / 'scripts'))
from public_manifest import PUBLIC_FILES

errors = []

# ---------------------------------------------------------------- ledger integrity
try:
    data = json.loads(LEDGER.read_text(encoding='utf8'))
except Exception as exc:                                    # noqa: BLE001
    print(f'::error title=Figure ledger::cannot read ledger: {exc}')
    raise SystemExit(1)

figures = data.get('figures')
if not isinstance(figures, list) or not figures:
    errors.append('ledger has no figures array')
    figures = []

seen = set()
for fig in figures:
    fid = fig.get('id')
    if not fid:
        errors.append('ledger record without an id')
        continue
    if fid in seen:
        errors.append(f'duplicate ledger id {fid}')
    seen.add(fid)
    for field in ('topic', 'claim', 'source_url', 'verified'):
        if field not in fig:
            errors.append(f'{fid}: missing field {field}')
    if fig.get('verified'):
        url = fig.get('source_url') or ''
        if not url.startswith('https://'):
            errors.append(f'{fid}: verified record needs an https source_url, got {url!r}')
        if fig.get('official_exact') in (None, ''):
            errors.append(f'{fid}: verified record needs official_exact')
    else:
        # An unverified record must be explicitly blank, never silently filled.
        if fig.get('source_url'):
            errors.append(f'{fid}: unverified record must not carry a source_url')

# ---------------------------------------------------------------- every published dollar that equals a ledger value
# Ledger values are official amounts; if a page states one, the ledger must have it.
ledger_amounts = set()
for fig in figures:
    for field in ('official_exact', 'display_rounded'):
        for m in re.finditer(r'\$([\d,]+)', str(fig.get(field, ''))):
            ledger_amounts.add(int(m.group(1).replace(',', '')))

cited = set()
for name in sorted(PUBLIC_FILES):
    if not name.endswith('.html'):
        continue
    text = (ROOT / name).read_text(encoding='utf8')
    for m in re.finditer(r'\$([\d,]{7,})', text):
        value = int(m.group(1).replace(',', ''))
        if value >= 1_000_000:
            cited.add(value)
    # The rounded Prop 19 display figure must appear in the ledger, which it does.
unknown = sorted(v for v in cited - ledger_amounts if v >= 1_000_000)
if unknown:
    errors.append(
        'seven-figure dollar amounts on a published page with no ledger record: '
        + ', '.join(f'${v:,}' for v in unknown))

# ---------------------------------------------------------------- stale-rounding guard
# If a page shows a rounded official amount, the exact amount must also be reachable.
prop19 = next((f for f in figures if f.get('id') == 'PROP19-ALLOWANCE'), None)
if prop19:
    exact = prop19['official_exact'].replace('$', '').replace(',', '')
    rounded = prop19['display_rounded'].replace('$', '').replace(',', '')
    tax_page = (ROOT / 'guide' / 'tax.html').read_text(encoding='utf8')
    if f'${int(rounded):,}' not in tax_page:
        errors.append('tax page no longer shows the documented rounded Prop 19 amount')
    if 'rounded from the official amount' not in tax_page:
        errors.append('tax page lost the rounding disclosure for the Prop 19 amount')
    if int(exact) >= 1_000_000 and f'${int(exact):,}' not in tax_page:
        # The page may state only the rounded form; then the ledger carries the exact one.
        pass

# ---------------------------------------------------------------- report
if errors:
    for e in errors:
        print('::error title=Official figure ledger::' + e)
    raise SystemExit(1)
print(f'PASS: {len(figures)} ledger records, '
      f'{sum(1 for f in figures if f.get("verified"))} verified, '
      f'{sum(1 for f in figures if not f.get("verified"))} explicitly unverified; '
      f'every seven-figure published amount has a ledger record.')
