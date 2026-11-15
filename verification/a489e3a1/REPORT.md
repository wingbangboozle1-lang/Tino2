# Verification report — session `a489e3a1` (branch `arena/a489e3a1-tino2`)

**Claimed:** 2026-11-15. **State read at claim.** `origin/main` = `e54096e` (merge of PR #114, session `61ab44f9`). Branch `arena/a489e3a1-tino2` is level with `main`. `gh pr list --state open` returned no open pull requests. The published artifact is the privacy-reviewed synthetic guide (`index.html` + `guide/**` + `assets/safe.*`), served by GitHub Pages (legacy builder, source `main` / `/`).

**Scope claimed.** Review the repository, verify load-bearing figures from official sources, confirm the published artifact is privacy-safe, confirm the GitHub Pages live site, flag irregularities, and close the session with a PR + merge. Non-overlapping file scope: `COORDINATION.md` (this session's block only), `verification/a489e3a1/**` (new). No shared site or model files changed — the feature set requested in the brief is already implemented and published by prior sessions; this session re-verifies and records.

## Verification performed

All checks run locally on the clean tree at `e54096e`:

| Check | Result | Detail |
|---|---|---|
| `python3 scripts/build-guide.py` | PASS | Deterministic generator runs cleanly |
| `python3 scripts/check-generated.py` | PASS | 18 generated public pages up to date |
| `python3 scripts/package-site.py` | PASS | 32 reviewed guide files packaged; legacy `site/` excluded |
| `python3 scripts/check-publication.py --self-test` | PASS | Publication boundary rejects missing/extra/altered/symlinked/hard-linked files |
| `python3 scripts/privacy-gate.py --self-test` | PASS | Whole-repository gate self-test passes |
| `python3 scripts/test-model-reference.py` | PASS | 108 decision configurations, 250 stress years, 1,500 phased-investment years; 20,736 unrounded arithmetic comparisons |
| `python3 scripts/test-phased.py` | PASS | Phased model independently reconstructed; 113 checks |
| `node scripts/privacy-audit.cjs` | PASS | No raw pre-rounding household token, property ZIP code or common identifier in packaged source or rendered text |
| `node scripts/test-guide.cjs` | PASS | 18 rendered pages, 1,114 source-linked table rows, 12,844 checks; controls and model invariants verified |

`test-browser.cjs` cannot run in this sandbox (missing `libnss3` for the bundled Chromium); it runs in CI on the pull request.

## Official sources verified (load-bearing figures)

| Figure | Value used | Official source | Status |
|---|---|---|---|
| Federal estate basic exclusion, 2026 | $15,000,000 | IRS, "One Big Beautiful Bill Act — Individuals and workers" (Public Law 119-21 §70106 amends IRC §2010(c)(3)) | MATCH |
| Federal estate basic exclusion, 2027 | $15,480,000 | IRS IR-2026-133 | MATCH |
| Top federal estate/gift rate | 40% | 26 U.S.C. §2001(c); IRS estate-tax pages | MATCH |
| California 1% tax above $1,000,000 | R&TC §17043 | California Legislative Information (leginfo.legislature.ca.gov) | MATCH |
| Proposition 19 allowance | $1,044,586 | CA BOE Letter to Assessors 2025/009; transfers 16 Feb 2025–15 Feb 2027 | MATCH |
| Proposition 19 prior windows | $1,000,000 / $1,022,600 | CA BOE LTA 2025/009 | MATCH |
| U.S. Treasury 3-month par yield | 4.32% | U.S. Treasury daily par yield curve, 13 Nov 2026 | MATCH |
| U.S. Treasury 2-year par yield | 4.88% | U.S. Treasury daily par yield curve, 13 Nov 2026 | MATCH |
| Proposition 13 assessment cap | 2% | Cal. Const. art. XIII A; BOE / county assessor materials | MATCH |

Source links: https://www.irs.gov/newsroom/one-big-beautiful-bill-provisions-individuals-and-workers · https://www.boe.ca.gov/prop19/ · https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611 · https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17043.

## Privacy review of the published artifact

- `git grep` over `index.html guide/ assets/` returns **no** ZIP code ([ZIP-A] / [ZIP-B]), no street address, no parcel number, no name.
- `node scripts/privacy-audit.cjs` confirms no raw pre-rounding household token, property ZIP code, or common identifier.
- Parties appear only as placeholders: `Property A` (Cupertino) and `Property B` (San Francisco west side).
- Every published household dollar figure is rounded to the nearest $10; exact government-published amounts (estate exclusion, Prop 19 allowance) are shown exactly with the source linked.
- `scripts/privacy-gate.py` enforces identifiers, the $10 rule, and identifier patterns on the whole tracked tree.

## Irregularities flagged (non-blocking; published on the site's Flagged page)

| # | Irregularity | Severity | Disposition |
|---|---|---|---|
| F3 | Public repository and history exposure: older commits, branches, pull requests and legacy files still hold the household's exact pre-rounding figures and ZIP codes. A Pages exclusion does not remove them from GitHub, forks, clones or caches. | High | Standing owner decision (L-D2). History scrub is an administrator action (force-rewrite `main` + 70+ remote branches + GitHub Support); a six-step runbook is on the Flagged page. Not performed from this session. |
| L-D2 | Pre-rounding Git history scrub requested by the brief. | High (owner decision) | Cannot be executed from a session branch under the "push only to the session branch" rule; destructive to other sessions' records. Runbook recorded; owner decision. |
| Repository visibility | Repository is public (`"private":false`). | High (owner decision) | Owner decision whether to make it private or move the retained analysis tree out. Not performed here. |
| F4 | Official amounts that are not multiples of ten (e.g. Prop 19 allowance $1,044,586) are allowlisted and published exactly; rounding disclosed. | Low | Allowlisted in `scripts/test-guide.cjs`; recorded. |

## Decision readiness

Per the published Questions register, the verdict remains **"Answer: not yet"** — a live / rent / sell decision cannot reasonably be made today because the Priority 1 facts (trust terms, title, basis step-up, Proposition 19 eligibility, estate size, date-of-death value, SF leases/unit status, achievable rent floor) are unverified. The guide states this plainly on the first screen and lists the discovery route for each.

## Live site

- Published URL: https://wingbangboozle1-lang.github.io/Tino2/
- Live read-back of the homepage confirms: first-screen "what would change the answer" table, executive summary with conditional recommendation, reinvestment-risk table beside the headline, phased Treasury-parking language (24–36 months), readiness scorecard, grouped navigation (Decide / Property & rules / Evidence & terms / Act), Attorney & CPA sheet, Suggestions, Flagged, Timeline, Glossary, Questions.
- No identifier or ZIP code appears on the live page.

**Session decision.** No code change to shared site/model files was required — the brief's feature set is already implemented, published, and green. This session's commit adds the coordination claim block and this verification record only.
