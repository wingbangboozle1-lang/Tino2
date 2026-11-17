# Session cd350c68 — verification report, 17 November 2026

Scope: periodic official-source recheck (F-2), the verified-source edits it settled (F-3), enacted-vs-proposal
dating (F-4), the dating/consistency audit (F-5), and the rebuild + suite + moved-check (F-6). F-7 (PR, merge,
Pages read-back) is recorded at the end and in `COORDINATION.md`. This report contains no household figure,
identifier or address; every value below is an official published amount or a synthetic-model output.

## 1. Official-source recheck (17 Nov 2026) — every item re-opened line by line

Result: **all 29 re-opened records matched the guide; nothing was contradicted.** Sources read:

| Source (official) | What was re-read | Result |
|---|---|---|
| IRS Instructions for Form 706 (07/2026) | 2026 basic exclusion $15,000,000; filing test (gross estate + adjusted taxable gifts + specific exemption, or portability); 9-month due date; Form 4768 auto 6-month file extension; "an extension of time to file does not extend the time to pay"; pay extension via Form 4768 (§6166/§6163); Form 8971 statement within 30 days of the Form 706 due date including extensions | MATCH |
| IRS Instructions for Form 4768 (02/2020) | Auto 6-month file extension; Part III pay extension ≤ 12 months at a time; reasonable cause 1 year at a time ≤ 10 years (deficiency ≤ 4 years); interest runs regardless | MATCH |
| SF Assessor-Recorder fee schedule (sf.gov, schedule dated 1 Jan 2026) | Transfer-tax tiers per $500 whole consideration: $2.50 (>$100–$250k), $3.40 (>$250k–<$1M), $3.75 ($1M–<$5M), $11.25 ($5M–<$10M), $27.50 ($10M–<$25M), $30.00 (≥$25M); Transfer Tax Affidavit requirement; recording fees $14 first/$3 add'l, SB2 $75/parcel ≤ $225 (exempt when transfer tax paid), PCOR $20, monument $10 | MATCH (schedule newly published on the guide; ledger SF-TRANSFER-TIERS / SF-RECORDING-FEES added) |
| Santa Clara County Clerk-Recorder (recording-real-estate, recording-document-fees, fee-schedule) | DTT $0.55/$500 (city add-on $1.65/$500 for San Jose/Palo Alto/Mountain View); first page $102 (incl. $75 SB2 + $2 AB1466 + $10 fraud fee, $10 subtracted when DTT-paid), add'l page $3, monument $10, multi-title $102; PCOR $20 | MATCH (ledger SCC-RECORDING-FEES added) |
| Santa Clara County DTAC secured-property-tax calendar | Bills mailed October; Nov 1 / Dec 10 first installment; Feb 1 / Apr 10 second; Jun 30 last day; Jan 1 lien | MATCH (ledger SCC-TAX-CALENDAR added; `sccTax` source URL moved to dtac.santaclaracounty.gov) |
| FTB 2025 Form 540 instructions | Line 62 BHST worksheet: (line 19 − $1,000,000) × 1%; Line 31 tax computed on taxable income — no preferential capital-gain rate (CA-CAPITAL-GAINS-ORDINARY is structural; no verbatim sentence exists — note retained) | MATCH |
| State Controller (sco.ca.gov estate-tax) | No CA estate-tax return for deaths on/after 1 Jan 2005; GST none after 31 Dec 2004; inheritance tax only before 8 Jun 1982 | MATCH |
| BOE LTA 2025/009 + LTA 2026/002 + boe.ca.gov/prop19 | $1M adjusted to $1,044,586 (transfers 16 Feb 2025–15 Feb 2027); 2026-27 factor 1.02 (40 of 51 years at the cap); homeowners' exemption within 1 year; exclusion claim within 3 years or before third-party transfer; principal residence of both parties | MATCH |
| IRS IR-2026-133 (5 Nov 2026) | 2027 BEA $15,480,000; annual gift $20,000 (2026: $19,000); non-citizen spouse $201,000 (2026: $194,000) | MATCH |
| Congress.gov H.R. 1301 | Death Tax Repeal Act, Feenstra [R-IA-4], introduced 13 Feb 2025, House Ways & Means; tracker "Introduced"; latest action = referral 13 Feb 2025 | MATCH — proposal, not law |
| leginfo SB-284 | "Property taxation: change in ownership: family homes and farms"; Active Bill - In Committee Process; Assembly; last amended 25 Jun 2025; latest action 14 Jul 2025 held in committee | MATCH — proposal, not law |
| SF Rent Board current rates | Allowable increase 1.6% (1 Mar 2026–28 Feb 2027); deposit interest 4.2%; File 261020 "has not been enacted" (notice 9 Nov 2026) | MATCH |
| SF Treasurer secured-property-taxes | FY 2026-27 secured rate 1.18162182%; bills mailed October; Dec 10 / Apr 10 penalties | MATCH |
| Treasury daily par yield curve (XML feed) + FRED CSV | 13 Nov 2026: 3-month 4.32%, 2-year 4.88% — the exact values the guide quotes; 16 Nov 2026: 4.34% / 4.83% (no drift needing a change) | MATCH |
| IRS estate-tax pages + Rev. Proc. 2025-32 record labels | Filing-threshold labels; 2026 gift figures | MATCH (labels conflict resolved 15 Nov; both labels supported) |

