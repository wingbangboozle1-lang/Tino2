# Session a29630ce — verification report (2026-11-13)

**Branch:** `arena/a29630ce-tino2` (from `main` `5f64fb8`, PR #69 merge). Working tree clean at claim; branch in sync with `origin/main`.

**Scope claimed in COORDINATION.md:** `verification/a29630ce/**` only. Line-by-line official-source verification of published rule figures, completeness pass vs. the owner's brief, build/package/boundary/runtime/arithmetic/privacy checks, then PR to `main`, merge, and GitHub Pages confirmation.

## 1. Verification method

Each published rule figure in the public guide was re-opened against the live official page/PDF and compared to the site claim. Unverified household inputs remain blank and flagged; nothing was inferred. All dollar figures in the published artifact are rounded to the nearest $10 (enforced by `scripts/test-guide.cjs`); exact agency amounts are cited with source.

## 2. Official sources re-verified live (13 Nov 2026)

| Guide figure / rule | Site claim | Official source (live) | Result |
|---|---|---|---|
| Federal basic estate exclusion — 2026 deaths | $15,000,000 | IRS IR-2026-133 (Rev. Proc. 2026-35), "Estates of decedents who die during 2027 ... $15,480,000, up from ... $15,000,000 for ... 2026" | MATCH |
| Federal basic estate exclusion — 2027 deaths | $15,480,000 | IRS IR-2026-133 | MATCH |
| Prop 19 intergenerational family-home value allowance | approx. $1,044,590 ($10-rounded) for transfers 16 Feb 2025–15 Feb 2027 | BOE LTA 2025/009: "$1,044,586" for 16 Feb 2025–15 Feb 2027; adjusted every other Feb 16 | MATCH ($1,044,586 rounds to $1,044,590) |
| Prop 19 conditions | transferee must occupy as primary residence within 1 year; file homeowners'/disabled-veterans' exemption within 1 year; BOE-19-P claim within 3 years | BOE Proposition 19 Fact Sheet (pub801.pdf) | MATCH |
| Trust death transfer reporting | trustee/transferee files change-in-ownership statement within 150 days after date of death | California RTC §480(b) | MATCH |
| California estate tax | no California Estate Tax Return required for deaths on/after 1 Jan 2005 | CA State Controller estate-tax page | MATCH |
| SF allowable rent increase | 1.6% for 1 Mar 2026–28 Feb 2027 | SF Rent Board current-rates page | MATCH |
| SF File 261020 | proposed, not enacted as of 9 Nov 2026 notice | SF Rent Board current-rates notice | MATCH |

**Sources not re-opened by this session** (relied on prior-session live verification recorded on the board, e.g. sessions 3938fab9 / c96c185e): IRS inherited-basis guidance, Rev. Rul. 2023-2, IRS home-sale exclusion, IRS rental property (Pub 527), IRS retirement beneficiaries, CA Probate Code §16061.7, Santa Clara County Assessor parent-child guidance, SF Treasurer secured rate, SFPUC water/sewer, City of Cupertino water, PG&E solar billing, CA Department of Insurance premium survey and earthquake guidance, HUD SAFMRs, CBO outlook, BLS CPI, FHFA house-price index, USGS earthquake outlook, SEC diversification guidance, FDIC insured deposits, Congress.gov H.R. 1301, CA Legislature SB 284, GitHub sensitive-data-removal guidance.

## 3. Completeness pass vs. owner's brief

| Requested element | Status | Where it appears in the public guide |
|---|---|---|
| Executive summary of important details | present | `index.html` hero + "Make the decision after the critical facts are known" |
| Dedicated suggestions section; review-before-implement; choose a path before changes | present | `guide/suggestions.html` ("Review before implementation", S01–S15 register with consider/defer/decline) |
| Questions / information / answers to resolve before deciding; discovery routes for missing information | present | `guide/questions.html` (priorities 1–3, "How to discover privately") |
| Personal information anonymized; placeholders only; nothing private on the site | present | placeholders throughout; `guide/review.html` privacy limits; privacy scan clean |
| Cupertino home inherited via trust (~2040–2050); SF home already owned by the inheritor | present | `guide/property.html` (Property A vs Property B roles; B not automatically in estate) |
| Black-swan / real-conditions section over a 50-year horizon | present | `guide/stress.html` (five variable 50-year paths incl. early/late crash, stagflation, disaster) |
| Costs rounded to nearest $10 | present | `guide/data/model.js` `round10`; enforced by tests |
| Live / rent / sell decision analysis with reasoning | present | `guide/decision.html` (equal-endpoint comparison, winner ranking) |
| Step-by-step inheritance / trust process | present | `guide/process.html` (dated checklist with official references) |
| Cost projections: property tax, water, electricity, insurance, maintenance | present | `guide/decision.html` annual tables + `guide/property.html` blank-pending-verification cost rows |
| House value / property tax / assessed value projected by year | present | `guide/decision.html` annual illustration (market, assessment, tax, costs) |
| Inheritance tax thresholds / headroom | present | `guide/tax.html` (2026/2027 exclusions; CA no estate tax; filing test vs. taxable estate); headroom left blank/unverified |
| Law-change watchlist | present | `guide/tax.html` (H.R. 1301, SB 284, SF Prop H, SF File 261020) |
| Sources page; every table row linked to official source or left blank/unverified | present | `guide/sources.html`; tests assert every row has an approved-agency https:// source |

**Privacy note:** The user's stated real property values (e.g. Cupertino 95014, SF 94122 estimates) are household case inputs. Per the privacy instruction they are treated as unverified and are NOT published; the guide uses clearly-labeled fictional example values. Real figures must be confirmed privately and must not be committed.

## 4. Test results (all PASS)

| Check | Result |
|---|---|
| `python3 scripts/package-site.py` | PASS — 18 reviewed guide files packaged; legacy site excluded |
| `python3 scripts/check-publication.py --self-test` | PASS — boundary rejects missing/extra/altered/symlinked/hard-linked files |
| `node scripts/privacy-audit.cjs` | PASS — no distinctive legacy input/history tokens or common identifiers (not proof of anonymity) |
| `node scripts/test-guide.cjs` | PASS — 10 rendered pages, 649 source-linked table rows, 9,061 checks; controls and model invariants verified |
| `python3 scripts/test-model-reference.py` | PASS — 108 decision configurations and 250 stress years independently reconstructed; 10,236 arithmetic comparisons |

## 5. Irregularities / flagged items (do not block merge; published on Flagged for Review page)

- Public repository, history, branches, pull requests and caches can still expose earlier household-derived details from prior legacy material; a Pages exclusion is not access control. Coordinate cleanup with collaborators / GitHub Support.
- Legacy Pages remains in `main`/root Jekyll mode; switching the Pages source to the Actions workflow was denied (HTTP 403). No settings change occurred.
- Privacy scan cannot prove anonymity; official source links verify rules/context only, not private household facts or projections.
- Household-specific values (property values, bills, insurance, rent, trust terms) are blank/unverified; no actual estate-tax headroom can be calculated.

## 6. Next steps

Open a PR from `arena/a29630ce-tino2` to `main`, merge without waiting, confirm GitHub Pages builds and the live site reads back, then record the PR link and merge result in this block of `COORDINATION.md`.
