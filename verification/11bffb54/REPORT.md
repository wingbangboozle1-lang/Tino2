# Session 11bffb54 — review and re-verification record (2026-11-11)

Repo-only file. It is not part of the published dashboard.

## 1. What was reviewed
- The repository as merged on `main` at `240f255`, plus the stale open PR #16 (`arena/f16e6e34-tino2`), merged into this branch.
- All 13 published pages (`index.html` and `site/*.html`) were rendered and read as text, section by section, against the owner's brief.

## 2. Official pages opened and read by this session
| Fact on the site | Result | Wording found | Official page |
|---|---|---|---|
| Federal basic exclusion $15,000,000 for 2026 | Match | "increasing the basic exclusion amount to $15,000,000 for calendar year 2026" | https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax |
| Federal basic exclusion $15,480,000 for 2027; annual gift exclusion $19,000 (2026), $20,000 (2027) | Match | "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000 ... annual exclusion for gifts increases to $20,000, up from $19,000" | https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts |
| No California estate-tax return for deaths on or after 1 Jan 2005 | Match | "For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return." | https://www.sco.ca.gov/ardtax_estate_tax.html |
| Inherited property: basis is generally fair market value at the date of death | Match | "The fair market value (FMV) of the property on the date of the decedent's death" | https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances |
| Prop 19 amount $1,044,586 for transfers 16 Feb 2025 – 15 Feb 2027; adjusted every other February by the prior calendar year's change in the FHFA California index (2.15% for 2024); next adjustment February 2027 | Match | "the $1 million amount is adjusted to $1,044,586 ... for transfers that occur February 16, 2025 through February 15, 2027" | https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf |
| Prop 19: principal residence of transferor and transferee; homeowners' exemption within 1 year; claim within 3 years or before transfer to a third party; no exclusion for other real property | Match | Comparison chart, "Proposition 19 (Current Law)" column | https://boe.ca.gov/prop19/ |
| San Francisco allowable rent increase 1.6% for 1 Mar 2026 – 28 Feb 2027 | Match (official page text read through a search result, not a direct fetch) | "the annual allowable increase amount effective March 1, 2026 through February 28, 2027 is 1.6%" | https://www.sf.gov/news--annual-rent-increase-3126-22827-announced |

Everything else on the site carries the verification status given to it by the session that added it (see `qa/ledger.json` and the Verified facts page). This session did not re-open those pages and does not claim to have.

## 3. Changes made
1. PR #16 taken over and merged (stale more than 60 minutes; mergeable; all its checks re-run and passing).
2. Household tax and assessment history restored as a table **rounded to $10**, every row marked unverified, on the Verified facts page. The owner's brief asks for these tables to be reported rounded to $10; an earlier session had withheld them. No exact figure is in any tracked file (scan of the working tree: 0 hits).
3. Landing page: cards for Best plan and Verified facts added; official 2027 exclusion stated.
4. Sources page watchlist: the row that said the post-2026 exclusion was unknown now states the published 2027 amount.

## 4. Irregularities (all published on the Flagged for Review page; none blocks the merge)
- **Exact household figures are still readable in the public commit history and in older branch tips.** The repository is public. A commit cannot remove them. Owner decision: make the repository private, or start a fresh repository from the current files, or ask GitHub Support to purge. Branch `arena/5a1bd5be-tino2` holds exact values and was not merged.
- Insurance: no official source gives a premium for either home; both $1,500 figures remain the household's guess. Quotes are needed.
- Property A's tax-rate area and both properties' direct charges are unconfirmed; the post-inheritance tax uses an assumed 1.2% rate.
- The household tax history has repeated yearly amounts for Property A and an unexplained 2018 jump for Property B.
- A direct URL guess for a San Francisco Rent Board page returned "not found"; the figure was confirmed on the official news page instead.
- The repository still holds earlier sessions' parallel dashboards (`pages/`, `dashboard/`, root legacy pages, `docs/`, `src/`). They are excluded from the published site by `_config.yml` and were left in place so no session's work is discarded.

## 5. Checks run on the final tree
See COORDINATION.md, section for session 11bffb54.
