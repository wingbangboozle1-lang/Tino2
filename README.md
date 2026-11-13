# Inheritance decision guide

A public, source-linked planning guide for comparing an anticipated Cupertino trust inheritance (Property A) with an already-owned San Francisco property (Property B). The planning premise for B is two rented units plus a third unit available for the owner without displacing those rents. The premise has not been independently verified.

**The public calculator is a teaching example, not a personalized analysis.** All property amounts, projected results and rates other than identified official rule values are fictional assumptions. Actual household data and documents must not be committed or placed in the public artifact. Official links explain laws and context; they do not verify private records or hypothetical projections.

## Important privacy incident

This GitHub repository is public. Older commits, branches, pull requests, existing legacy files, caches, forks or clones may contain distinctive household-derived financial information. A Pages exclusion, rounding, `robots.txt`, or deletion in a later commit **does not remove** that exposure. Coordinate cleanup with collaborators and [GitHub's sensitive-data-removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository). Copies outside the repository may remain. Do not commit personal information, case-specific assumptions, private links or records.

The new Pages artifact is deliberately limited to the public guide; the legacy `site/`, research, reports and other earlier material are preserved for coordination but are **not** part of that artifact. Their existence in this public repository is still a risk. An offline copy of the earlier analysis, if retained in a private workspace, is sensitive and has not been independently verified as a recommendation.

### Two artifacts, one publication decision (13 Nov 2026)

The repository holds **two** complete artifacts, and only one of them is published:

| Artifact | What it is | Published? |
|---|---|---|
| `index.html` + `guide/**` + `assets/safe.*` | The **synthetic** guide. Every figure in its calculators is an invented example; the household's own numbers appear nowhere on it. | **Yes** — this is what Pages serves |
| `index.html` (dashboard variant) + `site/**` + `assets/app.js`, `assets/styles.css` | The **real** decision dashboard built by session `662025f8` on the household's own inputs: the Cupertino ZIP, the stated value, the stated rent, the stated insurance and utility costs, projected year by year. It is complete, verified (`validate.js`, `stress-test.js`, `qa/gate-report.json`) and reviewed in `verification/662025f8/REPORT.md`. | **No** — retained in the repository, not served |

**The decision, and why.** The owner's brief asks for two things that pull in opposite directions: publish the real costs and numbers, rounded to the nearest $10, so the analysis is useful — and keep personal information out of the website entirely, because privacy is the stated highest priority and research-supplied personal information is internal-use only. Session `662025f8` resolved that in favour of publishing the real dashboard, on the grounds that `site/**` has been committed to this public repository for days, so excluding it from Pages never removed it from public reach. The final integration session (`b2418dfa`) took the opposite decision, for three reasons:

1. **The instruction is unconditional.** Research-supplied personal information must never appear on the final website product. The published dashboard would place the household's ZIP code, its exact stated value, its exact monthly rent and its unit count on the public web. Rounded to $10 or not, that combination re-identifies one household — which is the point of the privacy rule, not a detail it tolerates.
2. **The exposure argument cuts both ways.** "Already in the repository" is true of the files, but publication is what makes them readable to anyone without a GitHub account, indexed and cached. Excluding a file from Pages is not access control, but publishing it is still a disclosure; when one option can be undone and the other cannot, the reversible one should be chosen.
3. **The asymmetry of harm.** Reverting the publication pointer costs the owner a dashboard they can restore; publishing household financials cannot be undone once caches and clones exist.

**Nothing was deleted.** The dashboard, its landing page, its data files, its verification report and its ledger are all still in the repository, still verified on every push by CI, and still one command away from being republished:

```sh
# Republish the real dashboard instead of the synthetic guide
git checkout 22b7e69 -- _config.yml scripts/public_manifest.py scripts/package-site.py \
    scripts/check-publication.py scripts/test-browser.cjs .github/workflows/pages.yml index.html
```

That is an **owner decision**, not a technical one: it re-publishes household-derived figures to a public web page. The guide stays the default until the owner says otherwise. Two notes for whoever does it: the dashboard state does **not** run `scripts/check-generated.py` in CI (its workflow verifies the dashboard with `validate.js` and `stress-test.js` instead), and `python3 scripts/build-guide.py` would overwrite the dashboard's root `index.html` with the guide's landing page, so do not run it in that state.


## Build and preview the public artifact

Python 3 and Node.js are required for the checks. Never serve the repository root: it contains legacy material.

```sh
python3 scripts/build-guide.py
python3 scripts/package-site.py
python3 scripts/check-publication.py --self-test
python3 -m http.server 8080 --bind 0.0.0.0 --directory _public
```

The final command serves only the fictional public artifact. When using a shared machine or network, protect access to the server and the rest of the workspace. No backend, analytics, remote font or network data transfer is required by the guide. Suggestion choices, if used, store only a status in local browser storage; they never implement changes or collect household answers. Without JavaScript, the rule tables and navigation remain available, but interactive projection tables and choices do not render.

## Verify

```sh
npm install --prefix .cache/test --no-audit --no-fund --ignore-scripts jsdom@26.1.0
python3 scripts/package-site.py
python3 scripts/check-publication.py --self-test
node scripts/privacy-audit.cjs
node scripts/test-guide.cjs
python3 scripts/test-model-reference.py
```

The boundary check rejects missing, extra, linked or altered artifact files. The runtime checks inspect navigation, internal links, $10 rounding, row-level sources and controls. The independent Python reconstruction compares the model's arithmetic across settings and all 250 synthetic stress years. The privacy scan detects certain legacy input/history collisions and common identifiers, but **cannot prove anonymity**. Official law and local data must be rechecked before any real decision; source links do not establish case facts.

For a full Chromium smoke test when browser dependencies are available, install `playwright-core@1.49.1`, `@sparticuz/chromium@131.0.1` and `axe-core@4.10.3` under `.cache/test` and run `node scripts/test-browser.cjs`. Chromium may require the system NSS and NSPR shared libraries. The smoke test serves only `_public` on an ephemeral local port.

## Structure and publication

- `index.html`, `guide/*.html` — public overview, comparison, 50-year stresses, properties, tax, trust steps, questions, suggestions, review flags and sources.
- `guide/data/*.js`, `assets/safe.*` — fictional scenario engines, presentation and local-only suggestion choices.
- `scripts/build-guide.py` — deterministic page generator; regenerate and commit the resulting HTML when edited.
- `scripts/public_manifest.py`, `scripts/package-site.py` — explicit publication allowlist and packager.
- `scripts/check-publication.py`, `scripts/test-guide.cjs`, `scripts/test-model-reference.py`, `scripts/privacy-audit.cjs` — boundary, rendered-page, independent arithmetic and privacy-regression checks.
- `site/`, `docs/`, `research/`, `qa/`, `verification/` — retained legacy work, not safe to publish as Pages output and not necessarily independently verified.

The existing legacy Pages configuration serves `main`/root through Jekyll; `_config.yml` excludes known legacy paths and CI checks the Jekyll output as well as the explicit package. **Do not add `.nojekyll` at the repository root**, which bypasses Jekyll exclusions. Direct commits or bypassing checks can still make a denylist unsafe, and legacy Pages deployment is not gated by the separate CI check.

For a fail-closed publication boundary, a repository administrator can set **Settings → Pages → Build and deployment → Source → GitHub Actions**, then run **Verify public Pages boundary** on `main` from the Actions tab. The workflow deploys the checked `_public` allowlist only after all checks succeed; verify the deployment and the live site. This change still does not privatize the repository or its history.

This guide is educational, not legal, tax, insurance or investment advice.
