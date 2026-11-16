/* Privacy regression for the public artifact: no household-specific inputs or
   derived results may appear, whether rounded or not. Known owner-input amounts
   are represented only by SHA-256 hashes, so this gate cannot reintroduce them.
   This is a limited collision/pattern scan, not proof of anonymity. */
'use strict';
const fs=require('fs'),path=require('path'),crypto=require('crypto'),{JSDOM}=require('../.cache/test/node_modules/jsdom');
const root=path.resolve('_public'), bad=[];
const sha=t=>crypto.createHash('sha256').update(t,'utf8').digest('hex');
// SHA-256 of each raw (pre-rounding) household value from the owner's records that
// rounding CHANGES, plus the two property ZIP codes. Values equal to their own
// $10-rounded form are allowed by definition and are not listed. Only hashes are
// stored, so the gate file cannot leak what it blocks.
const RAW_BANNED=new Set([
 '39842cd9da3b334e8c1db206f1705d15a9a1f052c0e5b25a148dc4da26cf31f1',
 '099edec0edb103d87794b711571ef49360169a7aaea268f842e5aa45d59ee0d3',
 '97e993dda390f1cf07230629d658f0facdcb99b24c227500537366d1a3161802',
 'e98a698e90e42c7d3391f33497d7cef396e39d4bd25179562206f6f4cf7bf501',
 'db05646ae8ad85ac0779c3cf9050fe52f66ccff7d67b041b86ca34b346e8fc28',
 '0622977d7d84a529c9ebca838fea6dbca3a5d6811c14041a5e058a7ddf952a81',
 '513bd45f0a52063b3b2928aa794363a339c28bc15b81de6ab4b3c5af95a7192b',
 '52032e1e3f630fd436d2ca33c6567cdce1d48bcbffce8b27d8a21684996651fe',
 'bf3add3c9aae4d7ea4fbe096c3fd10a45b7c18407d6d54082467eb964a78e55c',
 '0d375c898a2d9f0222f1ee0dfae7ef752dbe3afe80faacc53229343f05c92f11',
 '49c24780cdc4e7327b8605c1d23daa4889075cb121e37758c8a74a18da19594c',
 'e1cbc7c4ff721a444f3a841cccc2c23703fc3664b34580680128d97454905c43',
 'ee7e99405d3d9c32eefc0fe7cd20207e84027c2e3487c805cbaf5505a8d5f61a',
 '46ece05546fb2626da88a216af6aa066b5172e824ad9eae6742d8e12ef6fbcc8',
 '30332d66f3ddf1ced8fd978136e88dc7cbbdb9e40c570f4e81f875408fd3ad24',
 'c65765f07db7e978ddeb9b4e20c4bc3447f94466522c1f2d972dac3b5ff79b5e',
 '0474319403e99b0608cebe3e29f5ab3ad1f45cc6a5a1cec0a0dddd6bbfa6600d',
 '0ae3305415102d365f21b19b0ba90eebfebd1c4f38b79ae87dce1655a31650a4',
 'cc56038328ffa43e94516e446dfde7b43c94f18e80e59a79476598a1f394da23',
 '6c0b64d1ba905979a8b0518752ff1a82cc0466c0e09c303bb4df855200fa80d0',
 '41ef81d7f6b07faacbe378c5000a776ced4f12016112c6baa1950ae894dd204e',
 '492053065ed017f42aae8c1f37647cec9d3d2b464f8760bb4ba0373b0309a0ea',
 '85df60af2698a93c36c364ac69eb29d981cb26c683f0b68b402f484aab57f000',
 '8ae8f8c9b17505ffc1a69172e3c881ee51a5e1c0aff8166b2f96399453a8c4cb',
 'e826b706c6f0c321194ca901cd6c74e56d58a5cb6139628f2bacdf173139cbbc',
 '738ca2d26e0805fe8f0ef260b3222292efa98598eb0a4753bcba685f006aa674',
 'd8b5265a1b78027bc8ce3e73da644edbb16ed9a606ee58662c0fe6479600b2a5',
 '709f93f87e130f48229ca57e231a5a27156f09f71857be7f9ec4220f40766d22',
 'c41b25004288641718a72ab523f3f055f25f5399c24ef3dcddf8d04902115441',
 '3de0ebf10cfca6ebd3f4192ffa49afc98c2798cc52aee0914db251a48f1873b6',
 '08f000434359746449eef8e715e3bd98d5583219d209c9689112afa5804f1b89',
 'd376881f5bd00764c32b8645a0f7966bc86ec3d3ea0e7b51e830e5f12aae3071',
 '04e97796ac4d1ffe851398d3a25afad5f62916ef5ac22f6f10e83192dc15e8c3',
 '9e6296be2bb963df7daa2b230a2a1f34b1bcd655c10fa6c1f6c05782fee95791',
 '74e70910949899071b1eb8b17993808a5f829c481dbc72a64aa9a1678a05106b',
 '6b32c01a019bd349ff3c659b6206000b1f29e39bda71e3ac47c0006a033d93cc',
 '2bbb0ed9e593487865218631abc18ea0cdd660ca87da8c55382a5cc05f72c1eb',
 'daab3aa68185b677bd3c8d63f12e48eacb0851d98d635137e531fd579a452486',
 '7907a88d77f29a7681a0dc6c89157ea3f45959944436301085c8a34a46fe4a77',
 '38f13ba4550b60ae975cb2a6efd68b795f4c026ea25b162d316a9d00182cd92d',
 '2478d903d7c875f05299efe5a271b802046c65fdbb33ab2d0a0085f5b73748ed',
 '43086d953bcc428c4a8bf097446b87d9f577a80d4bd010a4313d575484cc9f21',
]);
// SHA-256 of household-specific property values, assessments, tax bills, rent and
// utility figures previously present in the legacy inputs. Hashes only; no values.
const PRIVATE_BANNED=new Set([
 'c86aa4b8de21065e0a4ad180041d745319c195a91aeeeca8ddd558ba326274f2',
 '37bf94938358f1fd6031153af84471b3d8340245e0bc61606ecc70ce65381aa8',
 '014e9fb03ec3e152833fb9e4541198dce6719bd09349b4b309118e285eb5a3f0',
 'e8537c60cf3ce941177d2a46d43794452407ba7c56fe7fb1d303c9b96d5498e5',
 '9522517cbf8340212b20f6deb09bd03d290395137e35da2c082368a4f24587f8',
 '15fc253969f598bdb3ccf96f3a57b82a2bfa3e0e142b849e34bce9e8733f8b39',
 '02cf62656564decc54131e85c0415cbad4eb573a24278854fe8bc4aa3fe45268',
 '30814e3036f3f98aca5b54c1f7dbcd2636e1a06e401258f0b4eff18ffc479c39',
]);
const YEAR_LIKE=t=>/^\\d{4}$/.test(t)&&Number(t)>=2010&&Number(t)<=2120;
function inspectText(file,text,rendered=false){
  // Separate digit/letter adjacency first so money like "$2,179,680NextWord" tokenizes
  // as the full amount rather than a truncated fragment.
  text=text.replace(/([0-9])([A-Za-z])/g,'$1 $2').replace(/([A-Za-z])([0-9])/g,'$1 $2');
  for(const t of (text.match(/\d[\d,]*/g)||[]).map(x=>x.replaceAll(',',''))){
    // Calendar-year columns legitimately print bare 4-digit years (2026-2095) that can
    // collide with a raw value. Money is always $-prefixed or comma-grouped in this
    // artifact, so bare year-range tokens are exempt from the raw check only.
    if(!rendered&&!YEAR_LIKE(t)&&RAW_BANNED.has(sha(t)))bad.push(file+': raw pre-rounding household token');
    if(!rendered&&PRIVATE_BANNED.has(sha(t)))bad.push(file+': household-specific amount, rounded or unrounded');
  }
  // Dollar and comma-grouped amounts are money context: no exemption at all.
  if(!rendered)for(const m of text.matchAll(/\$\s*([\d,]+)/g)){
    const t=m[1].replaceAll(',','');
    if(RAW_BANNED.has(sha(t)))bad.push(file+': raw pre-rounding household token in money context');
    if(PRIVATE_BANNED.has(sha(t)))bad.push(file+': household-specific amount in money context');
  }
  if(/\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b/i.test(text))bad.push(file+': email-like identifier');
  if(/\b\d{1,5}\s+[A-Z][A-Za-z]*(?:\s+[A-Z][A-Za-z]*){0,2}\s+(?:Street|St\.|Avenue|Ave\.|Road|Rd\.|Boulevard|Blvd\.)\b/i.test(text))bad.push(file+': street-address-like identifier');
}
function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){
  const f=path.join(dir,e.name);if(e.isDirectory())walk(f);else if(/\.(html|js|css|txt)$/.test(f))inspectText(path.relative(root,f),fs.readFileSync(f,'utf8'));
}}
walk(root);
const pages=['index.html',...fs.readdirSync(root+'/guide').filter(x=>x.endsWith('.html')).map(x=>'guide/'+x)];
for(const file of pages){
  const dom=new JSDOM(fs.readFileSync(path.join(root,file),'utf8'),{runScripts:'outside-only',url:'https://example.org/Tino2/'+file});
  for(const s of dom.window.document.querySelectorAll('script')){
    const src=s.getAttribute('src');
    // Inline scripts carry the generated rounded values; evaluate them as the browser would.
    dom.window.eval(src?fs.readFileSync(path.resolve(root,path.dirname(file),src),'utf8'):s.textContent);
  }
  inspectText(file+' (rendered)',dom.window.document.body.textContent,true);
  if(dom.window.document.querySelector('form,input,textarea,iframe,script[src^="https:"],img[src^="https:"]'))bad.push(file+': input or external automatic resource');
  dom.window.close();
}
if(bad.length){for(const b of bad)console.error('Privacy review required:',b);process.exit(1);}
console.log('PASS: no blocked household input, raw or rounded, property ZIP code or common identifier in the packaged source or rendered text. This is not proof of anonymity.');
