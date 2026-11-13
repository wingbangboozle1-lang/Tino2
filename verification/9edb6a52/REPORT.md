# Session 9edb6a52 — independent verification report (2026-11-13)

**Branch:** `arena/9edb6a52-tino2` (synced to `origin/main` = `9771c8e`, merge of PR #71, before work began).
**Scope claimed in COORDINATION.md:** `verification/9edb6a52/**` plus this session's own board block. No shared public-artifact files were edited; zero defects were found in the published guide that would require one.

## 1. Method

- Read every published page of the live artifact line by line: `index.html`, `guide/{decision,stress,property,tax,process,questions,suggestions,review,sources}.html`, and the data engines they render from (`guide/data/*.js`, `assets/safe.js`).
- Re-opened the decision-critical official pages and documents live on 13 Nov 2026 and compared each site claim against the official text.
- Ran the repository's full verification suite locally on the synced tree.
- Read back the deployed GitHub Pages site live.

## 2. Official items independently re-opened by this session (13 Nov 2026)

| # | Published claim (page) | Official source (re-opened live) | Result |
|---|---|---|---|
| 1 | Prop 19 family-home allowance ≈ $1,044,590 (rounded) for 16 Feb 2025–15 Feb 2027; later amounts unknown (`guide/tax.html`) | BOE LTA 2025/009 — "$1,044,586" for that window; history table $1,000,000 → $1,022,600 → $1,044,586; next adjustment Feb 2027 | MATCH |
| 2 | Prop 19 conditions: transferee occupies within one year; homeowners'/disabled-veterans' exemption filed within one year; BOE-19-P within three years, before third-party transfer, or within six months of a supplemental/escape notice (`guide/tax.html`, `guide/process.html`) | BOE Pub 801 Fact Sheet (all conditions stated verbatim) | MATCH |
| 3 | Prop 19 framework: transferor+transferee principal residence; value cap = factored base value + allowance; renting fails the family-home condition (`guide/tax.html`, `index.html`) | BOE Proposition 19 page (comparison tables; RTC §63.2) | MATCH |
| 4 | Prop 13 mechanics: 2% cap, reassessment on change in ownership/new construction, decline-in-value relief (`guide/tax.html`, `guide/property.html`) | BOE LTA 2025/023 (Taxpayers' Rights Advocate, "How Property is Assessed") | MATCH |
| 5 | Santa Clara parent-child transfer requirements and BOE-19-P filing (`guide/property.html`, `guide/questions.html`) | Santa Clara County Assessor "Parent-Child Transfer (Proposition 19)" page | MATCH |
| 6 | Federal basic exclusion $15,000,000 (2026 deaths) and $15,480,000 (2027 deaths) (`guide/tax.html`) | IRS IR-2026-133 (Nov. 5, 2026): "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from … $15,000,000 … 2026" | MATCH |
| 7 | Filing threshold tests gross estate + adjusted taxable gifts + specific gift-tax exemption; deductions belong to taxable estate/tax, not the filing test (`guide/tax.html`) | IRS Estate tax page ("A filing is required if the gross estate … increased by the decedent's adjusted taxable gifts and specific gift tax exemption, is valued at more than the filing threshold"; 2026 row $15,000,000) | MATCH |
| 8 | No California estate-tax return for deaths on/after 1 Jan 2005 (`guide/tax.html`) | CA State Controller estate-tax page | MATCH |
| 9 | Inherited basis is generally date-of-death FMV with exceptions; the cited irrevocable grantor-trust fact pattern got no §1014 adjustment (`guide/tax.html`, `guide/decision.html`) | IRS Rev. Rul. 2023-2 (no basis adjustment where trust assets are not includible in the owner's gross estate) | MATCH |
| 10 | Federal home-sale exclusion $250,000/$500,000, ownership+use conditions, not automatic (`guide/tax.html`) | IRS Topic no. 701 | MATCH |
| 11 | Trustee notification within 60 days of the triggering event when required (`guide/process.html`) | Cal. Prob. Code §16061.7(f) ("not later than 60 days following the occurrence of the event") | MATCH |
| 12 | Trustee/transferee files change-in-ownership statement within 150 days of death for nonprobate trust transfers (`guide/process.html`) | Cal. Rev. & Tax. Code §480(b) | MATCH |
| 13 | H.R. 1301 introduced, referred to House Ways and Means, not enacted (`guide/tax.html`) | Congress.gov bill page ("Death Tax Repeal Act", Introduced 02/13/2025, committee referral is the latest action) | MATCH |
| 14 | SB 284 in committee, not enacted (`guide/tax.html`) | CA Legislature status page (Active Bill – In Committee Process; held under submission 07/14/25; amends RTC §63.2) | MATCH |
| 15 | SF allowable rent increase 1.6% for 1 Mar 2026–28 Feb 2027; File 261020 proposed and not enacted per 9 Nov 2026 notice (`guide/property.html`, `guide/tax.html`) | SF Rent Board "Current Rates" report | MATCH |
| 16 | USGS 72% chance of ≥1 M6.7 Bay Area earthquake 2014–2043 (`guide/stress.html`) | USGS Fact Sheet 2016-3020 (2014 Working Group on California Earthquake Probabilities) | MATCH |
| 17 | BLS Dec-2022 CPI: all items +6.5%, electricity +14.3% over 12 months (`guide/stress.html`) | BLS CPI news release archive cpi_01122023.htm (6.5% all items; electricity 14.3% 12-month table) | MATCH |
| 18 | CBO Feb-2026 outlook covers 2026–2036; PCE inflation returns to roughly 2% (Fed long-run goal) in 2030 (`guide/stress.html`) | CBO "The Budget and Economic Outlook: 2026 to 2036" (Feb 11, 2026), publication 61882 | MATCH |
| 19 | Deployed site serves the current guide (homepage + navigation to all subpages) | Live read-back of https://wingbangboozle1-lang.github.io/Tino2/ | CONFIRMED |

## 3. Items carried forward, not re-opened by this session

Verified live by prior sessions whose board entries and reports record the dates and URLs; this session reviewed the claims for consistency but did not fetch each URL again: IRS inherited-basis FAQ, IRS Pub 527, IRS retirement-beneficiary topics, IRS rental/Topic pages, SEC investor.gov diversification bulletin, FDIC insured-deposits brochure, CDI premium-survey and earthquake pages, HUD small-area rent data, FHFA HPI via FRED (ATNHPIUS41940Q), SFMTA Proposition H parcel page, SF Department of Elections Nov-2026 results, SFPUC 2026-27 water/sewer rate schedule, City of Cupertino water page, PG&E solar billing page, SF Treasurer secured-property page, GitHub sensitive-data-removal guidance. All are official `.gov`/agency domains and each row on the site carries its own link, so the requirement "every table row linked to an official source" remains satisfied.

## 4. Page-by-page review findings

- **No factual defects found.** Every rule figure checked matched its official source (Section 2). Hedged claims ("generally", "confirm with the assessor") are accurate and appropriately qualified.
- **No privacy defects found.** All property values, bills, rents, premiums, estate amounts are blank/`unverified` placeholders; the only dollar figures are official rule values, synthetic example values, and rounded illustrative figures. No name, address, parcel or ZIP appears in the published artifact.
- Internal navigation, per-row source links, `$10` rounding, model invariants and boundary checks all enforced by the suite below.

## 5. Local suite results on the synced tree (13 Nov 2026)

| Check | Result |
|---|---|
| `python3 scripts/check-generated.py` | PASS — 10 generated public pages up to date |
| `python3 scripts/test-model-reference.py` | PASS — 108 decision configurations + 250 stress years; 10,236 arithmetic comparisons |
| `python3 scripts/package-site.py` | PASS — 18 reviewed guide files packaged; legacy site excluded |
| `python3 scripts/check-publication.py --self-test` | PASS — missing/extra/altered/symlinked/hard-linked files rejected |
| `node scripts/test-guide.cjs` | PASS — 10 rendered pages, 649 source-linked rows / 9,061 checks before the concurrent PR #72 merged; re-run after rebase: 10 pages, 656 rows / 9,188 checks |
| `node scripts/privacy-audit.cjs` | PASS — no legacy input/history tokens or common identifiers (not proof of anonymity) |
| CI `Verify public Pages boundary` on current `main` | SUCCESS (run 43380470762, includes the Chromium/WCAG browser stage which this sandbox does not run locally) |

## 6. Irregularities and handoffs (none block merge; public items also live on `guide/review.html`)

1. **Stale PR #63 takeover.** `4061a2e5`'s record PR (opened 2026-11-12 22:20 UTC, no activity since) had become `CONFLICTING` against `main`. Closed on 13 Nov 2026 with a handoff comment; its publication-record text preserved verbatim at the end of `COORDINATION.md`, credited to `4061a2e5`. Facts recorded there: PR #58 merged as `4b6a5cd` (22:16:46 UTC, 2026-11-12), verification run `43318433633` success, Pages build `43318434822` success.
   - *Note on a duplicate handoff:* session `b2418dfa` (PR #72) also listed PR #63's takeover (its V-5) — both sessions detected the same stale PR within minutes. This session closed PR #63 first (comment at ~06:56 UTC 2026-11-13, before session `b2418dfa`'s block reached main); the handoff is documented in both sessions' blocks and in the PR comment. No site or data impact.
2. **Pages source hardening still unavailable.** Retried the Pages-source switch to the Actions workflow on 13 Nov 2026: HTTP 403 `Resource not accessible by integration` (same as sessions 2ddad241 and a29630ce). Pages remains in legacy `main`/root Jekyll mode; a repository administrator must make that change. The Jekyll-output audit continues to gate what is published.
3. **Public repository history.** Earlier public branches, PRs and caches may still expose prior legacy material. Rounding, exclusions or later deletion do not remove those copies. Coordination with collaborators and GitHub's sensitive-data-removal process remains necessary (flagged on `guide/review.html`; outside any session's reach).
4. **Household-specific facts.** Real values (property values, bills, insurance, rent, trust terms, estate composition) remain blank/unverified by design; the guide's figures are synthetic examples and cannot establish a personal best plan.

## 7. Publication

PR from `arena/9edb6a52-tino2` to `main` follows this report; merged without waiting for approval per the owner's instructions. Pages deployment and live read-back are recorded in this session's block in `COORDINATION.md`.

## 8. Mid-session concurrent merge (PR #72) and re-verification

While this session was verifying, session `b2418dfa` merged PR #72 into `main` (`8bdcf7d`): rule-level answers and a decision-readiness verdict on `guide/questions.html`, the SFMTA Proposition H FY 2027-28 schedule on `guide/property.html`, updated watchlist rows, a corrected Proposition 19 cadence flag, and a 13 Nov 2026 review stamp; `scripts/build-guide.py` and `scripts/test-guide.cjs` updated accordingly. Actions taken by this session:

- Rebased `arena/9edb6a52-tino2` onto `8bdcf7d`, resolving the append-only `COORDINATION.md` conflict by keeping both sessions' blocks in full (no work discarded on either side).
- Re-read the changed pages and reviewed the PR #72 diff (`9771c8e..8bdcf7d`, 11 files, all additive/hedged; no synthetic figure or model input changed).
- Independently re-verified the newly published Proposition H figures against the live SFMTA page (13 Nov 2026): multifamily $249 up to 5,000 sq ft, then $0.195/sq ft (max $50,000); single-family $129 up to 3,000 sq ft, then $0.42/sq ft over 3,000; voters approved 3 Nov 2026; first tax on FY 2027-28 bills; senior/SRO exemptions with June 1 application deadline. All MATCH the page; Property B's own amount remains blank/unverified as published.
- Re-ran the full local suite on the merged tree: all PASS (Section 5, updated counts).
- Findings unchanged: no factual, privacy or link defects found in the combined artifact.
