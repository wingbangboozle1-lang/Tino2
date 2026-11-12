# Session `9ca15d34` — Independent Verification, Source Re-Opening & Defect Remediation Report (2026-11-12)

## Summary

Synchronized with `origin/main` through `d35b53e` (PR #65 / session `fc58dcc8` merged, bringing ledger verification to `82/84` items with `SF-08`, `N-11`, `UT-04`, `N-12`, `FED-15`, and `UT-02` resolved). On top of `d35b53e`, this session completed an independent 18-page DOM/structural/anchor/parity audit, verified official sources directly on 12 November 2026, and remediated all remaining structural, source-key, URL/evidence, and wording defects across the dashboard without introducing personal identifiers, unrounded household amounts, or unverified claims.

All automated checks and custom DOM audits pass on the final merged workspace tree:
- `python3 qa/tools/build_ledger_js.py`: `site/data/ledger.js: 84 ledger entries, 6 series`
- `python3 scripts/package-site.py`: pass (canonical site only; legacy material excluded; `$10` rounding check passed)
- `python3 scripts/check-publication.py --self-test`: pass (`34` reviewed public files only; fail-closed checks reject unlisted files, symlinks, and missing pages)
- `node scripts/validate.js`: pass (`1,571` checks across `18` pages and `178` official sources, including `SCEN.simulate(..., "4BR_2027")` and `"3BR_2027"` parity against `MODEL.decision(...)`)
- `node scripts/stress-test.js`: pass (`50`-year paths, estate ownership, privacy, real-dollar, and shock tests)
- `node scripts/runtime-test.cjs`: pass (`18` rendered pages; `1,584` rendered rows source-linked; `0` runtime errors or broken local links)
- `node qa/tools/gate.cjs`: pass (`18` rendered pages, `1,584` table rows [`1,575` own official links, `9` context-only calculated rows], `5,008` dollar amounts checked [`120` official exact figures], `559` internal and `2,076` external links, `0` errors, `0` warnings)
- `python3 integration/tools/privacy_scan.py`: `0` errors (warnings limited to non-canonical files and documented official ledger figures)
- `python3 src/check_links.py .`: pass (`68` pages, `887` table rows, `128` distinct external links)
- JSDOM structural audit across `_public`: `0` duplicate element IDs, `0` broken `#anchor` links, `0` table header/body column mismatches, interactive `rentChoice` switching verified (`4BR`, `3BR`, `4BR_2027`, `3BR_2027`), `GATE` counts `{ total: 40, settled: 14, household: 11, missing: 15 }`, `READINESS` counts `{ open: 28, answered: 14, unknowable: 8 }`, and `LEDGER` counts `82` verified / `2` unverified (`INS-02`, `INS-03`).

---

## Defects Fixed on Top of `d35b53e`

1. **Broken `#Q01`–`#Q28` and `#A14` jump anchors in `site/questions.html`**:
   - Rows inside `#carried-q` used `data-q="${q.id}"` without `id="${q.id}"`, and `#answered` rows omitted `id="${a.id}"`, causing cross-links (`site/suggestions.html#Q01`, `#Q02`, `#A14`, etc.) to fail target resolution. Added `id="${q.id}"` and `id="${a.id}"` with zero ID collisions across all 18 pages.
2. **Table header/column mismatch and outdated insurance link in `site/questions-gate.html`**:
   - The `order` table had `6` `<th>` cells in `<thead>` against `7` `<td>` cells in `<tbody>`. Added `<th>Official source</th>`.
   - Updated the `live` group source key from `insuranceGuide` (2023 one-pager) to `cdiResGuide` (revised January 2026 CDI guide).
3. **Source-key mismatches in `site/data/gate.js`**:
   - `Q-09` (kinds of inherited money / 10-year retirement rule) pointed to `irsTopic559` (3.8% NIIT) instead of `irsBeneficiary`. Updated to `irsBeneficiary`.
   - `Q-22` (Section 1031 like-kind exchanges) pointed to `irsTopic409` (capital gains) instead of `irsLikeKind`. Updated to `irsLikeKind`.
   - `Q-29` (rebuild cost) and `Q-32` (60-day vacancy rule) pointed to `insuranceGuide` instead of `cdiResGuide` (the Jan 2026 revised guide containing both explicit rules). Updated both to `cdiResGuide`.
   - Preserved `d35b53e` updates to `Q-23` and `Q-24` (`status: "household"`, `src: "hudA2027"`), eliminating the stale FY2027 `"missing"` flag.
4. **Duplicate Jekyll exclusion in `_config.yml`**:
   - Removed duplicate `- assets/style.css-alternate.css` entry.
5. **Broken Prop 218 notice link & source/ledger clarifications (`site/data/sources.js`, `qa/ledger.json`, `site/data/ledger.js`, `site/verification.html`, `site/options.html`)**:
   - `sfpucRates2026` / `UT-03`: The older SFPUC Prop 218 notice URL failed to fetch on 12 Nov 2026 while the official Commission-adopted schedule PDF (`https://www.sfpuc.gov/sites/default/files/accounts-and-services/Rates_Schedule_Water_Sewer_2026-7.pdf`, Resolutions 26-0064 & 26-0066, April 28, 2026) opened cleanly and verified FY 2026–27 and FY 2027–28 schedules (`W-1A/B`, Wastewater Schedule `A`, Stormwater Schedule `D`). Updated `sfpucRates2026`, `UT-03`, and `site/verification.html` to point directly to the live adopted PDF.
   - `hudB2027` / `CF-05` & `hudB`: Verified ZIP 94122 FY2026 SAFMR (`$2,730` 1BR / `$3,310` 2BR) and FY2027 SAFMR (`$2,770` 1BR / `$3,410` 2BR) directly on `huduser.gov`; clarified that the Step-5 comparison line (`$2,977` 1BR / `$3,604` 2BR) reflects the metro-wide FY2026 FMR baseline rather than ZIP 94122's final FY2026 SAFMR.
   - `rtc11911`: Clarified that when a city imposes a half-rate documentary transfer tax (`$0.275` per `$500`), the taxpayer receives a credit against the `$0.55` per `$500` county tax.
   - `irsEstateFAQ`: Added `Checked 12 Nov 2026` and noted Rev. Proc. 2022-32 five-year simplified late portability election.
   - `site/options.html`: Clarified IRS Publication 523 wording to state `"depreciation taken after 6 May 1997 cannot be excluded"`.

---

## Independent Official-Source Checks Executed 12 Nov 2026

All primary pages listed below were fetched and read directly on 12 Nov 2026:
- California Secretary of State ballot measures (`https://electionresults.sos.ca.gov/returns/ballot-measures`, Nov 12, 10:50 a.m.): Prop 3 `60.7%` yes, Prop 42 `51.4%` yes, Prop 40 `47.6%` yes (`5,808,868`–`6,400,441`), Prop 43 `42.5%` yes (`5,057,119`–`6,834,825`).
- San Francisco Elections & City Attorney Measure H (`Title_and_Summary_-_Parcel_Tax_to_Fund_Public_Transit_Operations_002.pdf`): `74.4%` yes in Nov 10 tally; 15-year tax starting July 1, 2027 (`$249` + `$0.195/sq ft` >5,000 sq ft, `$50,000` cap, `50%`/`$65`-unit rent-controlled pass-through for pre-June 1, 2027 leases).
- HUD FY2026 (`zcta=94122`) & FY2027 (`zip=95014`, `zip=94122`) SAFMR calculators.
- BOE 2026 LTAs (`2026.htm`, ending at `2026/044`), BOE Prop 19 (`boe.ca.gov/prop19/`), and Santa Clara Assessor Prop 19 page (noting `"adjusted annually beginning in 2023"` vs BOE biennial rule).
- IRS Estate Tax (`estate-tax`, `IR-2026-133`, `i706`, `frequently-asked-questions-on-estate-taxes`, `tc559`, `tc409`, `like-kind-exchanges`, `rr-23-02.pdf`, `retirement-topics-beneficiary`, `p551.pdf`, `publications/p527`, `publications/p523`). Note: standalone `p527.pdf` failed PDF fetch while official HTML `publications/p527` opened cleanly.
- SFPUC adopted rate schedules (`Rates_Schedule_Water_Sewer_2026-7.pdf`) & San Jose Water (`grc-2025-27/`, `2026-rates/`).
- Congress.gov (`S.587`, `H.R.1301`, `H.R.601` `/all-actions`): all at `Introduced` status with zero committee/floor movement.
- SF Rent Board (`reports--current-rates-including-rent-increase-relocation-sec-deposit`), SF Treasurer (`secured-property-taxes`), California Controller (`ardtax_estate_tax.html`), California Leginfo (`RTC §11911`).

---

## Remaining Open / Unverified Items Preserved Honestly

- **Unresolved household & parcel records (`site/review.html` / `site/questions-gate.html`)**: trust instrument revocability (`Q-01`), deed vesting (`Q-02`), liquid estate balances/account mix (`Q-09`), Property A Cupertino tax-rate area & actual parcel bills, Property A & B binding insurance quotes and rebuild cost (`INS-02`, `INS-03`), Property A water provider & solar PTO date (`UT-04` system year), and Property B building square footage for SF Measure H.
- **Historical & statutory caveats retained on `site/review.html` / ledger notes**: 1% Behavioral Health Services Tax over `$1,000,000` (`CA-04` note), full Prop 42 text (`CA-06` note), and standing public-repository history / author email items (`F-I1`, `F-I2`) documented on `site/review.html` and `site/suggestions.html`.
