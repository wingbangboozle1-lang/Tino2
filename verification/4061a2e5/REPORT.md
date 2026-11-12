# Independent final audit — session 4061a2e5

**Audit date:** 12 November 2026 (UTC)  
**Tree audited:** `origin/main` at `052e626e4e126908f2b4c0f069cb6f0a101c81d7`, plus this report  
**Scope:** canonical Pages source (`index.html`, `assets/`, `site/`), model inputs and formulas, rendered rows, publication boundary, privacy controls, and representative official sources. This report contains no names, street addresses, parcel numbers, account identifiers, or trust documents.

## Result

The canonical site is buildable and internally consistent on the audited tree. It already contains the requested executive summary, the Property A / Property B distinction, a step-by-step inheritance plan, decision-readiness registers, a review-before-implementation Suggestions page, a Flagged for Review page, official source links, year-by-year projections, and separate black-swan / recorded-economic-data sections.

No new public-site content was needed from this audit. The issues below remain review items rather than silently filled-in facts. They are not a reason to treat the model as an appraisal, quote, legal opinion, tax return, or investment recommendation.

## Automated checks

All commands were run from the repository root after installing the development-only `jsdom` dependency into the ignored `.cache/test` directory. The dependency is not committed.

| Check | Result | What it covers |
|---|---:|---|
| `node scripts/validate.js` | **PASS** | 1,561 checks; 18 canonical pages; 177 registered source records; model arithmetic, rounding rules, syntax, local links, and source keys |
| `node scripts/stress-test.js` | **PASS** | 50-year paths, ownership distinction, privacy assertions, real-dollar conversion and shock tests |
| `node scripts/runtime-test.cjs` | **PASS** | 18 rendered pages; 1,583 rendered rows; no runtime errors or broken local links |
| `node qa/tools/gate.cjs` | **PASS** | 18 pages; 1,583 rows; 4,985 dollar amounts; 1,574 rows with their own official link and 9 calculated rows with an explicitly labelled framework/context link; 0 errors and 0 warnings |
| `python3 scripts/package-site.py` | **PASS** | Only the canonical dashboard was packaged; legacy material was excluded; publication rounding rule passed |
| `python3 scripts/check-publication.py --self-test` | **PASS** | 34 reviewed public files; fail-closed tests reject unexpected files, symlinks, and missing pages |
| `python3 src/check_links.py .` | **PASS** | 50 repository HTML pages; 879 static table rows; 128 distinct external URLs identified. External availability is not machine-checked by this command |
| Manual privacy scan of the canonical source and packaged artifact | **PASS with existing review items** | No names, home addresses, parcel identifiers, account identifiers, or private documents found in the canonical Pages artifact. Public-history and rounded-context re-identification risks remain as described on the site’s Flagged page |

The repository does not contain the optional `privacy_scan.py` referenced by earlier coordination notes. The manual scan above is therefore recorded rather than reported as a nonexistent automated pass.

## Model and decision audit

### Ownership and inheritance

- **Property A** is the future inherited Cupertino property. Its transfer year is a scenario between 2040 and 2050. The model uses a date-of-death market-value basis proxy and separately models Proposition 19 primary-residence relief.
- **Property B** is the heir’s already-owned San Francisco three-unit property. It is not included in the decedent’s estate model and remains in the background of each Property A strategy. The model does not pretend that the two properties have the same ownership, tax basis, or transfer path.
- The model does not conclude that the estate owes no federal tax: the money and other assets in the estate, prior taxable gifts, debts, deductions, marital/charitable transfers, and DSUE are not supplied.

### Base-case arithmetic

For a 2040 inheritance held for ten years to 2050, the validator reproduces the published rounded results:

| Strategy | Terminal result | Treatment |
|---|---:|---|
| Sell Property A and reinvest | **$7,683,290** | Immediate sale costs; after-tax portfolio-return proxy; Property B retained |
| Rent Property A, then sell | **$6,249,830** | Full reassessment, vacancy and management reserves, positive-NOI tax proxy, later sale |
| Live in Property A, then sell | **$5,135,780** | Partial Proposition 19 relief if eligibility is met; carrying costs; housing service not monetized |

