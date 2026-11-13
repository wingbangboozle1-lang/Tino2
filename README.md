# Inheritance decision guide

A public, source-linked planning dashboard for comparing an anticipated Cupertino trust inheritance (**Property A**) with an already-owned San Francisco three-unit property (**Property B**). The planning premise for B is two rented units plus a third unit available for the owner without displacing those rents. The premise has not been independently verified.

**Privacy model.** No name, street address, parcel number, account number or e-mail address appears on any published page. The two properties are referred to only as Property A and Property B, and every dollar figure in the decision analysis is rounded to the nearest $10 — except amounts published by a government body, which are shown exactly and recorded in the verification ledger. Rounding is not anonymisation: a rounded financial history attached to a known location can still identify a household, and this repository is public. That residual risk is disclosed on the **Flagged for Review** page rather than hidden.

**What is an assumption.** Market values, growth rates, rents, insurance, water, electricity, maintenance, sale costs and tax rates applied to a specific parcel are assumptions or supplied household inputs, not official figures. Every table row carries a link to the official rule or benchmark it relies on; the link explains the rule, it does not verify a household number.

## Important privacy incident

This GitHub repository is public. Older commits, branches, pull requests, existing legacy files, caches, forks or clones may contain distinctive household-derived financial information. A Pages exclusion, rounding, `robots.txt`, or deletion in a later commit **does not remove** that exposure. Coordinate cleanup with collaborators and [GitHub's sensitive-data-removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository). Copies outside the repository may remain. Do not commit personal information, case-specific assumptions, private links or records.

**Publication decision (13 Nov 2026).** An earlier session replaced the dashboard with a purely synthetic public guide, because rounded figures can still identify a household. The owner's brief asks for the opposite: anonymise personal information with placeholders and use the real costs and numbers rounded to the nearest $10. The published artifact now follows that instruction and shows the real analysis. This **adds no new exposure** — the same files have already been committed to this public repository, so excluding them from Pages never removed them from public reach. The earlier synthetic `guide/` is retained in the repository for audit but is no longer published.

The only effective remedies for the underlying exposure are repository-level: move to a fresh private repository, make this repository private, or coordinate a purge of Git history, pull-request refs and caches with GitHub Support. Exclusions, rounding, `robots.txt` and `noindex` do none of those things. Copies outside the repository may remain. Do not commit personal information, case-specific assumptions, private links or records.

## Build and preview the public artifact

Python 3 and Node.js are required for the checks. Never serve the repository root: it contains legacy material.

```sh
python3 scripts/package-site.py
python3 scripts/check-publication.py --self-test
python3 -m http.server 8080 --bind 0.0.0.0 --directory _public
```

The final command serves only the reviewed public artifact. When using a shared machine or network, protect access to the server and the rest of the workspace. No backend, analytics, remote font or network data transfer is required by the dashboard. Suggestion choices, if used, store only a status in local browser storage; they never implement changes or collect household answers. Without JavaScript, the rule tables and navigation remain available, but interactive projection tables and choices do not render.

## Verify

```sh
npm install --prefix .cache/test --no-audit --no-fund --ignore-scripts jsdom@26.1.0
node scripts/validate.js
node scripts/stress-test.js
python3 scripts/package-site.py
python3 scripts/check-publication.py --self-test
node scripts/runtime-test.cjs
node qa/tools/gate.cjs
python3 integration/tools/privacy_scan.py _public
```

`validate.js` checks the model's arithmetic, the official source register and every page's structure. `stress-test.js` exercises the 50-year paths, estate ownership and shock cases. The boundary check rejects missing, extra, symlinked, hard-linked or altered artifact files. `runtime-test.cjs` renders every page and requires each table row to carry an `https://` source and each internal link to resolve. `gate.cjs` re-checks, on the rendered package, that every dollar figure of $1,000 or more is a multiple of $10 unless it is an officially published amount, that every row has a source, and that no identifier pattern appears. The privacy scan detects common identifiers and unrounded household values, but **cannot prove anonymity**. Official law and local data must be rechecked before any real decision; source links do not establish case facts.

For a full Chromium smoke test when browser dependencies are available, install `playwright-core@1.49.1`, `@sparticuz/chromium@131.0.1` and `axe-core@4.10.3` under `.cache/test` and run `node scripts/test-browser.cjs`. Chromium may require the system NSS and NSPR shared libraries. The smoke test serves only `_public` on an ephemeral local port.

## Structure and publication

- `index.html` — executive summary: the recommendation, the three paths, projected values and taxes, holding costs, estate-tax thresholds and the six blocking questions.
- `site/*.html` — the dashboard: best plan, decision lab, black swans, shock replays, 50-year paths, properties, operating costs, SF property, estate tax, trust steps, questions, decision gate, suggestions, flagged for review, sources, verified facts and other options.
- `site/data/*.js` — the deterministic model, the recorded-history and Monte Carlo engines, the question register, the official source register and the verification ledger.
- `assets/app.js`, `assets/styles.css` — shared navigation, table rendering and styling loaded by every published page.
- `scripts/public_manifest.py`, `scripts/package-site.py`, `scripts/check-publication.py` — explicit publication allowlist, packager and fail-closed boundary audit.
- `scripts/validate.js`, `scripts/stress-test.js`, `scripts/runtime-test.cjs`, `qa/tools/gate.cjs`, `integration/tools/privacy_scan.py` — model arithmetic, stress paths, rendered-page and row-source checks, publication gate and privacy scan.
- `guide/`, `assets/safe.*`, `scripts/build-guide.py`, `scripts/test-guide.cjs`, `scripts/test-model-reference.py`, `scripts/privacy-audit.cjs` — the earlier synthetic guide, retained unpublished for audit.
- `docs/`, `research/`, `qa/`, `verification/` — working papers and per-session verification reports, not part of the published artifact.

The existing legacy Pages configuration serves `main`/root through Jekyll; `_config.yml` excludes known legacy paths and CI checks the Jekyll output as well as the explicit package. **Do not add `.nojekyll` at the repository root**, which bypasses Jekyll exclusions. Direct commits or bypassing checks can still make a denylist unsafe, and legacy Pages deployment is not gated by the separate CI check.

For a fail-closed publication boundary, a repository administrator can set **Settings → Pages → Build and deployment → Source → GitHub Actions**, then run **Verify public Pages boundary** on `main` from the Actions tab. The workflow deploys the checked `_public` allowlist only after all checks succeed; verify the deployment and the live site. This change still does not privatize the repository or its history.

This guide is educational, not legal, tax, insurance or investment advice.
