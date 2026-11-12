# Session `364b453d` — verification report

**Branch:** `arena/364b453d-tino2`, from `main` = `bfb2268`.
**Work:** the suggestions, decision-readiness and choose-a-path page (`site/suggestions.html`), plus the navigation entry, landing-page card, publication manifest and page-count assertion it needs.
**Scope limit:** no model input, no published figure, no recommendation and no other page's content was changed. This report covers only what the new page states.

## 1. Why this page, and what it does not do

The brief asks, twice, for a dedicated suggestions section: suggestions to improve the site for decision making, and a place where those suggestions can be reviewed and a path chosen **before** anything is implemented. A full-text search of the published pages, `assets/app.js` and `README.md` found no such page and no navigation entry for one. The existing pages carry the analysis, the open-items register (`site/review.html`) and the verification ledger (`site/verification.html`), but not a reviewable queue with a recorded choice.

The new page adds:

1. a register of fifteen improvements to the analysis, each with its official evidence, effort and suggested window;
2. a table of the ten decision-critical questions, each with what the site has, what is missing, where the answer lives, and what changes if the answer goes either way;
3. six proposals for the dashboard itself, one of which (the decision record) is built on the page;
4. a five-step suggested sequence;
5. a choose-a-path control: approve, defer or decline per item, stored only in the reader's browser, with print, copy and clear;
6. the guardrails that any implementation must keep (privacy, blanks stay blank, $10 rounding, a source per row, no advice).

It deliberately does **not** restate the model, add a projection, or claim that an approved suggestion is a finding. Approving “get an insurance quote” changes nothing until the quote is added as a dated input and re-verified.

## 2. Official pages opened in this session

All opened 12 November 2026 from this sandbox. Quoted wording is what the page returned.

| # | Official page | Wording found (short quote) | Supports |
|---|---|---|---|
| 1 | IRS, IR-2026-133, *IRS releases tax inflation adjustments for tax year 2027* — https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts | “Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from a total of $15,000,000 for estates of decedents who died in 2026.” · “the first $20,000 of gifts to any person” (calendar 2027) | A-08, Q-03 |
| 2 | IRS, *Estate tax* (filing threshold by year of death) — https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax | Table row “2026 \| $15,000,000”; “A filing is required if the gross estate … is valued at more than the filing threshold for the year of the decedent's death” | A-08 |
| 3 | California State Controller, *California Estate Tax* — https://www.sco.ca.gov/ardtax_estate_tax.html | “For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return.” | Guardrail on state tax, Q-03 context |
| 4 | California Franchise Tax Board, *Gifts and inheritance* — https://www.ftb.ca.gov/file/personal/income-types/gifts-and-inheritance.html | “If you received a gift or inheritance, **do not** include it in your income.” (page “Last updated: 09/24/2025”) | State treatment of the inheritance itself |
| 5 | Board of Equalization, *Proposition 19* — https://boe.ca.gov/prop19/ | “Value limit of current taxable value plus $1,000,000 (as biennially adjusted)” · “File for homeowners' exemption within 1 year of transfer” · “File claim for exclusion within 3 years or before transfer to third party” | A-02, A-11, A-06, Q-02 |
| 6 | Board of Equalization, Letter to Assessors 2026/026 (3 August 2026) — https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf | “plus $1 million. The $1 million is adjusted on February 16, 2023, and every other February 16 thereafter.” · “If the family home becomes ineligible for the Homeowners' or Disabled Veterans' Exemption, the exclusion will be removed” · claim deadlines as in row 5 | A-02, A-11, A-06 |
| 7 | Board of Equalization, news release NR 25-02 — https://www.boe.ca.gov/news/2025/NR-25-02.htm | Dated “March 7, 2025”; “transfers occurring on February 16, 2025, through February 15, 2027”; “increased by 2.15 percent, from $1,022,600 to $1,044,586” | A-06 (timing of the last adjustment) |
| 8 | Department of Insurance, 2026 homeowners premium comparison, Cupertino, 40-year-old home, $1,000,000 dwelling — the survey result page | “All premiums displayed on this page are annual premiums and are effective as of May 1, 2026.” · “This is not an insurance premium quote.” | A-03, Q-04 |
| 9 | Department of Insurance, *Residential Insurance: Homeowners and Renters* (Form 401, revised January 2026) — https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/res-ins-guide.cfm | “The ‘dwelling’ limit should be the amount it would cost to replace your home. This may have nothing to do with the purchase price or the current market value of your home” · earthquake listed among perils “generally not covered” · “Losses to house vacant for 60 days or more” | A-03, A-04 |
| 10 | USGS, earthquake probability FAQ — https://www.usgs.gov/faqs/what-probability-earthquake-will-occur-los-angeles-area-san-francisco-bay-area | San Francisco Bay area, next 30 years: “72% that an earthquake measuring magnitude 6.7” | A-04, Q-05 |
| 11 | HUD, FY2026 Small Area FMR calculation for ZIP 95014 — https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=95014&year=2026 | Table: Three-Bedroom “$5,870”, Four-Bedroom “$6,390” | A-05 |
| 12 | HUD, Small Area FMR data index — https://www.huduser.gov/portal/datasets/fmr/smallarea/index.html | FY2027 section present with an interactive lookup; FY2026 “\[Effective October 1, 2025\]” | A-05 (why the input is one year behind) |
| 13 | CPUC, *Customer-Sited Renewable Energy Generation* — https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/demand-side-management/net-energy-metering | “These tariffs are closed to new enrollments.” · “Since April 15, 2023, customers applying for interconnection have taken service on the new net billing tariff” · NBT pays exported generation “at a rate reflecting the value of this generation to the grid” | A-13, Q-06 |
| 14 | San Francisco Rent Board, *Current Rates* — https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit | “1.6% for March 1, 2026 – February 28, 2027” · relocation $8,245.00 per tenant, maximum $24,733.00 a unit, plus $5,497.00 · notice posted 9 November 2026 that File 261020 “has not been enacted and is subject to change” | A-07, A-12, Q-08 |
| 15 | San Francisco Rent Board, *The Rent Board Fee* — https://www.sf.gov/rent-board-fee | “$59.00 per dwelling unit” · “The deadline to submit a Request for Exemption for the 2027 Rent Board fee is December 14, 2026.” · fee due March 1, late penalties to 15% | A-11 |
| 16 | IRS, Revenue Ruling 2023-2 — https://www.irs.gov/pub/irs-drop/rr-23-02.pdf | “the basis of Asset is not adjusted to its fair market value on the date of A's death under § 1014 because Asset was not acquired or passed from a decedent as defined in § 1014(b)” | A-01, Q-01 |
| 17 | California Legislative Information, Probate Code §10800 — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10800 | “for ordinary services the personal representative shall receive compensation based on the value of the estate accounted for” (4%, 3%, 2%, 1%, one-half of 1% bands) | A-10 |

