# Inheritance decision guide

A public, source-linked educational guide for comparing possible inheritance and property-management paths using fictional examples only. No household-specific facts or outputs are published.

**Privacy-first publication policy (reaffirmed 16 Nov 2026).** The public guide contains no household-specific facts, values, costs, occupancy details, addresses, identifiers, or derived household results. Public calculators use invented examples only; these are not estimates, recommendations or advice. Keep any real property, estate, tax and financial records offline in an access-controlled private workspace. Rounding is not anonymization and must not be treated as permission to publish private figures. This is not legal or tax advice.

## Important privacy incident

This GitHub repository is public. Older commits, branches, pull requests, existing legacy files, caches, forks or clones may contain distinctive household-derived financial information. A Pages exclusion, rounding, `robots.txt`, or deletion in a later commit **does not remove** that exposure. Coordinate cleanup with collaborators and [GitHub's sensitive-data-removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository). Copies outside the repository may remain. Do not commit personal information, case-specific assumptions, private links or records.

The Pages artifact is limited to the public guide; the legacy `site/`, research, reports and other earlier material are preserved for coordination but are **not** part of that artifact. Their existence in this public repository is still a risk. An offline copy of the earlier analysis, if retained in a private workspace, is sensitive and has not been independently verified as a recommendation.

### Privacy boundary and repository history

The current public guide uses invented inputs, not household inputs. The analysis code no longer contains a household-data publication switch, and the public model uses fictional teaching values. The packaged site is checked for known private-input tokens, identifiers and unexpected files. These controls protect only the current checked artifact; they do not sanitize Git history or external copies.

Older commits, branches, pull requests, retained legacy files, caches, forks and clones may still expose sensitive material. This checkout is shallow and the current branch is not authorized to rewrite `main` or other branches. History cleanup therefore remains an administrator task: inventory refs and pull requests, coordinate with collaborators, use GitHub's documented sensitive-data-removal procedure, and request cache/fork remediation. Do not force-push or mirror-rewrite from this task branch. A history rewrite cannot erase copies already cloned.

Legacy repository folders are not part of the GitHub Pages package. Their presence in a public Git repository remains a separate exposure risk; a Pages exclusion is not access control. Do not add private property facts to the repository or this site.

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

The boundary check rejects missing, extra, linked or altered artifact files. The runtime checks inspect navigation, internal links, source-linked rows and controls. The independent Python reconstruction compares the fictional model's arithmetic across settings and stress years. The privacy scan checks known private-input tokens and common identifiers in the packaged artifact, but **cannot prove anonymity or clean repository history**. Official law and local data must be rechecked before any real decision; source links do not establish case facts.

For a full Chromium smoke test when browser dependencies are available, install `playwright-core@1.49.1`, `@sparticuz/chromium@131.0.1` and `axe-core@4.10.3` under `.cache/test` and run `node scripts/test-browser.cjs`. Chromium may require the system NSS and NSPR shared libraries. The smoke test serves only `_public` on an ephemeral local port.

## Structure and publication

- `index.html`, `guide/*.html` — public overview, comparison, 50-year stresses, properties, tax, trust steps, questions, suggestions, review flags and sources.
- `guide/data/*.js`, `assets/safe.*` — fictional scenario engines, presentation and local-only suggestion choices.
- `scripts/build-guide.py` — deterministic page generator; regenerate and commit the resulting HTML when edited.
- `scripts/public_manifest.py`, `scripts/package-site.py` — explicit publication allowlist and packager.
- `scripts/check-publication.py`, `scripts/test-guide.cjs`, `scripts/test-model-reference.py`, `scripts/privacy-audit.cjs` — boundary, rendered-page, independent arithmetic and privacy-regression checks.
- `site/`, `docs/`, `research/`, `qa/`, `verification/` — legacy material excluded from Pages and still subject to the repository-history privacy incident; do not treat it as safe or current.

The existing legacy Pages configuration serves `main`/root through Jekyll; `_config.yml` excludes known legacy paths and CI checks the Jekyll output as well as the explicit package. **Do not add `.nojekyll` at the repository root**, which bypasses Jekyll exclusions. Direct commits or bypassing checks can still make a denylist unsafe, and legacy Pages deployment is not gated by the separate CI check.

For a fail-closed publication boundary, a repository administrator can set **Settings → Pages → Build and deployment → Source → GitHub Actions**, then run **Verify public Pages boundary** on `main` from the Actions tab. The workflow deploys the checked `_public` allowlist only after all checks succeed; verify the deployment and the live site. This change still does not privatize the repository or its history.

This guide is educational, not legal, tax, insurance or investment advice.
