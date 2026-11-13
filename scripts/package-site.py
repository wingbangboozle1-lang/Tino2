#!/usr/bin/env python3
"""Package only explicitly reviewed public files. Never add household records."""
from pathlib import Path
import shutil
from public_manifest import PUBLIC_FILES

root = Path(__file__).resolve().parents[1]
out = root / '_public'
if out.is_symlink():
    raise SystemExit('Refusing a symlinked output directory')
if out.exists():
    shutil.rmtree(out)
out.mkdir()
for relative in sorted(PUBLIC_FILES):
    parts = Path(relative).parts
    src = root / relative
    if (not parts or Path(relative).is_absolute() or '..' in parts
            or any((root.joinpath(*parts[:n])).is_symlink() for n in range(1, len(parts)+1))
            or not src.is_file() or not src.resolve().is_relative_to(root)
            or src.stat().st_nlink > 1):
        raise SystemExit(f'Missing or unsafe publication source: {relative}')
    dst = out / relative
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
# This marker exists only inside the explicit artifact, never at repository root.
(out / '.nojekyll').touch()
print(f'PASS: packaged {len(PUBLIC_FILES)} reviewed guide files; legacy site excluded.')
