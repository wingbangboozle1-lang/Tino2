# Inheritance decision guide

A source-linked educational guide for comparing inheritance, property-operation and investing paths. The public site uses synthetic examples only. It does not contain a personalized recommendation or load household records.

## Privacy boundary

Household property values, tax bills, rents, leases, utilities, insurance details and identifiers are private and must not be added to the public site, repository, issues, pull requests or commit messages. Rounding is not anonymization. Current public calculations use clearly labelled synthetic inputs; official links support legal rules and public benchmarks, not private facts.

**Important unresolved incident:** earlier repository content and Git history may contain household-derived information. The current site boundary, a later commit, Jekyll exclusions, or a passing privacy scan do not remove old Git objects, other refs, pull-request refs, cached pages, forks or clones. This session did not rewrite history. A repository administrator must restrict repository access and assess the public-data remediation using [GitHub's sensitive-data removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository). Do not use a mirror force-push or history rewrite from a session branch. Independent copies may remain.

The guide is educational, not legal, tax, insurance, accounting or investment advice. A real decision requires private documents and advice from qualified professionals.

## Public guide features

- Executive summary and first-screen decision questions.
- Pure and mixed paths compared at common transfer dates and horizons.
- Phased-investing examples, reinvestment risk and black-swan stress cases.
- Tax, basis, assessment, estate, transfer-cost and deadline references.
- A printable Attorney & CPA briefing sheet, question register, glossary and review flags.
- Suggestions that can be reviewed without applying changes or submitting private data.
- Source-linked tables. Synthetic values are not factual estimates; unknown private values remain blank.

## Build and preview

Python 3 and Node.js are required. Never serve the repository root: it contains legacy and coordination material.

```sh
python3 scripts/build-guide.py
python3 scripts/check-generated.py
python3 scripts/check-figures.py
python3 scripts/package-site.py
python3 scripts/check-publication.py --self-test
python3 -m http.server 8080 --bind 0.0.0.0 --directory _public
```

The last command serves only the explicitly packaged guide. No backend, analytics, remote font or automatic network transfer is required. Suggestion choices stay in the browser's local storage and record status only.

## Verify

```sh
npm install --prefix .cache/test --no-audit --no-fund --ignore-scripts jsdom@26.1.0
node scripts/privacy-audit.cjs
node scripts/test-guide.cjs
python3 scripts/test-model-reference.py
python3 scripts/test-phased.py
node scripts/validate.js
node scripts/stress-test.js
python3 scripts/privacy-gate.py
python3 scripts/privacy-gate.py --self-test
```

The package boundary check rejects missing, extra, linked or altered artifact files. Runtime checks cover navigation, internal links, $10 display rounding, source-linked rows, controls and privacy regressions. The independent model reconstruction tests arithmetic across configurations and stress paths. Privacy scans are limited checks; they cannot prove anonymity or scrub Git history.

For browser testing, install `playwright-core@1.49.1`, `@sparticuz/chromium@131.0.1` and `axe-core@4.10.3` under `.cache/test`, then run `node scripts/test-browser.cjs`. The sandbox may lack Chromium system libraries such as NSS; CI is the fallback when local browser launch fails.

## Publication

- `index.html`, `guide/*.html`, `guide/data/*.js`, and `assets/safe.*` are the public guide and synthetic model.
- `scripts/build-guide.py` generates the HTML. Regenerate pages after editing it.
- `scripts/public_manifest.py`, `scripts/package-site.py`, and `scripts/check-publication.py` define and check the publication boundary.
- `scripts/test-guide.cjs`, `scripts/test-model-reference.py`, `scripts/privacy-audit.cjs` and `scripts/privacy-gate.py` test the rendered site, model arithmetic and limited privacy rules.
- Legacy research and analysis files are not part of the Pages artifact. Their presence in a public Git repository is not a privacy control.

An administrator can set GitHub Pages to deploy through the checked Actions workflow; doing so does not privatize the repository or erase its history.