These are nominal scenario outputs, not official values. The ranking is conditional on the model’s assumptions: approximately 3.5% annual home appreciation, 3% operating-cost inflation, 5% after-tax portfolio return, 6% selling cost, unverified insurance allowances, simplified rental taxation, no mortgage, no depreciation/recapture, no estate tax, and no value assigned to the housing received by living in Property A.

Property A’s modeled tax rate after reassessment is an explicitly hypothetical 1.2% combined levy because the actual tax-rate area and direct charges were not supplied. Property B uses the official San Francisco ad valorem rate as a rate input but excludes unknown flat parcel charges and reconciliations. Neither is a property-specific bill.

### Stress and black-swan treatment

The site does not present a single 50-year growth line as a forecast. It provides:

- recorded CPI, interest-rate, equity and FHFA house-price series as historical context;
- twelve named shock/replay cases, including inflation, insurance, earthquake and home-price drawdowns;
- 2,000 seeded five-year-block histories with the limitations and non-probabilistic nature stated on the page; and
- a separate stress laboratory through 2095 where invented shock sizes are labelled hypothetical.

The historical series are metro, county, national, or statewide series as labelled. They are not represented as a Cupertino parcel appraisal or as a probability distribution for the household.

## Official pages re-opened or checked for this audit

Each link is provided for manual review. The source register remains the authoritative mapping used by the site; exact official amounts are retained in the source notes where legal precision matters, while household and model display values are rounded to the nearest $10.

