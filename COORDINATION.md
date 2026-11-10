# Coordination — Tino2 Inheritance Decision Analysis

Repo: wingbangboozle1-lang/Tino2
Branch of this session: `arena/7c9c2cc4-tino2` (session ID: `arena-7c9c2cc4`)
Parallel session: `arena/64131d11-tino2` (session ID: `64131d11`) — work merged into `main` via PR #1; this branch merged origin/main on 2026-11-10 and preserved that session's `pages/`, `assets/`, `.nojekyll`, and `research/` files.
Last updated: 2026-11-10

## Privacy rule (highest priority)
No personal information (names, exact addresses, contact info) may appear in the published site. Use placeholders (e.g. [OWNER], [TRUSTEE], [DECEDENT]; "Owner", "Heir", "Property A / Cupertino 95014", "Property B / SF 94122"). Any personal info discovered in research is internal-only and must not appear on the website.

## Number rule
All costs/figures rounded to nearest $10 in decision analysis and projections.

## Rules followed
- All work on branch `arena/7c9c2cc4-tino2`; push only to that branch.
- Every table row carries an official source link or is left blank + flagged as unverified. Never infer or fill in unconfirmed values.
- Merge conflicts resolved without discarding the other session's work; handoffs logged below.

## Task board (combined, both sessions)

| # | Task | Status | Owner session | Files touched | Notes |
|---|------|--------|---------------|---------------|-------|
| 1 | COORDINATION.md setup (shared task board) | done | arena-7c9c2cc4 | COORDINATION.md | Unified board after merging origin/main |
| 2 | Research: Federal estate/inheritance tax (IRS, 2026 exemption, step-up basis) | done | 64131d11 | research/federal-tax.md | IRS.gov, Congress.gov |
| 2b | Research: federal estate/inheritance tax thresholds (IRS) | done | arena-7c9c2cc4 | docs/federal-estate-tax.md | IRS Form 706 instr., Rev. Proc. 2025-32 ($15M, OBBBA permanent) |
| 3 | Research: CA property tax — Prop 13, Prop 19, inheritance reassessment | done | 64131d11 | research/ca-property-tax.md | boe.ca.gov, ftb.ca.gov, county assessors |
| 3b | Research: Prop 13 & Prop 19 parent-child transfer rules | done | arena-7c9c2cc4 | docs/prop13-prop19.md | boe.ca.gov/prop19 ($1,044,586 cap 2025–2027) |
| 4 | Research: CA estate/inheritance tax (CA FTB/BOE) | done | arena-7c9c2cc4 | docs/california-tax.md | ftb.ca.gov (no CA estate/inheritance tax) |
| 5 | Research: Cupertino 95014 + SF 94122 property data, insurance, utilities | done | 64131d11 | research/properties.md | county assessor/recorder, insurer data, SJWC, SFPUC |
| 5b | Research: Santa Clara County / Cupertino property tax rates | done | arena-7c9c2cc4 | docs/cupertino-tax.md | ~1.25–1.34% effective on assessed value |
| 5c | Research: San Francisco property tax rates | done | arena-7c9c2cc4 | docs/sf-tax.md | ~1.18–1.22% effective |
| 6 | Research: homeowners insurance CA (primary + rental) | done | arena-7c9c2cc4 | docs/insurance.md | insurance.ca.gov; ZIP-level quotes flagged unverified |
| 7 | Research: water & electricity costs (San Jose Water, PG&E) | done | arena-7c9c2cc4 | docs/utilities.md | sjwater.com, pge.com |
| 8 | Research: Alternatives — rent vs sell & reinvest projections | done | 64131d11 | research/alternatives.md | flagged if not official |
| 8b | Data model & projections: Cupertino house | done | arena-7c9c2cc4 | docs/cupertino-model.md | projections flagged as assumptions (3%/yr appreciation) |
| 8c | Data model & projections: SF house | done | arena-7c9c2cc4 | docs/sf-model.md | 3 units, $7,150/mo rent |
| 9 | Decision analysis: live / rent / sell | done | arena-7c9c2cc4 | docs/decision-analysis.md | rounded to nearest $10 |
| 9b | Alternatives — rent vs sell & reinvest projections | done | 64131d11 | research/alternatives.md | market data, flagged if not official |
| 10 | Step-by-step inheritance (trust) process | done | arena-7c9c2cc4 | docs/inheritance-process.md | CA Probate Code, BOE, IRS, FTB |
| 10b | Inheritance process page | done | 64131d11 | pages/inheritance-process.html | step-by-step trust workflow |
| 11 | Executive summary | done | arena-7c9c2cc4 | docs/executive-summary.md | anonymized, placeholder PII |
| 11b | Executive summary page | done | 64131d11 | index.html (their landing) | key findings incl. 4%/yr appreciation projection |
| 12 | Build GitHub Pages site (landing + subpages, dashboard UI, tables w/ sources) | done | both | this branch: *.html, css/style.css; main: pages/*, assets/*, .nojekyll | Two dashboard layouts coexist; root index.html is this session's landing page |
| 13 | Verification pass: every table row has official source link or flagged unverified | done | arena-7c9c2cc4 | docs/flagged.md; both sites' flagged pages | Blank + flag where no official source |
| 14 | GitHub Pages deploy, PR to main, merge, confirm Pages deploy, record result | done | arena-7c9c2cc4 | COORDINATION.md | PR #2 https://github.com/wingbangboozle1-lang/Tino2/pull/2 MERGED (commit ddb1692); Pages build ddb1692 status built, no errors; live https://wingbangboozle1-lang.github.io/Tino2/ |

## Merge log
- 2026-11-10: Session 64131d11 created board; repo was empty (README only). Research done; site built (index.html + pages/{tax-laws,properties,inheritance-process,projections,decision-analysis,flagged}.html + assets/style.css + .nojekyll). Figures rounded to nearest $10. Irregularities flagged: Property B 2018 tax +18.4% vs +2% assessment; Property A 2026 tax blank in source data; 2045 Prop 19 cap unknown; rental estimate for Property A unverified; insurance/maintenance are averages/assumptions.
- 2026-11-10: Session arena-7c9c2cc4 built a parallel root-level dashboard (index.html, cupertino.html, san-francisco.html, inheritance.html, taxes.html, decision.html, flagged.html, sources.html + css/style.css + docs/*).
- 2026-11-10: Merged origin/main into arena/7c9c2cc4-tino2. Conflicts in COORDINATION.md and index.html resolved without discarding session 64131d11's work: their pages/, assets/, .nojekyll, research/ files retained; root index.html kept from this session.
- 2026-11-10: PR #2 (https://github.com/wingbangboozle1-lang/Tino2/pull/2) arena/7c9c2cc4-tino2 -> main: MERGED via `gh pr merge 2 --merge` (merge commit ddb1692). GitHub Pages (sourced from main) build ddb1692 status: built, no errors. Live site: https://wingbangboozle1-lang.github.io/Tino2/ . Verified live: cupertino.html, san-francisco.html, inheritance.html, taxes.html, decision.html, flagged.html, sources.html all serve this session's content. Root index.html edge-cache may briefly show the prior session's landing page; origin/main:index.html verified as this session's file.

## Notes on overlapping content
- Both sessions produced dashboards with similar structure but different projection assumptions (session 64131d11: 4%/yr appreciation, Property A ≈ $6,530,000 by 2045; session arena-7c9c2cc4: 3%/yr appreciation, ≈ $5,435,870 by 2045). Both are flagged as assumptions, not official figures. Integration verification should confirm both flagged pages list these discrepancies.
