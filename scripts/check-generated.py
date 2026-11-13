#!/usr/bin/env python3
"""Fail if committed HTML differs from the deterministic dashboard generator."""
from pathlib import Path
import subprocess, sys
from public_manifest import PUBLIC_FILES

root=Path(__file__).resolve().parents[1]
pages=sorted(name for name in PUBLIC_FILES if name.endswith('.html'))
before={name:(root/name).read_bytes() if (root/name).is_file() else None for name in pages}
# Regenerate from the model snapshot first, so a stale snapshot cannot hide a
# stale page.
subprocess.run(['node', str(root/'scripts/snapshot.cjs')], cwd=root, check=True)
subprocess.run([sys.executable, str(root/'scripts/build_site.py')], cwd=root, check=True)
changed=[name for name in pages if before[name] != (root/name).read_bytes()]
if changed:
    raise SystemExit('Generated pages were stale; regenerated: '+', '.join(changed))
print(f'PASS: {len(pages)} generated public pages are up to date.')