| Topic | Official page | Check |
|---|---|---|
| Federal estate exclusion and annual gift exclusion | [IRS 2027 inflation adjustments](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) | IRS reports a $15,480,000 basic exclusion for deaths in 2027 and a $20,000 annual gift exclusion for 2027; the site keeps later years as assumptions |
| Proposition 19 amount | [California BOE News Release NR 25-02](https://www.boe.ca.gov/news/2025/NR-25-02.htm) and [LTA 2025/009](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) | BOE states the $1,044,586 amount applies from 16 February 2025 through 15 February 2027 and that the next adjustment occurs in February 2027; the future amount is not filled in |
| California estate-tax status | [California State Controller](https://www.sco.ca.gov/ardtax_estate_tax.html) | The Controller states that no California estate-tax return is required for deaths on or after 1 January 2005; this is not treated as a federal-tax exemption |
| Basis of inherited property | [IRS gifts and inheritances FAQ](https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances) and [Revenue Ruling 2023-2](https://www.irs.gov/pub/irs-drop/rr-23-02.pdf) | The general date-of-death FMV basis rule and the trust-estate inclusion caveat are linked; the actual trust terms remain missing |
| California transfer rules | [Revenue and Taxation Code §13301](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=13301) and [§11930](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=11930) | State/local inheritance and death-transfer taxes are not modeled as separate taxes; a later sale is treated separately from the transfer at death |
| HUD rent context | [HUD Small Area FMR dataset](https://www.huduser.gov/portal/datasets/fmr/smallarea/index.html) | HUD describes SAFMRs as ZIP-code benchmarks for the voucher program, not a guaranteed private-market lease rent. FY2027 lookup values are offered as sensitivities, not as confirmed achievable rent |
| California insurance guidance | [California Department of Insurance residential guide](https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/res-ins-guide.cfm) and [premium comparison tool](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111%3A20) | The Department’s survey is for hypothetical profiles and is not a quote; replacement cost, policy type, deductible, vacancy wording, earthquake cover, and multi-unit landlord underwriting still require private quotes |
| FAIR Plan context | [California FAIR Plan key statistics](https://www.cfpnet.com/key-statistics-data/) | Last-resort policy counts and exposure are treated as risk context, not as either property’s premium |
| Long-run economic baseline | [CBO 2026–2036 outlook](https://www.cbo.gov/publication/62105), [CBO data tables](https://www.cbo.gov/system/files/2026-02/61882-By-the-Numbers.pdf), and [Federal Reserve September 2026 SEP](https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm) | Official near-term projections are shown beside, not substituted for, the dashboard’s long-run scenario assumptions |
| San Francisco Measure H | [Ballot Title and Summary](https://media.api.sf.gov/documents/Title_and_Summary_-_Parcel_Tax_to_Fund_Public_Transit_Operations_002.pdf), [economic impact report](https://media.api.sf.gov/documents/MUNI_parcel_tax_economic_impact_final.pdf), and [SF election results](https://www.sfelections.org/results/20261103/index.html) | The site identifies the preliminary result and the parcel-tax terms, but does not model Property B’s amount because building square footage and lease facts are not confirmed |
| San Francisco Rent Board | [Rent Board fee](https://www.sf.gov/rent-board-fee), [current rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit), and [housing inventory](https://www.sf.gov/rent-board-housing-inventory) | $59 per dwelling unit and the owner-unit exemption conditions are cited; the annual exemption window and any future deadline must be rechecked against the current annual notice before relying on it |

## Irregularities and review queue

These are intentionally not silently inferred or filled in:

1. **High — repository-history privacy risk.** The current Pages allowlist excludes coordination logs, research, verification, and legacy pages, but the public Git repository’s earlier branches/commits and pull-request metadata may retain exact household values or a commit e-mail address. A Pages exclusion cannot erase Git history. The existing `site/review.html` and `site/suggestions.html` publish the risk without repeating the sensitive values. Owner action is required if the repository must be made private, archived, or history-scrubbed.
2. **High — household estimates are not official parcel records.** Property values, tax/assessment history, rent, utility midpoints, and insurance allowances are rounded planning inputs supplied by the household. The site labels them as inputs and keeps the strict verification worksheet blank, but a strict policy that every unconfirmed number must be absent would require synthetic examples or a private data layer before publication. No professional should treat rounded inputs as verified.
3. **Medium — the amount beginning 16 February 2027 under Proposition 19 is not yet a published number in the audited source set.** The model’s later values are marked assumptions and must be replaced when BOE publishes the next amount.
4. **Medium — election and local-rule values are time-sensitive.** Measure H and other November 2026 results, rent-board dates, proposed local rules, and HUD FY2027 figures need a recheck before a live transfer, lease increase, filing, or purchase. The site does not book Measure H into Property B without the missing square footage and lease facts.
5. **Medium — insurance remains a blank decision input.** The regulator’s survey narrows the context but cannot quote this primary residence or the three-unit landlord risk. Earthquake cover is separate and is not in the base model.
6. **Medium — property-tax and trust facts remain open.** The actual Santa Clara tax-rate area/direct charges, trust revocability and estate inclusion, title, trustee powers, successor beneficiaries, date-of-death appraisal, and inherited-money inventory are not public and are not inferable from the supplied estimates.
7. **Low — external-link availability.** Internal link checks and source-key checks pass. The static link checker identifies external URLs but does not fetch all of them in this sandbox; official pages should be opened again on the cadence shown on the Sources page.

## Suggested review order

The existing Suggestions page is the review-before-implementation queue. The most decision-efficient order is:

1. keep all private records offline and resolve the repository privacy decision;
2. have counsel confirm trust title, revocability, estate inclusion, trustee powers, and distribution rules;
3. obtain a date-of-death/appraisal workflow, actual tax bills and the Santa Clara tax-rate area;
4. obtain written owner-occupied, landlord, and earthquake insurance quotes plus rebuild-cost estimates;
5. verify the San Francisco units, leases, lawful use, Rent Board inventory/fee exemption, parcel charges, utilities and Measure H square footage;
6. obtain local private-market rent opinions for Property A rather than relying on HUD SAFMRs alone;
7. provide the CPA/attorney with private estate balances, prior gifts, DSUE, basis, deductions and filing history; and
8. rerun the Decision Lab and stress cases using the verified inputs, then choose sell, rent, or live only after the decision gate passes.

No choice stored by the public Suggestions or Questions pages transmits private information or changes the model. Choices are browser-local and require a later, separately verified implementation decision.
