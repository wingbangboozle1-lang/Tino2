# Session 76e91231 — repository review

**Scope:** the tracked tree and the published artifact on `main` at `5f64fb8`, reviewed 13 November 2026.
**Rule applied:** this report describes *where* sensitive material is and *what kind* it is. It deliberately does not reproduce any household value, name, address or identifier. Counts and file paths only.

---

## 1. What is published right now

| Check | Result | Evidence |
|---|---|---|
| Published artifact contents | 18 reviewed files + build marker, matching `scripts/public_manifest.py` exactly | `python3 scripts/package-site.py`, `python3 scripts/check-publication.py --self-test` — PASS |
| Rendered pages | 10 pages, 649 source-linked rows, 9,061 structural checks | `node scripts/test-guide.cjs` — PASS |
| Model arithmetic | 108 selector combinations, 250 stress years, 10,236 unrounded comparisons against an independent Python reconstruction | `python3 scripts/test-model-reference.py` — PASS |
| Legacy household tokens in the **packaged** artifact | none detected | `node scripts/privacy-audit.cjs` — PASS |
| Pages deployment | `status: built`, source `main` / root, `build_type: legacy`, HTTPS enforced | GitHub Pages API, 13 Nov 2026 |

The public site itself is a clean, clearly labelled synthetic guide. That part is working as designed and this session did not weaken it.

## 2. The open exposure is the repository, not the website

GitHub Pages serves only the manifest. **GitHub itself serves every tracked file at `raw.githubusercontent.com`, and every historical commit and branch remains fetchable.** The privacy boundary in `_config.yml` and the packager does not apply to those paths.

I enumerated the tracked files that contain values transcribed from the owner's brief (property-tax history, assessed-value history, property values, rent, and related figures) by exact string match against the amounts supplied in the brief and the legacy model:

| File | Kind of material | Reachable as |
|---|---|---|
| `site/data/model.js` | household-derived baseline inputs and both assessment histories | raw + Pages-disabled path + Git history |
| `site/verification.html` | rendered households assessment history in a table | raw + Git history |
| `site/properties.html`, `site/san-francisco.html` | household property value and rent figures | raw + Git history |
| `verification/c96c185e/REPORT.md` | property-tax and assessed-value amounts quoted in a verification narrative | raw + Git history |
| `verification/0d6ec51e/options.json` | several assessment and value amounts | raw + Git history |
| `verification/d9c69069/REPORT.md` | value and rent amounts | raw + Git history |
| `verification/3938fab9/audit_math.py` | a household value used as a test constant | raw + Git history |
| `scripts/validate.js`, `scripts/stress-test.js` | the same values used as test fixtures | raw + Git history |
| `research/60ca3e1f/*` | a few amount strings that coincide with official published figures; **not** household-specific on inspection | low risk, but see note |

**Note on the research files.** The strings matched in `research/60ca3e1f/` are coincidental collisions with official published amounts (they appear inside a survey script and its JSON output). They are listed for completeness, not because they expose a household fact. Every other row above is material transcribed from the owner's brief.

**Total: 13 tracked files contain at least one distinctive household-derived value.** All 13 are excluded from the Pages artifact, and none is linked from the public guide. None of this is fixed by the `robots.txt`, the `noindex` meta, or the Jekyll `exclude` list.

## 3. Why rounding did not solve it

The brief asks for values rounded to the nearest $10 so they cannot be traced. Rounding to $10 does not remove a thirteen-year assessment series: a two-percent compounding sequence is a fingerprint. Anyone who has the county roll, or who simply guesses the county, can match a 13-row sequence exactly. **The site's own claim that rounding is not anonymization is correct, and it is the reason the public guide replaced those figures with invented ones.** The remaining task is the repository copy, which is a deletion and history problem, not a formatting problem.

## 4. Recommended remediation, in order

