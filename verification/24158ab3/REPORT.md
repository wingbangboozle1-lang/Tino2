# Session `24158ab3` — final integration verification report (2026-11-15)

**Scope.** Integrate the stale, conflicting PR #104 (session `22614eaa`) into the published
artifact, re-verify the combined data line by line against official sources, and complete
publication. No household figure, ZIP code, parcel number, address or name appears in this
report or in any file this session committed; parties appear only as placeholders.

## 1. Integration performed

PR #104's entire content is a single commit, `987d758` (merge-base with `main` is
`9292664`, the merge of PR #102). It was cherry-picked onto this branch and the three
content conflicts resolved as follows:

- `scripts/build-guide.py` — merged cleanly. `money()` now renders a negative as
  `−$x` instead of `$-x`, and the executive-summary source column reads
  "Official source, or context for a model row".
- `scripts/test-guide.cjs` — merged cleanly. The published $10 rounding gate now also
  matches an amount carrying a sign, and every rendered page fails if a `$-` form appears.
- `COORDINATION.md` — both records kept: this session's claim block and `22614eaa`'s
  post-merge follow-up block, appended verbatim (board records stay verbatim).
- `guide/stress.html`, `guide/summary.html` — kept `main`'s version and regenerated with
  `python3 scripts/build-guide.py`, so the signed-amount fix flows through the generator
  rather than a hand-merge. Regenerated output shows `−$19,190` etc. in the required form.

Final diff against `main`: 5 files, +17/−5 — exactly PR #104's intended content; nothing
from `dff8604e`'s merged work was regressed.

## 2. Line-by-line re-verification (all re-opened on 2026-11-15)

| # | Claim in the combined artifact | Official source re-opened | Result |
|---|---|---|---|
| 1 | Federal estate-tax basic exclusion: $15,000,000 (2026), $15,480,000 (2027) | IRS IR-2026-133, 5 Nov 2026 — irs.gov newsroom | **MATCH** — "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from a total of $15,000,000 for estates of decedents who died in 2026." |
| 2 | Proposition 19 allowance: current taxable value plus $1,000,000 (biennially adjusted); homeowners'-exemption claim within 1 year of transfer; exclusion claim within 3 years or before transfer to a third party | California BOE — boe.ca.gov/prop19/ | **MATCH** — comparison chart states the value limit, and the filing period "File for homeowners' exemption within 1 year of transfer / File claim for exclusion within 3 years or before transfer to third party." |
| 3 | Treasury parking yields used by the phased model: 4.32% at 3 months, 4.88% at 2 years (13 Nov 2026) | U.S. Treasury daily par yield curve, November 2026 — home.treasury.gov | **MATCH** — row 11/13/2026: 3 Mo 4.32, 2 Yr 4.88. |
| 4 | San Francisco covered-unit rent increase: 1.6% for 1 Mar 2026 – 28 Feb 2027; File No. 261020 is proposed, not enacted | SF Rent Board — sf.gov "Current Rates" | **MATCH** — "1.6% for March 1, 2026 – February 28, 2027"; the page states the File 261020 legislation "has not been enacted and is subject to change." |
| 5 | Santa Clara County documentary transfer tax: $0.55 per $500 (=$110 per $100,000); missing-PCOR fee $20; R&T Code §11911 | Santa Clara County Clerk-Recorder — clerkrecorder.santaclaracounty.gov | **MATCH** — "computed at a rate of $.55 per $500 or fractional portion"; "$20.00" PCOR penalty; R&T Code 11911 cited. (San Jose / Palo Alto / Mountain View: $1.65 per $500 — read and noted; not used for Property A, which is not in those cities.) |
| 6 | FDIC trust deposit-insurance ceiling: $1,250,000 per owner for a trust with five or more beneficiaries | FDIC — "Your Insured Deposits" — fdic.gov | **MATCH** — "the maximum insurance coverage for a trust owner with five or more beneficiaries is $1,250,000 per owner for all trust accounts… held at the same bank" (effective 1 Apr 2024). |
| 7 | December 2022 CPI-U: 6.5% all items, 14.3% electricity over the 12 months | BLS CPI news release (USDL-23-0017) — bls.gov archives | **MATCH** — "the all items index increased 6.5 percent" and "the index for electricity rose 14.3 percent." |
| 8 | CBO February 2026 outlook: PCE inflation returning to roughly 2% in 2030 | CBO, "The Budget and Economic Outlook: 2026 to 2036" (Pub. 61882) — cbo.gov | **MATCH** — "Inflation returns to a rate roughly in line with the Federal Reserve's long-run goal of 2 percent in 2030." |
| 9 | California mental-health-services tax: 1% on taxable income above $1,000,000 | CA Revenue & Taxation Code §17043 — leginfo.legislature.ca.gov | **MATCH** — "an additional tax shall be imposed at the rate of 1 percent on that portion of a taxpayer's taxable income in excess of one million dollars ($1,000,000)." |
| 10 | Bay Area earthquake: 72% probability of at least one M≥6.7 before 2043 | USGS Fact Sheet 2016-3020 — pubs.usgs.gov | **MATCH** — "a 72 percent probability… of at least one earthquake of magnitude 6.7 or greater striking somewhere in the San Francisco Bay region before 2043." |
| 11 | Home-sale exclusion: $250,000 single / $500,000 joint, ownership and use tests | IRS Topic 701 — irs.gov | **MATCH** — "exclude up to $250,000 of that gain… or up to $500,000… if you file a joint return." |
| 12 | Black-swan templates: 1929 Dow −89% (peak 3 Sep 1929 381.17 → trough 8 Jul 1932 41.22, ~34 months); 2008 S&P 500 −57% (Oct 2007 → Mar 2009, ~17 months) | Federal Reserve History essays — federalreservehistory.org | **MATCH** — Great Recession essay: "the S&P 500 index fell 57 percent from its October 2007 peak to its trough in March 2009." 1929 essay: peak 3 Sep 1929 at 381.17, low 8 Jul 1932 at 41.22, "89 percent below its peak." |

