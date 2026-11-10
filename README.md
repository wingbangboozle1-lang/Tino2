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

Open `http://localhost:8080`. There is no build step, package dependency, analytics script, backend, or external font request. JavaScript calculations run locally in the browser. GitHub Pages can serve the repository root directly; `.nojekyll` disables Jekyll processing.

## Structure

- `index.html` — executive summary and base-case recommendation
- `site/properties.html` — annual values, assessments, taxes, operating costs, rental economics, and household histories
- `site/decision.html` — interactive live/rent/sell model, worked formulas, sensitivities, and CSV export
- `site/inheritance.html` — trust, assessor, tax-basis, filing, and distribution checklist
- `site/estate-tax.html` — federal thresholds, real-estate-only headroom, California status, and missing estate inputs
- `site/san-francisco.html` — Property B rental economics and regulatory context
- `site/sources.html` — official source register, assumptions, methodology, and legal watchlist
- `site/review.html` — unresolved items and verification routes
- `site/data/model.js` — deterministic calculations; full precision retained until display
- `site/data/sources.js` — official URLs and reviewed notes
- `assets/` — shared layout, styling, and navigation
- `scripts/validate.js` — model, syntax, internal-link, and source checks

## Model conventions

Displayed projection dollars round to the nearest $10. Historical household bills retain their supplied exact amounts. The model uses a date-of-death fair-market-value basis proxy, selling costs, after-tax cash flows, and same-endpoint terminal values. It deliberately does **not** impute depreciation, passive-loss benefits, land/building allocations, recapture, or taxpayer-specific brackets. Living in Property A excludes the value of housing service and any release of Property B’s owner unit, so its terminal dollar result is not a complete lifestyle comparison.

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