| # | Action | Who can do it | Effect | Risk if skipped |
|---|---|---|---|---|
| R1 | Stop publishing case-specific values in any future commit. Put real figures in an offline file outside the repository. | Anyone committing | Prevents new exposure | Re-creates the incident |
| R2 | Remove the household values from the 13 tracked files, replacing them with clearly labelled synthetic constants. Use `git rm` for reports that quote them, keeping a private offline copy. | Repository owner | Removes them from the current tree | Values stay fetchable at HEAD |
| R3 | Purge the values from **history** (`git filter-repo` or BFG) and force-push, or follow GitHub's sensitive-data-removal process | Repository owner / GitHub Support | Removes them from older commits and branches | Values stay fetchable at every old commit |
| R4 | Ask GitHub Support to purge cached views and PR refs; check forks and clones | GitHub Support, owner | Reduces copies outside the owner's control | Copies persist indefinitely |
| R5 | Treat any previously published value as **already disclosed** in the threat model | Owner | Prevents false comfort | A later decision is made on a false assumption of secrecy |

Actions R2–R5 require repository-owner or GitHub Support authority. A session such as this one cannot rewrite shared history without discarding other sessions' work, and the brief forbids discarding it. This session therefore **did not** delete or rewrite anything. R2 was outside what could be done safely here because the same commit history is shared by many session branches; the integration note is in `COORDINATION.md`.

## 5. Irregularities found by this session

| # | Severity | Finding | Handling |
|---|---|---|---|
| I-1 | Critical | Household-derived values remain in 13 tracked files in a public repository; every one is fetchable at HEAD and in history. Pages exclusion does not cover this. | Reported here and on the Flagged page. Not fixable by this session. |
| I-2 | High | `_config.yml` uses a **denylist**. Any future root file not listed is published by the legacy Jekyll build, and in `legacy` mode the CI audit is not a deployment gate. | Documented; README records that an administrator must switch Pages to GitHub Actions for a fail-closed boundary. |
| I-3 | Medium | PR #63 has been idle for more than 8 hours. Under the 60-minute rule it is takeover-eligible, but its content is a superseded bookkeeping record. | Left untouched; logged in `COORDINATION.md`. |
| I-4 | Medium | `guide/tax.html` displayed the Prop 19 allowance as `$1,044,590` while the official published amount is `$1,044,586`. The rounding is disclosed, but a reader matching against the BOE letter will not find the displayed number. | Now carries an explicit "rounded from the official amount" note plus the exact figure in the ledger and on the Sources page. |
| I-5 | Low | The site used a **seasonally adjusted** CPI series where an annual-average published series is the normal comparison basis, which shifts the historical mean slightly. | The new real-conditions page uses the unadjusted annual-average series and states the basis. |
| I-6 | Low | `site/**` legacy pages are reachable at `main`-root paths that the guide 404s only because Jekyll excludes them. A future `_config.yml` edit silently republishes them. | Documented in I-2. |

## 6. What was re-verified line by line on 13 Nov 2026

Every rule figure the public guide publishes was re-opened at its official source. The machine-readable result is `guide/figures/official-figures.json`; the build refuses to package a figure whose `verified` flag is false and whose ID is cited on a page. Verified this session:

IRS estate-tax exclusion 2026 and 2027 and the filing test; California Controller's no-estate-tax and no-inheritance-tax positions; inherited FMV basis and the alternate-valuation condition; the $250,000/$500,000 home-sale exclusion and its ownership/use tests; BOE LTA 2025/009 Prop 19 allowance and the two prior periods; Prop 19 occupancy, exemption-timing and claim-deadline rules; Prop 13's 2% cap and decline-in-value mechanics; BOE LTA 2026/002's 2026-27 factor and full 51-year factor history; the San Francisco 2026-27 secured rate; the SF Rent Board 1.6% increase and the File 261020 not-enacted notice; RTC §480(b)'s 150-day trust-transfer rule; Probate Code §16061.7(f)'s 60-day notice; H.R. 1301 and SB 284 status; the BLS December 2022 CPI release; CBO publication 61882; USGS Fact Sheet 2016-3020; Freddie Mac PMMS; and the City of Cupertino's three-provider water structure.

One item could **not** be verified from an official source and is left unverified and unpublished as a rate: the Santa Clara County documentary transfer tax. See `SCCTRANSFER-TAX` in the ledger.
