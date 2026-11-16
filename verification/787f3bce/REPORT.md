# Privacy-first integration audit — session `787f3bce`

**Date:** 16 Nov 2026. **Branch:** `arena/787f3bce-tino2`. The audit began on `8b27103` and followed concurrent integrations through `7a11f4c` (PR #129), which added the pre-commitment register and a separately documented 16 Nov source review. This session's latest local checks ran on that tree plus a one-line `scripts/validate.js` output suppression. PRs #130 and #131 were open and not included in these local results. No household facts, identifiers, property locations, or household-derived figures are reproduced in this report.

## Scope and result

This was an independent audit of the existing synthetic-only public guide and its repository checks. No generated page, model input, source row, or recommendation was changed by this session. The current tree includes the first-screen decision-change table and executive summary; pure and mixed paths; common-horizon comparison; what-if controls; phased 24/36-month Treasury parking beside crash-entry risk; timeline, glossary, questions and answers, suggestions, the pre-commitment register, and flagged items; and a printable one-page Attorney & CPA sheet. Private household facts remain blank or explicitly unverified in the public product.

The published guide is limited by the checked package boundary to 32 reviewed guide files. The retained legacy dashboard and research material are not part of the Pages artifact. This separation is not a Git access control and does not clean the repository's history.

## Local checks

The checks below were rerun on the tree at `7a11f4c` (including PRs #127–#129) plus this session's output-only change to `scripts/validate.js`. They do not include the still-open PRs #130 or #131. The full workflow passed on the previous combined main commit `2740f40`, including rendered-page and browser tests; a new verification/deployment run for `7a11f4c` was still in progress at the time of this update. The only initial local environment issue was a missing `jsdom` dependency; it was installed under the ignored `.cache/test/` directory only, with no dependency manifest or generated package committed.

| Check | Result |
|---|---|
| `python3 scripts/check-generated.py` | PASS — 19 generated public pages current |
| `python3 scripts/check-figures.py` | PASS — 39 figure-ledger records; all 39 marked verified in the ledger |
| `python3 scripts/package-site.py` | PASS — 33 reviewed guide files packaged; legacy `site/` excluded |
| `python3 scripts/check-publication.py --self-test` | PASS — package boundary and rejection tests pass |
| `python3 scripts/privacy-gate.py` | PASS — 243 tracked text files scanned; this pre-PR-#131 gate checks registered identifiers, unrounded household-scale amounts and contact/parcel patterns, but is not proof that all raw tokens are absent |
| `python3 scripts/privacy-gate.py --self-test` | PASS — registered-token detection works |
| `node scripts/privacy-audit.cjs` | PASS — no registered hashed household-input token, property locator, or common identifier found in packaged source/rendered text |
| `python3 scripts/test-model-reference.py` | PASS — 108 decision configurations, 250 stress years, 1,500 phased-investment years, and 20,736 arithmetic comparisons |
| `python3 scripts/test-phased.py` | PASS — 113 phased-investment checks |
| `node scripts/test-guide.cjs` | PASS — 19 rendered pages, 1,107 source-linked table rows, 12,837 checks |
| `node scripts/validate.js` | PASS — 1,613 checks across 19 retained-dashboard pages and 178 registered official sources; after this session's change it prints check counts only, not a financial outcome summary |
| `node scripts/stress-test.js` | PASS — 50-year, ownership, privacy, real-dollar, and shock tests |

These privacy scans are limited regression checks, not proof of anonymity or a history scrub. `check-figures.py` validates the published figure ledger, not any private household fact. The then-open PR [#131](https://github.com/wingbangboozle1-lang/Tino2/pull/131) reports residual raw-token matches in the tracked tree and proposes a stronger whole-repository gate/redaction; that PR was not merged at this audit point, so the repository must still be treated as exposed until the proposed remediation is reviewed, merged, and retested.

## Source and legal verification boundary

This session did **not** independently fetch non-GitHub official-government websites. The current source links and ledger were inspected locally, but that is not a fresh source re-opening. The current tree includes [`verification/070d6a2e/REPORT.md`](../070d6a2e/REPORT.md), which records a separate 16 Nov official-source recheck and the pre-commitment register, and [`verification/e72015ae/REPORT.md`](../e72015ae/REPORT.md), which records the separate Form 540 sensitivity, IRS Forms 706/4768, and Proposition H review with unresolved items explicitly listed. Prior dated reviews are available in [`verification/9edb6a52/REPORT.md`](../9edb6a52/REPORT.md), [`verification/9a2a5cce/REPORT.md`](../9a2a5cce/REPORT.md), and [`verification/9ad78d96/REPORT.md`](../9ad78d96/REPORT.md); the public [Sources page](../../guide/sources.html) links official references for manual review. Those records do not turn present law or market rates into a forecast for a future transfer.

PR [#119](https://github.com/wingbangboozle1-lang/Tino2/pull/119) was closed with a handoff; its dated report is preserved in [`verification/84257489/REPORT.md`](../84257489/REPORT.md) and is historically tied to an older tree. It must not be treated as a current-tree privacy review. The current main also has in-progress, conflicting PRs #130 and #131; this session did not edit their files or treat their unmerged changes as verified.

## Deployment check

PR [#127](https://github.com/wingbangboozle1-lang/Tino2/pull/127) merged at 17:56:48 UTC as `2740f40`; it included the concurrent PR #128 tax/timeline update. On that commit, `Verify public Pages boundary` run [43923663254](https://github.com/wingbangboozle1-lang/Tino2/actions/runs/43923663254) and `pages build and deployment` run [43923661827](https://github.com/wingbangboozle1-lang/Tino2/actions/runs/43923661827) both succeeded, including rendered-page and browser checks. After PR #129 advanced `main` to `7a11f4c`, verification run [43924938101](https://github.com/wingbangboozle1-lang/Tino2/actions/runs/43924938101) and Pages run [43924936511](https://github.com/wingbangboozle1-lang/Tino2/actions/runs/43924936511) both completed successfully, including browser tests. The Pages API still returned `building` on the immediate follow-up check, so the API status needs a fresh read before declaring that latest deployment `built`. The `7a11f4c` run predates this session's `scripts/validate.js` output suppression, so its public job log may contain the former derived summary; the new output-only change has not yet run in CI. GitHub emitted non-blocking workflow annotations on the prior build about `upload-artifact@v4` moving from Node 20 to Node 24 and the `ubuntu-latest` runner migration. This session used the GitHub API and did not independently fetch the public HTML for a live content read-back.

## Critical outstanding privacy issue

The current Pages artifact is synthetic-only, but the repository remains public. The checkout is shallow and this session is restricted to its current branch; it did not rewrite `main`, other remote refs, pull-request refs, or Git history. Earlier commits, retained legacy files, branches, pull-request refs, forks, clones, and caches may still expose prior household-derived material. The passing package and privacy gates do not establish that those copies are clean. Keep P-4 on the Flagged page as an urgent repository-administrator action; follow [GitHub's sensitive-data removal procedure](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) and verify repository visibility and all remote copies before considering the incident contained.

**Additional logging surface and mitigation.** The public verification workflow runs `scripts/validate.js` on the retained dashboard; its former final output included a calculated sell/rent/live summary. This session removed that output line only: the validator still runs all assertions and now emits only the non-financial check count. A local run passed (1,613 checks). This does not remove legacy model inputs or past GitHub Actions logs; both remain within the administrator's broader P-4 review.

## Remaining decision blockers

No personal household recommendation can be supported by this public synthetic model. The public Questions and Flagged pages correctly leave household-specific facts for private verification, including trust authority/title, date-of-death valuation and income-tax basis, estate assets/prior gifts/portability, Proposition 19 eligibility and occupancy, property-specific assessment/tax-rate data, leases/local rules, independent rent/value evidence, insurance quotations, debt, and five-year capital plans. Obtain and review those documents with qualified counsel and tax professionals before choosing a path. See the [Questions register](../../guide/questions.html), [Suggestions register](../../guide/suggestions.html), and [Flagged page](../../guide/review.html).
