"""Allowlist public output: never ship legacy research or private tax histories."""
from pathlib import Path
import shutil, re, hashlib
root=Path(__file__).resolve().parents[1]
out=root/'_public'
if out.exists(): shutil.rmtree(out)
out.mkdir()
shutil.copy2(root/'index.html',out/'index.html')
(out/'assets').mkdir()
for name in ['styles.css','app.js']: shutil.copy2(root/'assets'/name,out/'assets'/name)
shutil.copytree(root/'site',out/'site')
(out/'.nojekyll').touch()
(out/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
# Exact private amounts are stored only as SHA-256 hashes so this script does not republish them.
FORBIDDEN_HASHES={'39842cd9da3b334e8c1db206f1705d15a9a1f052c0e5b25a148dc4da26cf31f1', '099edec0edb103d87794b711571ef49360169a7aaea268f842e5aa45d59ee0d3', '492053065ed017f42aae8c1f37647cec9d3d2b464f8760bb4ba0373b0309a0ea', 'ee7e99405d3d9c32eefc0fe7cd20207e84027c2e3487c805cbaf5505a8d5f61a'}
for p in out.rglob('*'):
 if p.suffix in ['.html','.js']:
  text=p.read_text()
  for token in re.findall(r'(?<![\d.])\d[\d,]*(?![\d])', text):
   assert hashlib.sha256(token.replace(',','').encode()).hexdigest() not in FORBIDDEN_HASHES, f'Private exact amount in {p}'
print('Packaged canonical site only; legacy material excluded.')
