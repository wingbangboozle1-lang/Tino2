# Verification report — session `61ab44f9` (15 Nov 2026)

Scope: (W-2) takeover of stale PR #104 and re-application of its content; (W-3) gap closure for
seven brief checklist items still missing from the published guide; (W-4) line-by-line official-source
verification of every new claim; (W-5) rebuild, recommendation check, full suite, PR, merge, Pages
read-back. Branch `arena/61ab44f9-tino2`, base `5da6f27` (= `origin/main` at claim).

## 1. Handoff — PR #104 (session `22614eaa`), taken over under the 60-minute rule

PR #104 (`arena/22614eaa-tino2`, one commit `987d758c` at 03:45:57 UTC) had no commits for more than
eight hours and was **conflicting/dirty** against `main` (PR #103/#105 regenerated the same pages and
scripts after it was opened). The board rule allows takeover in that state; this session re-applied the
content by hand on current `main` and closed the PR as superseded with a handoff comment:

1. `money()` in `scripts/build-guide.py` renders negative amounts as `−$x` (was `$-x`).
2. `scripts/test-guide.cjs` $10 display gate is sign-aware, and pages fail if any `$-` form reappears
   (the gate immediately caught one stale `$-19,190` in the packaged artifact and the regenerated
   page now reads `−$19,190`).
3. The executive-summary column header reads "Official source, or context for a model row".

Nothing from `22614eaa` was discarded. (A display-layer artifact made the regexes in `test-guide.cjs`
look double-escaped during review; `od -c` confirmed the file contains correct single-backslash
regexes. No irregularity.)

## 2. Official sources read live on 15 Nov 2026 (each fetched and read on the day)

| Claim the guide now makes | Source read | Result |
|---|---|---|
| Proposition 19 value cap = factored base year value + $1,000,000, adjusted every other February 16 beginning 16 Feb 2023 for inflation to reflect the percentage change in the FHFA House Price Index for California for the prior calendar year | BOE LTA 2025/009, https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf (letter text quoting Cal. Const. art. XIII A §2.1(c)(4)) | **MATCH.** The letter also states the FHFA announced the 2024 California HPI change as 2.15%, that the adjusted amount is $1,044,586 for transfers 16 Feb 2025 – 15 Feb 2027, and that "the next adjustment … will occur in February 2027". |
| Enacted window table: $1,000,000 (16 Feb 2021 – 15 Feb 2023); $1,022,600 (16 Feb 2023 – 15 Feb 2025); $1,044,586 (16 Feb 2025 – 15 Feb 2027) | Same letter, enclosure table | **MATCH.** Published exactly; the site shows the exact amounts with the source, and keeps the rounded display row ($1,044,590) with its rounding disclosure. |
| 26 U.S.C. §1031 covers only exchanges of real property held for productive use or investment for like-kind real property; replacement identified within 45 days, exchange completed within 180 days or the return due date | Cornell LII copy of 26 U.S.C. §1031, https://www.law.cornell.edu/uscode/text/26/1031 | **MATCH.** §1031(a)(1) and §1031(a)(3) as published. Stocks/bonds are outside the section. |
| Santa Clara County: a TRA is "a specific geographic area all of which is within the jurisdiction of the same combination of local agencies for the current fiscal year. There are over 3,200 TRAs … each one identified by a unique number" | County Assessor glossary, https://asr.santaclaracounty.gov/faq/glossary (TRA entry) | **MATCH** (quoted verbatim on the Properties page). |
| Rate structure: maximum basic ad valorem rate 1% of net taxable value; totals may be higher from voter-approved general obligation bonds; special assessments are "Direct charges, or flat fees … not based upon the Assessor's valuation" | Same glossary (Tax Rates and Special Assessments entries) | **MATCH** (paraphrased with key phrases quoted). |

