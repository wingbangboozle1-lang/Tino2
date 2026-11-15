# Verification report — session fdf0ec80 (branch arena/fdf0ec80-tino2), 15 Nov 2026

Base: `main` at `9ecdc55` (PR #98 merged). Scope: review of the current repository and published guide, privacy re-check, and one new flagged item. No household figures were added to any committed or published file.

## What was checked

| Check | Result |
|---|---|
| `check-generated.py` | PASS, 17 generated pages up to date |
| `check-figures.py` | PASS, 28 ledger records, 28 verified, 0 explicitly unverified |
| `test-model-reference.py` | PASS, 108 configurations, 250 stress years, 1,500 phased years, 20,736 arithmetic comparisons |
| `package-site.py` + `check-publication.py --self-test` | PASS, 31 reviewed files; extra, missing, altered, symlinked and hard-linked files rejected |
| `test-phased.py` | PASS, 113 checks |
| `test-guide.cjs` | PASS, 17 rendered pages, 922 source-linked table rows (+1 from the new flagged row), 11,530 checks |
| `privacy-audit.cjs` | PASS (limited collision scan; not proof of anonymity) |
| `test-browser.cjs` | **Not run in this sandbox**: Chromium needs `libnss3`, which is not installed and cannot be fetched from the allowed hosts. CI runs it on the pull request. |
| Live site (`https://wingbangboozle1-lang.github.io/Tino2/`, `guide/suggestions.html`) | Read back on 15 Nov 2026; renders the decision overview, what-would-change table, reinvestment table and suggestions register |

## Privacy findings

1. **Published artifact:** no household ZIP code, value, tax-bill figure or rent figure appears in the 31 packaged files. The only hits for `7150` on the what-if page are inside numeric model outputs (for example `…7150`), not the rent figure.
2. **Legacy files at the branch tip (Critical, newly flagged):** exact household figures and ZIP codes remain in files outside the Pages artifact, for example `cupertino.html`, `decision.html`, `flagged.html`, `docs/*`, `pages/*`, `dashboard/*`, `integration/ledger/official_amounts.txt`. GitHub displays them even though Pages does not. This session did not remove them, because other sessions' records depend on them; removal is logged as an owner decision.
3. **Git history (existing item N02 / L-D2):** full history was fetched (`git fetch --unshallow`, 385 commits). Exact household tokens occur in these numbers of commits: Cupertino tax-assessment values 5 commits each (two values), Cupertino stated value 6, San Francisco stated value 3, Cupertino ZIP 47, San Francisco ZIP 38. (Counts from `git log --all -S<token>`; token strings are not reproduced here.) Rewriting history is not performed here; it needs collaborator sign-off.

## Irregularities for review

- Rounding rule: the owner's brief asks for $10 rounding of household figures. The repository keeps them out of published files (decision L-D1 in COORDINATION.md). That conflict is for the owner to resolve; it is listed as N01.
- External rule figures were **not re-fetched** in this session. Their verification stands on `verification/12f68358/REPORT.md` (14 Nov 2026). Re-verify before relying on any figure after that date.

## Sources (official, for manual review)

- IRS Form 706 instructions (basic exclusion): https://www.irs.gov/instructions/i706
- IRS inherited basis FAQ: https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances
- California BOE Proposition 19: https://www.boe.ca.gov/prop19/
- U.S. Treasury daily par yield curve: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611
- GitHub, removing sensitive data: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
