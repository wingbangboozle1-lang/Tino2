# Independent review — 16 November 2026

Session: `e3f08d9e` · branch: `arena/e3f08d9e-tino2` · baseline: `8b27103dbff74945d726dfa9fd7ce4eb2039f9ee` (`origin/main`, merge of PR #125).

## Outcome

The owner's 16 Nov brief asks for one thing the published Black-swan page could not answer: what
happens to a **phased-investing plan tested against real economic conditions**, where sale proceeds
sit in 3-month-to-2-year Treasuries for 24–36 months after the inheritance before moving into
stocks, specifically to see how a 1929- or 2008-style entry behaves and **what the reinvestment risk
on the parked money costs beside the headline**. The page published at the baseline answered that
only with two smooth geometric templates and a **flat** 4.32% parking yield.

This session added the recorded-history test to the generator and published it as section
`04 / recorded history` of `guide/stress.html`, built from `scripts/phased_history.py` at build time
(no hand-written figures anywhere in the section, so a page and its model cannot disagree). Six
tables, every row source-linked, every dollar rounded to the nearest $10. Alongside it: the two
stale items handed over from PR #119 (the renamed IRS newsroom source, and the annual gift
exclusion, which no page displayed), three new flagged items, four new suggestions, four new figure
ledger records, an administrator-facing Git-history exposure audit wired into CI, and a written
remediation runbook.

**The model's conditional ranking did not move.** No input to `scripts/analysis_model.py`,
`scripts/phased_model.py` or the retained dashboard changed; `node scripts/validate.js`
(1,610 checks, 19 pages, 178 official sources) and `node scripts/stress-test.js` (50-year paths,
estate ownership, privacy, real-dollar and shock tests) both pass unchanged, and the retained
dashboard's base case is still sell $7,683,290 / rent $6,249,830 / live $5,135,780 for
2040→2050 — figures that belong to the retained, unpublished tree and are recorded here only to
show that nothing shifted. What the new section adds is a **price on the timing decision**, which
the ranking does not express: on the record, parking and phasing is a plan that usually costs money
and occasionally buys a shallower drawdown.

## What was built, and how it was verified

- `scripts/phased_history.py` — the engine. Reads the two official CSV extracts under
  `research/data/` and nothing else. `simulate(entry_year, strategy)` walks 120 months: parked cash
  earns the published **annual average** of the H.15 constant-maturity yield for that calendar year,
  compounded at one-twelfth of the annual rate; the phase-in is twelve equal monthly tranches sized
  from the balance the account holds when the parking window closes; the stock leg follows a
  geometric interpolation between the two December observations of the price index, with one stated
  dividend assumption. Strategies: invest now, park 24, park 36, park 24 at the 2-year note yield,
  stay in bills.
- `research/data/fred_treasury_annual_2026-11-16.csv` (`DGS3MO` annual averages 1982–2026, `DGS2`
  1977–2026) and `research/data/fred_equity_annual_2026-11-16.csv`
  (`SPASTT01USM661N` December levels 1970–2025, `CPIAUCNS` annual averages), each with a README
  recording the series, the retrieval command, the cross-checks performed on 16 Nov 2026 and the
  limits. **No household figure is an input to any of it.**
- Cross-checks that passed on 16 Nov 2026 against the official series pages: `DGS3MO` annual
  2007–2009 and 2011–2012 = 4.48, 1.40, 0.15, 0.14, 0.05; the daily series shows the collapse inside
  the crash window (4.64% on 2007-08-14 → 3.12% on 2007-08-20 → 0.25% on 2008-10-10 → 0.02% on
  2008-11-21); the index's December 2007/2008/2009 levels match the extract already in the repo; all
  thirteen `CPIAUCNS` annual averages 2013–2025 match, with 2026 blank as expected.
- `scripts/test-phased-history.py` — an independent guard, not a copy of the engine: it recomputes
  terminal values and worst-points for **35 entry years × 5 strategies × 3 dividend settings** and
  several yield overrides in closed form, asserts the tranche arithmetic (`full_tranches`), asserts
  the interpolation reproduces the December observations exactly and stays inside the bracket,
  asserts the window bounds, and asserts the **specific figures the page publishes** (the median
  −$42,860, the 2008 gain $41,030, the flat-yield flattery $17,610, the maturity bound $11,620 and
  median $2,700, and the median/mean triple quoted on the flagged page). It prints
  `PASS … 1303 checks`. A model edit that moves a published figure now fails this test.
