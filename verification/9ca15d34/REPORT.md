# Session `9ca15d34` — Independent Verification, Source Re-Opening & Defect Remediation Report (2026-11-12)

## Summary

Following repository synchronization through `origin/main` commit `bb42f14` (PR #60 merged), this session independently checked the entire 18-page canonical dashboard (`_public`), verified model/DOM invariants, directly opened previously unverified or fast-changing official sources on 12 November 2026, and remediated all verified structural, source-key, parity, and freshness defects across the site and ledger without introducing unverified claims, personal identifiers, or unrounded household amounts.

All automated checks and custom DOM audits pass on the final workspace tree:
- `python3 qa/tools/build_ledger_js.py`: `site/data/ledger.js: 84 ledger entries, 6 series`
- `python3 scripts/package-site.py`: pass (canonical site only; legacy material excluded; `$10` rounding check passed)
- `python3 scripts/check-publication.py --self-test`: pass (`34` reviewed public files only; fail-closed checks reject unlisted files, symlinks, and missing pages)
- `node scripts/validate.js`: pass (`1,563` checks across `18` pages and `177` official sources, including `SCEN.simulate(..., "4BR_2027")` and `"3BR_2027"` parity against `MODEL.decision(...)`)
- `node scripts/stress-test.js`: pass (`50`-year paths, estate ownership, privacy, real-dollar, and shock tests)
- `node scripts/runtime-test.cjs`: pass (`18` rendered pages; `1,583` rendered rows source-linked; `0` runtime errors or broken local links)
- `node qa/tools/gate.cjs`: pass (`18` rendered pages, `1,583` table rows [`1,574` own official links, `9` context-only calculated rows], `5,008` dollar amounts checked [`115` official exact figures], `559` internal and `2,074` external links, `0` errors, `0` warnings)
- `python3 integration/tools/privacy_scan.py`: `0` errors (warnings limited to non-canonical files and documented official ledger figures)
- `python3 src/check_links.py .`: pass (`68` pages, `887` table rows, `128` distinct external links)
- JSDOM structural audit across `_public`: `0` duplicate element IDs, `0` broken `#anchor` links, `0` table header/body column mismatches, interactive `rentChoice` switching verified (`4BR`, `3BR`, `4BR_2027`, `3BR_2027`), `GATE` counts `{ total: 40, settled: 14, household: 11, missing: 15 }`, `READINESS` counts `{ open: 28, answered: 14, unknowable: 8 }`.

---

## Defects Fixed

1. **Stale executive-summary counters in `index.html`**:
   - Line 86 stated `"Twenty-two open questions, twelve points already settled..."`, contradicting `site/data/questions.js` (`28` open, `14` settled, `8` unknowable). Updated to `"Twenty-eight open questions, fourteen points already settled by an official source, and eight that no document can settle"`.
   - Line 126 stated `"(8 improvement proposals, trade-offs & export)"`, contradicting `site/data/suggestions.js` (`27` proposals). Updated to `"(27 improvement proposals, trade-offs & export)"`.
2. **Broken `#Q01`–`#Q28` and `#A14` jump anchors in `site/questions.html`**:
   - Rows inside `#carried-q` used `data-q="${q.id}"` without `id="${q.id}"`, and `#answered` rows omitted `id="${a.id}"`, causing cross-links (`site/suggestions.html#Q01`, `#Q02`, `#A14`, etc.) to land on missing targets. Added `id="${q.id}"` and `id="${a.id}"` with zero ID collisions across the site.
3. **Table header/column mismatch and outdated insurance link in `site/questions-gate.html`**:
   - The `order` table had `6` `<th>` cells in `<thead>` against `7` `<td>` cells in `<tbody>`. Added `<th>Official source</th>`.
   - Updated the `live` group source key from `insuranceGuide` (2023 one-pager) to `cdiResGuide` (revised January 2026 CDI guide).
4. **Source-key mismatches and stale FY2027 rent gate item in `site/data/gate.js`**:
   - `Q-09` (kinds of inherited money / 10-year retirement rule) pointed to `irsTopic559` (3.8% NIIT) instead of `irsBeneficiary`. Updated to `irsBeneficiary`.
   - `Q-22` (Section 1031 like-kind exchanges) pointed to `irsTopic409` (capital gains) instead of `irsLikeKind`. Updated to `irsLikeKind`.
   - `Q-29` and `Q-32` pointed to `insuranceGuide` instead of `cdiResGuide` (which states the replacement-cost rule and explicit 60-day vacancy exclusion). Updated to `cdiResGuide`.
   - `Q-23` now notes both FY2026 (`$6,390` 4BR / `$5,870` 3BR) and verified FY2027 (`$5,800` 4BR / `$5,440` 3BR).
   - `Q-24` (`status: "missing"`, claiming FY2027 HUD rent had not been looked up) updated to `status: "household"` with source `hudA2027`, reflecting direct verification on 12 Nov 2026 and live selector parity in Decision Lab and Black Swans.
5. **FY2027 rent selector parity on `site/black-swan.html` and `site/data/history-engine.js`**:
   - Added `4BR_2027` (`$5,800`) and `3BR_2027` (`$5,440`) options to `rentChoice` in `site/black-swan.html` and updated `SCEN.simulate()` in `site/data/history-engine.js` while retaining `"4BR"` (`$6,390`) as default. Added parity assertions in `scripts/validate.js` confirming `SCEN.simulate(..., "4BR_2027")` and `"3BR_2027"` match `MODEL.decision(...)` terminal rental results within `< $0.01`.
6. **Duplicate Jekyll exclusion in `_config.yml`**:
   - Removed duplicate `- assets/style.css-alternate.css` entry.

---

## Live Official-Source Re-Opening & Freshness Updates (12 Nov 2026)

| Source / Ledger ID | Official URL Re-Opened 12 Nov 2026 | Findings & Updates Applied |
|---|---|---|
| `CA-05`, `CA-06`, `CA-07` (`sosResults`, `sosResults2026`) | `https://electionresults.sos.ca.gov/returns/ballot-measures` | Updated unofficial counts from Nov 11 (`6:51 p.m.`) to Nov 12, `10:50 a.m.` (certification due Dec 11, 2026): Prop 3 `60.7%` yes (`7,358,722` / `4,768,582`), Prop 42 `51.4%` yes (`6,226,483` / `5,887,134`), Prop 40 `47.6%` yes (`5,808,868` / `6,400,441`, vs. earlier `47.5%`), Prop 43 `42.5%` yes (`5,057,119` / `6,834,825`, vs. earlier `42.6%`). Updated `sources.js`, `sources.html`, `review.html`, and `qa/ledger.json`. |
| `hudB`, `hudB2027`, `CF-05` | `huduser.gov` FY2026 (`zcta=94122`) & FY2027 (`zip=94122`, `zip=95014`) | Verified FY2026 ZIP 94122 SAFMR (`$2,730` 1BR / `$3,310` 2BR) and FY2027 ZIP 94122 SAFMR (`$2,770` 1BR / `$3,410` 2BR). Clarified in `hudB2027` and `CF-05` that the Step-5 row (`$2,977` 1BR / `$3,604` 2BR) is the metro-wide FY2026 FMR baseline rather than ZIP 94122's final FY2026 SAFMR. |
| `rtc11911` | `leginfo.legislature.ca.gov` RTC §11911 | Clarified wording to state that when a city imposes a half-rate documentary transfer tax (`$0.275` per `$500`), the taxpayer receives a credit against the `$0.55` per `$500` county tax. |
| `UT-03`, `sfpucRates2026` | `https://www.sfpuc.gov/sites/default/files/accounts-and-services/Rates_Schedule_Water_Sewer_2026-7.pdf` | Older Prop 218 notice URL failed to fetch on 12 Nov 2026; official Commission-adopted schedule PDF (`Resolutions 26-0064 & 26-0066`, April 28, 2026) opened cleanly and confirms FY 2026–27 and FY 2027–28 adoption across Schedule W-1A/B water, Schedule A wastewater (`95%` MF flow factor), and Schedule D residential stormwater tiers. Updated `sfpucRates2026`, `UT-03`, `site/review.html`, and `site/verification.html` consistently. |
| `UT-02` | `https://www.sjwater.com/grc-2025-27/` & `https://www.sjwater.com/2026-rates/` | Directly opened GRC 2025–27 page (`$107.44` -> requested `$120.62` 2025, `$125.44` 2026, `$131.12` 2027 pre-surcharge) alongside ~2.8% Jan 1, 2026 approved rate page; promoted `UT-02` from `unverified` search-extract status to `verified`. |
| `FED-15` (`hr1301`, `hr601`, `S. 587`) | `congress.gov/bill/119th-congress/{senate-bill/587,house-bill/1301,house-bill/601}/all-actions` | Directly opened all three bill action pages; confirmed all remain at `Introduced` status since early-2025 committee referral with zero subsequent action. Promoted `FED-15` to `verified` and updated `sources.js` & `site/review.html`. |
| `FED-14`, `N-04`, `N-12` (`irsPub527`, `irsPub551`, `irsPub523`, `irs706TableA`, `irs1041es`, `irsEstateFAQ`) | `irs.gov` official pages/PDFs | Directly opened Pub 527 HTML (`publications/p527`; `p527.pdf` failed PDF fetch), Pub 551 PDF (`p551.pdf`), Pub 523 HTML (`publications/p523`), Form 706 Instructions (`i706`), Form 1041-ES (`f1041es.pdf`), and Estate Tax FAQ; verified 27.5-year GDS depreciation, `$25,000` active-participation allowance (`$100,000–$150,000` MAGI phaseout), donor gift basis & California community-property double step-up, post-2008 nonqualified use & post-May 6, 1997 depreciation, Table A `$345,800` + `40%` over `$1,000,000`, 2026 trust `37%` bracket over `$16,000`, and 5-year simplified late portability election. Updated `N-12` to `verified`, updated `sources.js`, `site/options.html`, and `site/review.html`. |

---

## Remaining Open / Unverified Items Preserved Honestly

- **Unresolved household & parcel records (`site/review.html` / `site/questions-gate.html`)**: trust instrument revocability (`Q-01`), deed vesting (`Q-02`), liquid estate balances/account mix (`Q-09`), Property A Cupertino tax-rate area & actual property tax bills, Property A & B binding insurance quotes and rebuild cost (`INS-02`, `INS-03`), Property A water provider & solar PTO date (`UT-04` system year), and Property B building square footage for SF Measure H.
- **Historical & statutory nuances retained as `unverified`**: `SF-08` (June 2018 `$298` school parcel tax start date from non-official summaries), `CA-04` note (1% Behavioral Health Services Tax over `$1,000,000` not printed on FTB 2025 Schedule X/Y PDF), `CA-06` note (full Prop 42 text), and standing public-repository history / author email items (`F-I1`, `F-I2`) documented on `site/review.html` and `site/suggestions.html`.