Pages cited on the new page that were **not** reopened this session (accepted from the existing register and the session that added them, and not re-verified here): `irsInherited`, `irs706TableA`, `irsTopic704`, `irsPub527`, `caRentCaps`, `irsTopic701`, `hr1301`, `sfRentProposal`, `sosResults2026`, `sjw2026`, `sfpucRates2026`, `fredSccCounty`, `investorRisk`, `boeLta2026`, `githubSensitive`. Each is used as a link for a route, not as the sole support for a figure. No figure on the new page depends on an unopened source.

## 3. Every dollar amount on the new page

| Amount | Status |
|---|---|
| $6,390 a month | HUD FY2026 four-bedroom Small Area FMR for ZIP 95014, verified this session (row 11) |
| $1,000,000 | Proposition 19 value cap added to the factored base year value, verified this session (rows 5–6) |
| $15,000,000 | Federal basic exclusion for a death in 2026, verified this session (rows 1–2) |
| $15,480,000 | Federal basic exclusion for a death in 2027, verified this session (row 1) |
| $10 | The site's rounding rule, not a projection |

No other dollar figure appears on the page. No household figure appears anywhere on it, and the page contains no name, address, parcel number, account number or e-mail address.

## 4. Checks run on the resulting tree

| Check | Result |
|---|---|
| `node scripts/validate.js` | PASS — 1,149 checks, 16 pages, 171 source keys; base case unchanged (sell $7,683,290 / rent $6,249,830 / live $5,135,780 for 2045→2055) |
| `node scripts/stress-test.js` | PASS — 50-year paths, estate ownership, privacy, real-dollar and shock tests |
| `python3 scripts/package-site.py` | PASS — rounding rule, no exact household amounts |
| `python3 scripts/check-publication.py --self-test` | PASS — 29 reviewed public files (was 28; the new page is now in the reviewed manifest) |
| `node scripts/runtime-test.cjs` | PASS — 16 rendered pages, 1,352 rows, every `tbody` row with an https source link, no runtime error, no broken local link |
| `node qa/tools/gate.cjs` | PASS — 1,352 rows (1,343 with their own official link, 9 calculated rows with a context link only), 4,824 amounts checked, 103 official exact figures, 0 errors, 0 warnings |
| `python3 src/check_links.py .` | PASS — 64 pages, 871 table rows, 124 distinct external links (external links are not machine-checked from this sandbox) |
| `python3 integration/tools/privacy_scan.py` | 0 errors, 198 warnings — all pre-existing (ledger and research files); the new page produces no warning |