- Two engine bugs were found during this session and fixed. (1) Interest was credited only on the
  residual cash while tranches were bought at a fixed `PRINCIPAL / 12`; the tranche is now sized from
  the balance at the month the window closes, which raised every published park figure by $15k–$21k
  per $100,000 (e.g. the 1987 park-24 result moved $287,360 → $302,570). The first run's numbers are
  superseded and are not quoted anywhere. (2) `summary()` was taking the upper-centre value for an
  even count; it now uses a `median()` helper that averages the two central values, so the two-case
  deep-crash group reports $13,440 (the mean of +$41,030 and −$14,160) rather than one of them.

## The result published on the page, in one place

Per $100,000 of illustrative proceeds over ten years, month 0 = the December before the entry year,
entry years 1982–2016 (n = 35), 2.0-point-a-year dividend assumption:

| Group | Entries | Park 24 beat invest-now | Median | Best / worst | Worst point improved |
| --- | --- | --- | --- | --- | --- |
| Every entry year | 35 | 6 (1999, 2000, 2001, 2006, 2007, 2008) | −$42,860 | +$66,060 / −$132,870 | 11 of 35 |
| Years the index rose or held flat | 26 | 4 (1999, 2000, 2006, 2007) | −$46,670 | +$66,060 / −$132,870 | 3 of 26 |
| Years it fell | 9 | 2 (2001, 2008) | −$30,950 | +$41,030 / −$65,880 | 8 of 9 |
| Years it fell by 10% or more | 2 | 1 (2008) | +$13,440 | +$41,030 / −$14,160 | 2 of 2 |

Selected entry years, as published: 1987 invest-now $335,900 / worst $96,810 against park-24
$302,570 at a 6.42% parked yield; 1989 $451,950 / $100,000 against $400,060 at 8.07%; 2000
$129,550 / $79,800 against $165,720 at 4.73%; 2002 $146,470 / $83,970 against $132,310 at 1.33%;
2007 $148,720 / $63,240 against $214,780 at 2.93%; 2008 $157,940 / $57,430 against $198,970 at
0.77%; 2015 $220,630 / $96,140 against $191,720 at 0.18%.

The two findings the brief asked to see beside each other:

- **Reinvestment risk is not a footnote.** Assuming today's 4.32% persists over the 2008 parking
  window instead of the recorded 1.40%-then-0.15% path adds **$17,610** to the parked result
  ($216,580 against $198,970) — about a fifth of the median cost of waiting. An invented flat 1.00%
  adds $1,410; 5.00% adds $21,190.
- **Maturity is second-order; the entry date is not.** Rolling 3-month bills versus holding 2-year
  notes moved the ten-year outcome by at most **$11,620** per $100,000 across all 35 entries and
  about **$2,700** at the median, while the entry date moved it by tens of thousands. A 36-month
  park costs about a year more of the same trade: **−$61,620** at the median against −$42,860.

## Bounds a reader must not cross

These are stated on the page and repeated here, because they are the difference between a test and
a marketing claim:

1. **The window is 1982–2016, not 1929–2026.** `DGS3MO` begins 1 September 1981, so no earlier entry
   can be replayed on recorded yields; the price index ends 2025, so the last entry year whose ten
   years fit inside it is 2016. **A 1929-style entry is not reachable by this test at all** — the
   template section above it is the only view of that shape, and the page says so.
2. **The equity series is a price index.** Distributions are not in it. The 2.0-point-a-year
   dividend assumption is invented here, and it moves the headline a lot: the median cost of waiting
   is −$22,740 with none, −$42,860 at 2.0 points and −$64,730 at 4.0 (means: −$23,130 / −$40,190 /
   −$62,280). Anyone reusing this must fix their own total-return convention first.
3. **December sampling understates within-year swings.** On the record, 1987 reads −5.1% year-end
   although the same series fell 26.8% between its August 1987 monthly value and its December value,
   and 2000 reads +1.1% in a year that began with a five-month decline. The "fell by 10% or more"
   group therefore contains **two cases, not a rate**, and the page labels it that way rather than
   quoting a frequency.
