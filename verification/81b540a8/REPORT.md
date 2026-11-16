# Privacy-first public guide hardening

**Date:** 16 November 2026

**Branch:** `arena/81b540a8-tino2`

**Scope:** Current Pages artifact and its deterministic generator only. No household values or identifiers are included in this report.

## Changes made

- Replaced public calculator defaults with invented teaching inputs and removed the household-data switch and household input dictionaries from the public-page generator.
- Replaced household-specific public summaries, costs, occupancy premises and recommendations with explicit withheld/private states and a no-personalized-recommendation statement.
- Kept the Attorney & CPA sheet, comparisons, what-if controls, mixed paths and Black swan/phased-investing scenarios, but they now use fictional inputs only.
- Changed the public notice and README to state that rounding is not anonymization and that Pages exclusions do not clean public Git history.
- Added hashes for known private-input amounts to the packaged-artifact regression test. Values are not stored in the test source. The scan checks packaged source and rendered pages for common identifier patterns; it is a limited control, not proof of anonymity.
- Replaced the force-push runbook with an administrator-coordinated process. No history rewrite, branch deletion, repository-visibility change or force-push was performed.

## Official source checked

- [GitHub Docs — Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository), opened 16 Nov 2026. It says history removal requires careful coordination, describes the risk of recontamination and loss of collaborators’ work, and notes that sensitive commits may remain accessible through clones, forks, cached views and pull requests. GitHub Support may assist with cached views and PR references. This supports the flagged status; it does not establish that this repository’s history has been cleaned.

No legal or tax rule was changed by this privacy update. Existing law and benchmark rows retain their existing official source links and verification record.

## Verification performed

All passed locally after rebuilding and packaging:

- `python3 scripts/build-guide.py`
- `python3 scripts/package-site.py` — 32 allowlisted public files; legacy files excluded
- `python3 scripts/check-publication.py --self-test`
- `node scripts/privacy-audit.cjs` — no blocked household input token, property ZIP code or common identifier in the package or rendered text
- Public wording scan — no owner-stated input labels, distinctive unit-count premise, or property ZIP code in the HTML artifact
- `node scripts/test-guide.cjs` — 18 rendered pages, 1,088 source-linked rows, 12,604 checks
- `python3 scripts/check-generated.py` — 18 generated pages current
- `python3 scripts/check-figures.py` — 39/39 ledger records verified
- `python3 scripts/test-model-reference.py` — 20,736 independent arithmetic comparisons
- `python3 scripts/test-phased.py` — 113 checks
- `python3 scripts/privacy-gate.py --self-test` and `python3 scripts/privacy-gate.py` — pass; repository gate reported no blocked identifier, unrounded household-scale amount, contact or parcel pattern
- `node scripts/validate.js` — 1,611 checks across 19 pages and 178 official sources
- `node scripts/stress-test.js` — 50-year paths, ownership, privacy, real-dollar and shock tests
- `git diff --check` — pass

**Browser-test limitation:** `node scripts/test-browser.cjs` was attempted after installing its npm dependencies. Chromium could not start because this environment lacks `libnss3.so`. The jsdom runtime tests passed; the Chromium smoke test remains for CI or an environment with the required system libraries.

## Irregularities / still needs review

1. **Historical exposure remains unresolved (High).** The repository is a public GitHub repository. The current Pages artifact is privacy-reviewed, but retained legacy files and earlier commits, branches and pull requests may still contain material. The current checkout is shallow and this session is restricted to its task branch; a safe rewrite of `main` and other refs cannot be performed here. Coordinate a full ref inventory and history cleanup with a repository administrator, then contact GitHub Support and coordinate with fork/clone owners as appropriate. A rewrite cannot erase copies already cloned.
2. The broad repository gate is not a proof of anonymity and does not remove historical Git objects. The site-level hashed-token scan checks the explicit known private amounts in the current public artifact, but cannot detect every possible inference or quasi-identifier.
3. Current Pages configuration remains under the repository’s existing publication mechanism. The PR checks must pass and the deployed site must be read back before declaring the live update complete.