**Left blank / flagged (not inferred):** San Francisco documentary transfer-tax rate (no
official page located; already flagged), Form 4768 mechanics, county DTAC mailing dates,
R&T §74.9 ADU exclusion text, and the household-specific facts (occupancy, basis, gross
estate, prior gifts) which have no public source and stay in the private questions register.

## 3. Test suite on the integrated branch (all PASS except the noted browser item)

- `check-generated.py` — PASS (18 generated public pages up to date).
- `check-figures.py` — PASS (32 ledger records, 32 verified, 0 unverified).
- `test-model-reference.py` — PASS (108 configurations / 250 stress years / 1,500 phased
  years; 20,736 unrounded arithmetic comparisons).
- `test-phased.py` — PASS (phased Treasury-parking model reproduced by an independent
  tranche reconstruction; 113 checks).
- `test-guide.cjs` (jsdom, CI-identical install) — PASS (18 rendered pages, 1,039
  source-linked table rows, 12,400 checks).
- `package-site.py` + `check-publication.py --directory _public` — PASS (32 reviewed
  files).
- `privacy-audit.cjs` — PASS (no raw pre-rounding token, ZIP or identifier in the
  packaged artifact or rendered text).
- `privacy-gate.py` + `--self-test` — PASS (232 tracked text files).
- `validate.js` + `stress-test.js` — PASS (1,613 checks; 50-year paths, privacy, real-dollar
  and shock tests). Base case 2040→2050 (rounded, private-analysis figures): sell leads,
  rent and live behind it — consistent with the published conditional recommendation.
- `test-browser.cjs` — **not run in this sandbox**: Chromium cannot start (`libnss3.so`
  missing), the same limitation session `fdf0ec80` recorded; it runs in CI on the pull
  request and on `main`.

## 4. Irregularities logged for the owner

1. **PR #104 handover.** The owning session recorded all tasks done but left the PR
   conflicting and the promised publish record unwritten; idle >60 minutes, so this session
   took it over, integrated it, and completes the record here. Nothing from `22614eaa` was
   discarded.
2. **Standing owner decisions (unchanged):** L-D2 pre-rounding history scrub (runbook on
   the Flagged page; needs force-rewrites and GitHub Support — outside session permissions)
   and the repository-visibility decision (repo remains public; legacy household-figure
   files are excluded from Pages by `_config.yml` but visible on GitHub).
3. **Pages mode** remains the legacy builder (source `main` / `/`); `_config.yml`
   exclusions are the live control. Switching to the Actions artifact needs Pages admin
   rights this connection lacks (403, as sessions `2ddad241`, `a29630ce`, `9edb6a52` and
   `fdf0ec80` also found).
4. `scripts/runtime-test.cjs` remains stale (scans the un-produced `_public/site`) —
   retained dashboard tooling, not part of the published artifact.
