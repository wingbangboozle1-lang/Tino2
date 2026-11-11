"""Fail closed if the Pages artifact differs from the reviewed publication manifest.

Run after package-site.py. Research/verification/coordination are repository-only.
New public files require an explicit manifest review, not merely a Jekyll exclusion.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / '_public'
ALLOWED = {
    '.nojekyll', 'robots.txt', 'index.html',
    'assets/app.js', 'assets/styles.css',
    'site/black-swan.html', 'site/decision.html', 'site/estate-tax.html',
    'site/inheritance.html', 'site/properties.html', 'site/review.html',
    'site/san-francisco.html', 'site/scenarios.html', 'site/sources.html',
    'site/stress.html', 'site/plan.html', 'site/verification.html',
    'site/operating-costs.html',
    'site/data/ledger.js', 'site/data/history-engine.js', 'site/data/history.js',
    'site/data/model.js', 'site/data/scenarios.js',
    'site/data/sources.js', 'site/data/stress.js', 'site/data/costs.js',
}


def audit(directory):
    errors = []
    files = set()
    if not directory.is_dir():
        return ['Missing _public; run python3 scripts/package-site.py first.']
    for path in directory.rglob('*'):
        relative = path.relative_to(directory).as_posix()
        if path.is_symlink():
            errors.append(f'Symlink forbidden: {relative}')
        elif path.is_file():
            files.add(relative)
            if path.stat().st_nlink > 1:
                errors.append(f'Hard link forbidden: {relative}')
    errors.extend(f'Unexpected public file: {name}' for name in sorted(files - ALLOWED))
    errors.extend(f'Missing public file: {name}' for name in sorted(ALLOWED - files))
    return errors


if __name__ == '__main__':
    if '--self-test' in sys.argv:
        import tempfile
        import shutil
        with tempfile.TemporaryDirectory() as temp:
            fixture = Path(temp) / 'public'
            shutil.copytree(PUBLIC, fixture)
            assert not audit(fixture), audit(fixture)
            marker = fixture / 'verification' / 'INTERNAL.md'
            marker.parent.mkdir()
            marker.write_text('Synthetic non-personal test sentinel')
            assert any('Unexpected' in e for e in audit(fixture))
            marker.unlink()
            marker.symlink_to(fixture / 'index.html')
            assert any('Symlink forbidden' in e for e in audit(fixture))
            marker.unlink()
            (fixture / 'site' / 'decision.html').unlink()
            assert any('Missing public file' in e for e in audit(fixture))
        print('PASS: fail-closed tests reject unlisted files, symlinks and missing pages.')
    target = ROOT / sys.argv[sys.argv.index('--directory') + 1] if '--directory' in sys.argv else PUBLIC
    if '--jekyll' in sys.argv:
        # Jekyll root publication does not synthesize package-only crawler markers.
        ALLOWED.difference_update({'.nojekyll', 'robots.txt'})
        # GitHub Pages' default theme generates this stylesheet (not private input).
        ALLOWED.add('assets/css/style.css')
    errors = audit(target)
    if errors:
        for error in errors:
            # Keep failures readable through the Checks API when runner logs are restricted.
            print('::error title=Publication boundary::' + error)
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(ALLOWED)} reviewed public files only; internal material excluded.')
