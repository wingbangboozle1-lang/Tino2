# Inheritance decision dashboard

A public, source-linked decision dashboard for comparing what to do with an
anticipated Cupertino trust inheritance (Property A) alongside an already-owned
San Francisco three-unit building (Property B). It is anonymised by design and
every published amount is rounded to the nearest $10.

**This is a planning tool, not advice.** All projections are stated estimates
built from published official rates and explicit assumptions, listed in full on
the [method page](guide/method.html). The two property values are round planning
anchors, not appraisals and not record values.

## Privacy

This repository is public. Older commits, branches, pull requests, caches, forks
and clones may still contain household-derived figures from earlier sessions,
even though they are excluded from the published site. A Pages exclusion,
rounding, `robots.txt` or deleting a file in a later commit **does not remove**
that exposure. Coordinates cleanup with collaborators and follow
[GitHub's sensitive-data-removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

What the site itself does:

- no names, addresses, parcel numbers, account values or document figures;
- the Proposition 13 base is published only as a ratio band, because a base-year
  value is the one figure that identifies a specific parcel in a public
  assessor database;
- no form posts anywhere, no analytics, no cookies, no remote assets;
- the interactive controls compute in the browser and store only a one-word
  suggestion status in local storage.

## Build

Python 3 and Node.js are required. Never serve the repository root: it contains
legacy material.

```sh
node scripts/snapshot.cjs          # run the model, write scripts/data/snapshot.json
python3 scripts/build_site.py      # write index.html and guide/*.html
python3 scripts/package-site.py    # copy the allowlist into _public
python3 -m http.server 8080 --bind 0.0.0.0 --directory _public
```

`scripts/check-generated.py` re-runs the first two steps and fails if the
committed HTML differs, so a model change cannot ship without regenerating.

## Verify

```sh
npm install --prefix .cache/test --no-audit --no-fund --ignore-scripts jsdom@26.1.0
python3 scripts/package-site.py
python3 scripts/check-publication.py --self-test
python3 scripts/check_rounding.py _public
python3 scripts/check-jekyll.py
python3 scripts/test-model-reference.py
node scripts/privacy-audit.cjs
node scripts/test-guide.cjs
```

| Check | What it proves |
|---|---|
| `test-model-reference.py` | An independently written Python model reproduces every published table to the dollar, without running the JavaScript. |
| `check_rounding.py` | Every published dollar amount is a multiple of $10, or a listed official agency amount. |
| `check-publication.py` | The artifact is exactly the reviewed allowlist: no extra, missing, altered, symlinked or hard-linked files. |
| `check-jekyll.py` | The legacy root Jekyll build would publish exactly the same reviewed files. |
| `test-guide.cjs` | Each page renders, loads its scripts, has complete navigation, no broken local links, a source link in every table row and no non-$10 amount. |
| `privacy-audit.cjs` | No distinctive legacy household figure, identifier or external resource reaches the artifact. |

A passing privacy scan **cannot prove** anonymity, and a passing link check does
not make a legal claim correct.

## Structure

- `index.html`, `guide/*.html` — the twelve public pages.
- `guide/data/model.js` — the only implementation of the arithmetic.
- `guide/data/stats.js` — empirical baselines from the published series.
- `scripts/params.py` — every assumption with its stated basis.
- `scripts/snapshot.cjs` — runs the model once and freezes the figures the
  static tables show.
- `scripts/build_site.py` — deterministic page generator.
- `scripts/public_manifest.py` — the publication allowlist.
- `site/`, `docs/`, `research/`, `qa/`, `verification/` — retained earlier work,
  not published, and not necessarily verified.

## The model in one paragraph

At the transfer date the home is reassessed to market value unless Proposition 19
relief applies, which requires the heir to occupy it. Selling pays no gain tax
because basis resets at death. Renting pays income tax on positive net operating
income after a 27.5-year depreciation shield and 25% recapture at exit. Living in
gets the relief and the $250,000 home-sale exclusion but no rent. All three are
valued at the same endpoint, with cash flows reinvested at the same net return.
Stress tests replay five real historical shocks and resample the 1976-2025 joint
record of California inflation and county house prices 2,000 times.

## Publication boundary

Pages serves `main`/root through Jekyll, and `_config.yml` excludes the legacy
paths. The workflow checks both the packaged artifact and the Jekyll output. For
a fail-closed boundary, a repository administrator can set **Settings → Pages →
Build and deployment → Source → GitHub Actions**; the workflow then deploys the
checked `_public` allowlist only after every check passes. That change does not
make the repository private and does not touch history.

Do not add `.nojekyll` at the repository root: it would bypass the Jekyll
exclusions.

If the Pages source is switched to Actions, the resulting site is still public,
and the entire Git history with it.
