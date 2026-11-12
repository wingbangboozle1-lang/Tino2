# Inheritance planning dashboard

A privacy-safe, dependency-free GitHub Pages site for comparing three strategies for a future Cupertino inheritance:

1. occupy Property A as a primary residence;
2. rent Property A and sell later; or
3. sell at inheritance and reinvest the net proceeds.

Property B in San Francisco is modeled separately as continuing rental context. The site includes annual property and estate projections through 2050, trust-administration steps, current-law sources, a legal-change watchlist, and a **Flagged for Review** register.

## Privacy

Property names are placeholders. Do **not** add personal names, street addresses, parcel numbers, account identifiers, trust documents, tax returns, leases, death certificates, or other private records to this repository. Household inputs are labeled as unverified planning inputs; official sources support rules and benchmarks, not those private amounts.

## Run locally

```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

Open `http://localhost:8080`. There is no build step, package dependency, analytics script, backend, or external font request. JavaScript calculations run locally in the browser. GitHub Pages can serve the repository root directly; `_config.yml` excludes legacy research and historical dashboards from the GitHub Pages build. Do not add `.nojekyll`: that would bypass these privacy exclusions.

## Structure

- `site/questions.html` — **Decision readiness**: 22 open questions, 12 points already settled by an official source, 8 that no document can settle, a 12-item discovery plan, and a browser-local answer tracker (data in `site/data/questions.js`)
- `site/suggestions.html` — **Suggestions to review**: 27 proposals with the uncertainty each removes, effort, cost and limits, four ready-made paths the owner can compare and choose before anything is implemented, and the two earlier sessions' shortlists reconciled in their own IDs (data in `site/data/suggestions.js`)
- `site/stress.html` — automatic 50-year variable-growth, inflation, crash and disaster paths
- `index.html` — executive summary and base-case recommendation
- `site/properties.html` — annual values, assessments, taxes, operating costs, rental economics, and household histories
- `site/decision.html` — interactive live/rent/sell model, worked formulas, sensitivities, and CSV export
- `site/options.html` — completeness check: hold-then-sell and empty-house cases, depreciation in the rental case, the pre-2021 reassessment rule as a test, estate tax by amount of money, rules by kind of money, and filing steps missing from the checklist (engine in `site/data/options.js`, independent calculation in `verification/0d6ec51e/`)
- `site/scenarios.html` — black-swan and real-conditions stress cases: recorded inflation, mortgage, home-price, insurance and earthquake anchors replayed as seven path-based scenarios, with break-even thresholds and cost/catastrophe sensitivities
- `site/inheritance.html` — trust, assessor, tax-basis, filing, and distribution checklist
- `site/estate-tax.html` — federal thresholds, real-estate-only headroom, California status, and missing estate inputs
- `site/san-francisco.html` — Property B rental economics and regulatory context
- `site/suggestions.html` — the suggestions register: improvements to the analysis and to the dashboard, the questions to answer before deciding, a suggested sequence, and a local-only record of which items were approved, deferred or declined
- `site/sources.html` — official source register, assumptions, methodology, and legal watchlist
- `site/review.html` — unresolved items and verification routes
- `site/data/model.js` — deterministic calculations; full precision retained until display
- `site/data/scenarios.js` — stress-case engine; reproduces `MODEL.decision()` exactly at base assumptions and adds path-based shocks
- `site/data/sources.js` — official URLs and reviewed notes
- `assets/` — shared layout, styling, and navigation
- `scripts/validate.js` — model, syntax, internal-link, and source checks

## Review before change

Two pages exist so that the dashboard can be reviewed rather than rewritten:

- **Decision readiness** separates the questions that are settled by an official source from the ones that are open and discoverable, and from the ones that are unknowable until the event. Every open row names the document, office or lookup that settles it. Marks are stored in the reader's browser only.
- **Suggestions** is the change backlog. Each proposal states the uncertainty it removes, the readiness questions it would close, the household time it costs, and the limits it does not fix. Choosing a path or an item writes to the browser only; nothing on the site, in the model or in the recommendation changes until the choice is recorded in `COORDINATION.md` and implemented in a later session under the same verification rules.

## Model conventions

Displayed projection dollars round to the nearest $10. Household tax and assessment history is published rounded to the nearest $10 on `site/properties.html`; exact bills are not stored in the current files. Rounded inputs remain unverified scenarios; rounding is not guaranteed anonymization. The model uses a date-of-death fair-market-value basis proxy, selling costs, after-tax cash flows, and same-endpoint terminal values. It deliberately does **not** impute depreciation, passive-loss benefits, land/building allocations, recapture, or taxpayer-specific brackets. Living in Property A excludes the value of housing service and any release of Property B’s owner unit, so its terminal dollar result is not a complete lifestyle comparison.