4. **Yields are annual averages, applied monthly.** H.15 is quoted on an investment basis; daily
   compounding within a crash month is not modelled, and the daily series shows how fast those rates
   moved in 2008.
5. **Real-terms figures are this site's approximation, not published numbers.** The deflated median
   (−$31,170 against the nominal −$42,860) comes from deflating a December-to-December path by
   annual CPI-U averages. No TIPS, no inflation-linked security, no tax, no transaction cost, no
   mid-parking change of mind.
6. **Nothing here is a forecast, and no probability is attached to any entry year.** The illustrative
   $100,000 is the same invented amount the template test uses; it is not a household figure.

## Official statements re-read for the K-2 items, 16 Nov 2026

- **IRS news release IR-2026-133, dated Nov. 5, 2026** (citing Rev. Proc. 2026-35): "Estates of
  decedents who die during 2027 have a basic exclusion amount of **$15,480,000**, up from a total of
  $15,000,000 for estates of decedents who died in 2026. For calendar year 2027, the first
  **$20,000** of gifts to any person are not included in the total amount of taxable gifts made
  during the year – up from **$19,000** for calendar year 2026." The same release gives the
  **non-citizen-spouse** gift exclusion as **$201,000** for 2027, up from **$194,000**. The Taxes
  page now carries the gift pair, the Questions register states the rule, and four ledger records
  (`FED-GIFT-EXCLUSION-2026/2027`, `FED-GIFT-SPOUSE-NONCITIZEN-2026/2027`) back it. The link was
  already registered as `estate27`, so no page had to change its citation — only the figures.
- **Rev. Proc. 2025-32, §2.14**: OBBBA §70106 amended **§2010(c)(3)** to set the basic exclusion at
  **$15,000,000 for calendar year 2026**, with §2631(c) GST exemption likewise $15,000,000, both
  "adjusted for inflation for calendar year 2027 and future years". The document names the statute
  "One, Big, Beautiful Bill Act", P.L. 119-21, 139 Stat. 72 (4 July 2025). Now a register row
  (`rp2532`) and cited by the 2026 gift record.
- **Congress.gov, H.R. 1301** (re-read 16 Nov 2026): Rep. Randy Feenstra [R-IA-4], introduced
  13 Feb 2025, House Ways and Means, latest action still the 13 Feb 2025 referral, tracker status
  "Introduced", zero CBO cost estimates. The watchlist row now states this; the page does not treat
  repeal as law.
