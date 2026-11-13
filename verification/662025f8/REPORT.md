# Verification report — session `662025f8` (13 November 2026)

Branch `arena/662025f8-tino2`. Scope claimed in `COORDINATION.md` before any work began.

## What this session changed and why

| File | Change | Reason |
|---|---|---|
| `index.html` | Rewritten as a real executive summary | The published landing page had been replaced by a synthetic guide (PR #67), so the site no longer contained the analysis the brief asks for |
| `_config.yml` | `site/`, `assets/app.js`, `assets/styles.css` published; `guide/`, `assets/safe.*` excluded | The Pages boundary must serve the dashboard the landing page links to |
| `scripts/public_manifest.py` | Regenerated to the 33 reviewed dashboard files | The fail-closed boundary audit must match what Jekyll actually publishes |
| `scripts/package-site.py`, `scripts/check-publication.py` | Wording and self-test fixture updated to the new manifest | The self-test referenced a `guide/` page that is no longer published |
| `scripts/test-browser.cjs` | Smoke-test routes repointed from `guide/*` to `site/*` | The old routes no longer exist in the artifact |
| `.github/workflows/pages.yml` | Guide-specific steps replaced by `validate.js`, `stress-test.js`, `runtime-test.cjs`, `gate.cjs`, `privacy_scan.py` | The guide tests assert that the package contains synthetic pages; they would fail against the dashboard |
| `site/review.html` | One new **High** item recording the publication decision | The decision to publish real, rounded figures was an owner call and must be visible on the Flagged page |
| `README.md` | Privacy model, publication decision, structure and verify commands updated | The README described a build that no longer exists |

`guide/`, `assets/safe.*`, `scripts/build-guide.py`, `scripts/test-guide.cjs`, `scripts/test-model-reference.py` and `scripts/privacy-audit.cjs` were **not deleted**. They are retained, unpublished, for audit.

## Sources re-opened directly on 13 November 2026

Every URL below was fetched and read in full during this session; none is carried forward from an earlier session's note.

| Figure | Value | Official source | Result |
|---|---|---|---|
| Federal estate tax — 2026 filing threshold / basic exclusion | $15,000,000 | [IRS, Estate tax](https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax) | Confirmed. The page's own "Filing threshold for year of death" table lists 2026 at $15,000,000 and 2025 at $13,990,000 |
| Federal estate tax — 2027 basic exclusion | $15,480,000 | [IRS IR-2026-133](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) and Rev. Proc. 2026-35 §3.44 | Confirmed: "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from a total of $15,000,000 for estates of decedents who died in 2026" |
| California estate / inheritance tax | None for deaths on or after 1 Jan 2005 | [California State Controller](https://www.sco.ca.gov/ardtax_estate_tax.html) | Confirmed: "For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return" |
| Proposition 19 intergenerational exclusion amount | $1,044,586 | [BOE News Release NR 25-02](https://www.boe.ca.gov/news/2025/nr-25-02.htm) | Confirmed exactly, and the period is confirmed as 16 Feb 2025 – 15 Feb 2027, adjusted every other year off the FHFA California HPI (+2.15% from $1,022,600) |
| Proposition 19 structure and deadlines | Principal residence of transferor *and* transferee; homeowners' exemption within 1 year; claim within 3 years | [BOE Proposition 19](https://www.boe.ca.gov/prop19/) | Confirmed, in the BOE's own comparison table and filing-requirements checklist |
| Proposition 19 and trust-held property | Date of death is the change in ownership; RTC §61(h) | [BOE Proposition 19 FAQ, item 09](https://www.boe.ca.gov/prop19/) | Confirmed verbatim |
| HUD FY2027 SAFMR, ZIP 95014 | 0BR $3,040 · 1BR $3,440 · 2BR $4,050 · 3BR $5,440 · 4BR $5,800 | [HUD FY2027 calculation summary, 95014](https://www.huduser.gov/datasets/fmr/fmr2027/zip-calc?year=2027&zip=95014&cbsasub=METRO41940M41940) | Confirmed. Matches `site/data/model.js` `aRent4BR_2027` = 5800 and `aRent3BR_2027` = 5440. The page also confirms the FY2026 values of $6,390 / $5,870 used as the model baseline |
| HUD FY2027 SAFMR, ZIP 94122 | 0BR $2,370 · 1BR $2,770 · 2BR $3,410 · 3BR $4,460 · 4BR $5,020 | [HUD FY2027 calculation summary, 94122](https://www.huduser.gov/datasets/fmr/fmr2027/zip-calc?year=2027&zip=94122&cbsasub=METRO41860MM7360) | Confirmed. Matches `bRent1BR_2027` = 2770 and `bRent2BR_2027` = 3410 |
| San Francisco adopted secured property tax rate, FY2026–27 | 1.18162182% | [SF Treasurer & Tax Collector, Secured Property Taxes](https://sftreasurer.org/property/secured-property-taxes) | Confirmed: "The secured property tax rate for Fiscal Year 2026-27 is 1.18162182%". Matches `site/data/model.js` `B_RATE` |
| Insurance premiums, Cupertino | Median $1,380 at $500k rebuild, $2,020 at $750k, $2,690 at $1M | [CDI 2026 homeowners premium survey](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111%3A20) | Read in `research/60ca3e1f/insurance-survey-2026.json`; the tool states results are not quotes. Both premiums remain blank and flagged |

### Not confirmed, and left blank or flagged

| Item | Status |
|---|---|
| Property A's tax-rate area and flat direct charges | **Unverified.** The model uses a flat 1.20%, close to the ~1.16% published for the Cupertino city district, but the parcel's TRA is not known. Flagged |
| Rebuild cost of Property A, and therefore the insurance premium | **Unverified.** The household's $1,500 fits a ~$500k rebuild and is below every surveyed insurer at $1M. Flagged |
| Property B's flat direct charges | **Unverified.** Five official flat items total about $829 for three units in FY2025-26; roughly $260 of the latest bill is unexplained. The rate-only projection understates the bill. Flagged |
| Federal exclusion after 2027 | **Modelled at 2%/yr, not official.** Every table row after 2027 is labelled "Modelled, not official" |
| Proposition 19 amount after 15 Feb 2027 | **Not published.** The model applies one step of home-price growth every second 16 February, per BOE LTA 2023/012 and 2025/009 |
| Date of death, gross estate, prior gifts, DSUE, trust terms | **Blank by design.** These are household facts, not public figures. They are the six blocking questions on the landing page and in the decision gate |

## Checks run on the final tree

```
node scripts/validate.js
  PASS: 1559 checks across 18 pages and 178 official sources.
  Base case 2040→2050: sell $7,683,290, rent $6,249,830, live $5,135,780.

node scripts/stress-test.js
  PASS: 50-year paths, estate ownership, privacy, real-dollar and shock tests

python3 scripts/package-site.py
  PASS: packaged 33 reviewed dashboard files; guide/ and legacy trees excluded.

python3 scripts/check-publication.py --self-test
  PASS: extra, missing, altered, symlinked and hard-linked files rejected.
  PASS: publication matches 33 reviewed source files plus build marker.

node scripts/runtime-test.cjs
  PASS: 18 rendered pages; 1578 rendered rows source-linked; no runtime errors or broken local links

node qa/tools/gate.cjs
  PASS: 18 rendered pages · 1578 table rows (1569 with their own official link,
  9 calculated rows with a context link only) · 5059 dollar amounts checked
  (118 official exact figures) · 549 internal and 2070 external links · 0 errors · 0 warnings

python3 integration/tools/privacy_scan.py _public
  0 error(s), 0 warning(s)
```

Every one of the 1578 rendered table rows carries an `https://` link to an official source, or is a calculated value carrying an explicitly labelled context link. Every dollar figure of $1,000 or more on a rendered page is a multiple of $10, with 118 exceptions that are amounts published by a government body and recorded in `qa/ledger.json`.

## Irregularities flagged

1. **High — the re-identification risk is real and unresolved.** Publishing rounded, placeholder-labelled household figures is what the brief asks for, and it adds no new exposure because these files are already in the public repository. It is still not anonymisation. Recorded on the Flagged page and in the README, with the three repository-level remedies.
2. **High — public Git history, branches and pull requests.** Not fixable by any change in this branch. Prior sessions also found the account's primary e-mail address exposed in commit metadata (GitHub e-mail privacy was off); that remains an owner setting.
3. **Medium — legacy Pages mode.** `build_type` is `legacy` (Jekyll from `main`/root), so a direct commit can publish a file without passing CI. The Actions workflow supplied by an earlier session is a fail-closed alternative but needs an administrator to switch the Pages source; an API attempt by session `2ddad241` was refused with HTTP 403.
4. **Medium — the model's Property A tax rate is an assumption.** 1.20% versus roughly 1.16% for the Cupertino city district. Both figures are shown; the parcel's TRA is not confirmed.
5. **Low — the earlier synthetic guide is still in the repository.** `guide/`, `assets/safe.*` and their build and test scripts are retained unpublished. They are not part of the Pages artifact, but they are readable on GitHub.

## Privacy statement

No name, street address, parcel number, account number or e-mail address was added to any published file. The only labels used are Property A and Property B, plus role placeholders. Every figure added to `index.html` is produced by `site/data/model.js` at render time from inputs that were already in the repository and already rounded to the nearest $10; no household number was typed into the new page.
