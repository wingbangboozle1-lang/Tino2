# Session `d9c69069` — independent verification report

**Date:** 2026-11-11 (all access dates are 2026-11-11 UTC)
**Branch:** `arena/d9c69069-tino2`
**Tree verified:** `main` at `660be98` (PR #20, session `11bffb54`, merged 07:49:54 UTC), merged into this branch.
**Role:** read-only independent auditor. This report is the only substantive file this session adds. No file owned by another session was edited; corrections that belong in someone else's file are logged as requests in `COORDINATION.md`.

**Privacy statement.** No personal name, street address, parcel number, account number or contact detail appears in this report. Properties are "Property A" (Cupertino 95014) and "Property B" (San Francisco 94122). Household figures quoted here are already the $10-rounded values the site publishes; no exact household amount is reproduced.

---

## 1. Automated suite re-run on the merged tree

| Check | Command | Result |
|---|---|---|
| Model, syntax, link and source validation | `node scripts/validate.js` | PASS — 737 checks, 13 pages, 100 official sources |
| 50-year stress paths, estate ownership, real-dollar tests | `node scripts/stress-test.js` | PASS |
| Rendered-page gate (JSDOM): rows, source links, dollar rounding, links | `node qa/tools/gate.cjs` | PASS — 13 rendered pages, 963 table rows (951 with their own official link, 12 calculated rows with a context link), 4,194 dollar amounts (54 official exact figures), 254 internal + 1,376 external links, 0 errors, 0 warnings |
| Publication allowlist packaging | `python3 scripts/package-site.py` | PASS |
| Internal links across the whole repository | `python3 src/check_links.py .` | 58 pages, 871 table rows, 124 distinct external links, 0 errors |
| Privacy scanner | `python3 integration/tools/privacy_scan.py` | 0 errors, 102 warnings — see §4 |

`qa/tools/gate.cjs` needs the optional dev dependency `jsdom`, installed outside the repository
(`npm install --prefix .cache/test jsdom`); `.cache/` is gitignored, so the repository stays dependency-free.

Base case reproduced by the model on the merged tree (2040 inheritance, 2050 endpoint):
sell **$7,683,290** · rent **$6,249,830** · live **$5,135,780**.

---

## 2. Independent re-verification against official sources

Every page below was **opened and read by this session on 2026-11-11**, directly (not through a search
result or another session's file). "Wording found" is quoted from the official page.

| # | Figure as published on the site | Result | Wording found on the official page | Official source |
|---|---|---|---|---|
| 1 | Federal basic exclusion for deaths in 2026 = $15,000,000 | **Match** | "WFTC amends § 2010(c)(3) by increasing the basic exclusion amount to $15,000,000 for calendar year 2026." | [IRS — What's new, estate and gift tax](https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax) |
| 2 | Federal basic exclusion for deaths in 2027 = $15,480,000 | **Match** | "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from a total of $15,000,000 for estates of decedents who died in 2026." | [IRS IR-2026-133 (5 Nov 2026)](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) |
| 3 | Annual gift exclusion $19,000 (2026) / $20,000 (2027); non-citizen spouse $194,000 / $201,000 | **Match** | "For calendar year 2027, the annual exclusion for gifts increases to $20,000, up from $19,000 for calendar year 2026 … to a spouse who is not a citizen … increases to $201,000 … up from $194,000." | [IRS IR-2026-133](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) |
| 4 | No California estate-tax return for deaths on/after 1 Jan 2005 | **Match** | "For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return." | [State Controller — California Estate Tax](https://www.sco.ca.gov/ardtax_estate_tax.html) |
| 5 | Prop 19 requires the home to be the principal residence of transferor **and** transferee; homeowners' exemption within 1 year; claim within 3 years or before transfer to a third party; no exclusion for other real property | **Match** | Comparison chart, "Proposition 19 (Current Law)" column: "Principal residence of transferor and transferee … File for homeowners' exemption within 1 year of transfer — File claim for exclusion within 3 years or before transfer to third party … Eliminates exclusion for other real property other than the principal residence" | [BOE — Proposition 19](https://boe.ca.gov/prop19/) |
| 6 | Prop 19 adjusted $1 million amount = $1,044,586 for transfers 16 Feb 2025 – 15 Feb 2027; next adjustment Feb 2027 | **Match** | "the $1 million amount is adjusted to **$1,044,586** … for transfers that occur February 16, 2025 through February 15, 2027 … The next adjustment of the $1 million amount will occur in February 2027." | [BOE LTA 2025/009 (PDF)](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) |
| 7 | Prop 19 amount is indexed to the FHFA California house-price index for the prior calendar year (2024: 2.15%) | **Match** | "adjust the one million dollar ($1,000,000) amount … for inflation to reflect the percentage change in the House Price Index for California for the prior calendar year, as determined by the Federal Housing Finance Agency … the annual percentage change … for 2024 was 2.15 percent." | [BOE LTA 2025/009 (PDF)](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) |
| 8 | Prop 13 inflation factor: lesser of California CPI or 2%; 2026-27 factor 1.02 (CCPI +3.307%) | **Match** | "please prepare your **2026** assessment roll using an inflation factor of **1.02**"; table row "2026-27 \| 3.307 \| 2% \| 1.02" | [BOE LTA 2026/002 (PDF)](https://www.boe.ca.gov/proptaxes/pdf/lta26002.pdf) |
| 9 | Trustee notification due within 60 days of death | **Match** | §16061.7(f): "The notification by trustee shall be served not later than 60 days following the occurrence of the event requiring service of the notification by trustee" | [Probate Code §16061.7](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=16061.7) |
| 10 | Change-in-ownership statement for property held in trust due within 150 days of death | **Match** | §480(b): "including a transfer through the medium of a trust, the change in ownership statement or statements shall be filed by the trustee (if the property was held in trust) or the transferee … within 150 days after the date of death." | [Revenue & Taxation Code §480](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=480) |
| 11 | San Francisco secured property tax rate FY 2026-27 = 1.18162182% | **Match** | "The secured property tax rate for Fiscal Year 2026-27 is 1.18162182%." | [SF Treasurer & Tax Collector](https://sftreasurer.org/property/secured-property-taxes) |
| 12 | SF flat parcel charges FY 2025-26: School Parcel Tax of 2020 $334.38; SFUSD Teacher Support $319.34; SFUSD Facilities $21.50 per unit (multi-family); City College $99; Bay Restoration $12 | **Match** (all five) | "$334.38 parcel tax in FY 2025–26 and adjusted for inflation annually"; "$319.34 parcel tax in FY 2025-26"; "$21.50 per dwelling unit on multi-family residential parcels in FY 2025-26"; "$99 per year and adjusted for inflation annually"; "$12 per year" | [SF Treasurer — Parcel Taxes](https://sftreasurer.org/property/parcel-tax-exemptions-and-special-assessments) |
| 13 | SF allowable rent increase 1.6% (1 Mar 2026 – 28 Feb 2027); 1.4% (2025-26); 1.7% (2024-25) | **Match** (by direct fetch; session `11bffb54` had it via a search result) | Table "Allowable rent increase": "March 1, 2026 – February 28, 2027 \| 1.6%" | [SF Rent Board — Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) |
| 14 | Owner move-in relocation: $8,245 per tenant, max $24,733 per unit, plus $5,497 for each elderly/disabled tenant or household with minor children | **Match** (all three, to the cent) | Table row "3/01/26 – 2/28/27 \| $8,245.00 \| $24,733.00 \| $5,497.00" | [SF Rent Board — Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) |
| 15 | Board of Supervisors File No. 261020 is **pending, not enacted**: would cap combined banked + capital-improvement increases at 10%/year for increases noticed or petitions filed on/after 15 Sep 2026 | **Match** | "**This legislation has not been enacted and is subject to change.**" | [SF Rent Board — Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) |
| 16 | SF Rent Board fee $59.00 per dwelling unit for 2026-27, due 1 March; paid directly by owners since 2022 | **Match** | "For the 2026-2027 tax year, the fee is: **$59.00 per dwelling unit**"; "owners must pay this fee to the Rent Board directly as of 2022"; "Deadline: **March 1**" | [SF.gov — The Rent Board Fee](https://www.sf.gov/rent-board-fee) |
| 17 | Cupertino water: quantity rate and service charge up about 2.8% from 1 Jan 2026, plus a Valley Water wholesale increase from 1 Jul 2026 | **Match** | "Year 2 of our 2025-27 GRC Filing shows an increase in the quantity rate and service charge of approximately 2.8%, effective January 1"; "Valley Water … is increasing its water rates effective July 1, 2026." | [San Jose Water — 2026 Rates](https://www.sjwater.com/2026Rates) |
| 18 | HUD FY2026 Small Area FMR, ZIP 95014: 4-bedroom $6,390; 3-bedroom $5,870 | **Match** | "Efficiency $3,340 \| One-Bedroom $3,800 \| Two-Bedroom $4,440 \| Three-Bedroom $5,870 \| Four-Bedroom $6,390" | [HUD FY2026 SAFMR calculation, 95014](https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=95014&year=2026) |

**Not re-opened by this session** (status is the one given by the session that added it; no claim is made here):
SFPUC proposed water/sewer rates, Santa Clara County tax-rate book components, HUD SAFMR for ZIP 94122,
CDI statewide residential insurance experience, IRC §1014 / §121 / §1411 / Form 706 pages, and the
California Secretary of State ballot-measure returns. Two of these were attempted and are recorded in §5.

---

## 3. Independent arithmetic and consistency checks

These are checks this session computed from scratch, not re-runs of another session's validator.

| Check | Method | Result |
|---|---|---|
| Household tax/assessment history rounded to the nearest $10 | Recomputed all 52 published values from the owner-supplied exact figures using round-half-up to $10, and compared with `site/verification.html` | **52 / 52 correct.** No rounding error. Convention is half-up (e.g. `x,565 → x,570`, `x,x05 → x,x10`) and is applied consistently |
| BOE Prop 13 factor table (51 roll years, 1976-77 … 2026-27) | Transcribed the official table from LTA 2026/002 by hand and diffed every CCPI percentage and every factor against `qa/series.json` | **51 / 51 rows match exactly.** No missing, extra or altered row |
| Site claim: "The assessed-value changes match the Board of Equalization's factor in every year" | Compared each of the 13 household assessment changes (2014–2026) with the official factor for that roll year | **Confirmed, 13 / 13.** 2014 +0.5% vs official 0.454%; 2016 +1.5% vs 1.525%; 2021 +1% vs 1.036%; the other ten +2% vs factor 1.02 |
| Site claim: "the tax bills do not move with the assessment" | Compared household tax-bill changes with the assessment changes | **Confirmed.** The two series diverge in most years, which is what flat direct charges and exemptions produce |
| Site claim: 2021 Property B bill drop "consistent with the Rent Board fee leaving the tax bill" | Checked the official fee page | **Confirmed.** "While this fee was previously collected on the property tax bill, owners must pay this fee to the Rent Board directly as of 2022." The 2021 bill fell 5.9% while its assessment rose 1% |
| Property B three-unit parcel-tax total $829.22 | Summed the five official amounts for a 3-unit multi-family parcel | **Confirmed exactly**: 334.38 + 319.34 + (3 × 21.50 = 64.50) + 99 + 12 = **829.22** |
| Derived stats rendered on the Verified facts page | Recomputed from the official 51-row table | 2% cap applied in **40 of 51** rolls; geometric-average factor **+1.81% a year**. Both consistent with the page's own formulas |
| Base-case decision output | Re-ran the model on the merged tree | sell **$7,683,290** · rent **$6,249,830** · live **$5,135,780** (2040 inheritance, 2050 endpoint). The `live` figure moved from $5,196,300 (pre-PR #20) because of the HPI-indexed Prop 19 cap; that is an intended correction, not a regression |
| Publication payload = allowlist | Enumerated every git-tracked file, applied `_config.yml` exclusions, and diffed against the `_public/` artifact from `scripts/package-site.py` | **24 files each side, identical set** (only `.gitignore` and `_config.yml` differ, and Jekyll consumes those). `qa/**` and `verification/**` are now excluded, so no internal audit file is served |
| Privacy headers | Grepped every published page | All **13** pages carry `<meta name="robots" content="noindex,nofollow,noarchive">` |
| Navigation completeness | Cross-checked every published page against `assets/app.js` | All **13** pages are reachable from the shared navigation; no orphan page |

---

## 4. Privacy audit

| Check | Method | Result |
|---|---|---|
| Exact household figures in the current `main` tree | Scanned every git-tracked file on `main` for all 40 owner-supplied figures that $10-rounding actually obscures (both comma and plain forms, 80 patterns) | **0 hits.** The published tree and the working tree contain no exact household amount that rounding was meant to hide |
| Exact household figures in the published artifact | Same scan over `_public/` | **0 hits** |
| Personal identifiers | Grepped published pages for names, street addresses, parcel numbers (APN), account numbers, emails, phone numbers | **None found.** Parties are "Property A" / "Property B"; the only phone numbers published are government contact numbers on official-source citations |
| Search-engine exposure | Grepped every published page | All 13 carry `noindex,nofollow,noarchive` |
| Internal audit files served publicly | Compared served payload with the allowlist | `qa/**` and `verification/**` are now excluded by `_config.yml`; **no internal file is served** |
| Unmerged public branch tips | Scanned `origin/arena/5a1bd5be-tino2` (public, never merged) for the 40 distinct values that $10-rounding actually obscures | **All 40 are present**, in 5 files: `index.html`, `model/projections.html`, `site/inheritance.html`, `site/properties.html`, `site/sources.html`. See irregularity D-I-2 |
| Public git history | Could not be scanned: this clone is shallow (`.git/shallow`), so historical commits are not available locally | **Not established either way.** Prior sessions documented that exact figures exist in commits `be7733d` and `6e3fb83`; this session neither confirms nor denies it and does not claim history is clean |

## 5. Brief-coverage check (household inputs the owner supplied)

Each owner-supplied figure was traced into `site/data/model.js` `MODEL.BASE`. All ten are present, and
range inputs use the midpoint of the owner's stated range.

| Owner input | Model field | Value used | Check |
|---|---|---|---|
| Cupertino water $100–$150 / month | `aWaterMonthly` | 125 | midpoint of the stated range |
| Solar credit, profit $10–$20 / month | `aSolarMonthlyCredit` | 15 | midpoint of the stated range |
| Cupertino insurance "around $1,500" | `aInsuranceAnnual` | 1500 | owner's guess; ledger `INS-02` is **unverified** and labelled so |
| SF water $330–$400 / month (3 units) | `bWaterMonthly` | 365 | midpoint of the stated range |
| SF electricity $30–$70 / month | `bElectricMonthly` | 50 | midpoint of the stated range |
| SF insurance "somewhere around $1,500" | `bInsuranceAnnual` | 1500 | owner's guess; ledger `INS-03` is **unverified** and labelled so |
| SF rental income ~$7,150 / month (2 units) | `bRentMonthly` | 7150 | as supplied |
| Cupertino value $3,100,000 (Nov 2026) | `aValue` | 3100000 | as supplied, labelled a household input, not an appraisal |
| SF value $1,800,000 (Nov 2026) | `bValue` | 1800000 | as supplied |
| 2026 Cupertino assessment / 2025 SF assessment | `aAssessed`, `bAssessed2025` | 550540, 114250 | rounded to $10 (verified correct in §3) |

**No owner-supplied input is missing from the model, and none is silently altered.**

---

## 6. Irregularity register

Severity: **High** = privacy or a figure the decision turns on. **Medium** = a published claim that needs a
qualifier or a correction. **Low** = cosmetic or immaterial to the result. None of these blocks publication;
all are logged as requests to the owner of the file, because this session's scope forbids editing them.

### D-I-1 — HIGH — $10 rounding cannot anonymise three of the owner's figures (inherent, not a mistake)

The brief asks for figures to be rounded to $10 "so it cannot be traced back to the source or traced online
through search". Three of the 43 owner-supplied amounts are **already exact multiples of $10**, so their
rounded form equals the exact value and remains searchable as-is:

- Property A, **2020 assessed value**
- Property A, **2015 property tax**
- Property B, **2017 property tax**

They are published in that form in `site/verification.html` (and mirrored in `qa/ledger.json`,
`site/data/ledger.js` — both now excluded from Pages, and in legacy excluded files). Rounding is correct per
the brief; the brief's stated *purpose* is simply unachievable for these three values.
**Owner decision needed:** band them (e.g. publish "≈$493,500" or a range), drop those three rows, or accept
the exposure. No file was edited by this session.

### D-I-2 — HIGH — exact household figures remain publicly retrievable from an unmerged branch tip

`main` is clean (§4: 0 hits), but the public branch `arena/5a1bd5be-tino2` still serves **all 40** exact
figures in 5 files. Deleting them from `main` does not remove them: the repository is public, the branch tip
is readable, and prior sessions recorded that the same figures also exist in historical commits
(`be7733d`, `6e3fb83`) — this session could not scan history locally because the clone is shallow, and does
**not** claim history is clean.
**Owner decision needed** (same three options session `11bffb54` recorded, plus one): make the repository
private; start a fresh repository from the current files; ask GitHub Support to purge; **or delete the
stale unmerged branch tips**, which is the cheapest partial mitigation and is the only one that can be done
inside GitHub's normal tooling. Branch deletion is outside this session's scope.

### D-I-3 — RESOLVED while this session was working — the publication privacy guard was incomplete, and has since been replaced by a stronger one

**What this session found, and when.** On `main` at `815289a` (the commit this branch started from),
`scripts/package-site.py` guarded publication with a hard-coded set of **four** unsalted SHA-256 hashes of
exact private amounts. This session hashed all **40** distinct owner-supplied figures that $10-rounding can
actually obscure and found only **4** were covered: the other **36** would have passed the guard silently if
reintroduced. That was logged as a MEDIUM privacy irregularity.

**Already fixed on the current tree, by a better method.** PRs #20/#26 (sessions `f16e6e34` / `11bffb54`)
removed the hash set entirely. The script's own docstring gives the reason, which this session confirms is
correct and is a sharper point than the coverage gap: *"Hashes of 4- and 6-digit numbers can be reversed by
trying every number, so the hashes re-published the amounts."* An unsalted hash of a 6-digit dollar amount is
trivially invertible, so the old guard was itself a disclosure. It is replaced by a **rule** that stores no
household data at all: any dollar amount of $1,000 or more in a published file must be a multiple of $10
unless it is an official figure listed in `qa/ledger.json`.

**This session then tested the replacement rather than trusting it.** Replicating the rule's allowlist
derivation over `qa/ledger.json` (114 official figures) and testing all 40 exact household values against it:

- values the allowlist would **wrongly** permit: **0 of 40**
- values the rule **would catch**: **40 of 40**
- values below the rule's $1,000 threshold: **none** (the smallest owner-supplied figure is above it)

`python3 scripts/package-site.py` exits 0, and PR #28's CI workflow `.github/workflows/pages.yml` now runs it
on every push and pull request to `main`, together with `scripts/check-publication.py --self-test`,
`node scripts/validate.js`, `node scripts/stress-test.js`, `node scripts/runtime-test.cjs` and — importantly —
a real `actions/jekyll-build-pages` build whose `_site` output is audited against the allowlist.
The workflow's last four runs on `main` all concluded **success**.

**Net effect: the finding is closed, and the remaining gap this session had identified — that the allowlisted
`_public/` artifact was not proof of what Jekyll actually serves — is closed too**, because CI now audits the
real Jekyll output. No action requested. Recorded so the audit trail shows the guard was tested, not assumed.

### D-I-4 — MEDIUM — SF Rent Board fee: the owner-unit exemption is **not** automatic, and has a filing deadline

The base model charges `bRentBoardFeeAnnual = 118` (2 × $59) and `site/san-francisco.html` discloses
"$59 × 2; exemption assumed for owner unit … charging all three units would add $59". The disclosure is
honest and the magnitude is right, but the official page adds two conditions the site does not state:

- **Vacant units are charged.** "All residential property owners must pay a per-unit Rent Board fee unless
  the unit(s) have a current exemption. **This includes … vacant units**, and units occupied by friends or
  family members." The third unit is currently vacant, so today's correct charge is **$177 (3 × $59)**, not $118.
- **The exemption must be applied for, by a deadline.** "**you must submit a Request for Exemption**" between
  October and early December; "The deadline to submit a Request for Exemption for the 2027 Rent Board fee is
  **December 14, 2026**." It also requires owner-of-record occupancy with the unit "not rented at any time".
- **Half is recoverable from tenants.** "you can recover 50 percent of the fee from the tenants … $29.50 per
  dwelling unit", if the tenant was in occupancy as of 1 November. The model charges the full fee and books
  no recovery, so it is conservative by up to $59 a year.

Source: [SF.gov — The Rent Board Fee](https://www.sf.gov/rent-board-fee), opened 2026-11-11.
**Request:** owner of `site/san-francisco.html` / `site/data/model.js` to add the 14 December 2026 filing
deadline and the vacancy rule. Immaterial to the Property A ranking ($59 a year), but it is an actionable
calendar date for the owner.

### D-I-5 — MEDIUM — the rent-growth assumption runs above the latest official change in the same benchmark

Property A's rent uses HUD's FY2026 SAFMR for ZIP 95014 and grows it at `rentGrowth = 3%` a year. The same
official page publishes the prior year, so the actual year-over-year change is visible:

| SAFMR 95014 | FY2025 | FY2026 | Change |
|---|---|---|---|
| Efficiency | $3,410 | $3,340 | **−2.1%** |
| 1-bedroom | $3,880 | $3,800 | **−2.1%** |
| 2-bedroom | $4,500 | $4,440 | **−1.3%** |
| 3-bedroom | $5,850 | $5,870 | +0.3% |
| 4-bedroom | $6,370 | $6,390 | **+0.3%** |

Source: [HUD FY2026 SAFMR calculation for 95014](https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=95014&year=2026), opened 2026-11-11.
The 4-bedroom benchmark the model rents Property A at rose **0.3%** in the latest official year, and every
smaller unit **fell**. The site already labels 3% as an assumption, so nothing is wrong — but the assumption
is roughly ten times the latest official movement in its own benchmark, and the rent case is the one the site
calls "highly sensitive to achievable rent". **Request:** show the FY2025→FY2026 official change next to the
3% assumption on the Decision and Properties pages, or add a 0.3% rent-growth stress row.

### D-I-6 — MEDIUM — Proposition 3 result is published as an unofficial snapshot percentage

`qa/ledger.json` CA-05/06/07 publish the November 2026 ballot outcomes with specific percentages
("Passing — Yes 60.6%", "Yes 51.5%", "No 52.6% / No 57%"), each labelled "in the unofficial count".
That label is honest, but the number moves with the count: this session found **58.66%** (CBS 8, 4 Nov
02:59 PT), **60.5%** (AP call via KQED) and **59.9%** (Secretary of State count as of 6 Nov, reported by
californiatoday.com). The Secretary of State **certifies on 11 December 2026**.
The *substance* is not in doubt and is the part the decision depends on: **Prop 3 passed**, so the 10.3% /
11.3% / 12.3% high-income rates become permanent instead of sunsetting, and **Prop 40 (one-time wealth tax)
is failing**. California still taxes capital gains as ordinary income, which is what the sell-and-reinvest
case is priced on.
**Request:** owner of `qa/ledger.json` / `site/verification.html` to replace the decimal percentage with
"passed — unofficial count; certified 11 December 2026", so the figure cannot go stale. Note: this session
could not open `electionresults.sos.ca.gov` directly (see D-I-8), so the outcome above rests on press
reporting of the official count and is labelled accordingly — it is **not** an official-source match.

### D-I-7 — LOW — Ellis Act relocation amounts are materially higher and are not on the plan page

`site/plan.html` prices "taking the unit back later" using owner move-in relocation
($8,245 / $24,733 / $5,497 — verified in §2). If the owner ever considered permanently removing units from
rental use instead, the **Ellis Act** schedule applies and is much larger:
**$11,110.05 per tenant, $33,330.13 maximum per unit, plus $7,443.90** for each elderly (62+) or disabled
tenant, for notices served 1 Mar 2026 – 28 Feb 2027.
Source: [SF Rent Board — Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit), opened 2026-11-11.
**Request:** add as a context row; it is the difference between the two legal routes to reclaiming Property B.

### D-I-8 — LOW — two official pages could not be opened from this sandbox; recorded as gaps, not as passes

Direct fetches of the **SFPUC Proposition 218 rate notice** (UT-03) and the **California Secretary of State
ballot-measure returns** (CA-05/06/07) failed repeatedly with a proxy signature error (`SignatureDoesNotMatch`)
after 14 successful official fetches. Those two facts keep the status given by the session that added them.
This session does **not** claim to have verified them.

### D-I-9 — LOW — the two privacy gates disagree, because the older one's allowlist is stale

`integration/tools/privacy_scan.py` reports **102 warnings / 0 errors**. This session inspected every warning
in the *published* files: they are all **official** amounts, not household data —
SF Rent Board relocation payments ($8,245 / $24,733 / $5,497), a BOE Letter to Assessors worked example
(its Q50 factored base year value, value cap and excess), the California income-tax bracket thresholds, and
CDI statewide premium aggregates. The scanner allowlists against `integration/ledger/facts.jsonl`, which
predates `qa/ledger.json`, so it does not know the newer official figures. `qa/tools/gate.cjs` allowlists 54
official exact figures and reports **0 errors, 0 warnings** on the same tree.
**Request:** owners of `integration/**` (`7eeb5f71`) and `qa/**` (`11bffb54`) to sync the two allowlists, or
retire the older scanner, so a clean run is unambiguous.

### D-I-10 — LOW — two of the owner's own stated percentages differ slightly from their own dollar history

Recomputing the owner's percentage changes from the owner's dollar history gives **+2.9%** where the brief
states **+2.8%** for the Property A 2019 tax bill, and **+5.4%** where the brief states **+5.3%** for the
Property B 2025 tax bill. Both are tenth-of-a-point rounding in the brief, not site errors:
`site/verification.html` publishes the percentages "exactly as supplied", which is the right call.
Recorded so that nobody later "corrects" the site to the recomputed values. The site's substantive claim —
that **assessed-value** changes match the official BOE factor in every year — is confirmed (13/13, §3);
both discrepancies are in tax bills, which the site explicitly says do not track the assessment.

### D-I-11 — LOW — cosmetic

`_config.yml` lists `assets/style.css-alternate.css` twice. Harmless (Jekyll de-duplicates), owner: whoever
next edits `_config.yml`.

---

## 7. Does the verified evidence support the published recommendation?

The site recommends **selling Property A at inheritance and reinvesting the net proceeds**, with the explicit
caveat that this is a financial result and not an instruction. This session did not re-derive the
recommendation; it checked whether the **verified** legal and rate facts point the same way. They do, and the
reason is worth stating plainly because it is the hinge of the whole analysis:

| Verified fact | Official source (§2) | Effect on the ranking |
|---|---|---|
| Prop 19 preserves the low assessment **only** if the home is the principal residence of the transferor **and** the transferee; it "eliminates exclusion for other real property other than the principal residence" | BOE Prop 19 chart (#5) | **Renting Property A gets no exclusion at all.** It is reassessed to full market value on transfer. This is the single largest driver of the rent case's weakness |
| Prop 19 value cap = factored base year value + $1,044,586 (transfers 16 Feb 2025 – 15 Feb 2027), and the formula is market value − exclusion when the cap is below market value | BOE LTA 2025/009 (#6, #7) | The **live** case keeps a low base; on a $3,100,000-class home the preserved benefit is large, but the site correctly notes the heir must actually occupy it and file |
| Property A's assessed value is roughly one sixth of its market value | owner input, rounding verified (#3) | Losing Prop 19 multiplies the tax base several times over — which is why the rent case's first-year after-tax cash is the weakest of the three |
| Prop 13 caps annual growth at the lesser of California CPI or 2%; factor 1.02 for 2026-27 | BOE LTA 2026/002 (#8) | Once reassessed, the bill still only grows ~2% a year, so the rent case is not catastrophic — it is a level shift, not a slope change |
| No California estate-tax return for deaths on/after 1 Jan 2005 | State Controller (#4) | No state estate tax to plan around; the only estate exposure is federal |
| Federal basic exclusion $15,000,000 (2026), $15,480,000 (2027) | IRS (#1, #2) | Property A alone sits far below the threshold. The brief's "considerable amount of money" is what could breach it — and the site correctly leaves the actual estate tax **blank** because the gross estate, gifts and DSUE are unknown |
| Trustee notice 60 days; change-in-ownership statement 150 days for property held in trust | Prob. Code §16061.7 (#9), R&TC §480 (#10) | The step-by-step inheritance path is correct on both clocks, and the trust route does **not** avoid the assessor filing |
| SF rate 1.18162182% FY 2026-27 and $829.22 of flat parcel charges for three units | SF Treasurer (#11, #12) | Property B's carrying cost is verified, so "keep B" rests on real numbers rather than an estimate |
| SF rent increases are capped at 1.6% while the building's costs rise faster | SF Rent Board (#13, #16) | Confirms the site's point that Property B's income grows more slowly than its expenses — a reason not to buy more SF rental exposure with Property A proceeds |

**Conclusion.** Every verified fact is consistent with the published ranking, and the two facts that decide it
— Prop 19's principal-residence condition, and the gap between Property A's assessment and its market value —
are both confirmed on official pages this session opened. The recommendation does not rest on an unverified
figure. What it *does* rest on that remains unverified is: the insurance premiums (both $1,500 guesses),
Property A's actual tax-rate area and direct charges (the model uses a hypothetical 1.2% levy), the
achievable rent, and the full composition of the estate. All four are already flagged on the site.

---

## 8. Summary of requests to file owners

Logged in `COORDINATION.md` (session `d9c69069` block). None was applied by editing another session's file.

| Ref | Requested of | File(s) | Ask |
|---|---|---|---|
| D-I-1 | owner / repo owner | `site/verification.html` | Decide whether to band or drop the three figures that are already multiples of $10 |
| D-I-2 | repo owner | branch `arena/5a1bd5be-tino2`, git history | Delete stale public branch tips; decide on private repo / fresh repo / GitHub Support purge |
| D-I-3 | `11bffb54` (took over `scripts/`) | `scripts/package-site.py` | Extend `FORBIDDEN_HASHES` from 4 to all 40 exact household values |
| D-I-4 | `11bffb54` | `site/san-francisco.html`, `site/data/model.js` | State that vacant units are charged and that the exemption request is due **14 December 2026** |
| D-I-5 | `11bffb54` | `site/decision.html`, `site/properties.html` | Show the official FY2025→FY2026 SAFMR change (+0.3% for 4-bedroom) beside the 3% rent assumption |
| D-I-6 | `11bffb54` | `qa/ledger.json`, `site/verification.html` | Replace snapshot ballot percentages with "passed — unofficial; certified 11 December 2026" |
| D-I-7 | `11bffb54` | `site/plan.html` | Add Ellis Act relocation amounts as context ($11,110.05 / $33,330.13 / $7,443.90) |
| D-I-9 | `7eeb5f71`, `11bffb54` | `integration/tools/privacy_scan.py`, `integration/ledger/facts.jsonl` | Sync or retire the stale allowlist so a clean run is unambiguous |
| D-I-11 | next editor of `_config.yml` | `_config.yml` | Remove the duplicated `assets/style.css-alternate.css` line |

## 9. Verdict

The published site is **sound and safe to leave live**. On the merged tree:

- 6/6 automated checks PASS, including the rendered-page gate (13 pages, 963 rows, 0 errors, 0 warnings);
- **18 of 18** official-source re-checks performed by this session **Match**, each by direct fetch with the
  wording recorded above;
- every arithmetic check this session recomputed from scratch passes: **52/52** rounding, **51/51** BOE factor
  rows, **13/13** household assessment changes against the official factor, and the **$829.22** parcel-tax sum
  to the cent;
- **no exact household figure** that rounding can obscure appears anywhere in `main` or in the published
  artifact, and the served payload is byte-for-byte the allowlisted set (24 files);
- all 13 pages are `noindex,nofollow,noarchive`, all 13 are in the navigation, no orphan pages.

The open items are the ones the site already flags plus the eleven recorded here. The two **High** items are
both about exposure that predates the current tree — figures already multiples of $10, and figures still
reachable on a stale public branch and in git history. Neither can be fixed by editing the site, and neither
blocks publication. Nothing in this report is inferred: where a value could not be confirmed from an official
source this session, it is marked as not re-opened (§2) or as a fetch failure (D-I-8).

## 10. Publication record

_Filled in after the pull request is merged — see `COORDINATION.md`, session `d9c69069` block._