Not read (kept blank and flagged, per the never-infer rule): R&T §74.9 (leginfo text is JS-only and did not
render in two sessions; do not retry `codes_displaySection`); the Form 1041 fiscal-year election convention;
insurance premiums; parcel-specific Prop H and property-tax bills; basis/Prop 19 household documents.

## 2. Defects found and fixed by this session

1. **Timeline page rendered the wrong body (latent since 16 Nov).** The pre-commit block reassigned `body`
   before `page('timeline', ...)` read it, so `guide/timeline.html` showed the pre-commitment register and the
   entire deadline timeline — a core brief item — was missing from the site. Fixed by capturing
   `timeline_body=body` before the pre-commit block. The timeline now renders its own table (date of death,
   60-day trustee notice, 9-month Form 706, Form 4768 periods, Form 8971 30-day row, property-tax calendar
   with the county citation, Prop 19 windows).
2. Duplicate contradictory "Not on this timeline yet" callouts (one stale, still listing items since verified)
   — stale copy deleted.
3. `sccTax` source URL pointed at an unfetchable page — moved to the DTAC calendar page.
4. Stale review stamps (attorney-cpa and summary headers "16 Nov") — re-dated to the 13–17 Nov 2026 window;
   the bare "4.32%" parking quote and the what-if parked-cash label now carry their 13 Nov 2026 reading date.
5. `README.md` Verify block still listed `scripts/validate.js` and `scripts/stress-test.js`, which PR #149
   deleted with the retained analysis tree — replaced with the current suite
   (`test-engine-agreement.py`, `test-imputed-rent.py`, `test-history-audit.py`, `test-phased-history.py`,
   `runtime-test.cjs`).

## 3. Ledger (`guide/figures/official-figures.json`)

- Added (verified 17 Nov 2026): `FED-706-DUE-9M`, `FED-4768-FILE-EXT`, `FED-4768-PAY-EXT`, `FED-8971-BASIS`,
  `SF-TRANSFER-TIERS`, `SF-RECORDING-FEES`, `SCC-RECORDING-FEES`, `SCC-TAX-CALENDAR`.
- Re-marked `checked: 2026-11-17` on the 27 records re-read today (each re-read matched the record).
- Merged without loss with the parallel session's `MODEL-IMPUTED-RENT-25Y` record (PR #148/#149 lineage).
- Gate result: 53 records, 52 verified, 1 explicitly unverified (`MODEL-IMPUTED-RENT-25Y`, a model record the
  other session chose to flag); every seven-figure published amount has a ledger record.

