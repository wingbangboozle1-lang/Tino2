# Independent Verification Report — Session `5eb05dce`

**Date:** 2026-11-12  
**Branch:** `arena/5eb05dce-tino2` (rebased onto `origin/main` `444be2e`)  
**Scope:** Independent verification of the canonical 18-page / 34-file GitHub Pages dashboard (`index.html`, `site/*.html`, `site/data/*.js`, `assets/{app.js,styles.css}`). No site files were modified because zero factual calculation errors or broken checks were found.

---

## 1. Automated Validation & Boundary Suite (`444be2e` tree)

Every automated repository check passed with zero errors:

| Check | Command | Result |
|---|---|---|
| Schema, math, source & completeness check | `node scripts/validate.js` | **PASS** — 1,561 checks across 18 pages and 177 official sources |
| 50-year economic & shock stress suite | `node scripts/stress-test.js` | **PASS** — 50-year paths, estate ownership, privacy, real-dollar, and shock tests |
| Canonical site packaging | `python3 scripts/package-site.py` | **PASS** — packaged canonical site only; legacy material excluded |
| Fail-closed publication boundary | `python3 scripts/check-publication.py --self-test` | **PASS** — 34 reviewed public files only; internal material excluded; symlinks/unlisted files rejected |
| Headless DOM runtime & row source links | `node scripts/runtime-test.cjs` | **PASS** — 18 rendered pages, 1,583 rendered rows source-linked, 0 runtime errors, 0 broken local links |
| Rendered QA gate | `node qa/tools/gate.cjs` | **PASS** — 18 rendered pages, 1,583 table rows (1,574 own official link, 9 calculated rows with context link), 4,985 dollar amounts checked (115 official exact figures), 559 internal and 2,074 external links, 0 errors, 0 warnings |
| Legacy + site link inventory | `python3 src/check_links.py .` | **PASS** — 68 pages, 887 table rows, 128 distinct external links |
| Public privacy & `$10` rounding scan | `python3 integration/tools/privacy_scan.py _public --quiet` | **PASS (0 errors)** — 53 warnings, all on exact published government figures (`ledger.js`, `sources.js`, `plan.html` SF Rent Board relocation `$8,245`/`$24,733`/`$5,497`, `review.html` FTB bracket `$371,479`); zero unrounded household figures |
| Whole-repo privacy scan | `python3 integration/tools/privacy_scan.py --quiet` | **PASS (0 errors)** — 228 warnings, all on official figures or archived legacy/research directories excluded by `_config.yml` |

### Base-Case Deterministic Model Reproduction (`site/data/model.js`)

Reproduced directly in Node (`MODEL.decision({...MODEL.BASE, inheritYear: Y}, 10)`):

| Inheritance → Horizon | Property A Market Value | Prop 19 Modeled Allowance | Sell & Reinvest | Rent, then Sell | Live, then Sell | Leader |
|---|---:|---:|---:|---:|---:|---|
| **2040 → 2050** | $5,017,950 | $1,329,010 | **$7,683,290** | $6,249,830 | $5,135,780 | `sell` |
| **2045 → 2055** | $5,959,750 | $1,473,490 | **$9,125,340** | $7,395,620 | $6,068,080 | `sell` |
| **2050 → 2060** | $7,078,320 | $1,578,440 | **$10,838,040** | $8,752,170 | $7,164,510 | `sell` |

Estate headroom (`MODEL.estateRow(Y)`): 2026 `$11,900,000` (official `$15,000,000` exclusion), 2027 `$12,271,500` (official `$15,480,000` exclusion), 2040 `$15,007,080` (modeled at 2%/yr indexing). Property B is excluded from the decedent's gross estate because the heir already owns it.

---

## 2. Live Official-Source Verification (Re-Opened 2026-11-12)

Twenty-eight official government and utility pages were fetched live during this session and compared against the published dashboard:

| Domain | Official URL Re-Opened Live | Verified Wording / Figures | Site Match |
|---|---|---|---|
| **IRS Estate Exclusion (2026)** | `https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax` | Public Law 119-21 (July 4, 2025) sets 2026 basic exclusion at `$15,000,000`. Note: TD 10055 increased Letter 627 (ETCL) user fee `$56 → $76` effective Oct 26, 2026. | **Match** |
| **IRS 2027 Inflation Adjustments** | `https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts` | IR-2026-133 (Nov 5, 2026): 2027 basic exclusion `$15,480,000`; annual gift exclusion `$20,000` (2026: `$19,000`). | **Match** |
| **IRS Capital Gains / Home Sale / NIIT** | `https://www.irs.gov/taxtopics/tc409`, `.../tc701`, `.../tc559` | 0/15/20% CG rates (25% §1250); `$250,000`/`$500,000` 2-of-5-yr exclusion; 3.8% NIIT above `$200k`/`$250k` (`$15,650` trust threshold for 2025). | **Match** |
| **CA Estate Tax** | `https://www.sco.ca.gov/ardtax_estate_tax.html` | No California estate-tax return required for decedents dying on or after Jan 1, 2005. | **Match** |
| **CA Prop 19 Rules & Allowance** | `https://boe.ca.gov/prop19/`, `https://www.boe.ca.gov/news/2025/nr-25-02.htm` | Principal residence of parent + child, 1-yr homeowners exemption + 3-yr claim, `$1,044,586` cap for Feb 16, 2025–Feb 15, 2027 (+2.15% from `$1,022,600`), biennial FHFA CA HPI adjustment. | **Match** |
| **CA Prop 13 Roll Factor** | `https://www.boe.ca.gov/proptaxes/pdf/lta26002.pdf` | 2026–27 roll factor `1.02` (CCPI +3.307% Aug 2024–Aug 2025, capped at 2%); full 1976–2027 factor table matches `verification.html`. | **Match** |
| **Santa Clara County Assessor & Controller** | `https://asr.santaclaracounty.gov/tax-savings/transferring-your-assessed-value/parent-to-child-2`, `https://controller.santaclaracounty.gov/property-tax-distribution/property-tax-rate-book` | County page still states `"adjusted annually beginning in 2023"` (already flagged in `review.html` vs BOE biennial rule); FY2025-26 remains latest Rate Book listed. | **Match (Flagged)** |
| **CA FTB Capital Gains & Form 593** | `https://www.ftb.ca.gov/file/personal/income-types/capital-gains-and-losses.html`, `https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html` | CA taxes capital gains as ordinary income; 3 1/3% real estate withholding unless exempt on Form 593 prior to close. | **Match** |
| **CA Probate Code & SB-974** | `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=16061.7.&lawCode=PROB`, `.../billStatusClient.xhtml?bill_id=202520260SB974` | 60-day trustee notice under § 16061.7; SB-974 Chapter 665, Statutes of 2026 (approved Sept 27, 2026). | **Match** |
| **Pending Federal Bills** | `https://www.congress.gov/bill/119th-congress/house-bill/1301/all-actions`, `.../601/all-actions`, `.../7034/all-info` | H.R. 1301, H.R. 601, H.R. 7034 all remain at `Introduced / Referred to House Ways and Means` (not enacted). | **Match** |
| **SF Secured Tax Rate** | `https://sftreasurer.org/property/secured-property-taxes` | FY 2026–27 secured rate `1.18162182%`; Dec 10 / Apr 10 delinquency dates. | **Match** |
| **SF Rent Board Rates, Fee & AB 1482** | `https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit`, `.../rent-board-fee`, `.../ab-1482` | `1.6%` increase, `4.2%` deposit interest, ordinary relocation `$8,245 / $24,733 / +$5,497`, Ellis `$11,110.05 / $33,330.13 / +$7,443.90`; `$59` fee (50% recoverable, Dec 14, 2026 exemption deadline); AB 1482 `8.8%` max, Jan 1, 2030 sunset. | **Match** |
| **SF File 261020** | `https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770` | Proposed 10% combined banked + CI cap remains `Pending Committee Action` in Land Use & Transportation Committee. | **Match** |
| **SF Measure H (Ballot & Tally)** | `https://www.sfelections.org/results/20261103/index.html`, `.../Title_and_Summary_-_Parcel_Tax_to_Fund_Public_Transit_Operations_002.pdf`, `.../MUNI_parcel_tax_economic_impact_final.pdf` | Nov 10 tally `74.4%` Yes (`244,760` / `84,209`); multifamily `$249` base + `$0.195/sq ft > 5,000`, July 1, 2027–June 30, 2042, 50% / `$65` unit pass-through. | **Match** |
| **CA Statewide Ballot Measures** | `https://electionresults.sos.ca.gov/returns/ballot-measures` | Live Nov 12, 10:50 a.m. update: Prop 3 `60.7%` yes, Prop 40 `47.6%` yes, Prop 42 `51.4%` yes, Prop 43 `42.5%` yes (site date-stamps Nov 11 `47.5%` / `42.6%`; outcomes identical, uncertified until Dec 11). | **Match (dated)** |
| **HUD FY2026 & FY2027 SAFMRs** | `https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=95014&year=2026`, `...zcta=94122&year=2026`, `https://www.huduser.gov/datasets/fmr/fmr2027/zip-calc?year=2027&zip=95014&cbsasub=METRO41940M41940`, `...zip=94122&cbsasub=METRO41860MM7360` | FY26 `95014`: `$5,870` 3BR / `$6,390` 4BR; `94122`: `$2,730` 1BR / `$3,310` 2BR. FY27 `95014`: `$5,440` 3BR / `$5,800` 4BR; `94122`: `$2,770` 1BR / `$3,410` 2BR. | **Match** |
| **Utilities & Solar** | `https://www.sjwater.com/media/qeeh013c/adv-628a_web.pdf`, `https://www.sfpuc.gov/sites/default/files/accounts-and-services/Rates_Schedule_Water_Sewer_2026-7.pdf`, `https://www.cpuc.ca.gov/.../net-energy-metering`, `https://www.cupertino.gov/.../Accessory-Dwelling-Units` | SJWC AL 628A +3.71% effective July 1, 2026 (Valley Water `$2,673/AF` pump, `$2,788/AF` purchased); SFPUC FY26–27 adopted April 2026; CPUC NEM closed / NBT since Apr 15, 2023; Cupertino ADU rules match. | **Match** |
| **Macro, Insurance & Hazard** | `https://www.freddiemac.com/pmms`, `https://www.cbo.gov/publication/61882`, `https://www.ssa.gov/oact/TR/2026/II_C_assump.html`, `https://www.usgs.gov/faqs/what-probability-earthquake-will-occur-los-angeles-area-san-francisco-bay-area`, `https://www.cfpnet.com/key-statistics-data/`, CDI APEX tool | PMMS Nov 12, 2026: `7.11%` 30-yr FRM (down from `7.18%` Nov 5 cited on site); CBO 2% PCE by 2030; SSA 2.4% CPI-W / 2.3% real yield; USGS `72%` M6.7+ in 30 yrs; FAIR Plan Sep 2026 `$773B` exposure / `698,307` PIF / `$2.04B` premium; CDI live 2026 survey confirms non-quote status. | **Match** |