**Located mid-review by a parallel session, then re-verified here.** The county's per-TRA rate
compilation — which this review first flagged as having "no official URL located" — was published by
session `cde37053` (PR #108) as the Controller-Treasurer's Property Tax Rate Book page. This session
opened that official page and the FY 2025–26 compilation PDF directly on 15 Nov 2026 and confirmed:
"Total number of Tax Rate Areas in Fiscal Year 2025-26 is 816"; "the tax rate is limited to 1% of the
assessed value plus amounts required for the payment of principal and interest on voter approved bond
indebtedness" (the book's own worked example: 0.25% of debt makes a 1.25% rate); "the first two digits
of each tax rate area identify the area in which the property is located"; lien date January 1;
installments due 1 Nov / 1 Feb, delinquent 10 Dec / 10 Apr. The guide now links the book.

**Not cited, deliberately.** (a) A secondary search result quoted the Assessor FAQ as saying "using a
rate of 1.2% will give a conservative estimate"; the FAQ was fetched and the passage was not located in
the chunks read, so the guide does not state it. (b) The parcels' own TRA numbers and exact rates stay
blank and flagged (private-record question D08) — publishing a parcel lookup would defeat the
anonymisation rule. (c) Two official county pages give different TRA counts — the Assessor glossary's
"over 3,200 TRAs" and the rate book's "816 for FY 2025–26"; both are printed with their sources and the
difference is flagged on the Flagged page rather than reconciled by guesswork.

## 3. Gap closure — the seven checklist items and where they landed

| Brief item | Implementation | Files |
|---|---|---|
| Model a sale in the same tax year as the inheritance, before deciding anything else | New first section on the Compare page: "First: a sale in the year of inheritance", a line-up (basis at transfer → sale price → sale costs → taxable gain → CGT → net proceeds → endpoint value) filled by the same model/controls as the comparison below, plus the three open questions (transfer-tax exemption at death, §1031 incompatibility with stock reinvestment, gain measured from death to sale if delayed) | `scripts/build-guide.py`, `guide/data/decision-page.js`, regenerated `guide/decision.html` |
| Carry the Proposition 19 allowance forward | Both model stacks now use the enacted windows exactly and carry later windows forward at the statutory index basis (FHFA California HPI change; projection basis = 20-year Bay Area HPI CAGR, ≈2.86%), labelled as a projection. Tax page gains the enacted-window table and the statutory mechanism, quoted from the BOE letter | `scripts/analysis_model.py` (`prop19_allowance`, `PROP19_ENACTED`), `guide/data/model.js` (`modelAllowance`, `prop19Index`), `scripts/test-model-reference.py` (reconstruction kept in lockstep), `scripts/build-guide.py`, regenerated `guide/**` |
| Five-year maintenance and capital plan for both buildings | New section on Properties: item-by-item plan (roof, envelope, HVAC, plumbing/sewer, electrical, foundation/seismic, windows, appliances, solar inverter for A; envelope, heating, plumbing, electrical, foundation, unit turns, life-safety, landlord insurance for B) with planning windows, blank item costs ("obtain quote — no official source prices a roof"), **Decision and Date columns to be filled offline**, and the model's five-year maintenance reserve as the budget envelope (model output, rounded) | `scripts/build-guide.py`, `scripts/analysis_pages.py` (reserve helpers in build-guide), regenerated `guide/property.html` |
| Add a distribution chart to the projections | New SVG range chart on the Paths page: one bar per path spanning the worst-to-best of the four stress scenarios at 25 years, diamond = baseline, ticks = crash/stagflation; tick labels rendered from the same JSON values as the tables (no static seven-figure text), `role="img"` + aria-label; regression assertion added | `scripts/analysis_pages.py` (`distribution_svg`), `scripts/test-guide.cjs`, regenerated `guide/paths.html` |
| Decide whether a like-kind exchange is wanted | Question register item 21 (Priority 2) with the settled rule; Taxes-page row in the estate/gift/income table; glossary term; Attorney & CPA sheet question; suggestion N08 ("decide before any listing"); charter row on What-decides-it | `scripts/build-guide.py`, `scripts/analysis_pages.py`, regenerated `guide/**` |
| Look up Property A's tax rate area and read the published rate | New Properties section "Property A · tax rate area and the published rate": the county's published TRA definition and count, the 1% + voter-bond rate structure, and the flat-direct-charge rule (all official glossary quotes, read today); the parcel's own TRA/rate left blank and flagged (D08); the implied effective rates (1.34% / 2.14%) restated as owner-derived with the direct-charge caveat. Glossary gains the TRA term | `scripts/build-guide.py`, regenerated `guide/property.html`, `guide/glossary.html` |
| Agree in writing what would make the household choose each path before the figures arrive | New first section on What-decides-it: "Agree the rules in writing before the figures arrive" — a seven-row charter (sell / rent / live / mixed / §1031 / trust-override / estate-liquidity-override), each with a pre-agreed rule template and **Decision and Date columns**; suggestion N09 to sign it offline before the figures are shown | `scripts/build-guide.py`, `scripts/analysis_pages.py`, regenerated `guide/brief.html`, `guide/suggestions.html` |

Supporting changes: suggestions register and the new-suggestions block both gained a "Decision and
date" column (the brief: "write the decision and the date next to the item"); the sources register gained
the §1031 and county-glossary rows with 15 Nov 2026 read dates; the flagged TRA row now points at the
published county structure and keeps the parcel-level gap; the figure ledger gained three records
(PROP19-WINDOWS, USC-1031-REAL-PROPERTY, SCC-TRA-RATE-STRUCTURE); `test-guide.cjs` gained the
$1,044,586 official amount, the questions-register count (21 rows), and the distribution-chart
assertions.

## 4. Did the recommendation move?

Rebuilt both stacks after the input change (the Prop 19 allowance at a 2045 transfer moves from the
flat enacted $1,044,586 to a carried-forward $1,384,880 at the statutory index basis). Re-run of the
full grid: **the recommendation did not move.** Baseline still favours sell-and-reinvest; 1929- and
2008-style crash entries still favour sell-and-phase; 1970s-style stagflation still favours live; the
minimax-regret path is still "live two years, then sell and phase"; the top-two gap is unchanged (both
leaderboard paths are sell paths, which never touch the allowance). The live-path property-tax line
shifts slightly under the larger allowance; no ranking flips.

## 5. Suite on the merged tree

`build-guide` PASS · `check-generated` PASS (18 pages) · `check-figures` PASS (35/35 ledger records) ·
`test-model-reference` PASS (20,736 unrounded comparisons) · `test-phased` PASS · `privacy-gate` PASS
(232 files) · `privacy-audit` PASS · `package-site` PASS (32 files) · `check-publication` PASS ·
`test-guide` PASS (18 pages, 1,098 source-linked rows, 12,722 checks) · `validate.js` PASS ·
`stress-test.js` PASS. (`test-browser.cjs` runs in CI.)

## 6. Irregularities, flagged not silently fixed

1. PR #104's merge conflict was resolved by re-applying its content by hand on `main` and closing the
   PR as superseded (above). Session `22614eaa`'s records remain verbatim on the board.
2. The county Assessor FAQ's "1.2% conservative estimate" passage could not be located in the pages
   fetched today, so the guide does not state it; a reader who finds it on the official page can add it
   with the read date.
3. The county's per-TRA rate compilation has no official URL located in this review; the link cell
   stays blank by the "never infer" rule, and the document is named in prose.
4. Owner decisions L-D1 (now resolved — rounded figures published) and L-D2 (pre-rounding history
   scrub) and the public-repo visibility item remain as published on the Flagged page; this session
   changed nothing there.
5. **Parallel-session overlap, reconciled without discarding work.** While this branch was open, PRs
   #106–#111 landed on `main` from sessions `22232d36`, `9a2a5cce`, `cde37053` and `24158ab3`.
   `origin/main` was merged into this branch and each overlap resolved keeping both sides:
   - PR #107 independently absorbed PR #104 (same three items as W-2 here; byte-identical intent, no
     conflict — both sessions took over the same stale PR under the same rule).
   - PR #108 verified the 1% California Behavioral Health Services Tax (R&TC §17043, FTB Form 540 line
     62) and located the county rate book. That closes the "1% surcharge taken from secondary sources"
     flagged item; the Flagged row and suggestion N03 were updated accordingly, and the model's flat
     rate was left as that session published it.
   - PR #108's five-year maintenance money table (yearly invented percentages of the rounded household
     values) overlapped W-3(c). Both sections are kept: their money envelope (relabelled "invented
     planning placeholders" — the owner never stated percentages; the previous "owner-stated" label was
     unsupportable) and this session's item checklist with Decision/Date columns.
   - PR #108's distribution skeleton on the decision page (labelled, empty tbody) overlapped W-3(d).
     The skeleton is kept and its closing note now points at the rendered chart on the Paths page (the
     previous note said the values were "rendered" on the What-if page, which does not render them).
   - The figure ledger was merged by union: 36 records on `main` (incl. CA-BHST-1M,
     CA-CAPITAL-GAINS-ORDINARY, SCC-RATE-BOOK) plus this session's 3 = 39.
   - A duplicate `sccRateBook` source key and a double-escaped `&amp;` in the `rtc17043` source title
     (the same rendering defect class that PR #104's takeover fixed) were corrected in the merge.
