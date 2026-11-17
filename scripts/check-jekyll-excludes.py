#!/usr/bin/env python3
"""Fail if the legacy Jekyll builder would serve a file the reviewed manifest does not list.

The Actions artifact is built from an explicit manifest, so it can never publish an
unreviewed file. The legacy root Jekyll build does the opposite: it publishes
everything in the repository that _config.yml does not exclude. The two are only
kept honest by one CI step, and that step runs on GitHub, not here -- so a file
added to a directory the config no longer excludes turns the whole public boundary
red with no local signal and no way to see which file did it.

This reproduces the exclusion decision locally, from the same two inputs CI uses
(_config.yml and scripts/public_manifest.py), so the failure is visible before a
merge. It is a gate on the manifest, not a proof of anonymity: a file listed in the
manifest is published whether or not it should be.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from public_manifest import PUBLIC_FILES  # noqa: E402


def excluded_paths():
    """Every entry under any 'exclude:' key in _config.yml, plus Jekyll's own defaults."""
    names = set()
    for line in (ROOT / '_config.yml').read_text(encoding='utf8').splitlines():
        stripped = line.strip()
        if stripped.startswith('exclude:'):
            in_block = True
            continue
        if stripped.startswith('- ') and 'in_block' in dir() and in_block:
            names.add(stripped[2:].strip().strip('"').strip("'"))
            continue
        if stripped and not stripped.startswith('#') and not stripped.startswith('-'):
            in_block = False
    # Jekyll never serves these either, with or without an exclude entry.
    names |= {'_public', '_site', '.cache', '.git', 'node_modules', 'vendor'}
    return names


def jekyll_would_publish():
    """Tracked files the root Jekyll build would copy, approximated from the excludes."""
    excludes = excluded_paths()
    out = []
    for relative in subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True,
                                   text=True, check=True).stdout.split():
        parts = Path(relative).parts
        if parts[0].startswith(('_', '.')):
            continue
        if any('/'.join(parts[:n]) in excludes for n in range(1, len(parts) + 1)):
            continue
        out.append(relative)
    return sorted(out)


def audit():
    """Files Jekyll would serve but the reviewed manifest does not list."""
    expected = set(PUBLIC_FILES)
    return [f for f in jekyll_would_publish() if f not in expected], \
           [f for f in sorted(expected) if not (ROOT / f).is_file()]


if __name__ == '__main__':
    if '--self-test' in sys.argv:
        saved = (ROOT / '_config.yml').read_text(encoding='utf8')
        try:
            (ROOT / '_config.yml').write_text(
                'theme: null\nexclude:\n  - COORDINATION.md\n', encoding='utf8')
            extra, missing = audit()
            assert extra, 'the self-test config must leave an unreviewed file to find'
            print('PASS: an unexcluded file outside the manifest is reported.')
        finally:
            (ROOT / '_config.yml').write_text(saved, encoding='utf8')
        extra, missing = audit()
        assert not extra and not missing, (extra, missing)
        print('PASS: the real configuration publishes nothing outside the manifest.')
    else:
        extra, missing = audit()
        problems = ['Jekyll would publish an unreviewed file: ' + f for f in extra]
        problems += ['Manifest lists a missing file: ' + f for f in missing]
        # A file the manifest lists is reviewed; a file Jekyll serves is not.
        for problem in problems:
            print('::error title=Publication boundary::' + problem)
        if problems:
            raise SystemExit(1)
        count = len(jekyll_would_publish())
        print(f'PASS: every one of the {count} files the Jekyll fallback would serve '
              'is in the reviewed manifest.')
