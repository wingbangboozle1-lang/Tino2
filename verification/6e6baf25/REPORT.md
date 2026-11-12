# Session 6e6baf25 — integration review, 12 November 2026

## Scope and limits

The pre-existing canonical dashboard was reviewed selectively, not line by line. This session directly opened the official references listed below and checked the statements and URLs on the new Suggestions page against their contents. An official framework link does **not** verify a household amount, assumption, or model output. Historical values are household-provided and unverified; the full historical source ledger and every external link were not freshly reverified. No assurance of anonymity is possible from rounding.

| Source opened | Material checked | Limit |
|---|---|---|
| [California Board of Equalization, Proposition 19](https://www.boe.ca.gov/prop19/) | Parent/child principal-residence conditions, value limit, and claims overview | Future eligibility and allowance are unknown |
| [IRS estate tax](https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax) | Gross estate, deductions, adjusted taxable gifts, unified credit, portability | No family estate documents reviewed; tax cannot be calculated |
| [IRS Topic 703](https://www.irs.gov/taxtopics/tc703) | Basis and adjustments | Does not verify this property's basis |
| [IRS Topic 701](https://www.irs.gov/taxtopics/tc701) | Sale exclusion and ownership/use conditions | Eligibility is not established |
| [California Department of Insurance](https://www.insurance.ca.gov/01-consumers/105-type/5-residential/) | Shop for residential coverage and compare; FAIR Plan gaps | No building-specific premium established |
| [SEC Investor.gov](https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/diversify-your-investments) | Diversification does not guarantee against loss | No forecast or personal recommendation |
| [FDIC deposit insurance FAQ](https://www.fdic.gov/resources/deposit-insurance/faq/) | Deposit coverage and nondeposit investment exclusion | Individual coverage depends on ownership and accounts |
| [SF Rent Board current rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | Current posted rates and proposed, not enacted File 261020 | Does not establish any unit's coverage |
| [GitHub sensitive data removal](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) | History, pull requests, clones, cached copies and removal limitations | Official platform documentation; not a government authority |

A guessed older CDI URL and an older BOE URL led to official not-found pages; neither was added to the site. Correct current URLs are in the table above. Not all existing external links have been checked for live availability. Network policy prevents direct live Pages read-back; GitHub's build and Actions APIs are used for deployment state, not as proof of live content.

## Findings and disposition

- Added a dedicated, review-only suggestions and questions page with explicit private-discovery routes and no collection of user information. No proposed changes to model methodology have been implemented.
- Fixed suggestions-page and footer language that might imply anonymization is assured. Public context and history still create re-identification risk; no history rewrite, repository visibility change or purge was performed.
- Fixed the claim that all strategies were liquidated and taxed identically at the endpoint, and removed a claim that the two sensitivity values bound the actual outcome. The model itself remains unchanged.
- Clarified that living in the San Francisco owner unit is a scenario, not a statement about current occupancy.
- Corrected an oversimplified estate-tax statement in the review register; actual estate tax remains unknown and excluded from strategy projections.
- Flagged that publishing unverified household inputs, even when labeled and rounded, does not meet the strict instruction to leave all unconfirmed values blank. This is not asserted to be resolved.
- Simultaneous session 62b76b9d merged PR #43 while this session was working, overlapping the landing-page scope and adding an on-page suggestions table. Rebase stopped on the shared board; both session blocks were retained. The stash restored the index changes without conflict and preserved that session's table. This page adds a complementary, more detailed review section; no prior work was discarded.

## Checks

Local `validate.js`, `package-site.py`, `check-publication.py --self-test`, `stress-test.js`, `runtime-test.cjs`, `qa/tools/gate.cjs`, and `verification/60ca3e1f/check.cjs` were run. The gate audits rendered rows for HTTPS source links and internal paths; it does not establish that every source supports every claim or that all external links are live. Re-run on the final integrated tree before merging.
