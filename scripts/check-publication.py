#!/usr/bin/env python3
"""Fail closed on missing, extra, linked or altered public-artifact files.

The legacy root-based Pages builder is also checked in CI. A manifest check is
not a proof of anonymity and does not protect public repository history.
"""
from pathlib import Path
import sys
from public_manifest import PUBLIC_FILES
ROOT = Path(__file__).resolve().parents[1]


def audit(directory, jekyll=False):
    expected = set(PUBLIC_FILES)
    # GitHub's default Pages theme generates this CSS under the legacy builder.
    expected.add('assets/css/style.css' if jekyll else '.nojekyll')
    if directory.is_symlink() or not directory.is_dir():
        return ['Missing or symlinked output directory']
    files, errors = set(), []
    for p in directory.rglob('*'):
        rel = p.relative_to(directory).as_posix()
        if p.is_symlink():
            errors.append('Symlink forbidden: ' + rel)
        elif p.is_file():
            files.add(rel)
            if p.stat().st_nlink > 1:
                errors.append('Hard link forbidden: ' + rel)
    errors += ['Unexpected public file: ' + x for x in sorted(files-expected)]
    errors += ['Missing public file: ' + x for x in sorted(expected-files)]
    for name in sorted(files & PUBLIC_FILES):
        original = ROOT / name
        if original.is_symlink() or not original.is_file() or (directory/name).read_bytes() != original.read_bytes():
            errors.append('Altered or missing reviewed source: ' + name)
    return errors


if __name__ == '__main__':
    target = ROOT / sys.argv[sys.argv.index('--directory')+1] if '--directory' in sys.argv else ROOT / '_public'
    jekyll = '--jekyll' in sys.argv
    if '--self-test' in sys.argv:
        import os, tempfile, shutil
        if jekyll:
            raise SystemExit('Run --self-test on the packaged artifact, not Jekyll output')
        with tempfile.TemporaryDirectory() as tmp:
            fixture=Path(tmp)/'public'
            shutil.copytree(target,fixture)
            assert not audit(fixture), audit(fixture)
            unexpected=fixture/'private.txt'; unexpected.write_text('synthetic marker')
            assert any('Unexpected' in x for x in audit(fixture)); unexpected.unlink()
            unexpected.symlink_to(fixture/'index.html')
            assert any('Symlink' in x for x in audit(fixture)); unexpected.unlink()
            os.link(fixture/'index.html',unexpected)
            assert any('Hard link' in x for x in audit(fixture)); unexpected.unlink()
            page=fixture/'guide/decision.html'
            original=page.read_bytes(); page.write_bytes(original+b'\n<!-- tamper test -->')
            assert any('Altered' in x for x in audit(fixture)); page.unlink()
            assert any('Missing' in x for x in audit(fixture))
        print('PASS: extra, missing, altered, symlinked and hard-linked files rejected.')
    errors=audit(target,jekyll=jekyll)
    if errors:
        for e in errors:
            print('::error title=Publication boundary::'+e)
        raise SystemExit(1)
    print(f'PASS: publication matches {len(PUBLIC_FILES)} reviewed source files plus build marker.')
