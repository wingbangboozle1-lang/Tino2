# Session c96c185e — final independent verification (2026-11-12)

Branch `arena/c96c185e-tino2` from `main` `052e626` (PR #52). Claim pushed before any other work; `git ls-remote` + open PRs re-checked before the claim commit (no other live claim, no open PRs).

## 1. Local suite on the `main` tree — all PASS

| Check | Result |
|---|---|
| `node scripts/validate.js` | PASS — 1,561 checks, 18 pages, 177 official sources; base case 2040→2050: sell $7,683,290 / rent $6,249,830 / live $5,135,780 |
| `node scripts/stress-test.js` | PASS — 50-year paths, estate ownership, privacy, real-dollar and shock tests |
| `python3 scripts/package-site.py` | PASS — canonical site only; rounding rule passed |
| `python3 scripts/check-publication.py --self-test` | PASS — 34 reviewed public files only |
| `node scripts/runtime-test.cjs` (jsdom installed per CI) | PASS — 18 rendered pages, 1,583 rendered rows source-linked, no runtime errors or broken local links |
| `node qa/tools/gate.cjs` | PASS — 18 pages, 1,583 rows (1,574 with own official link, 9 calculated with context link), 4,985 dollar amounts (115 official exact figures), 0 errors, 0 warnings |
| `python3 src/check_links.py .` | PASS — 68 pages, 887 table rows, 128 distinct external links |
| `python3 integration/tools/privacy_scan.py` | 0 errors, 228 warnings (standing pre-existing warnings for official exact figures in excluded research/verification files; unchanged by this session) |

## 2. Fresh official-source spot verification (this session, 2026-11-12)

Each page below was opened and read by this session; wording compared to the site's claim.

| Site claim (ledger ID) | Official page opened | Result |
|---|---|---|
| Federal filing thresholds 2011 $5,000,000 … 2026 $15,000,000 (FED-04) | IRS Estate tax | **MATCH** — table reproduced row by row, identical |
| 2026 basic exclusion $15,000,000 (FED-01) | IRS What's new — Estate and gift tax | **MATCH** — "WFTC amends § 2010(c)(3) by increasing the basic exclusion amount to $15,000,000 for calendar year 2026" |
| 2027 basic exclusion $15,480,000; gift $20,000 (FED-02/FED-03) | IRS IR-2026-133 (Nov 5, 2026) | **MATCH** — "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from … $15,000,000 for … 2026"; gift $20,000 up from $19,000 |
| Prop 19 value limit = taxable value + $1,000,000 (biennially adjusted); claim within 3 years; homeowners' exemption within 1 year | BOE Proposition 19 page | **MATCH** — comparison table states the same limits and filing periods |
| Prop 19 amount $1,044,586 for Feb 16, 2025–Feb 15, 2027, +2.15% from $1,022,600 (P19-10/P19-11) | BOE NR 25-02 (Mar 7, 2025) | **MATCH** — "increased by 2.15 percent, from $1,022,600 to $1,044,586" |
| HUD FY2027 SAFMR 95014: 3BR $5,440 / 4BR $5,800 (CF-04) | HUD FY2027 ZIP calc 95014 | **MATCH** — table: Eff $3,040 / 1BR $3,440 / 2BR $4,050 / 3BR $5,440 / 4BR $5,800 |
| HUD FY2027 SAFMR 94122: 1BR $2,770 / 2BR $3,410 (CF-05) | HUD FY2027 ZIP calc 94122 | **MATCH** — table: Eff $2,370 / 1BR $2,770 / 2BR $3,410 / 3BR $4,460 / 4BR $5,020 |
| No California estate-tax return for deaths on/after Jan 1, 2005 | CA State Controller — California Estate Tax | **MATCH** — "For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return" |
| SF allowable rent increase 1.6% Mar 1, 2026–Feb 28, 2027; File 261020 not enacted | SF Rent Board — Current Rates | **MATCH** — 1.6% table; notice states the legislation "has not been enacted" |
| CBO: PCE inflation returns to ~2% by 2030; 10-yr Treasury rises gradually then stable | CBO Budget and Economic Outlook 2026–2036 (Feb 11, 2026) | **MATCH** — "Inflation returns to a rate roughly in line with the Federal Reserve's long-run goal of 2 percent in 2030"; "Longer-term interest rates … rise gradually in 2027 and remain relatively stable" |
| Insurance premiums for both properties | CDI survey pages (carried from session 60ca3e1f) | **CORRECTLY BLANK** — site publishes survey ranges only and states "The results of these surveys are not premium quotes"; no property-specific premium is published. Left blank per the brief's rule. |

No mismatch found. Nothing was inferred or filled in.

## 3. Privacy audit of the published tree

- Published pages use placeholders (Property A / Property B) only; no personal names, street addresses, parcel numbers, or account identifiers in `site/`, `index.html`, or `assets/`.
- Household inputs in `site/data/model.js` are the owner's own round estimates ($3,100,000 / $1,800,000 / $7,150/mo) — each a multiple of $10 — labeled as unverified planning inputs. No exact bill, assessment, or tax figure from the brief's tables appears in the published tree (grep for `550537`, `539743`, `7207`, etc. returns nothing).
- Household tax/assessment history on `site/properties.html` is published rounded to $10 per the brief.
- `privacy_scan.py`: 0 errors. The 228 warnings are pre-existing and concern official exact figures in files excluded from the Pages build (research/, verification/, qa/); this session added no new warnings.

## 4. Live-site read-back

- `https://wingbangboozle1-lang.github.io/Tino2/site/questions.html` fetched after this session's checks: renders with 28 open / 14 settled / 8 unknowable counts, the five-answer priority table, and Group 1 questions with official source links. Site is live.
- Pages API: status `built`, source `main` / root, HTTPS enforced.

## 5. Irregularities

- **C-I1 (note, not a defect).** The three household planning inputs are exact round numbers from the brief itself; they are multiples of $10 and labeled unverified. No action needed.
- **C-I2 (note).** IRS IR-2026-133 returned HTTP 502 on first fetch; succeeded on retry. No site change needed.
- No other irregularity found. Standing **needs review** items (blank insurance premiums, blank household figures, privacy positions F-I1/F-I2) remain published on Flagged for Review and do not block publication.

## 6. Publication

This session changed no site file: the published tree already met every requirement of the brief and passed the full suite. This report plus the coordination record are the only changes in this PR.
