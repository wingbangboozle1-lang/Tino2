# Session `d9c69069` — independent verification report

**Date:** 2026-11-11 (all access dates are 2026-11-11 UTC)
**Branch:** `arena/d9c69069-tino2`
**Tree verified:** `main` at `660be98` (PR #20, session `11bffb54`, merged 07:49:54 UTC), merged into this branch.
**Role:** read-only independent auditor. This report is the only substantive file this session adds. No file owned by another session was edited; corrections that belong in someone else's file are logged as requests in `COORDINATION.md`.

**Privacy statement.** No personal name, street address, parcel number, account number or contact detail appears in this report. Properties are "Property A" (Cupertino 95014) and "Property B" (San Francisco 94122). Household figures quoted here are already the $10-rounded values the site publishes; no exact household amount is reproduced.

---

## 1. Automated suite re-run on the merged tree

| Check | Command | Result |
|---|---|---|
| Model, syntax, link and source validation | `node scripts/validate.js` | PASS — 737 checks, 13 pages, 100 official sources |
| 50-year stress paths, estate ownership, real-dollar tests | `node scripts/stress-test.js` | PASS |
| Rendered-page gate (JSDOM): rows, source links, dollar rounding, links | `node qa/tools/gate.cjs` | PASS — 13 rendered pages, 963 table rows (951 with their own official link, 12 calculated rows with a context link), 4,194 dollar amounts (54 official exact figures), 254 internal + 1,376 external links, 0 errors, 0 warnings |
| Publication allowlist packaging | `python3 scripts/package-site.py` | PASS |
| Internal links across the whole repository | `python3 src/check_links.py .` | 58 pages, 871 table rows, 124 distinct external links, 0 errors |
| Privacy scanner | `python3 integration/tools/privacy_scan.py` | 0 errors, 102 warnings — see §4 |

`qa/tools/gate.cjs` needs the optional dev dependency `jsdom`, installed outside the repository
(`npm install --prefix .cache/test jsdom`); `.cache/` is gitignored, so the repository stays dependency-free.

Base case reproduced by the model on the merged tree (2040 inheritance, 2050 endpoint):
sell **$7,683,290** · rent **$6,249,830** · live **$5,135,780**.
