# Coordination — Tino2 Inheritance Decision Project

Session scope: single agent session on branch `arena/1dab34fa-tino2`. Session ID: `session-arena`.

Task board format: each row = task, status (unclaimed / in progress / done / needs review), owning session ID, files touched, sources verified (Y/N), irregularities.

| # | Task | Status | Owner | Files touched | Sources verified | Irregularities |
|---|------|--------|-------|---------------|------------------|----------------|
| 1 | Create coordination board | done | session-arena | COORDINATION.md | N/A | None |
| 2 | Research: Santa Clara County / Cupertino property tax, Prop 13 base-year assessment, Prop 19 parent-child transfer rules | done | session-arena | docs/research/01-cupertino-property-tax.md | Y | Prop 19 inflation-adjusted cap figure ($1,044,586) comes from secondary sources citing BOE Letter to Assessors 2025/009 — confirm against BOE at transfer time |
| 3 | Research: San Francisco property tax, assessment, rental property tax treatment | done | session-arena | docs/research/02-sf-property-tax.md | Y | None |
| 4 | Research: homeowners insurance costs Cupertino 95014 (primary residence) and SF 94122 (rental/investment property) | done | session-arena | docs/research/03-insurance-costs.md | Partial | CA-specific figures from commercial quote aggregators; official CA data are statewide averages only (CDI, NAIC) |
| 5 | Research: water (San Jose Water / SFPUC) and electricity (PG&E solar NEM) costs | done | session-arena | docs/research/04-utilities.md | Y | Solar profit claim ($10-20/mo) is user-provided, not externally confirmed; NBT export credits are ~3.9 cents/kWh |
| 6 | Research: federal estate tax exemption + California estate/inheritance tax, inheritance law changes pending | done | session-arena | docs/research/05-inheritance-tax.md | Y | IRS confirms $15M for 2026; "permanent vs sunset 2034" claims conflict across secondary sources — IRS page is the authority |
| 7 | Research: step-up in basis (IRC 1014), capital gains on sale of inherited home, primary-residence exclusion, rental income tax | done | session-arena | docs/research/06-basis-capital-gains.md | Y | None |
| 8 | Build decision model: projections of value, property tax, repairs, utilities, insurance, rent vs live vs sell | done | session-arena | docs/projections.md | — | Assumptions clearly labeled; verified items cited |
| 9 | Build executive summary (anonymized, placeholders for personal information) | done | session-arena | docs/executive-summary.md | — | — |
| 10 | Create GitHub Pages site: clean landing page + category subpages, dashboard-style tables, every row with source link or blank+unverified flag | done | session-arena | index.html, pages/*, assets/*, site config | — | — |
| 11 | Verify every table row against official source; flag unverified items | done | session-arena | pages/flagged-review.html | — | All unverified cells flagged; external source links included per row |
| 12 | Enable GitHub Pages, confirm build/deploy with no broken links | in progress | session-arena | GitHub Pages settings (repo) | — | PR to main pending |
| 13 | Create PR from integration branch to main, summarize changes/sources/irregularities; merge; record PR link and merge result | unclaimed | session-arena | (GitHub PR) | — | — |

Rules followed: single session claims all tasks; scopes non-overlapping; small frequent commits; `git pull --rebase` before every push; unverified values left blank and flagged; personal information anonymized with placeholders; costs rounded to nearest $10.
