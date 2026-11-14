#!/usr/bin/env python3
"""Verify every file in the public review boundary exists as a readable file.

The public artifact is the hand-authored decision dashboard under site/ (plus the
root landing page and its assets). It is not produced by build-guide.py, so this
check replaces the old "committed HTML matches the generator" comparison with a
manifest-existence check. package-site.py performs the real packaging validation.
"""
from pathlib import Path
import sys
from public_manifest import PUBLIC_FILES

root = Path(__file__).resolve().parents[1]
errors = []
for relative in sorted(PUBLIC_FILES):
    parts = Path(relative).parts
    src = root / relative
    unsafe = (
        not parts
        or Path(relative).is_absolute()
        or '..' in parts
        or any((root.joinpath(*parts[:n])).is_symlink() for n in range(1, len(parts) + 1))
        or not src.is_file()
        or not src.resolve().is_relative_to(root)
        or src.stat().st_nlink > 1
    )
    if unsafe:
        errors.append(f'Missing or unsafe publication source: {relative}')
    elif src.stat().st_size == 0:
        errors.append(f'Empty publication source: {relative}')

if errors:
    for e in errors:
        print('::error title=Publication boundary::' + e)
    raise SystemExit(1)
print(f'PASS: {len(PUBLIC_FILES)} reviewed public boundary sources are present.')
