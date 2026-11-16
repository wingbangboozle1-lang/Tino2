# Privacy-first integration audit — session `787f3bce`

**Date:** 16 Nov 2026. **Branch:** `arena/787f3bce-tino2`. The audit began on `8b27103`; after rebasing onto PR #126, PR #128 (`e72015ae`) added independently source-reviewed tax/timeline updates before PR #127 merged. The combined main merge commit is `2740f40`. This session reran the full local suite on `2740f40`; GitHub verification and Pages deployment on the same commit also passed. No household facts, identifiers, property locations, or household-derived figures are reproduced in this report.

## Scope and result

This was an independent audit of the existing synthetic-only public guide and its repository checks. No generated page, model input, source row, or recommendation was changed. The requested public-guide features are already present: the first-screen decision-change table and executive summary; pure and mixed paths; common-horizon comparison; what-if controls; phased 24/36-month Treasury parking beside crash-entry risk; timeline, glossary, questions and answers, suggestions, and flagged items; and a printable one-page Attorney & CPA sheet. Private household facts remain blank or explicitly unverified in the public product.

The published guide is limited by the checked package boundary to 32 reviewed guide files. The retained legacy dashboard and research material are not part of the Pages artifact. This separation is not a Git access control and does not clean the repository's history.

## Local checks

The checks below were rerun on the combined tree at `2740f40`, including PR #128's tax/timeline update. The complete `Verify public Pages boundary` workflow also passed on that commit, including the rendered-page and browser tests. The only initial local environment issue was a missing `jsdom` dependency; it was installed under the ignored `.cache/test/` directory only, with no dependency manifest or generated package committed.

| Check | Result |
|---|---|
| `python3 scripts/check-generated.py` | PASS — 18 generated public pages current |
| `python3 scripts/check-figures.py` | PASS — 39 figure-ledger records; all 39 marked verified in the ledger |
| `python3 scripts/package-site.py` | PASS — 32 reviewed guide files packaged; legacy `site/` excluded |
| `python3 scripts/check-publication.py --self-test` | PASS — package boundary and rejection tests pass |
| `python3 scripts/privacy-gate.py` | PASS — 240 tracked text files scanned; no registered blocked identifier, unrounded household-scale amount in analysis artifacts, or contact/parcel pattern detected |
| `python3 scripts/privacy-gate.py --self-test` | PASS — registered-token detection works |
| `node scripts/privacy-audit.cjs` | PASS — no registered hashed household-input token, property locator, or common identifier found in packaged source/rendered text |
| `python3 scripts/test-model-reference.py` | PASS — 108 decision configurations, 250 stress years, 1,500 phased-investment years, and 20,736 arithmetic comparisons |
| `python3 scripts/test-phased.py` | PASS — 113 phased-investment checks |
| `node scripts/test-guide.cjs` | PASS — 18 rendered pages, 1,058 source-linked table rows, 12,405 checks |
| `node scripts/validate.js` | PASS — 1,610 checks across 19 retained-dashboard pages and 178 registered official sources; this dashboard is not in the Pages package |
| `node scripts/stress-test.js` | PASS — 50-year, ownership, privacy, real-dollar, and shock tests |

These privacy scans are limited regression checks, not proof of anonymity or a history scrub. `check-figures.py` validates the published figure ledger, not any private household fact.

## Source and legal verification boundary

This session did **not** independently fetch non-GitHub official-government websites. The current source links and ledger were inspected locally, but that is not a fresh source re-opening. The current tree also includes [`verification/e72015ae/REPORT.md`](../e72015ae/REPORT.md), a separately completed 16 Nov official-source review covering the Form 540 sensitivity, IRS Forms 706/4768, and Proposition H schedule, with unresolved items explicitly listed. Prior dated reviews are available in [`verification/9edb6a52/REPORT.md`](../9edb6a52/REPORT.md), [`verification/9a2a5cce/REPORT.md`](../9a2a5cce/REPORT.md), and [`verification/9ad78d96/REPORT.md`](../9ad78d96/REPORT.md); the public [Sources page](../../guide/sources.html) links the official references for manual review. Those records do not turn present law or market rates into a forecast for a future transfer.

PR [#119](https://github.com/wingbangboozle1-lang/Tino2/pull/119) remains open and conflicting. Its report is based on an earlier tree, predates the current synthetic-only privacy change, and includes a statement about the older household-input model that is not true of the current tree. It was not merged or used as current-tree verification in this audit. Any future integration of that report must preserve its historical date and correct the stale privacy-state description first.

## Deployment check

GitHub reports Pages as `built` from `main` at `https://wingbangboozle1-lang.github.io/Tino2/`. PR [#127](https://github.com/wingbangboozle1-lang/Tino2/pull/127) merged at 17:56:48 UTC as `2740f40`; it included the concurrent PR #128 tax/timeline update. On that combined commit, `Verify public Pages boundary` run [43923663254](https://github.com/wingbangboozle1-lang/Tino2/actions/runs/43923663254) and `pages build and deployment` run [43923661827](https://github.com/wingbangboozle1-lang/Tino2/actions/runs/43923661827) both completed successfully. The verification workflow includes the rendered-page and browser tests. The Pages API now reports `built`. GitHub emitted non-blocking workflow annotations about `upload-artifact@v4` moving from Node 20 to Node 24 and the `ubuntu-latest` runner migration; neither affected this deployment. This session used the GitHub API and did not independently fetch the public HTML for a live content read-back.

## Critical outstanding privacy issue

The current Pages artifact is synthetic-only, but the repository remains public. The checkout is shallow and this session is restricted to its current branch; it did not rewrite `main`, other remote refs, pull-request refs, or Git history. Earlier commits, retained legacy files, branches, pull-request refs, forks, clones, and caches may still expose prior household-derived material. The passing package and privacy gates do not establish that those copies are clean. Keep P-4 on the Flagged page as an urgent repository-administrator action; follow [GitHub's sensitive-data removal procedure](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) and verify repository visibility and all remote copies before considering the incident contained.

**Additional logging surface found.** The public verification workflow runs `scripts/validate.js` on the retained dashboard; its final output includes a calculated sell/rent/live summary. The workflow itself describes the retained dashboard as household-derived, so those values may appear in public GitHub Actions logs even though the dashboard is excluded from Pages. This session has expanded scope to remove only that summary output while preserving the validation assertions. Existing run logs and legacy model data remain outside this code change and require separate administrator review.

## Remaining decision blockers

No personal household recommendation can be supported by this public synthetic model. The public Questions and Flagged pages correctly leave household-specific facts for private verification, including trust authority/title, date-of-death valuation and income-tax basis, estate assets/prior gifts/portability, Proposition 19 eligibility and occupancy, property-specific assessment/tax-rate data, leases/local rules, independent rent/value evidence, insurance quotations, debt, and five-year capital plans. Obtain and review those documents with qualified counsel and tax professionals before choosing a path. See the [Questions register](../../guide/questions.html), [Suggestions register](../../guide/suggestions.html), and [Flagged page](../../guide/review.html).
