# Verification Report — `55c16cea` (12 November 2026)

## Scope Delivered
1. **Official Facts & Data Refresh (`2026-11-12`)**:
   - **HUD FY2027 SAFMRs** (effective 1 Oct 2026, Notice `91 FR 56156`) retrieved from `huduser.gov/datasets/fmr/fmr2027/zip-calc`:
     - ZIP `95014` (Cupertino / Property A): Eff `$3,040`, 1-BR `$3,440`, 2-BR `$4,050`, 3-BR `$5,440`, 4-BR `$5,800` (down 9.2% from FY2026 `$6,390`). Added as `CF-04` (`qa/ledger.json`) and optional sensitivity controls (`4BR_2027`, `3BR_2027`) in `site/decision.html` while keeping `MODEL.BASE` FY2026 continuity intact.
     - ZIP `94122` (SF Outer Sunset / Property B): Eff `$2,370`, 1-BR `$2,770`, 2-BR `$3,410`, 3-BR `$4,460`, 4-BR `$5,020` (up from original FY2026 `$2,730`/`$3,310`). Added as `CF-05` (`qa/ledger.json`) and displayed in `site/san-francisco.html`.
   - **San Francisco Measure H** rate schedule verified from the official Ballot Title & Summary PDF and Controller OEA Economic Impact Report (`SF-09`, `sfMeasureHTerms`, `sfMeasureHOea`): 15-year parcel tax effective July 1, 2027–June 30, 2042 (`$249/yr base + $0.195/sq ft` over 5,000 sq ft for multifamily parcels; `$50,000` cap; CPI-adjusted from July 2028; 50% / `$65/unit` tenant pass-through on pre-June 1, 2027 base rents).
   - **CA SOS Unofficial Tallies & SF DOE Re-checks**: Refreshed `CA-05`, `CA-06`, `CA-07` to the Nov 11, 2026 6:51 p.m. release and re-checked `SF-04`, `SF-05`, `sources.js` entries on `2026-11-12`; preserved `P19-12` (BOE biennial Prop 19 adjustment cadence vs. Santa Clara County wording) from `origin/main`. Total ledger entries: `84` (`78` verified, `6` open/not confirmed).
2. **Pre-Decision Readiness & Discovery Register (`site/questions.html` + `site/data/questions.js`)**:
   - Unified 28 open questions across 6 groups (`Q01`–`Q28`), 14 official settled rules (`A01`–`A14`, including verified FY2027 HUD ZIP `95014` & `94122`, SF Measure H `$249/yr + $0.195/sq ft`, and Prop 19 biennial adjustment `P19-12`), 8 unknowables (`U01`–`U08`), 12 discovery tasks (`D01`–`D12`), 24 carried-forward Group A–D items, priority/group filters, Markdown export, and CSV blank discovery checklist download.
3. **Interactive Site & Decision Suggestions (`site/suggestions.html` + `site/data/suggestions.js`)**:
   - Unified 27 proposals (`S01`–`S27`), 4 bundles (`P1`–`P4`), 3 privacy-path comparisons (with interactive `PRIVACY_PATH` selector), 7 carried questions, 15+10+6 reconciled items (including updated FY2027 HUD `A-05` & Measure H `A-07`), guardrails, and Markdown/JSON exports — zero model changes implemented until an owner approves & verifies inputs.
4. **Cross-Site Quality & Defect Cleanup (`R-D3`, `R-D4`, `R-D5`)**:
   - Expanded `Net operating income (NOI)` on first use across `decision.html`, `properties.html`, `san-francisco.html`, `black-swan.html`, and `sources.html`.
   - Cleaned internal `"session"` / `"audit note"` / `"the brief"` wording across public pages, removed duplicate repository-history entry in `site/review.html`, fixed `Checked 12 Nov 2026` check-date precedence in `site/sources.html`, and updated footer and page verification stamps to `12 Nov 2026`.
   - Updated `scripts/check-publication.py` (`ALLOWED` for 34 public files / 18 pages including `site/questions-gate.html` + `site/data/gate.js`) and `scripts/validate.js`.

## Verification Results
- `python3 scripts/package-site.py`: PASS (`Packaged canonical site only`)
- `python3 scripts/check-publication.py --self-test`: PASS (`34 reviewed public files only`)
- `node scripts/validate.js`: PASS (`18 pages and 177 official sources`)
- `node scripts/stress-test.js`: PASS
- `node scripts/runtime-test.cjs`: PASS (`18 rendered pages`)
- `node qa/tools/gate.cjs`: PASS (`0 errors · 0 warnings`, output written to `qa/gate-report.json`)
- `node verification/60ca3e1f/check.cjs`: PASS (`78 of 78 checks passed`)
- `node verification/62b76b9d/test.cjs`: PASS
- `node verification/55c16cea/check.cjs`: PASS