- **leginfo, SB 284** (re-read 16 Nov 2026): "Active Bill - In Committee Process", House Location:
  Assembly, last amended 25 Jun 2025, latest history action 14 Jul 2025 ("Set, final hearing. Held in
  committee and under submission"), amending R&T Code §63.2 and adding §63.2.1. Proposal, not law.
- Both date-stamped statements in the law-watch table header moved from "checked 15 Nov 2026" to
  "re-read 16 Nov 2026", and the hero, footer and sources-page note record the 13–16 Nov 2026
  re-read range.

## Privacy work in this changeset

`scripts/privacy-history-audit.py` (new) answers the standing owner item L-D2/P-4 in the only form a
session branch can: an **inventory**, not a cleanup. It walks `git rev-list --objects --all --reflog`,
scans each unique text blob **once** through a single batched `git cat-file --batch`, and applies
`scripts/privacy-gate.py`'s own `scan_text` — imported, not copied, so history and HEAD cannot drift
apart in policy. It prints counts, rule names, file **paths** and blob ids, never a matched string or
blob content, so its own output is safe to paste into a ticket. Default exit 0; `--strict` exits 1;
`--json` for machine-readable counts.

- Proved non-vacuous in a throwaway three-commit repository (16 Nov 2026): a `docs/bad.md` carrying a
  registered identifier and `$1,234`, then amended twice, produced `flagged blobs: 4` and
  `BLOCKED-IDENTIFIER×4, ROUNDING×2`, while the clean sibling produced nothing; `--strict` exited 1.
- `.github/workflows/pages.yml` now runs its `--self-test` as a **blocking** step in the verify job,
  and a separate **non-blocking** `history-audit` job runs the inventory with `fetch-depth: 0` and
  prints both the human and `--json` reports. CI measures; it does not gate a merge on a history
  finding, because remediation is an owner decision (S16/S25).
- `docs/history-remediation-runbook.md` (new, `docs/` is excluded from Pages) separates the three
  layers — published artifact, repository at HEAD, Git history and external copies — and sets out
  the four options with the consequences GitHub documents: **on GitHub Free a published Pages site
  is automatically unpublished when a repository becomes private**, and **public forks are detached
  and are not made private**; a rewrite needs git-filter-repo ≥ 2.47, the `refs/pull/*/head` check,
  a force-push that will fail on read-only `refs/pull/*`, and a Support request to remove cached views
  and PR references; Support may offer dereferencing, which keeps PR bodies and comments; one merge
  from a stale clone can reintroduce the purged objects, which is why the board forbids sessions
  from force-pushing at all.
- **Honest limit, and the first real finding.** This clone is shallow: `.git/shallow` is present and
  before the merge `git rev-list --all --count` returned **2**. The audit run then reported
  `unique text blobs scanned: 239`, `flagged blobs: 0`, and printed that a clean report from a two-commit clone is a
  statement about what was fetched, not about the remote history. After merging 30 commits of `main` — 33 reachable
  commits, 401 unique text blobs — the same run reported **2 flagged blobs, `RAW-FIGURE×6`**, on an earlier
  `COORDINATION.md` blob and an earlier `verification/c96c185e/REPORT.md` blob, both of which are clean at HEAD. That
  is the exposure class L-D2 describes, measured rather than assumed, and it is why the audit labels every hit as
  "still the blob at HEAD" or "history only": the first kind needs a file change, the second needs a rewrite. **No claim is made that history is clean, and none is made that it is
  dirty — it has not been measurable from here.** `scripts/privacy-gate.py` on the tracked tree still
  passes (238 files), and `scripts/privacy-audit.cjs` still passes on packaged source and rendered
  text. Both remain "a guard, not proof of anonymity".

## Merge with `main`, and the duplicate work it revealed

`origin/main` advanced 30 commits during this session (PRs #126–#132, seven other sessions). The branch was merged
with `origin/main` and the result re-verified; the merge touched only what this session claimed, and the resolution
kept **both** sides everywhere they differed:

- **Both sides wrote a gift-exclusion row and both added ledger records.** Upstream had already published the 2026
  $19,000 amount citing Rev. Proc. 2025-32 §4.42(1) (`GIFT-ANNUAL-2026`). This session's row adds the 2027 $20,000
  figure and the non-citizen-spouse pair from IR-2026-133. The two rows on the Taxes page were merged into one row
  that cites both documents, the non-citizen-spouse row was kept, and both ledger records were kept — 44 records,
  unique ids, no duplicate claim. That is a real overlap in scope, not a mistake in either session: the board had
  assigned the gift figure to nobody, and two sessions picked it up off the same stale-flag list. The coordination
  board records it.
- **Two sections on the same page, deliberately.** Upstream's `03c / ladder and shape` section adds a
  return-to-peak 1929 shape and a 3-month/2-year ladder on the *template* model; this session's `04 / recorded
  history` section replays the same decision on *recorded* yields and prices. They answer different questions and are
  now ordered so each introduction names the other correctly. One of this session's flagged rows ("crash shapes are
  illustrative") was superseded by upstream's amended version and the merge kept upstream's.
- **This session's four suggestions renumbered to S33–S36** because upstream registered S30–S32 first; S16 and S25,
  which the published callouts cite, are unchanged.
- **The privacy gate grew a fourth rule mid-session** (`RAW-FIGURE`, upstream `8712a6e`). Rather than leave the
  history audit enforcing three of four, it now reads that list through the same gate import and passes it into
  `scan_text`, so the object walk and the working tree still cannot drift apart.
- Counts in this report are from the merged tree: 19 generated pages, 33 packaged files, 44 ledger records,
  1,231 source-linked rows, 13,783 rendered checks, 291 tracked files in the whole-repository gate, 20,736 model
  comparisons, 200 phased-model checks, 1,303 recorded-history checks.

## Checks run, all on the merged tree

`python3 scripts/build-guide.py` · `check-generated.py` PASS (19 generated public pages up to date) ·
`check-figures.py` PASS (**44** ledger records, 44 verified, 0 explicitly unverified, every
seven-figure published amount backed) · `package-site.py` PASS (33 reviewed guide files, legacy site
excluded) · `check-publication.py --self-test` PASS (extra, missing, altered, symlinked and
hard-linked files rejected) · (the `--directory _site --jekyll` variant of that check runs in CI,
where Jekyll builds `_site`; it was not run locally) ·
`node scripts/test-guide.cjs` PASS (19 rendered pages, **1,231** source-linked table rows, **13,783**
checks) · `node scripts/privacy-audit.cjs` PASS · `python3 scripts/privacy-gate.py` PASS (291 tracked text files, now including the upstream RAW-FIGURE rule) ·
`privacy-gate.py --self-test` PASS · `privacy-history-audit.py --self-test` PASS ·
`test-model-reference.py` PASS (108 configurations, 250 stress years, 1,500 phased years, 20,736
comparisons) · `test-phased.py` PASS (200 checks) · `test-phased-history.py` PASS (1,303 checks) ·
`node scripts/validate.js` PASS (1,610 checks, 19 pages, 178 official sources) ·
`node scripts/stress-test.js` PASS · `python3 -c "import ast; ast.parse(...)"` on both new Python
files and the generator.

Environment note for the next session in a fresh sandbox: the node suites need
`npm install --prefix .cache/test --no-audit --no-fund --ignore-scripts jsdom@26.1.0` (`.cache` is
git-ignored), and `node scripts/test-guide.cjs` reads `_public`, so **run `package-site.py` before
it** or it fails against a stale copy. `node scripts/test-browser.cjs` still cannot launch Chromium
here (`libnss3.so` absent); CI covers it.

## Findings for review — not implemented here

1. **Standing contradiction, for the owner to adjudicate.** This brief asks for real rounded household
   figures and a recommendation on the site; sessions `742b77cb` and `b2418dfa` deliberately made the
   published artifact synthetic-only, with the real dashboard retained under `site/**` and excluded
   from Pages. Both cannot be the intended public product. Every page here follows the
   synthetic-only rule, and the household history table on the Properties page remains owner-stated
   and rounded. Nothing in this session resolved it, and it should not be resolved by a session.
2. **Medium — the recorded test needs a total-return series, not a price index, to be usable as
   policy.** `SPASTT01USM661N` is price-only. A published total-return series (or an official TIPS
   yield series for the cash leg) would replace two of the assumptions here. Deliberately not
   invented: the sensitivity table shows the range instead.
3. **Medium — monthly history would fix the sampling bias.** Annual averages and December levels hide
   the shape that matters for a 24-month park. The official index is published monthly (the December
   values in this extract were read from the monthly endpoint), so a within-year series for both the
   index and the bill yields is a fetch away; that would let the test read peak-to-trough rather than
   December-to-December. Deliberately not done here, because it changes every published figure and
   needs its own re-verification pass.
4. **Low — `verification/**` is outside `ROUND_SCOPE`.** The gate's *rounding* rule deliberately covers the
   analysis artifacts, not these reports, so the $10 convention is honoured here by hand. Upstream's new RAW-FIGURE
   rule now does apply to every tracked file, and it is what caught the c96c185e report; but a *new* un-rounded
   household amount written into a report outside `ROUND_SCOPE` is still not caught by the general rule. If the owner
   wants the $10 rule everywhere, that is a one-line change to `scripts/privacy-scrub.py`'s scope tuple, which this
   session did not touch — the file belongs to the privacy owner, not to this scope.

## Checks not claimed

- No Git history was rewritten, no branch deleted, no force-push, no repository visibility change, no
  GitHub Support request. Those are administrator actions and remain open.
- The passing working-tree scans do **not** establish that the complete remote history, other
  branches, PR refs, forks, caches or clones are clean; the opposite is more likely, which is what
  the runbook is for.
- No private records were accessed. No appraisal, tax bill, lease, insurance quote, trust instrument
  or estate inventory exists in this repository, and none is inferred in the published pages.
- The site is an analysis of fictional examples plus published law. It is not an appraisal, a tax
  return, a legal opinion, an insurance quote or a personalised investment recommendation, and the
  recorded-history section in particular must not be read as an expected return for any household.
