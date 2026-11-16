# Verification report — session `070d6a2e` (pre-commitment register + 16 Nov 2026 recheck)

**Checked:** 16 November 2026 (UTC). **State read at claim:** `origin/main` = `ace7057` (merge of PR #126);
this branch was level with `8b27103` and its working tree clean. One open pull request at claim time (**#119**,
last push 2026-11-16 01:07 UTC, stale past the 60-minute rule) — taken over, see §4.

**Scope.** (1) Close the deployment item session `9ad78d96` left open. (2) Dated re-read of the official pages the new
pre-commitment register relies on. (3) Publish the register itself (`guide/precommit.html`). (4) Take over PR #119.
No household value, rent, bill, identifier or ZIP code is written in this file; all page content stays synthetic or
government-published.

## 1. Deployment item left open by session `9ad78d96` — CLOSED

That session recorded that the privacy-remediated guide was merged but that live Pages still served the earlier
household-figure version, and asked that the item stay flagged until a successful deployment and a fresh read-back
showed the inputs withheld.

| Check | Result |
|---|---|
| `GET /repos/wingbangboozle1-lang/Tino2/pages/builds/latest` on 16 Nov 2026 | commit `ace7057`, status **built** |
| Live read-back of `https://wingbangboozle1-lang.github.io/Tino2/guide/property.html` on 16 Nov 2026 | Serves the synthetic-only version: the notice reads “Only synthetic example inputs are used…”, the property table reads “— private appraisal required”, and no household amount appears. |

**Conclusion:** the item is closed. No code change was needed for it; the evidence is the API status plus the live page.

## 2. Official pages opened and read on 16 November 2026

Every row below was opened in this session at the URL given and read; the column on the right is what the page
states in the words used on the new page. Nothing here is inherited from a previous session's report.

| # | Official page | What was read (as the page states it) | Use on the site |
|---|---|---|---|
| 1 | [CA RTC §63.2, leginfo](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=63.2) | “(b) The exclusions provided for in this section shall not be allowed unless a claim for the exclusion sought, pursuant to subdivision (f), is filed with the assessor.” Also (a)(1)(A): the transfer must be of the transferor’s principal residence and become the transferee’s principal residence within one year; (a)(1)(B): the transferee files for the homeowners’ or disabled veterans’ exemption within a year. | “Claimed, not automatic” rule row |
| 2 | [BOE Proposition 19 comparison charts](https://www.boe.ca.gov/prop19/) | “File for homeowners’ exemption within 1 year of transfer”; “File claim for exclusion within 3 years or before transfer to third party”; value limit = current taxable value plus $1,000,000 “(as biennially adjusted)”; implementing statute RTC §63.2. | Claim windows; cadence |
| 3 | [BOE LTA 2025/009 (PDF)](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) | Intergenerational transfer exclusion: $1,000,000 for 16 Feb 2021–15 Feb 2023, $1,022,600 for 16 Feb 2023–15 Feb 2025, **$1,044,586** for 16 Feb 2025–15 Feb 2027; adjustment “every other February 16”; 2024 California HPI change 2.15%. | Prop 19 allowance figures (unchanged) |
| 4 | [BOE 2026 Letters to Assessors index](https://www.boe.ca.gov/proptaxes/2026.htm) | Lists **2026/026 — Proposition 19 Intergenerational Transfer Exclusion Frequently Asked Questions and Answers** as the current published exclusion guidance, plus the 2026 series (2026/002 the 2026-27 CPI factor). | Confirms the Q&amp;A is current; source added to the register |
| 5 | [BOE LTA 2026/026 (PDF)](https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf) | “two claim forms must be filed”: exemption claim within one year; exclusion claim within three years or before a third-party transfer, whichever is earlier; a claim is timely if filed no later than six months after a supplementary or escape notice; after all deadlines, “prospective relief only”; the home must be “continually used” and if it becomes ineligible “the exclusion will be removed” with the new base-year value enrolled on the following lien date. | Continued-use and claim-window rows |
| 6 | [IRS, Estate tax](https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax) | “A filing is required if the gross estate of the decedent, increased by the decedent’s adjusted taxable gifts and specific gift tax exemption, is valued at more than the filing threshold for the year of the decedent’s death”; filing-threshold table: 2025 $13,990,000, **2026 $15,000,000**. | Filing-test row (unchanged figure, re-read) |
| 7 | [CA State Controller, California Estate Tax](https://www.sco.ca.gov/ardtax_estate_tax.html) | “For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return”; inheritance tax collected only for decedents who died before 8 June 1982. | California row |
| 8 | [FTB, 2025 Form 540 rate schedules (PDF)](https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf) | Schedule X: 12.30% “AND OVER” $742,953; Schedule Y: 12.30% over **$1,485,906**; Schedule Z: 12.30% over **$1,010,417**. | Capital-gain row |
| 9 | [FTB, 2025 Instructions for Form 540](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html) | Line 62 “Behavioral Health Services Tax”: “If your taxable income is more than $1,000,000”, worksheet = (line 19 − $1,000,000) × 1%. | Surcharge row; the guide's 13.3% combined top rate is derived from these two published items |
| 10 | [IRS Topic 701, Sale of your home](https://www.irs.gov/taxtopics/tc701) | Up to $250,000 of gain excluded ($500,000 joint); ownership test 24 months of the last 5 years, use test 24 months of the previous 5 years; the exclusion applies to a main home. | Home-sale exclusion row |
| 11 | [26 U.S.C. §1031 (Cornell LII)](https://www.law.cornell.edu/uscode/text/26/1031) | Like-kind exchange applies to real property exchanged for real property; 45-day identification, 180-day completion. | Like-kind row |
| 12 | [26 U.S.C. §6075(a) (Cornell LII)](https://www.law.cornell.edu/uscode/text/26/6075) | “Returns made under section 6018(a) … shall be filed within 9 months after the date of the decedent’s death.” | Filing-deadline row |
| 13 | [IRS, Instructions for Form 706 (07/2026)](https://www.irs.gov/instructions/i706) | Confirms a “Portability election” section, a “Table of Basic Exclusion Amounts” and a “When To File” section; the return is due nine months after death (statute cited above). Text-level amounts were not extracted from this long page in this session; the $15,000,000 / $15,480,000 figures stay on their existing ledger records. | Portability row (qualitative only) |
| 14 | [CA Department of Insurance, Compare Insurance Premiums](https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/) | “The results of these surveys are not premium quotes”; “The California Department of Insurance is a regulatory agency and not an insurance agent. As such, we cannot provide actual quotes.” | Insurance-quote rule row |
| 15 | [HUD USER, Small Area Fair Market Rents](https://www.huduser.gov/portal/datasets/fmr/smallarea/index.html) | “SAFMRs are FMRs calculated for ZIP Codes. Small Area FMRs are required to be used to set Section 8 Housing Choice Voucher payment standards…” | Rent-benchmark rule row |
| 16 | [SF Rent Board, current rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | 1.6% allowable increase for 1 Mar 2026–28 Feb 2027; notice posted 9 November 2026: Board of Supervisors File No. 261020 “has not been enacted and is subject to change”. | Proposed-is-not-law row |
| 17 | [Congress.gov, H.R.1301](https://www.congress.gov/bill/119th-congress/house-bill/1301) | Status **Introduced**; latest action 02/13/2025 “Referred to the House Committee on Ways and Means”. | Enacted-vs-proposed context |
| 18 | [Santa Clara County Controller-Treasurer, Property Tax Rate Book archive](https://controller.santaclaracounty.gov/property-tax-distribution/property-tax-rate-book) | Archive lists FY2025-26 as the most recent rate book; no FY2026-27 book posted as of this read date. | Confirms the guide's “FY2026-27 not yet posted” statement still holds on 16 Nov 2026 |

### Two things deliberately NOT added

- **A “HUD-calculated” characterisation of SAFMRs.** A secondary description was seen in a search excerpt; the HUD
  page above does not use that wording, so the page says only what HUD says.
- **The HUD Housing Choice Voucher Guidebook chapter 7 URL** was opened and resolved to the HUD home page rather than
  to the chapter. It was removed from the source dictionary before any page used it. No claim depends on it.

## 3. What the register asserts, and how each assertion is bounded

The new page is deliberately thin on numbers: the only figures it prints are government-published ones already in the
figure ledger. Every household-specific threshold is blank or generic.

| Kind of statement on the page | Example | Bound |
|---|---|---|
| Enacted rule, quoted | “shall not be allowed unless a claim … is filed with the assessor” | Row 1 above; link on every row |
| Enacted amount | 12.30% top schedule rate; 1% above $1,000,000; $1,044,586 allowance | Rows 3, 8, 9; ledger records |
| Agency caveat | “these surveys are not premium quotes” | Row 14 |
| Proposed, not law | File 261020 “has not been enacted” | Row 16 |
| Household threshold | occupancy years, rent floor, allowance, review date | **Blank.** “Household sets in writing”; no figure published |
| Model output | rent break-even crossing point | **Blank.** “— to be computed privately”; the page states plainly that some crossings are not computed on the public site |

## 4. PR #119 takeover (60-minute rule)

`gh pr view 119` on 16 Nov 2026: opened 2026-11-16T01:07:41Z, last push 2026-11-16T01:07Z, branch
`arena/84257489-tino2`, two files (`COORDINATION.md` +14, `verification/84257489/REPORT.md` +48), check run
`43784400266` **success**. The owning session did not merge it. Its content is a dated cross-check record of the same
figures this session re-read independently; nothing in it conflicts with this work. It is taken over: its report is
preserved verbatim in the tree and its work is superseded by §2 above, not discarded.

## 5. Local suite on the final tree

| Check | Result |
|---|---|
| `check-generated.py` | PASS — 19 generated public pages up to date |
| `package-site.py` | PASS — 33 reviewed files |
| `check-publication.py` (and `--self-test`) | PASS — 33 files + build marker; extra/missing/altered/symlink/hard-link rejected |
| `check-figures.py` | PASS — 39 ledger records, 39 verified, 0 unverified; every seven-figure amount has a record |
| `privacy-gate.py` (and `--self-test`) | PASS — 238 tracked files, no blocked identifier, no un-rounded household-scale amount |
| `test-guide.cjs` | PASS — **19 rendered pages, 1,101 source-linked rows, 12,793 checks**, including the new register invariants |
| `privacy-audit.cjs` | PASS — no hashed household token, locator or identifier in packaged source or rendered text |
| `test-model-reference.py` | PASS — 108 configurations, 250 stress years, 1,500 phased years, 20,736 comparisons |
| `test-phased.py` | PASS — 113 checks |
| `validate.js` | PASS — 1,612 checks across 19 pages, 178 official sources |
| `stress-test.js` | PASS — 50-year paths, ownership, privacy, real-dollar and shock tests |
| `test-browser.cjs` | Not run here: Chromium cannot launch in this sandbox (`libnss3.so` absent). It runs in CI on the PR. |

## 6. Irregularities found in this session

| # | Item | Severity | Disposition |
|---|---|---|---|
| I-1 | The guide's stamp read “re-opened 13–15 Nov 2026” while the pages re-read today are dated 16 Nov. | Low | **Fixed** — the stamp now reads 13–16 Nov 2026 and the sources note says which pages were re-read on 16 Nov. Figures themselves did not change. |
| I-2 | The IRS Instructions for Form 706 page is long; this session confirmed the portability, Table of Basic Exclusion Amounts and filing sections exist, but did not re-extract the dollar amounts from it. | Low | Amounts keep their existing ledger records and are **not** re-dated by this session. The register cites §6075 for the deadline and the IRS estate-tax page for the 2026 threshold, both re-read today. |
| I-3 | The 13.3% combined top California rate is a derivation (12.30% schedule + 1% line 62), not a published single rate. | Low (standing) | Already labelled as a computation on the Taxes page; the register repeats the two published inputs instead of the derived headline. |
| I-4 | The HUD guidebook URL resolved to the HUD home page. | Info | Removed before use; no claim depends on it. |
| I-5 | Standing owner/administrator items are unchanged: repository history scrub (L-D2), repository visibility, Property A's tax rate area and independent appraisal/comparables. | High (standing) | Not touched from this branch; still published on the Flagged page. |
