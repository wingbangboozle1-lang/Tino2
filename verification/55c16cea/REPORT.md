# Verification Report — `55c16cea` (12 November 2026)

## Scope Delivered
1. **Official Facts & Data Refresh (`2026-11-12`)**:
   - **HUD FY2027 SAFMRs** (effective 1 Oct 2026, Notice `91 FR 56156`) retrieved from `huduser.gov/datasets/fmr/fmr2027/zip-calc`:
     - ZIP `95014` (Cupertino / Property A): Eff `$3,040`, 1-BR `$3,440`, 2-BR `$4,050`, 3-BR `$5,440`, 4-BR `$5,800` (down 9.2% from FY2026 `$6,390`). Added as `CF-04` (`qa/ledger.json`) and optional sensitivity controls (`4BR_2027`, `3BR_2027`) in `site/decision.html` while keeping `MODEL.BASE` FY2026 continuity intact.
     - ZIP `94122` (SF Outer Sunset / Property B): Eff `$2,370`, 1-BR `$2,770`, 2-BR `$3,410`, 3-BR `$4,460`, 4-BR `$5,020` (up from original FY2026 `$2,730`/`$3,310`). Added as `CF-05` (`qa/ledger.json`) and displayed in `site/san-francisco.html`.
   - **San Francisco Measure H** rate schedule verified from the official Ballot Title & Summary PDF and Controller OEA Economic Impact Report (`SF-09`, `sfMeasureHTerms`, `sfMeasureHOea`): 15-year parcel tax effective July 1, 2027–June 30, 2042 (`$249/yr base + $0.195/sq ft` over 5,000 sq ft for multifamily parcels; `$50,000` cap; CPI-adjusted from July 2028; 50% / `$65/unit` tenant pass-through on pre-June 1, 2027 base rents).
   - **CA SOS Unofficial Tallies & SF DOE Re-checks**: Refreshed `CA-05`, `CA-06`, `CA-07` to the Nov 11, 2026 6:51 p.m. release and re-checked `SF-04`, `SF-05`, `sources.js` entries on `2026-11-12`. Total ledger entries: `83` (`77` verified, `6` open/not confirmed).
2. **Pre-Decision Q&A & Discovery Guide (`site/questions.html`)**:
   - 17 structured questions across 6 domains (`Trust & Title`, `Estate & Liquid Assets`, `Property A · Cupertino`, `Property B · San Francisco`, `Heir Profile & Strategy`, `Privacy & Legal Triggers`), separating supplied/verified facts from missing private answers and offering offline discovery steps, priority/domain filters, and blank CSV checklist export.
3. **Interactive Site & Decision Improvement Suggestions (`site/suggestions.html`)**:
   - 8 multi-path proposals (`S1`–`S8`) with `0 of 8 implemented` gating, pros/trade-offs, prerequisites, local RAM-only path selectors, live summary table, and Markdown/JSON export.
4. **Cross-Site Quality & Defect Cleanup (`R-D3`, `R-D4`, `R-D5`)**:
   - Expanded `Net operating income (NOI)` on first use across `decision.html`, `properties.html`, `san-francisco.html`, `black-swan.html`, and `sources.html`.
   - Cleaned internal `"session"` / `"audit note"` / `"the brief"` wording across public pages, removed duplicate repository-history entry in `site/review.html`, fixed `Checked 12 Nov 2026` check-date precedence in `site/sources.html`, and updated footer and page verification stamps to `12 Nov 2026`.
   - Updated `scripts/check-publication.py` (`ALLOWED` for 30 public files / 17 pages) and `scripts/validate.js`.

## Verification Results
- `python3 scripts/package-site.py`: PASS (`Packaged canonical site only`)
- `python3 scripts/check-publication.py --self-test`: PASS (`30 reviewed public files only`)
- `node scripts/validate.js`: PASS (`1187 checks across 17 pages and 175 official sources`)
- `node scripts/stress-test.js`: PASS
- `node scripts/runtime-test.cjs`: PASS (`17 rendered pages; 1378 rendered rows source-linked`)
- `node qa/tools/gate.cjs`: PASS (`0 errors · 0 warnings`, output written to `qa/gate-report.json`)
- `node verification/60ca3e1f/check.cjs`: PASS (`78 of 78 checks passed`)
- `node verification/62b76b9d/test.cjs`: PASS
- `node verification/55c16cea/check.cjs`: PASS