Current law is separated from assumptions and proposed legislation. Future Proposition 19 and federal estate exclusion amounts are scenarios, not official forecasts. Unknown values remain blank.

## Validate

Requires Node.js only:

```bash
node scripts/validate.js
```

The validator checks key arithmetic, non-refund treatment of rental losses, rounding, HTML script syntax, local asset/page links, source references, and HTTPS source URLs. External sources still require periodic manual review because laws, rates, forms, and URLs change.

## Deployment

Enable GitHub Pages for the `main` branch, `/ (root)`. After a merge to `main`, confirm the Pages build and public URL before recording completion in `COORDINATION.md`.

## Disclaimer

This is educational scenario modeling, not an appraisal, legal opinion, tax return, insurance quote, rent opinion, or investment recommendation. Revalidate official sources and obtain professional advice before acting.

---

## Previously integrated research and dashboards

The other sessions' pages and models remain available. The prior integrated landing page is preserved at [`research-portal.html`](research-portal.html). The new dashboard links to it from the Sources page.

| Site section | Path | Built by |
|---|---|---|
| Prior landing page and summary pages | `research-portal.html`, `cupertino.html`, `san-francisco.html`, `inheritance.html`, `taxes.html`, `decision.html`, `flagged.html`, `sources.html`, `css/`, `docs/` | session arena-7c9c2cc4 |
| Second set of pages | `pages/`, `assets/` | session 64131d11 |
| Scenario dashboard (year-by-year tables, break-even model, estate-tax headroom, flagged list) | `dashboard/` (generated), `src/` (model and build script) | session 6ed42dca |

Rebuild and check the scenario dashboard:

```
python3 src/build.py          # writes dashboard/
python3 src/check_links.py    # dashboard only: links, source link on every row, rounding
python3 src/check_links.py .  # internal links across the whole site
```

Coordination between the parallel sessions is recorded in `COORDINATION.md`.

## 11 November 2026 audit

Property B is already owned by the heir and excluded from the decedent’s estate model. Property A-only 2026 illustrative headroom is $11,900,000 before other estate items, gifts and deductions—not a verified amount of tax-free inheritance. Actual estate tax remains blank. Historic bill-to-assessment ratios are no longer extrapolated after reassessment: A uses a hypothetical 1.2% levy; B uses a carried-forward city ad valorem rate excluding unknown direct charges.

`node scripts/stress-test.js` tests all five automatic 50-year paths. `python3 scripts/package-site.py` produces an allowlisted local artifact and rejects known exact household fingerprints. Pages retains its existing main/root configuration; `_config.yml` excludes old HTML, research, coordination logs and model source trees. GitHub integration permits repository/PR work but returns HTTP 403 for changing Pages configuration, so no settings change is required.

Current-session source checks: IRS estate threshold and filing FAQ, BOE Proposition 19 overview, California Controller estate tax, BLS December 2022 CPI release, FDIC deposit insurance and CDI residential guidance. Other source-register entries are carried forward, explicitly flagged for revalidation; no blanket fresh verification is claimed.

Prior public Git history and third-party caches may retain earlier exact household figures. A publication change does not erase those. See Flagged for Review. Legacy files are retained in Git to preserve previous sessions’ work, but are not part of the public Pages artifact.

Rendered-page tests (optional development-only dependency):

```sh
npm install --prefix .cache/test jsdom --no-audit --no-fund
python3 scripts/package-site.py
node scripts/runtime-test.cjs
```

This checks runtime errors, every rendered table row for an official framework link, and local links in the allowlisted output. It does not establish truth of a projection or verify every external document.

## Recorded-data stress tests (added 2026-11-11, session 70f163d0)

`site/black-swan.html` ("Recorded data") replays twelve scenarios from official annual series (BLS CPI-U, FHFA house-price indexes, Treasury yields, Freddie Mac mortgage rates, OECD share prices; 1970–2025) and runs 2,000 seeded random 50-year histories through the same cash-flow logic as the Decision lab (`site/data/history-engine.js`; with constant rates it reproduces `MODEL.decision()` exactly, checked in `scripts/validate.js`). Inputs are stored in `research/data/fred_annual_2026-11-11.csv`; regenerate `site/data/history.js` with `python3 scripts/build-history.py`. Notes: `research/black-swan.md`; verification log: `research/verification-2026-11-11.md`. The Prop 19 cap is modeled as compounding with home-price growth in two-year steps (BOE indexes it to the FHFA California HPI).

