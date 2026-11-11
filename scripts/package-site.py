"""Allowlist public output: never ship legacy research or private tax histories."""
from pathlib import Path
import shutil, re
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
for p in out.rglob('*'):
 if p.suffix in ['.html','.js']:
  text=p.read_text()
  for forbidden in ['550537','550,537','539743','539,743','114248','114,248','7207','7,207']:
   assert not re.search(r'(?<![\d.])'+re.escape(forbidden)+r'(?![\d])', text), f'Private exact amount in {p}'
print('Packaged canonical site only; legacy material excluded.')
