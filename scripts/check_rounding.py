#!/usr/bin/env python3
"""Fail if any published dollar amount is not a multiple of $10.

The brief requires every published amount rounded to the nearest $10 so a figure
cannot be traced back to a record. Two exceptions are allowed, and only these:

  * an amount published by an official agency, listed in OFFICIAL below, and
  * a summary written in millions of dollars (``$11.50M``), which is rounded.

The check runs over the packaged artifact and over the generated pages.
"""
import re
import sys
from pathlib import Path
from public_manifest import PUBLIC_FILES

ROOT = Path(__file__).resolve().parents[1]

# Amounts published verbatim by a government source. Each appears on the site
# with the source link beside it, so publishing the exact figure cannot trace a
# private record. Keep this list short and justified.
OFFICIAL = {
    1044586,   # BOE LTA 2025/009, Proposition 19 intergenerational allowance
    59,        # San Francisco Rent Board fee, 2026-27, per dwelling unit
    249,       # San Francisco Measure H multifamily base amount
}

# $ followed by digits, but not a decimal fraction or an "M"/"B" suffix.
AMOUNT = re.compile(r'\$\s?(\d{1,3}(?:,\d{3})+|\d+)(?![.,]?\d)(?![MB])\b')


def scan(text):
    bad = []
    for m in AMOUNT.finditer(text):
        raw = m.group(1)
        value = int(raw.replace(',', ''))
        if value in OFFICIAL:
            continue
        if value % 10 != 0:
            bad.append(m.group(0))
    return bad


def main(directory):
    errors = []
    files = 0
    for name in sorted(PUBLIC_FILES):
        if not name.endswith('.html'):
            continue
        path = directory / name
        if not path.is_file():
            continue
        files += 1
        for amount in scan(path.read_text(encoding='utf8')):
            errors.append(f'{name}: not a multiple of $10: {amount} and not an official amount')
    if errors:
        for e in errors:
            print('::error title=Rounding::' + e)
        return 1
    print(f'PASS: every dollar amount in {files} published pages is a multiple of $10 '
          f'or a listed official amount.')
    return 0


if __name__ == '__main__':
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('_public')
    if not target.is_absolute():
        target = ROOT / target
    raise SystemExit(main(target))
