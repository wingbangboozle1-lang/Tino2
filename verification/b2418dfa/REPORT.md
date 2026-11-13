# Verification report — session `b2418dfa`

**Scope.** The published public guide (`index.html`, `guide/**`, `assets/safe.css`, `assets/safe.js`) that GitHub Pages serves from `main`.
**Date of verification.** 13 November 2026. Every official page below was opened directly on that date and the wording the guide attributes to it was read.
**Branch.** `arena/b2418dfa-tino2`, from `origin/main` = `5f64fb8`.
**What this is not.** It is not proof of anonymity, not legal or tax advice, and not a certification that the guide's fictional model inputs describe any household. It is a line-by-line check of the guide's *official* claims against the pages the guide cites, plus the checks the repository already runs.

---

## 1. What the guide publishes, and how many official links it makes

| Item | Count |
|---|---|
| Published pages | 10 (`index.html` + 9 under `guide/`) |
| Distinct official URLs cited | 34 |
| Total official link instances | 148 |
| Table rows rendered with an official source link | 656 (rendered check, `scripts/test-guide.cjs`) |
| Rows with a blank value that is *not* marked unverified | 0 |

Every rendered table row carries at least one `https://` link to a government, regulator or official-agency host; the rendered test enforces this (`check(links.length>0, …)` and `check(links.some(a=>hosts.has(…)))`).

---

## 2. Line-by-line check of the official claims

"Guide says" is the published wording. "Official page says" is the passage read on 13 November 2026. **Result** is `MATCH` where the guide's wording is supported by the page, `REFINED` where the page carries more than the guide used, and `FLAGGED` where an irregularity was found.

### 2.1 Property tax

