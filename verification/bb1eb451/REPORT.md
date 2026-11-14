# Session bb1eb451 — integration verification (14 Nov 2026)

## Scope and publication boundary

After PR #91 was merged to `main` as `72ed78f`, and PR #92 added follow-up entry-risk clarifications before merging as `5cadc9b`, this branch was synchronized with the latest merged guide rather than resubmitting overlapping navigation, glossary, timeline, adviser brief, first-screen facts, or monthly phased-entry model. The only retained code difference is the mixed-path comparison: rent the inherited example property for a selected period then sell, or live in it for a selected period then sell. Property B remains an already-owned property and is not treated as inherited. Focused PR #94 is open; its latest status snapshot was CLEAN/MERGEABLE, with no GitHub checks yet reported. All figures remain fictional; no household facts were added. The mixed-path table rows link to IRS rule context. Eligibility for any home-sale exclusion is explicitly conditional and must be confirmed privately.

The calculation uses the existing fictional annual property cash flows and net portfolio return proxy, reinvests modeled cash, applies modeled transaction costs and gain tax at sale, and carries proceeds to the common endpoint. It omits housing-service value, moving costs, rental depreciation/recapture, financing and actual taxpayer eligibility; it is not tax or investment advice. No probabilities are assigned.

## Verification

- `python3 scripts/build-guide.py` — PASS; deterministic generation.
- `python3 scripts/check-generated.py` — PASS; 15 generated public pages.
- `python3 scripts/package-site.py` — PASS; 28 reviewed guide files; legacy site excluded.
- `python3 scripts/check-publication.py --self-test` — PASS; extra/missing/altered/symlinked/hard-linked file rejection; packaged boundary matches reviewed sources.
- `python3 scripts/check-figures.py` — PASS; 28/28 ledger records verified.
- `node scripts/test-guide.cjs` — PASS; 15 rendered pages, 875 source-linked table rows, 11,103 checks; mixed-period control and source rows covered.
- `python3 scripts/test-model-reference.py` — PASS; 108 baseline decision configurations, 648 independently reconstructed mixed-path configurations, 250 stress years, 1,500 phased-entry years, 27,000 arithmetic comparisons.
- `node scripts/stress-test.js` — PASS; 50-year path, estate ownership, privacy, real-dollar and shock tests.
- `node scripts/validate.js` — PASS; 1,606 checks across 19 pages and 178 official sources.
- `node scripts/privacy-audit.cjs` — PASS on packaged source and default rendered dollar values. This scan is limited and is not proof of anonymity.
- `git diff --check` — PASS.

Browser rendering, browser accessibility smoke tests, and print-fit remain unverified: Chromium cannot load `libnss3.so` in this environment. No deployment or live-site verification was run in this session. Public repository history and older branches/copies may still contain sensitive legacy material; this code change does not remediate that history exposure.