Rendered behaviour checked separately with jsdom: the page throws no error, shows 21 choice controls, persists a selection to `localStorage` under one key, updates the summary counts, and degrades without `navigator.clipboard`.

## 5. Irregularities and limitations

- **S-I1 — HUD FY2027 rent benchmark still unread (standing item, not resolved).** Attempted this session: the FY2026-style address for 2027 (`…/FY2027_code/2027zip_code_calc.odn?zcta=95014&year=2027`) returns “404 - File or directory not found”; the FY2027 section of the SAFMR index offers an interactive lookup and an `.xlsx` workbook. This sandbox's shell reaches only a small allowlist of hosts, so the workbook cannot be downloaded and the interactive lookup cannot be driven. The FY2027 data therefore stays blank, as the existing Flagged for Review item says, and the new page lists reading it as **A-05** rather than asserting a value.
- **S-I2 — Two wordings softened after checking.** (a) The first draft said the next Proposition 19 amount is “not on the Board's 2026 letter list”; this session did not re-open that list, so the page now attributes the finding to the site's earlier check and cites NR 25-02 for the timing that makes a delay plausible. (b) “Statutory fees on the full value” was replaced with the verified wording — a statutory percentage of the estate's value (Prob. Code §10800).
- **S-I3 — The record is per-browser.** The approve/defer/decline record lives in `localStorage` and is not durable across devices or private windows. That is deliberate — no account, no server, no analytics — and the page says so and offers print and copy. It is a limitation, not a defect; a durable record would require a personal document kept outside this repository.
- **S-I4 — Page count and manifest changed.** `scripts/validate.js` asserted fifteen pages and `scripts/check-publication.py` listed 28 files; both were updated for the sixteenth page. Any later session adding a page must do the same, or the build fails closed, which is the intended behaviour.
- **S-I5 — No personal information was added.** The new page contains placeholders, official rules and official amounts only. The standing privacy findings on Flagged for Review (public history, branches, account e-mail) are unchanged by this session and remain an owner decision.

## 6. Parallel sessions — the conflict and how it was resolved

Two other sessions were live while this one worked, and the claim check did not see them: `62b76b9d` merged PR #43 at 15:33 UTC and `6e6baf25` PR #44 at 15:36 UTC, both after this session's 15:35 UTC claim recorded “no open pull requests”. Between them they had already published a suggestions page, a landing-page suggestions table, and clarifications to the executive summary, `site/plan.html` and `site/decision.html`.

Merging `origin/main` (up to `ed9cbbd`) produced one content conflict in `COORDINATION.md` and one add/add conflict in `site/suggestions.html`; `assets/app.js`, `index.html`, `scripts/validate.js` and `scripts/check-publication.py` auto-merged but left two navigation entries and two landing-page cards for the same page.

Resolution, chosen to keep both sessions' work:

| File | What was done |
|---|---|
| `site/suggestions.html` | **Combined, not replaced.** Their privacy notice, privacy-path comparison table, seven structural improvements, seven questions and closing “How to use this list” note remain in full (the questions are kept unchanged inside a collapsed block, with their wording and links). This session's fifteen-item register, ten decision-critical questions, six dashboard proposals, five-step sequence and choose-a-path record were added around them. One hero, one page. |
| `assets/app.js` | The two nav entries were reduced to the published one; the other session's title and footer wording was kept. |
| `index.html` | The duplicate card was removed in favour of the published card, whose wording now mentions the recorded choice; all their executive-summary wording changes are intact. |
| `COORDINATION.md` | Both appended blocks kept in full, theirs first; the conflict and its resolution are recorded inside this session's block. |
| `scripts/validate.js`, `scripts/check-publication.py` | Both sessions had made the same two edits (16 pages; manifest entry); no conflict remains. |

Nothing of either other session was discarded, and no model figure, model input or published recommendation changed.

## 7. Checks re-run after the merge

`validate.js` PASS (1,151 checks, 16 pages, 171 sources; base case unchanged at sell $7,683,290 / rent $6,249,830 / live $5,135,780) · `stress-test.js` PASS · `package-site.py` PASS · `check-publication.py --self-test` PASS (29 files) · `runtime-test.cjs` PASS (16 pages, 1,375 rendered rows, all source-linked, no broken local link) · `qa/tools/gate.cjs` PASS (0 errors, 0 warnings; 4,824 amounts checked) · `src/check_links.py .` PASS (64 pages, 879 table rows) · `privacy_scan.py` 0 errors.

The combined page renders with one `h1`, five tables, forty-two rows and twenty-one choice controls; both sessions' sections are present and the record still persists to one `localStorage` key.