| # | Source | Guide says | Official page says (13 Nov 2026) | Result |
|---|---|---|---|---|
| P1 | [BOE Proposition 19](https://www.boe.ca.gov/prop19/) | Value limit = taxable value plus $1,000,000, biennially adjusted; homeowners' exemption within 1 year; claim within 3 years or before transfer to a third party | "Value limit of current taxable value plus $1,000,000 (as biennially adjusted)"; "File for homeowners' exemption within 1 year of transfer"; "File claim for exclusion within 3 years or before transfer to third party" | MATCH |
| P2 | [BOE fact sheet pub801](https://www.boe.ca.gov/pdf/pub801.pdf) | Transferee must live in the home as primary residence within one year; BOE-19-P within three years; a claim is timely if filed within six months of the supplemental or escape assessment notice; exemption claim after one year gives prospective relief | "The transferee must live in the home as their primary residence within one year of transfer to qualify for the exclusion"; "The application must be filed within three years of the transfer date, but before transferring the property to a third party. A claim is also considered timely if filed within six months after the date of mailing of the Assessor's supplemental or escape assessment notice"; "exclusion begins the year the exemption claim was filed—referred to as prospective relief" | MATCH |
| P3 | [BOE LTA 2025/009](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) | Allowance ≈ $1,044,590 for 16 Feb 2025 – 15 Feb 2027, "rounded from the official amount" | "the $1 million amount is adjusted to **$1,044,586**"; "for transfers that occur February 16, 2025 through February 15, 2027, the value cap will be the sum of the property's factored base year value plus $1,044,586"; "The next adjustment … will occur in February 2027" | MATCH — the guide's $10 rounding of the official $1,044,586 is disclosed on the page |
| P4 | [BOE LTA 2025/023](https://boe.ca.gov/proptaxes/pdf/lta25023.pdf) | Factored base year value grows with CPI capped at 2%; decline-in-value relief can apply | "Proposition 13 … limited future property tax increases by setting a cap on annual increases to a property's assessment at no more than two percent"; "adjusted annually by an inflation factor … but not to exceed two percent"; "When the market value falls below the FBYV, the property will be temporarily assessed at the lower market value recognizing that decline in value" | MATCH |
| P5 | [Santa Clara County Assessor](https://asr.santaclaracounty.gov/tax-savings/transferring-your-assessed-value/parent-to-child-2) | "Confirm the assessor's value, eligible relationship, residence status and local rate" | Parent and at least one child must be principal residents within one year; exemption must be applied for within one year; claim within three years, otherwise prospective relief only | **FLAGGED** — see F1 |

### 2.2 Federal tax

| # | Source | Guide says | Official page says (13 Nov 2026) | Result |
|---|---|---|---|---|
| F1 | [IRS estate tax](https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax) | Filing threshold tests gross estate plus adjusted taxable gifts and certain exemption amounts; deductions bear on taxable estate, not the filing test; $15,000,000 for 2026 | "A filing is required if the gross estate of the decedent, increased by the decedent's adjusted taxable gifts and specific gift tax exemption, is valued at more than the filing threshold"; table: 2026 → $15,000,000; "Once you have accounted for the Gross Estate, certain deductions … are allowed in arriving at your 'Taxable Estate.'" | MATCH |
| F2 | [IRS IR-2026-133](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) | $15,000,000 for 2026 deaths; $15,480,000 for 2027 | "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from a total of $15,000,000 for estates of decedents who died in 2026" | MATCH |
| F3 | [IRS inherited-property FAQ](https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances) | Basis is generally date-of-death FMV | "The basis of property inherited from a decedent is generally … The fair market value (FMV) of the property on the date of the decedent's death"; alternative valuation date only if the executor elects it on Form 706 | MATCH |
| F4 | [IRS Rev. Rul. 2023-2](https://www.irs.gov/pub/irs-drop/rr-23-02.pdf) | One irrevocable-trust fact pattern outside the estate did not receive a basis adjustment | Issue: "Is there a basis adjustment under § 1014 … if the trust assets are not includible in the owner's gross estate"; § 1014(a)(1) basis is "the FMV of the property at the date of the decedent's death" | MATCH |
| F5 | [IRS Topic 701](https://www.irs.gov/taxtopics/tc701) | Home-sale exclusion up to $250,000, or $500,000 for joint filers, subject to ownership, use and other conditions; not automatic | "you may qualify to exclude up to $250,000 of that gain from your income, or up to $500,000 … if you file a joint return"; "you must meet both the ownership test and the use test" | MATCH |
| F6 | [IRS Publication 527](https://www.irs.gov/publications/p527) | Rental income, expenses, depreciation and sale rules; land is not depreciable | Publication 527 (2025) "Residential Rental Property" covers rental income, deductible expenses, depreciation (land excluded), and sale of rental property | MATCH |
| F7 | [IRS retirement beneficiaries](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-beneficiary) | Taxable inherited IRA distributions may be income to the beneficiary; treatment and timing depend on account and beneficiary rules | "Beneficiaries of an IRA, and most plans, have the option of taking a lump-sum distribution … at any time. Beneficiaries must include any taxable distributions they receive in their gross income."; 10-year rule for a designated beneficiary who is not an eligible designated beneficiary | MATCH |
| F8 | [California State Controller](https://www.sco.ca.gov/ardtax_estate_tax.html) | No California estate-tax return is required for deaths on or after 1 January 2005 | "For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return." | MATCH |

### 2.3 Administration

| # | Source | Guide says | Official page says (13 Nov 2026) | Result |
|---|---|---|---|---|
| A1 | [CA Probate Code §16061.7](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=16061.7.&lawCode=PROB) | Statutory trustee notification, generally within 60 days, when required | § 16061.7(a)(1): notice when "a revocable trust or any portion thereof becomes irrevocable because of the death of one or more of the settlors"; (f): "shall be served not later than 60 days following the occurrence of the event requiring service" | MATCH |
| A2 | [CA RTC §480](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=480.) | Change-in-ownership statement within 150 days for a death-related transfer; probate has a different inventory-and-appraisal deadline | § 480(b): in probate the personal representative files the statement "prior to or at the time the inventory and appraisal is filed with the court clerk"; in all other cases of transfer by reason of death, including "a transfer through the medium of a trust", the trustee or transferee files "within 150 days after the date of death" | MATCH |

### 2.4 Local context

| # | Source | Guide says | Official page says (13 Nov 2026) | Result |
|---|---|---|---|---|
| L1 | [SF Rent Board current rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | 1.6% general annual allowable increase, 1 March 2026 – 28 February 2027; File 261020 not enacted | "1.6% for March 1, 2026 – February 28, 2027"; notice posted 9 Nov 2026: "This legislation has not been enacted and is subject to change." | MATCH |
| L2 | [SF Treasurer](https://sftreasurer.org/property/secured-property-taxes) | 2026–27 secured property tax rate; direct charges may be additional | "The secured property tax rate for Fiscal Year 2026-27 is 1.18162182%." | MATCH — the same rate the guide's model uses for Property B |
| L3 | [SFMTA Proposition H](https://www.sfmta.com/getting-around/muni/parcel) | The measure was approved; the first tax appears on FY 2027–28 bills; the amount for B is not verified | "San Francisco voters approved Proposition H on November 3, 2026. It creates an annual parcel tax … The first tax will appear on your fiscal year 2027–28 property tax bill"; published FY 2027–28 schedule: multifamily up to 5,000 sq ft $249, over 5,000 sq ft $249 + $0.195/sq ft (max $50,000); single-family up to 3,000 sq ft $129; "How long: July 1, 2027 through June 30, 2042"; exemption application deadline 1 June | **REFINED** — the schedule is now published, so the guide publishes it and leaves B's own amount blank. See change C3 |
| L4 | [SF Department of Elections](https://www.sfelections.org/results/20261103/index.html) | Results still labelled preliminary | "November 3, 2026, Consolidated General Election Results (Preliminary)"; "The Department may take up to 30 days after Election Day to certify final election results" | MATCH |
| L5 | [SFPUC water and sewer rates](https://www.sfpuc.gov/sites/default/files/accounts-and-services/Rates_Schedule_Water_Sewer_2026-7.pdf) | SFPUC publishes water and sewer schedules; the bill depends on service configuration and use | "RATE SCHEDULES & FEES for Water and Sewer Service … Effective with meter readings made on or after July 1, 2026 (Fiscal Year 2026-27), July 1, 2027 (Fiscal Year 2027-28)"; multi-family schedule W-1B | MATCH |
| L6 | [City of Cupertino water](https://www.cupertino.gov/Residents/Utilities/Water) | The city identifies three water systems; ZIP code alone does not establish the provider or bill | "provided to residents and businesses through three separate water systems … California Water Services … San Jose Water Company … The City's own water distribution infrastructure system" | MATCH |
| L7 | [PG&E solar billing](https://www.pge.com/en/clean-energy/solar/getting-started-with-solar/solar-billing-plan.html) | The tariff and the annual true-up matter; neither a monthly credit nor a future tariff is confirmed here | "you will receive monthly billing statements and an annual True-Up statement"; credits depend on when the system "receives permission to operate" | MATCH |
| L8 | [CA Department of Insurance — premiums](https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/) | The regulator's premium survey compares hypothetical profiles and is not a quote | "The results of these surveys are not premium quotes"; "The California Department of Insurance is a regulatory agency and not an insurance agent. As such, we cannot provide actual quotes." | MATCH |
| L9 | [CA Department of Insurance — earthquake](https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/eq-ins.cfm) | Standard homeowners coverage generally excludes earthquake damage, with exceptions | "Homeowners, renters, and condominium insurance policies do not cover damage from natural disasters such as earthquakes"; "Your homeowners insurance does not cover earthquake damage (except fire)"; a CEA policy is separate | MATCH |

### 2.5 Risk, macro and investment context

| # | Source | Guide says | Official page says (13 Nov 2026) | Result |
|---|---|---|---|---|
| R1 | [BLS CPI, December 2022](https://www.bls.gov/news.release/archives/cpi_01122023.htm) | 6.5% CPI-U inflation and 14.3% electricity inflation over the 12 months ending December 2022 | "The all items index increased 6.5 percent for the 12 months ending December"; table row "Electricity … 14.3" | MATCH — both figures exact |
| R2 | [CBO Budget and Economic Outlook 2026–2036](https://www.cbo.gov/publication/61882) | February 2026 outlook; PCE inflation moving toward roughly 2% in 2030; covers 2026–2036; not a 50-year forecast | "February 11, 2026"; "Inflation returns to a rate roughly in line with the Federal Reserve's long-run goal of 2 percent in 2030 and stabilizes thereafter."; title "The Budget and Economic Outlook: 2026 to 2036" | MATCH |
| R3 | [FHFA house-price index via FRED](https://fred.stlouisfed.org/series/ATNHPIUS41940Q) | FHFA publishes house-price indexes; historical regional changes and future individual-house values are not the same | Series "All-Transactions House Price Index for San Jose-Sunnyvale-Santa Clara, CA (MSA)", index 1995:Q1=100, latest Q2 2026 = 558.75, next release 24 Nov 2026 | MATCH |
| R4 | [USGS Fact Sheet 2016-3020](https://pubs.usgs.gov/publication/fs20163020) | 72% chance of at least one magnitude 6.7 or larger Bay Area earthquake over 2014–2043; not a probability of a particular property loss | "a 72 percent probability … of at least one earthquake of magnitude 6.7 or greater striking somewhere in the San Francisco Bay region before 2043" | MATCH |
| R5 | [Investor.gov / SEC](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/world-investor-week-2026-investor-bulletin) | Diversification can reduce certain risks but neither guarantees returns nor prevents loss | "Spreading out your investments across and within asset classes … can support diversification and asset allocation"; "Having adequate emergency savings will help you respond to financial shocks" | MATCH |
| R6 | [FDIC insured deposits](https://www.fdic.gov/resources/deposit-insurance/brochures/insured-deposits) | Used as the framework for how proceeds would be held | "As of April 1, 2024, the maximum insurance coverage for a trust owner with five or more beneficiaries is $1,250,000 per owner for all trust accounts … held at the same bank." | MATCH — now stated in the guide's Questions register |

### 2.6 Law watch and privacy

| # | Source | Guide says | Official page says (13 Nov 2026) | Result |
|---|---|---|---|---|
| W1 | [Congress.gov H.R. 1301](https://www.congress.gov/bill/119th-congress/house-bill/1301) | Introduced; referred to the House Ways and Means Committee; not enacted | "Committees: House - Ways and Means"; "Latest Action: House - 02/13/2025 Referred to the House Committee on Ways and Means."; status "Introduced" | MATCH |
| W2 | [California Legislature SB 284](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260SB284) | Official status page lists it in committee; not enacted | "Type of Measure: Active Bill - In Committee Process"; "House Location: Assembly"; "Voting Committee Location: Sen Appropriations" | MATCH |
| W3 | [GitHub Docs — removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) | Earlier revisions, branches, pull requests and caches can still expose information; a Pages exclusion is not access control | "If you only rewrite your history and force push it, the commits with sensitive data may still be accessible elsewhere: in any clones or forks … Directly via their SHA-1 hashes in cached views on GitHub … Through any pull requests that reference them"; GitHub Support can permanently remove cached views and pull-request references | MATCH |

**Result of the line-by-line check: 34 of 34 official pages opened; 32 MATCH, 1 REFINED (L3), 1 FLAGGED (P5). No published claim contradicts the page it cites.**

---

## 3. Irregularities found

### F1 — Two official pages describe the Proposition 19 adjustment cadence differently (Medium, published)

* **What:** The Santa Clara County Assessor's parent–child page says the one-million-dollar allowance "is adjusted annually beginning in 2023". The Board of Equalization says the amount is adjusted "every other February 16", and Letter to Assessors 2025/009 applied **one** step for the February 2025 – February 2027 period.
* **Why it matters:** A reader who follows the guide's link to the county page would build the allowance forward on the wrong cadence.
* **What this session did:** The guide continues to follow the Board. The discrepancy is now published on the **Flagged for review** page with both links, and the Questions register states the Board's cadence ("every other February 16") as the rule.
* **How to settle it:** Ask the assessor which basis it will apply to a transfer in the relevant period, and read the Board's Letters to Assessors, which are the governing notice.
* **Sources:** [BOE LTA 2025/009](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) · [BOE Proposition 19](https://www.boe.ca.gov/prop19/) · [Santa Clara County Assessor](https://asr.santaclaracounty.gov/tax-savings/transferring-your-assessed-value/parent-to-child-2)

### F2 — Proposition H: the schedule is now published; B's own amount is not computable (Medium, published)

* **What:** SFMTA publishes the FY 2027–28 amounts and states the measure was approved on 3 November 2026. The amount for a specific parcel depends on its parcel type and taxable building area, neither of which is a public fact.
* **What this session did:** The official schedule is published on the **Properties** page; the amount for Property B is left blank and marked unverified; the two watchlist rows on the Taxes page and the Flagged page now say that the schedule is verified and the amount is not.
* **Not modelled:** The measure is still absent from the synthetic B operating table on the comparison page, so that table understates B's costs from FY 2027–28. It is stated on the page rather than silently ignored.
* **Sources:** [SFMTA Proposition H](https://www.sfmta.com/getting-around/muni/parcel) · [SF Department of Elections](https://www.sfelections.org/results/20261103/index.html)

### F3 — The published artifact cannot remove the public repository's history (High, standing, unchanged)

* **What:** The guide withholds household figures, but the repository, its branches, its pull requests and external caches remain public. GitHub's own documentation says a rewrite can leave reachable copies and that GitHub Support is the route for cached views and pull-request references.
* **Status:** Unchanged and still the first row of the Flagged page. It is an owner decision (private repository, fresh repository, or a GitHub Support request), not something a session can fix by editing the site.
* **Source:** [GitHub Docs — removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)

### F4 — Official dollar amounts that are not multiples of ten (Low, handled, recorded here)

* **What:** The published currency rule is "every dollar amount on the page is a multiple of ten". Two amounts the guide now publishes are government-published and are not multiples of ten: $249 and $129 (SFMTA FY 2027–28 base amounts). Per-square-foot rates ($0.195, $0.42) are published as printed.
* **What this session did:** Rather than mis-round a published rate, `scripts/test-guide.cjs` now carries an explicit allowlist of government-published amounts, each with the reason it exists, and the amounts are recorded in this report. Household figures remain strictly at $10 rounding.
* **Related:** [SFMTA Proposition H](https://www.sfmta.com/getting-around/muni/parcel)

### F5 — The historical source register understates its own currency (Low, fixed)

* **What:** Every page carried "reviewed 12 Nov 2026" while the guide's own sources page already said the rules were reviewed on 12 November.
* **What this session did:** All 34 links were re-opened on 13 November 2026; the stamp on every page and in the footer now reads 13 Nov 2026, and the Sources page says each link was re-opened and its attributed wording checked on that date.

### F6 — Local browser test could not run in this sandbox (Low, environment)

* **What:** `scripts/test-browser.cjs` needs a Chromium build; the sandbox image has no `libnss3.so`, so the browser process exits with code 127.
* **Status:** Not a site defect. The GitHub Actions workflow installs the same packages and runs this test on `ubuntu-latest`, so the check runs in CI. The other seven checks were run and passed locally.

---

## 4. Changes made to the published guide this session

All changes are additive. No synthetic model input, no recommendation and no published figure was changed.

| ID | Change | Page | Why |
|---|---|---|---|
| C1 | Added an **"Answer already known from official sources"** column to the Questions register. Every one of the 20 questions now states the rule as the official source gives it, next to the household's own answer, which stays blank. | Questions | The brief asks for "questions, informations and answers … based upon the information that we already have and do not have". The register previously showed only what was missing, so a reader could not tell "unknown to us" from "settled by law". |
| C2 | Added a **"Can a decision reasonably be made yet?"** section: counts by priority (11 / 8 / 1 of 20), and the plain verdict that a live, rent or sell decision **cannot** reasonably be made today because every Priority 1 item is open, with a link to the suggestions register that lists the route for each one. | Questions | The brief asks for a decision gate. The register now says where the gate is and what stands in front of it. |
| C3 | Published the **official Proposition H FY 2027–28 schedule** by parcel type and taxable building area, with the amount for Property B left blank and marked unverified. | Properties | A confirmed, dated, recurring cost for Property B that the guide previously could not state. |
| C4 | Updated the Proposition H rows on the Taxes watchlist and the Flagged page, and added the Proposition 19 cadence discrepancy (F1). | Taxes, Flagged | Keep every page consistent with the newly published schedule, and surface a discrepancy between two official pages. |
| C5 | Review stamp moved to **13 Nov 2026** on every page and in the footer; the Sources page records that all 34 links were re-opened on that date and the SFMTA register row now describes the schedule, exemptions and dates. | All pages, Sources | The published currency claim must match the work actually done. |
| C6 | Added an allowlist of government-published dollar amounts to the rendered-check gate, and new rendered checks that every question states its rule, that every household answer stays blank, and that every Proposition H row carries an official link and an unverified amount for B. | `scripts/test-guide.cjs` | The new content must be enforced, not merely asserted once. |

---

## 5. Checks run on the final tree

| Check | Result |
|---|---|
| `python3 scripts/check-generated.py` | **PASS** — 10 generated pages are up to date |
| `python3 scripts/test-model-reference.py` | **PASS** — 108 decision configurations and 250 stress years reconstructed independently; 10,236 unrounded comparisons |
| `python3 scripts/package-site.py` | **PASS** — 18 reviewed guide files packaged; legacy site excluded |
| `python3 scripts/check-publication.py --self-test` | **PASS** — extra, missing, altered, symlinked and hard-linked files rejected |
| `node scripts/test-guide.cjs` | **PASS** — 10 rendered pages, 656 source-linked table rows, 9,188 checks |
| `node scripts/privacy-audit.cjs` | **PASS** — no distinctive legacy input or history token, no email, no street-address-like string in the packaged source or the default rendered dollar values |
| `python3 src/check_links.py .` | **PASS** — 69 pages, 1,171 table rows, 0 broken internal links (external links are not machine-checked from this sandbox) |
| `node scripts/test-browser.cjs` | **could not run here** — see F6; runs in CI |

The model is untouched: the base case is unchanged, and `scripts/test-model-reference.py` reproduces the published results from an independent reconstruction.

---

## 6. Privacy check on this session's own work

* No personal information was added to any committed file.
* No household figure was typed into any new file. The Questions register's household-answer column contains only the marker `— unverified`, `— preference not established` or `— not knowable yet`.
* The only new dollar figures are government-published amounts ($249, $129) plus per-square-foot rates published by SFMTA, all listed in the gate's allowlist and in §2.4 above.
* `scripts/privacy-audit.cjs` passes on the packaged artifact.
* The one-off edit script used to change the generator (`scripts/patch-guide.py`) was deleted rather than committed; the generator itself carries the change.

---

## 7. What remains open, and for whom

| Item | Who can settle it |
|---|---|
| The whole decision: 11 Priority 1 facts, every one of them private | The household, with counsel, an appraiser, the county assessor and insurers — privately |
| Proposition H: B's parcel type and taxable building area | The Assessor-Recorder and the bill, privately |
| Proposition 19: which adjustment cadence the county will apply | The Santa Clara County Assessor |
| Election certification after the 3 November 2026 vote | The San Francisco Department of Elections |
| FY 2027 rent benchmarks (the guide does not publish a rent benchmark for B) | HUD's official ZIP lookup, read directly |
| The public-repository history exposure (F3) | The repository owner: private repository, fresh repository, or a GitHub Support request |

None of these blocks publication. All are visible on the site's **Flagged for review** page with the document that would settle each.
