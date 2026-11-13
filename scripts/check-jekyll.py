#!/usr/bin/env python3
"""Check that the legacy Jekyll publication still matches the reviewed manifest.

GitHub Pages serves this repository from main/root through Jekyll. Jekyll only
removes what `_config.yml` excludes, so this script simulates that removal and
then applies the same byte-for-byte audit the packaged artifact gets.

If a reviewed file would be excluded by `_config.yml`, or an unreviewed file
would be published, this fails.
"""
import shutil
import sys
import tempfile
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name, filename):
    spec = spec_from_file_location(name, ROOT / 'scripts' / filename)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def excluded_paths():
    out, inside = set(), False
    for line in (ROOT / '_config.yml').read_text().splitlines():
        if line.startswith('exclude:'):
            inside = True
            continue
        if inside and line.startswith('  - '):
            out.add(line[4:].strip())
        elif inside and line and not line.startswith(' '):
            inside = False
    return out


def main():
    audit = load('check_publication', 'check-publication.py').audit
    public = load('public_manifest', 'public_manifest.py').PUBLIC_FILES
    excluded = excluded_paths()

    missing = [n for n in sorted(public)
               if any(n == e or n.startswith(e + '/') for e in excluded)]
    if missing:
        for n in missing:
            print('::error title=Jekyll exclusion::required file is excluded: ' + n)
        return 1

    # Jekyll serves everything in the repository root that it does not exclude,
    # so check the real tree rather than the allowlist alone.
    def hidden(rel):
        # Jekyll drops dotfiles and dot-directories at any depth.
        return any(part.startswith('.') for part in rel.parts)

    published = {rel.as_posix() for rel in
                 (p.relative_to(ROOT) for p in ROOT.rglob('*'))
                 if (ROOT / rel).is_file() and not hidden(rel)
                 and not any(rel.as_posix() == e
                             or rel.as_posix().startswith(e + '/')
                             for e in excluded)}
    unexpected = sorted(published - set(public))
    if unexpected:
        for n in unexpected:
            print('::error title=Jekyll output::unreviewed file would be '
                  'published: ' + n)
        return 1

    with tempfile.TemporaryDirectory() as tmp:
        jek = Path(tmp) / 'out'
        for name in sorted(public):
            dst = jek / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, dst)
        errors = audit(jek, jekyll=True)
    if errors:
        for e in errors:
            print('::error title=Jekyll output::' + e)
        return 1
    print(f'PASS: the legacy Jekyll output would publish exactly the {len(public)} '
          'reviewed files.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
