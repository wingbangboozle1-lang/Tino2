# Verification report — session `dff8604e` (15 Nov 2026)

Scope: resolve owner decision **L-D1** (publish the household figures rounded to $10 under the
owner's anonymisation rule), replace round-number assumptions with ranges or official survey
figures, re-anchor both model stacks to the household inputs, and re-verify every official claim
touched. Branch `arena/dff8604e-tino2`, base `9ecdc55` (= `origin/main` at claim).

## 1. Publication policy applied (owner brief, restated 15 Nov 2026)

| Rule | Implementation | Enforced by |
|---|---|---|
| Costs and numbers used, rounded to nearest $10 | All household figures rounded (`550,540`, `7,210`, `114,250`, `2,440`, `7,150`, ranges `$100–$150`, `$330–$400`, `$30–$70`, `+$10–$20`); market estimates `3,100,000` / `1,800,000` as supplied | `scripts/test-guide.cjs` $10 gate |
| Exact government amounts may appear exactly | CDI survey outputs, FTB thresholds, Prop H schedule, Prop 19 allowance (rounded display + disclosure) | `OFFICIAL_AMOUNTS` allowlist in `test-guide.cjs` |
| Identifiers replaced by placeholders | `Property A` / `Property B` only; no name, address, ZIP code, parcel, account or document number anywhere in the artifact | `scripts/privacy-audit.cjs` (email, street, ZIP scans) |
| Raw pre-rounding values never committed/published | The 39 raw tokens that rounding changes are hard-banned; values equal to their rounded form (e.g. `493530`, `6130`, `1740`) are allowed by definition | `scripts/privacy-audit.cjs` (`RAW_BANNED`) |
| Anything researched about the household's actual records stays internal | No assessor/parcel/listing lookup is performed or cited anywhere | this report; `analysis_pages.py` docstring |

Residual risk (published on the Flagged page): a rounded financial history attached to an area can
still narrow candidates. The owner's rule explicitly accepts rounding as the anonymisation method.

## 2. Figures published and their provenance

| Figure | Value published | Provenance | Verification |
|---|---|---|---|
| Property A/B market estimates | $3,100,000 / $1,800,000 | Owner brief, Nov 2026 estimates | Owner-stated; appraisal at transfer still required (flagged) |
| A assessment/tax history 2014–2026 | rounded table | Owner brief tables | Owner-stated; each row links the county verification route (flagged) |
| B assessment/tax history 2016–2025 | rounded table | Owner brief tables | Owner-stated; same treatment |
| A utilities | $100–$150 water; +$10–$20 solar credit | Owner brief ranges | Owner-stated ranges (midpoints used in models) |
| B utilities | $330–$400 water; $30–$70 electricity | Owner brief ranges | Owner-stated ranges (midpoints used in models) |
| Insurance benchmarks | Cupertino 40y: $1,543 / $2,690 / $6,430 (70y: $1,598 / $2,741 / $4,968); SF-Sunset 40y: $1,328 / $3,353 / $10,384 (70y: $1,413 / $3,191 / $10,384) | California Department of Insurance premium-comparison survey (effective 1 May 2026) | Captured from the CDI tool on 12 Nov 2026 by session `60ca3e1f` (`research/60ca3e1f/insurance-survey-2026.json`, profile URLs recorded). Not a quote (the survey says so). B row is the wrong product for a 3-unit building — flagged proxy |
| Rent benchmarks | HUD small-area FMR: 3BR $5,870 · 4BR $6,390 (FY2026) | HUD small-area FMR data | Verified against HUD's official page on 13 Nov 2026 by session `662025f8` (`verification/662025f8/REPORT.md`). Voucher benchmark, not a rent quote |
| Implied tax rates | A ≈ 1.34%, B ≈ 2.14% (bill ÷ assessed value) | Derived from owner tables | Arithmetic self-consistent; bill includes flat direct charges — caveat published on the Flagged page |

## 3. Official claims re-read live on 15 Nov 2026

| Claim | Source re-read | Result |
|---|---|---|
| Prop 19 value limit: family home capped at current taxable value plus $1,000,000 (biennially adjusted) | https://www.boe.ca.gov/prop19/ (comparison chart, read 15 Nov 2026) | **MATCH.** The model formula now implements the published limit: new base = `min(market, max(factored base, market − allowance))`, matching `guide/data/model.js` and the tax page's own wording ("the excess is added to the factored value") |
| Prop 19 filing periods: homeowners' exemption claim within 1 year of transfer; exclusion claim within 3 years or before transfer to a third party | https://www.boe.ca.gov/prop19/ (filing-period row, read 15 Nov 2026) | **MATCH.** Flagged item "claim periods not confirmed" resolved; periods now on the Timeline and the Attorney & CPA sheet |
| Federal basic exclusion amount 2026 = $15,000,000 | IRS Instructions for Form 706 (07/2026), https://www.irs.gov/instructions/i706 | **MATCH** (What's New: "The basic exclusion amount is $15,000,000") |
| Federal filing threshold 2026 = $15,000,000 | IRS estate-tax FAQ (updated 22 Dec 2025), https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-estate-taxes | **MATCH** (2026 filing threshold table). Flagged ledger-label conflict resolved: both labels verified |
| 2027 basic exclusion = $15,480,000 | IRS IR-2026-133 (verified 14 Nov 2026, ledger) | Not re-read today; unchanged on the site |

## 4. Model change and its verification

* **Prop 19 formula fix** in `scripts/analysis_model.py` (`simulate` and `annual_table`): the old
  `min(fmv, factored + allowance)` overstates the new base when `fmv < factored + allowance` and
  understates it otherwise. Replaced with `min(fmv, max(factored, fmv − allowance))`, which is the
  BOE value limit as published and the formula `guide/data/model.js` (and `test-guide.cjs`) already
  enforce. Independent arithmetic reconstruction (`test-model-reference.py`, 20,736 unrounded
  comparisons) passes after the fix.
* **Household inputs** replace the illustrative inputs in `guide/data/model.js` and
  `scripts/analysis_pages.py`; all formulas unchanged otherwise. Scenario knobs (growth 3.5%,
  portfolio 5% net, expense inflation 3%, vacancy 7%, management 8.5%, maintenance 0.75%/1.25%,
  sale cost 5.5%, flat tax scenarios) remain labelled assumptions and are exposed to the what-if
  controls where material.

## 5. Checks run on the final tree (all PASS)

| Check | Result |
|---|---|
| `scripts/check-generated.py` | PASS — 17 generated pages up to date |
| `scripts/check-figures.py` | PASS — 28 ledger records, 28 verified |
| `scripts/test-model-reference.py` | PASS — 108 configurations / 250 stress years / 1,500 staged years / 20,736 comparisons |
| `scripts/package-site.py` + `check-publication.py --self-test` | PASS — 31 reviewed files |
| `scripts/test-guide.cjs` | PASS — 17 rendered pages, 966 source-linked rows, 11,844 checks (controls, model invariants, $10 gate, row sources) |
| `scripts/privacy-audit.cjs` | PASS — no raw pre-rounding token, ZIP code or identifier; scanner tokeniser fixed (digit/letter adjacency) after it mis-split "$2,179,680" into a false raw match |
| `scripts/validate.js`, `scripts/stress-test.js` | PASS — retained dashboard still verified |
| `scripts/test-phased.py` | PASS — 113 checks |
| `scripts/test-browser.cjs` | Not runnable in this sandbox (bundled Chromium lacks system libs, exit 127); runs in CI on `ubuntu-latest` as before |

## 6. Irregularities and unverified items (all published on the Flagged page)

1. **L-D2 / history exposure (Critical).** Earlier commits, branches and PRs contain unrounded
   household figures. Not rewritten here: requires force-rewriting `main` and 70+ stale branches
   (outside this session's push scope; destructive to other sessions' records) and cannot erase
   clones/caches. Six-step administrator runbook published on the Flagged page.
2. **Residual re-identification risk** of rounded figures attached to an area — disclosed and
   accepted under the owner's own rule.
3. **Implied tax rates** include flat direct charges (slight overstatement on reassessed values) —
   flagged; TRA rate verification route published.
4. **Insurance**: CDI survey is not a quote; one-million-dollar cover may be below rebuild need; B's
   row is the wrong product (3-unit building) — flagged proxy.
5. **HUD rents**: voucher benchmarks, not quotes.
6. **CA 1% Mental Health Services Tax** above $1,000,000 and CA ordinary-income treatment of
   capital gains remain unverified on official FTB text — sensitivity values only (carried).
7. **Form 706 payment rule and Form 4768 period** — left blank (carried).
8. **Form 1041 due date** — not confirmed from IRS text; left off the timeline (carried).
9. **Prop H amount for B** — depends on non-public parcel facts; left unverified (carried).
10. **Trust facts** (terms, title, basis inclusion, occupancy intent, marital status, estate size)
    — unknown; the questions register and readiness verdict carry them (carried).

## 7. Sources (official, for manual review)

BOE Prop 19 · https://www.boe.ca.gov/prop19/ · BOE LTA 2025/009 · https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf
IRS Form 706 instructions · https://www.irs.gov/instructions/i706 · IRS estate-tax FAQ ·
https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-estate-taxes
CA Department of Insurance premium survey · https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/
HUD small-area FMR · https://www.huduser.gov/portal/datasets/fmr/smallarea/index.html
Santa Clara County Property Tax · https://www.santaclaracountyca.org/Property_Tax.html
SF Treasurer · https://sftreasurer.org/property/secured-property-taxes · SF Rent Board · https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit
(All 34+ guide source links are listed on the site's Sources page.)
