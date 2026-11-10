# COORDINATION.md — Shared Task Board

Repo: wingbangboozle1-lang/Tino2 — Branch: `arena/64131d11-tino2`
Session ID: `64131d11` (arena/64131d11-tino2)

## Privacy rule (highest priority)
No personal information (names, exact addresses, contact info) may appear in the
published site. Use placeholders (e.g., "Owner", "Heir", "Property A / Cupertino 95014").
Any personal info discovered in research is internal-only.

## Number rule
All costs/figures rounded to nearest $10 in decision analysis and projections.

## Task board
| Task | Status | Owner session | Files touched | Notes |
|---|---|---|---|---|
| Research: Federal estate/inheritance tax (IRS, 2026 exemption, step-up basis) | done | 64131d11 | research/federal-tax.md | IRS.gov, Congress.gov sources |
| Research: CA property tax — Prop 13, Prop 19, inheritance reassessment | done | 64131d11 | research/ca-property-tax.md | boe.ca.gov, ftb.ca.gov, county assessors |
| Research: Cupertino 95014 + SF 94122 property data, insurance, utilities | done | 64131d11 | research/properties.md | county assessor/recorder, insurer data |
| Research: Alternatives — rent vs sell & reinvest projections | done | 64131d11 | research/alternatives.md | market data, flagged if not official |
| Build GitHub Pages site (landing + subpages, dashboard UI, tables w/ sources) | done | — | index.html, pages/*, assets/* | — |
| Verification pass: every table row has official source link or flagged unverified | done | — | all pages, flagged-for-review.html | — |
| Integration: PR to main, merge, confirm Pages deploy, record PR link | in progress | — | COORDINATION.md | — |

## Log
- 2026-11-10: Board created by session 64131d11. Repo was empty (README only).

- 2026-11-10: Research tasks done by 64131d11. Sources: IRS (Rev. Proc. 2025-32, Pubs 523/527/551, estate tax FAQ, newsroom WFTC), CA BOE (Prop 19 FAQ + Fact Sheet pub801, LTA 2025/023, change-in-ownership FAQ), CA FTB, CA Courts self-help, CPUC (NEM 3.0), CA DOI/NAIC, SJWC tariffs, SFPUC Prop 218 notice, SF Assessor-Recorder transfer tax, RTC §63.2/§11911 via leginfo, Damodaran/NYU (market return assumption, flagged).
- 2026-11-10: Site built: index.html + pages/{tax-laws,properties,inheritance-process,projections,decision-analysis,flagged}.html + assets/style.css + .nojekyll. All analysis figures rounded to nearest $10. Verification: every law/rate row carries an official source link; user-provided values and assumptions are on the Flagged for Review page.
- 2026-11-10: Irregularities flagged: Property B 2018 tax +18.4% vs +2% assessment (possible new levy/correction); Property A 2026 tax blank in source data (projected at 1.33%); 2045 Prop 19 cap unknown (used published $1,044,586); rental estimate for Property A unverified; insurance/maintenance are averages/assumptions.
