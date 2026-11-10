# California Home Inheritance Decision Guide

A privacy-preserving, source-linked static research site for planning a future California trust-property inheritance. It covers the decision to occupy, rent, or sell/reinvest; California Proposition 13 and Proposition 19; federal estate/gift and inherited-basis rules; the trust-administration sequence; and an intentionally blank 2040–2050 projection worksheet.

## Privacy

The public site and repository do **not** contain the personal property facts, financial figures, locations, utility details, rents, or other identifiers supplied in the original planning request. No analytics, database, forms, or visitor inputs are included. Do not add personally identifying or property-specific financial information to this public repository.

## Run locally

This is a static site with no build dependencies. Open `index.html` directly, or serve the repository root with any static HTTP server. Check navigation and source links with:

```sh
python3 scripts/check_site.py
```

The checker verifies local links and requires each data-table row to include a source on the official-source allowlist. It does not assert that outside websites will remain online or that a legal interpretation applies to a particular transfer.

## Publish

The GitHub Actions workflow `.github/workflows/pages.yml` validates the site on pull requests to `main` and publishes the static files to GitHub Pages after a push to `main`. The repository must have GitHub Pages configured to use GitHub Actions.

## Research scope and limitations

Sources are linked inline and are primarily federal, California, county-assessor, court, local government, insurance-regulator, and SEC publications. Research was reviewed in November 2026. Public official materials establish general law and tax mechanics; they do not verify a particular property's market value, tax roll, lease, utility cost, insurance quote, repair budget, trust terms, or future investment result. Those amounts are blank by design, not zero. This is general information, not professional legal, tax, insurance, investment, or appraisal advice.
