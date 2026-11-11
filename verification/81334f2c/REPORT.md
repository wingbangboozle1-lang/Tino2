# Publication-boundary audit — 11 November 2026

Session: `81334f2c`, fixed branch `arena/81334f2c-tino2`.

## Executive summary

The existing canonical dashboard already provides an executive summary, Property A inheritance scenarios, Property B already-owned rental context, annual cost/value projections, estate-tax headroom scenarios, a trust checklist, recorded economic replays, 50-year variable-condition stress paths, and a Flagged for Review register. This audit preserves that work instead of creating another contradictory dashboard.

The existing base case favors selling Property A at inheritance and diversifying while retaining Property B. This is a conditional model result, **not a verified optimal plan**. It depends on rents, insurance, repair reserves, returns, tax assumptions, occupancy eligibility and estate facts that are not independently confirmed. Housing services are not monetized in the live-in comparison. Stock returns, inflation and home appreciation are not guaranteed; stress-case weights are not known probabilities. The public review page discloses these limitations.

## Privacy finding and remediation

The canonical packaging script is allowlisted, but the deployed Pages site uses legacy Jekyll root publication. Before this change, verification reports were not explicitly excluded by `_config.yml`. Testing only `_public` did not prove the contents of the actual Jekyll deployment.

Changes:

- Exclude all `verification/` notes from root/Jekyll publication. No private household figures are added by this session.
- Add `scripts/check-publication.py`: an exact reviewed public-file manifest, rejecting unexpected files, missing files, symlinks and hard links. Negative tests exercise rejection of synthetic internal material, symlinks and missing pages.
- Add a GitHub Actions check that runs the existing model/stress/runtime checks, builds with GitHub's Jekyll Pages action, and audits the actual Jekyll output as well as the packaged output.
- Preserve root/main Pages deployment. Switching Pages to artifact mode was attempted but the settings API returned HTTP 403, `Resource not accessible by integration`. This is an administrative permission constraint, not a claim that the GitHub connection is disconnected.

This CI check detects publication drift; while Pages stays in legacy mode, it does **not** gate the independently triggered deployment. Maintainers should require this PR check and migrate to artifact-only Pages when repository administration permissions permit. Never claim that `noindex` or rounding provides access control. Repository history and cached former deployments can retain previously exposed information; these changes do not erase them. Private records should be reviewed off-repository.

## Independent official-source spot checks

Only the following facts were newly re-read by this session. Links in other rows were tested for presence and reference integrity, not independently certified as proving every claim.

- IRS: 2026 federal basic exclusion is $15,000,000. This is not a per-beneficiary inheritance allowance and does not establish this estate's remaining headroom. [Official IRS update](https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax).
- California State Controller: no California estate-tax return requirement for decedents dying on or after January 1, 2005. The page separately describes historical inheritance/gift taxes. This is not an exemption from income, capital-gain or property taxes. [Official SCO page](https://www.sco.ca.gov/ardtax_estate_tax.html).
- BOE: the current intergenerational value allowance is about $1,044,590 (rounded for this report) for transfers February 16, 2025–February 15, 2027; BOE adjusts every other year using the FHFA California HPI. Principal-residence eligibility and the exemption application within one year matter. The exact legal amount is in the official source; future values are unknown. [Official BOE release](https://www.boe.ca.gov/news/2025/nr-25-02.htm).
- GitHub: custom Pages workflows publish an uploaded artifact; deploy jobs require Pages write and OIDC permissions, and a dependency on the build job. [Official custom-workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

Property-specific insurance, actual parcel levies, legal unit status, trusts, appraisals, rent ledgers and aggregate estate/gift amounts were not obtained or verified. They remain unresolved, not estimated facts. See the public [Flagged for Review page](https://wingbangboozle1-lang.github.io/Tino2/site/review.html).

## Validation

Local tests on this branch:

- `python3 scripts/package-site.py`: PASS; canonical files only.
- `python3 scripts/check-publication.py --self-test`: PASS; 21 manifest files; negative tests pass.
- `node scripts/validate.js`: PASS; 581 checks / 11 pages / 70 registered sources. Source registration does not establish factual correctness.
- `node scripts/stress-test.js`: PASS; 50-year paths, estate ownership, privacy, real-dollar and shock arithmetic.
- `node scripts/runtime-test.cjs`: PASS after installing isolated jsdom 26.1.0; 11 rendered pages / 763 source-linked rows; no runtime errors or broken local links.
- `python3 src/check_links.py .`: PASS; 54 repository HTML pages, 871 rows, 124 distinct external links. This includes legacy files and does not mean those files are published. External links are not all live-tested by that script.

Actual Jekyll output is tested in GitHub Actions; release and deployment results are recorded in COORDINATION.md after completion. No claim of a full external-source line-by-line recertification is made.
