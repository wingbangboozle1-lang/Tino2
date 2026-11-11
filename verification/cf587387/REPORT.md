# Session `cf587387` — final integration and verification record

**Date:** 11 November 2026. **Branch:** `arena/cf587387-tino2`. **Base:** `main` at `d82fbee`.
**Role:** final integration for the content items no live session owned, plus independent re-verification of everything this session published.

> This file is repository-only. `verification/` is excluded from the published site by `_config.yml` and by `scripts/check-publication.py`, so nothing here reaches the public page. It contains no personal information and no unrounded household figure.

## 1. Coordination

| Item | Result |
|---|---|
| Board read in full | 14 session blocks, 13 earlier sessions |
| Live sessions at join | none — every remote `arena/*` branch last moved at or before 08:14 UTC, five hours before this session's claim at 13:15 UTC |
| Stale claim taken over | PR [#31](https://github.com/wingbangboozle1-lang/Tino2/pull/31) (session `4e07c8e6`, task X-7), head commit 08:14 UTC, still open, so its findings were not on `main` |
| Owner requests taken over | **D-I-4** (Rent Board owner-unit exemption), **D-I-5** (rent-growth assumption), **D-I-7** (Ellis Act relocation), all addressed to "the owner of `site/**`" with no live owner since 08:18 UTC |
| Method | Content commit `d645997` cherry-picked rather than the PR branch merged, because the branch predates PR #32 and #33 and would have dropped `verification/d9c69069/**` and the last board block. Its generated `qa/gate-report.json` was regenerated instead of taken. |

## 2. Official sources this session opened and read itself

Every row below was read on 11 November 2026. The wording quoted is what the page said; nothing is carried over from another session's record.

| # | Claim on the site | Finding at the source | Source |
|---|---|---|---|
| 1 | Basis resets at death only for property included in the estate | Rev. Rul. 2023-2 asks whether §1014 applies "to the assets of a trust on the death of the individual who is the owner of the trust … if the trust assets are not includible in the owner's gross estate"; §1014(b)(2)–(3) cover revocable and amendable trusts. Matches the published wording | [IRS Rev. Rul. 2023-2](https://www.irs.gov/pub/irs-drop/rr-23-02.pdf) |
| 2 | Federal exclusion $15,000,000 for 2026 and $15,480,000 for 2027 | "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from a total of $15,000,000 for estates of decedents who died in 2026." Form 706 instructions agree: "2026 | $15,000,000" | [IR-2026-133](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts), [Form 706 instructions](https://www.irs.gov/instructions/i706) |
| 3 | California imposes no inheritance or estate tax | "For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return." | [State Controller](https://www.sco.ca.gov/ardtax_estate_tax.html) |
| 4 | Prop 19 value cap $1,044,586 through 15 February 2027 | "the $1 million amount is adjusted to **$1,044,586** … for transfers that occur February 16, 2025 through February 15, 2027" | [BOE LTA 2025/009](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) |
| 5 | A house held in an LLC cannot use the parent-child exclusion | Q32: "this exclusion does not apply to transfers to or from legal entities"; Q33: "the Children inherited interests in the LLC, not real property"; Q34: "it is treated as a separate legal entity for California property tax purposes, is excluded from eligibility under section 63.2(e)(8)". Q11 defines real property as not including "any interest in a legal entity" | [BOE LTA 2026/026](https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf) |
| 6 | Prop 19 relief survives a care facility only if the house is not rented outside the immediate family | Q11 quotes §218(b)(4): the absentee owner is deemed to occupy the dwelling if they would occupy it but for the confinement, intend to return, and "the dwelling is not rented or leased to anyone other than an immediate family member" | [BOE LTA 2026/026, Q11](https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf) |
| 7 | San Francisco bills the Rent Board fee on vacant units, and the owner-unit exemption is not automatic | "This includes single-family homes and condominiums, units built after 1979, vacant units, and units occupied by friends or family members"; "The deadline to submit a Request for Exemption for the 2027 Rent Board fee is December 14, 2026"; fee for 2026–27 "$59.00 per dwelling unit"; "you can recover 50 percent of the fee … $29.50 per dwelling unit" | [SF.gov · The Rent Board Fee](https://www.sf.gov/rent-board-fee) |
| 8 | Ellis Act relocation is far larger than ordinary no-fault relocation | Ellis row 3/01/26–2/28/27: "$11,110.05" per tenant, "$33,330.13" maximum per unit, plus "$7,443.90" for each tenant 62+ or disabled. Ordinary row: "$8,245.00" / "$24,733.00" / "$5,497.00" | [SF.gov · Current rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) |
| 9 | The 3% rent-growth assumption is not wildly out of line with the model's own benchmark | ZIP-level 4-bedroom benchmark: FY2024 $6,050 → FY2025 $6,370 (+5.3%) → FY2026 $6,390 (+0.3%); 3-bedroom $5,480 → $5,850 → $5,870. About 2.8% a year compounded over two years | [HUD FY2026 SAFMR 95014](https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=95014&year=2026), [FY2025](https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2025_code/2025zip_code_calc.odn?zcta=95014&year=2025) |

## 3. Independent arithmetic

### 3.1 Equal-terms break-even thresholds

The published pair (7.8% home growth, 2.8% portfolio return) taxes the house's end-of-period gain but never taxes the portfolio. A separate script written by this session — its own bisection over the site's scenario engine, with the portfolio's unrealised appreciation charged at the same capital-gains rate and the rent plan's reinvested reserve treated the same way — produced:

| Threshold | Published (unequal terms) | Equal terms, this session | Engine function added to `scenarios.js` |
|---|---|---|---|
| Home growth at which renting overtakes selling | 7.81% | **5.32%** | 5.32% |
| After-tax portfolio return below which selling stops winning | 2.80% | **3.97%** | 3.97% |

Both pages now call one shared function (`SCENARIOS.breakEvenHomeGrowthEqualTerms`, `…PortfolioReturnEqualTerms`) so the Best plan page and the Black swans page cannot drift apart. The sell ranking survives on either basis: at the base case, equal-terms terminal values are sell $7,959,170 against rent $7,387,340.

### 3.2 Headline results unchanged

`node scripts/validate.js`: base case 2040→2050 remains **sell $7,683,290 · rent $6,249,830 · live $5,135,780**, exactly as before this session. No model input was changed.

### 3.3 Rent-growth question, corrected

A prior audit item said the 3% rent assumption was "about ten times" the latest official movement in its own benchmark. That compared one year only. HUD's own pages give a two-year record of +5.3% then +0.3%, about 2.8% a year compounded. The assumption is therefore close to the benchmark, not ten times it. The correction is published on the Flagged for Review page and in `qa/ledger.json` entries CF-01…CF-03; the model was not changed.

## 4. Verification suite on the final tree

| Check | Result |
|---|---|
| `node scripts/validate.js` | PASS — 853 checks, 14 pages, 126 official sources |
| `node scripts/stress-test.js` | PASS — 50-year paths, estate ownership, privacy, real-dollar and shock tests |
| `python3 scripts/package-site.py` | PASS — canonical files only, rounding rule holds, no household data in the check |
| `python3 scripts/check-publication.py` | PASS — 26 reviewed public files; `--self-test` PASS |
| `node scripts/runtime-test.cjs` | PASS — 14 rendered pages, 1,153 rows all source-linked, no runtime errors, no broken local links |
| `node qa/tools/gate.cjs` | PASS — 1,153 rows (1,144 with their own official link, 9 calculated rows with a context link), 4,410 dollar amounts (70 official exact figures), 290 internal and 1,565 external links, **0 errors, 0 warnings** |
| `python3 src/check_links.py .` | 60 pages, 871 rows, 124 distinct external links; external links are not machine-checked from this sandbox |

## 5. Privacy and rounding

- No name, street address, parcel or account number, and no unrounded household amount, was added by this session. `$59`, `$29.50`, `$177` and `$118` are the department's published fee, the published recoverable half, three times the published fee, and two times it — not household data.
- Every added figure of $1,000 or more is a multiple of $10 except the amounts a government body publishes exactly ($11,110.05, $33,330.13, $7,443.90, $8,245.00, $24,733.00, $6,050, $6,370, $6,390); those are recorded in `qa/ledger.json` so the gate recognises them as official, and the gate confirms this with 0 errors.
- The standing **High** privacy findings from earlier sessions are unchanged and outside what any session can fix by editing the site: earlier branches and commits in the public repository still hold exact household figures, and several supplied amounts are themselves multiples of $10. They remain on the Flagged for Review page.

## 6. Items left open, flagged, not blocking

| Item | Why it stays open |
|---|---|
| Measure H amount for Property B | The measure passed only in the preliminary count of 3 November 2026; results are not certified until 11 December 2026, and the parcel amount by property type was not confirmed on an official page. Left blank and flagged. |
| Both insurance premiums | No official source prices a specific home. Left blank and flagged. |
| Property A tax-rate area, both meter sizes, Property B parcel tier, solar interconnection date | Need the bill or the account; all flagged. |
| Trust type (revocable vs irrevocable) | Decides whether the basis resets; unknown, and every result assumes it does. Flagged High. |
| Actual tenancy terms and rent history for Property B | Regulated separately from the HUD benchmark; unverified. |