## 4. Watchlist — enacted vs proposals (F-4)

Re-dated 17 Nov 2026 with statuses unchanged: **H.R. 1301** (Introduced, 13 Feb 2025 referral is still the
latest action) and **SB-284** (in committee, 14 Jul 2025 hold) remain proposals, not law. File 261020 "has
not been enacted". Proposition 19 adjustment-cadence conflict between two official pages remains open by
design (the guide follows the Board).

## 5. Rebuild + full suite (F-6), run 17 Nov 2026 on the merged tree

All green: `build-guide` (no-op) · `check-generated` 19 pages · `check-figures` 53/53 · `package-site` 33
files · `check-publication` (+ `--self-test`) · `test-model-reference` 20,736 arithmetic comparisons ·
`test-phased` 200 · `test-phased-history` 1,303 · `privacy-gate` 70 tracked text files (+ `--self-test`) ·
`privacy-history-audit --self-test` · `privacy-audit.cjs` · `test-guide` 19 pages / 1,225 source-linked rows
/ 13,789 checks · `runtime-test` 19 pages / 1,086 rows · `test-engine-agreement` 42 · `test-imputed-rent` 43 ·
`test-history-audit`. (`src/check_links.py`, `integration/tools/privacy_scan.py`, `verification/0d6ec51e/options.cjs`
and the dashboard validators left the tree with PR #149.)

## 6. Did the recommendation move?

The brief's rule: rebuild after input changes and record whether the answer moved. This session's edits are
text/ledger only — no model input changed in `F-3`–`F-5` (verified: those commits touch no file under
`guide/data/`). The **published synthetic example's leading path nevertheless moved, because the merged
parallel-session commits changed the model itself** (PR #148 "make the two calculators answer the same
question the same way"; the imputed-rent correction for living paths, disclosed on the Flagged page and
pinned by `test-imputed-rent` and `test-engine-agreement`). Measured on the published model, BASE inputs,
`MODEL.decision` terminal values:

| Point | Before (model at d645351) | After (current) | Leading path |
|---|---|---|---|
| inherit 2040, horizon 10 | sell $3,089,660 · rent $2,605,310 · live $2,043,220 | sell $4,078,170 · rent $3,999,570 · live $4,355,040 | **sell → live** |
| inherit 2040, horizon 20 | sell $5,032,740 · rent $3,671,580 · live $1,800,130 | sell $7,303,380 · rent $6,525,900 · live $7,492,980 | **sell → live** |
| inherit 2045, horizon 10 | sell $3,669,550 · rent $3,076,390 · live $2,385,520 | sell $5,180,150 · rent $4,995,420 · live $5,355,610 | **sell → live** |

These are synthetic-example outputs on invented inputs; the guide states they are not a recommendation.
The reason the live path rises is exactly the corrected treatment (living now carries its imputed rent
credit, adjustable on the what-if page); the sell/rent shifts come from the calculator-alignment commit.
Attribution for the record: movement enters with merged PRs #148/#149 (sessions 6f33482e/353a4b80), not
with this session's commits.

The earlier household-figure dashboard check (its own model outputs, recorded in prior session notes) is
**not reproduced here**: PR #149 deleted that tree from HEAD precisely because its assertions were built
from the household's own figures, and this report is a public file.

## 7. Open items (blank + flagged; none block the merge)

R&T §74.9 ADU rule (blank, do not retry the JS page) · Form 1041 fiscal-year convention (blank) · insurance
premiums (blank) · Prop H amount for Property B and estate/asset figures (private) · basis and Prop 19
eligibility documents (household) · Proposition 19 cadence conflict between two official pages (guide
follows the Board) · ledger-vs-page completeness is a process note, not a guarantee · repository history
scrub and visibility remain owner/admin decisions (L-D2 / P-4; runbook retained at
`docs/history-remediation-runbook.md`).

## 8. F-7 record

See the `COORDINATION.md` cd350c68 block: PR number, merge result, Pages deployment and live read-back are
appended there once F-7 completes.
