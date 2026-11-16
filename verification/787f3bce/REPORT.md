# Privacy-first integration audit — session `787f3bce`

**Date:** 16 Nov 2026. **Branch:** `arena/787f3bce-tino2`. **Audit baseline:** public guide at `8b27103`, with the latest integration commit `ace7057` (PR #126) subsequently rebased into this session branch. No household facts, identifiers, property locations, or household-derived figures are reproduced in this report.

## Scope and result

This was an independent audit of the existing synthetic-only public guide and its repository checks. No generated page, model input, source row, or recommendation was changed. The requested public-guide features are already present: the first-screen decision-change table and executive summary; pure and mixed paths; common-horizon comparison; what-if controls; phased 24/36-month Treasury parking beside crash-entry risk; timeline, glossary, questions and answers, suggestions, and flagged items; and a printable one-page Attorney & CPA sheet. Private household facts remain blank or explicitly unverified in the public product.

The published guide is limited by the checked package boundary to 32 reviewed guide files. The retained legacy dashboard and research material are not part of the Pages artifact. This separation is not a Git access control and does not clean the repository's history.

## Local checks

All checks below passed on the current code tree. The only initial environment issue was a missing `jsdom` dependency; it was installed under the ignored `.cache/test/` directory only, with no dependency manifest or generated package committed.

| Check | Result |
|---|---|
| `python3 scripts/check-generated.py` | PASS — 18 generated public pages current |
| `python3 scripts/check-figures.py` | PASS — 39 figure-ledger records; all 39 marked verified in the ledger |
| `python3 scripts/package-site.py` | PASS — 32 reviewed guide files packaged; legacy `site/` excluded |
| `python3 scripts/check-publication.py --self-test` | PASS — package boundary and rejection tests pass |
| `python3 scripts/privacy-gate.py` | PASS — 239 tracked text files scanned after adding this report; no registered blocked identifier, unrounded household-scale amount in analysis artifacts, or contact/parcel pattern detected |
| `python3 scripts/privacy-gate.py --self-test` | PASS — registered-token detection works |
| `node scripts/privacy-audit.cjs` | PASS — no registered hashed household-input token, property locator, or common identifier found in packaged source/rendered text |
| `python3 scripts/test-model-reference.py` | PASS — 108 decision configurations, 250 stress years, 1,500 phased-investment years, and 20,736 arithmetic comparisons |
| `python3 scripts/test-phased.py` | PASS — 113 phased-investment checks |
| `node scripts/test-guide.cjs` | PASS — 18 rendered pages, 1,053 source-linked table rows, 12,382 checks |
| `node scripts/validate.js` | PASS — 1,610 checks across 19 retained-dashboard pages and 178 registered official sources; this dashboard is not in the Pages package |
| `node scripts/stress-test.js` | PASS — 50-year, ownership, privacy, real-dollar, and shock tests |

These privacy scans are limited regression checks, not proof of anonymity or a history scrub. `check-figures.py` validates the published figure ledger, not any private household fact.

## Source and legal verification boundary

This session did **not** independently fetch non-GitHub official-government websites. The current source links and ledger were inspected locally, but that is not a fresh source re-opening. Prior dated source reviews are available in [`verification/9edb6a52/REPORT.md`](../9edb6a52/REPORT.md), [`verification/9a2a5cce/REPORT.md`](../9a2a5cce/REPORT.md), and [`verification/9ad78d96/REPORT.md`](../9ad78d96/REPORT.md); the public [Sources page](../../guide/sources.html) links the official references for manual review. These older verification records do not turn present law or market rates into a forecast for a future transfer.

PR [#119](https://github.com/wingbangboozle1-lang/Tino2/pull/119) remains open and conflicting. Its report is based on an earlier tree, predates the current synthetic-only privacy change, and includes a statement about the older household-input model that is not true of the current tree. It was not merged or used as current-tree verification in this audit. Any future integration of that report must preserve its historical date and correct the stale privacy-state description first.

## Deployment check

GitHub reports Pages as `built` from `main` at `https://wingbangboozle1-lang.github.io/Tino2/`. On the integrated main commit `ace7057`, `Verify public Pages boundary` run [43922231376](https://github.com/wingbangboozle1-lang/Tino2/actions/runs/43922231376) and `pages build and deployment` run [43922229596](https://github.com/wingbangboozle1-lang/Tino2/actions/runs/43922229596) both completed successfully. The verification workflow includes the rendered-page and browser tests. This session used the GitHub API and did not independently fetch the public HTML for a live content read-back.

## Critical outstanding privacy issue

The current Pages artifact is synthetic-only, but the repository remains public. The checkout is shallow and this session is restricted to its current branch; it did not rewrite `main`, other remote refs, pull-request refs, or Git history. Earlier commits, retained legacy files, branches, pull-request refs, forks, clones, and caches may still expose prior household-derived material. The passing package and privacy gates do not establish that those copies are clean. Keep P-4 on the Flagged page as an urgent repository-administrator action; follow [GitHub's sensitive-data removal procedure](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) and verify repository visibility and all remote copies before considering the incident contained.

## Remaining decision blockers

No personal household recommendation can be supported by this public synthetic model. The public Questions and Flagged pages correctly leave household-specific facts for private verification, including trust authority/title, date-of-death valuation and income-tax basis, estate assets/prior gifts/portability, Proposition 19 eligibility and occupancy, property-specific assessment/tax-rate data, leases/local rules, independent rent/value evidence, insurance quotations, debt, and five-year capital plans. Obtain and review those documents with qualified counsel and tax professionals before choosing a path. See the [Questions register](../../guide/questions.html), [Suggestions register](../../guide/suggestions.html), and [Flagged page](../../guide/review.html).