---

## 3. Non-Blocking Observations (No Factual Model Errors)

1. **Freddie Mac PMMS weekly release (`2026-11-12`):** `site/data/sources.js` (`freddiePmms`) and `site/scenarios.html` state `7.18% on 5 November 2026`, which is exact for that date. Freddie Mac's Nov 12, 2026 weekly release moved to `7.11%` (30-year) and `6.45%` (15-year).
2. **SFPUC FY2026–27 rate wording (`site/plan.html:100`):** `site/data/costs.js` correctly describes the ~12.6% / ~12.5% schedule as `"Adopted two-year schedule"` (approved April 28, 2026 via Resolutions 26-0064 and 26-0066, effective July 1, 2026); `site/plan.html:100` still says `"were proposed to rise"`. Non-material wording lag.
3. **CA SOS unofficial ballot update (`2026-11-12`):** Site notes are explicitly stamped `11 Nov 2026, 6:51 p.m.`; the Nov 12, 10:50 a.m. update shows +0.1 pp on Prop 40 (`47.6%` yes) and −0.1 pp on Prop 43 (`42.5%` yes), with outcomes identical and certification pending until Dec 11, 2026.
4. **IRS Estate Tax Closing Letter fee (`TD 10055`):** Increased from `$56` to `$76` effective Oct 26, 2026; neither figure is cited in the published dashboard.
5. **Measure H OEA report vs. Ballot Title typo:** OEA's Economic Impact Report summary cites `$1.19/sq ft` vs the Ballot Title & Summary's `$1.99/sq ft` on *single-family* parcels over 5,000 sq ft; Property B is multifamily (`$249` base + `$0.195/sq ft > 5,000`), which is identical in both documents and already unmodeled pending square-footage verification.

---

## 4. Privacy & Publication-Boundary Confirmation

- **Served manifest:** `scripts/check-publication.py --self-test` confirms `_public/` contains strictly the 34 reviewed canonical files (`index.html`, `robots.txt`, `.nojekyll`, `assets/{app.js,styles.css}`, 17 `site/*.html` pages, and 12 `site/data/*.js` modules). `_config.yml` excludes all legacy HTML pages, `docs/`, `research/`, `verification/`, `qa/`, `scripts/`, `src/`, `integration/`, `dashboard/`, and `pages/`.
- **Anonymization & rounding:** No personal names, street addresses, emails, SSNs, or parcel numbers appear in `_public/`. Household amounts are displayed rounded to `$10` via `MODEL.round10()` / `MODEL.fmtMoney()`, with unverified household inputs and residual Git-history/re-identification risks explicitly documented on `index.html`, `site/review.html`, and `site/suggestions.html`.
- **Live GitHub Pages check:** `https://wingbangboozle1-lang.github.io/Tino2/` (`status: built`, `https_enforced: true`, commit `444be2e`) and subpages (`site/verification.html`, `site/review.html`) were fetched live and confirmed rendering with working relative assets and links.
