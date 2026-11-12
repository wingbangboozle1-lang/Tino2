# Session f344fcd1 — whole-repository privacy audit and re-check (12 Nov 2026)

No household figure is typed in this file. Patterns used for the privacy scan were kept outside the repository.

## 1. Privacy audit (the repository is public, so every tracked file and the history count)

| Check | Result | Reference |
|---|---|---|
| Unrounded assessed values and tax bills in the 134 tracked files of `main` | None found | [GitHub Docs, sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) |
| Personal names, street addresses, parcel numbers, e-mail addresses in tracked files | None found (only government contact addresses inside official citations and tool patterns) | same |
| Unrounded assessed values in the history of `main` | **42 of 173 commits** (history of `main` at `9867620`) still hold them (newest: a merge of 11 Nov 2026 08:06 UTC that carried an old verification report) | same |
| Saved pull-request copies (`refs/pull/*/head`) | **9** hold exact assessed values | same |
| Remote branch tips | **10 of 32** hold exact assessed values. (This session's first fetch saw only `main` because the working copy was cloned with a single-branch refspec; `git ls-remote` shows 32 branches. The same cause explains the "only `main` exists" note of session `1e425502`.) | same |
| Commit metadata | **New finding.** 37 commits on `main` at `95e6d6a` (36 pull-request merges and the first commit) are authored with the account's primary e-mail address. It appears in no file and not on the site. | [GitHub Docs, commit email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address) |

What a session can and cannot do: it cannot rewrite the history of `main` or delete pull-request copies. This session tried to author its own merge with the account's no-reply address (`gh pr merge --author-email`); GitHub answered "Invalid email address" for both forms of that address, because e-mail privacy is off on the account. Every merge therefore adds one more commit with the address until the owner changes the setting. The remaining steps are the owner's and are listed on the Flagged for Review page.

## 2. Checks re-run on `main` at `9867620` and again on this branch

`package-site.py`, `check-publication.py --self-test`, `validate.js`, `stress-test.js`, `runtime-test.cjs`, `qa/tools/gate.cjs`: all pass (figures in COORDINATION.md). Session `1e425502` ran at the same time, re-opened most of the same pages and reached the same results; its work touched only its own directory and the board.

## 3. Official pages opened on 12 Nov 2026

| Fact on the site | Found on the official page | Result | Official source |
|---|---|---|---|
| Federal estate filing threshold, death in 2026: $15,000,000 | Table row "2026 — $15,000,000" | Confirmed | [IRS, Estate tax](https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax) |
| Basic exclusion, death in 2027: $15,480,000; gift exclusion $20,000 | "basic exclusion amount of $15,480,000, up from a total of $15,000,000"; "$20,000, up from $19,000" (IR-2026-133, 5 Nov 2026) | Confirmed | [IRS newsroom](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) |
| Basis of inherited property is the value at the date of death | "The fair market value (FMV) of the property on the date of the decedent's death" | Confirmed | [IRS FAQ](https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances) |
| No California estate tax return for deaths from 1 Jan 2005 | "there is no longer a requirement to file a California Estate Tax Return" | Confirmed | [State Controller](https://www.sco.ca.gov/ardtax_estate_tax.html) |
| Proposition 19 amount $1,044,586 until 15 Feb 2027; next change February 2027 | "February 16, 2025 – February 15, 2027 — $1,044,586"; "The next adjustment … will occur in February 2027" | Confirmed | [BOE LTA 2025/009](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) |
| Proposition 19: home of parent and child, value limit, homeowners' exemption within 1 year, claim within 3 years, no relief for other property | Comparison chart, column "Proposition 19 (Current Law)" | Confirmed | [BOE, Proposition 19](https://www.boe.ca.gov/prop19/) |
| San Francisco allowable rent increase 1.6% (1 Mar 2026 – 28 Feb 2027); relocation amounts; File No. 261020 not enacted | 1.6%; $8,245.00 / $24,733.00 / $5,497.00; Ellis $11,110.05 / $33,330.13 / $7,443.90; notice posted 9 Nov 2026 "has not been enacted" | Confirmed | [SF Rent Board](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) |
| HUD FY2026 four-bedroom benchmark for Property A's ZIP: $6,390 (FY2025: $6,370) | FY2026 row $6,390; FY2025 row $6,370 | Confirmed | [HUD FY2026 lookup](https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=95014&year=2026) |
| Ballot measures of 3 Nov 2026 | Count of 11 Nov 2026 5:17 p.m.: Prop 3 60.7% yes, Prop 42 51.4% yes, Prop 40 47.5% yes, Prop 43 42.6% yes; "Results will be certified by December 11, 2026" | **Changed slightly** — site updated | [Secretary of State](https://electionresults.sos.ca.gov/returns/ballot-measures) |
| HUD rent benchmark is the current one | FY2027 Small Area FMRs are listed and took effect 1 Oct 2026 | **Site is one fiscal year behind.** FY2027 amount for the ZIP: blank, not confirmed (interactive lookup; spreadsheet not readable) | [HUD SAFMR page](https://www.huduser.gov/portal/datasets/fmr/smallarea/index.html) · [91 FR 56156](https://www.federalregister.gov/documents/2026/09/01/2026-17891/fair-market-rents-for-the-housing-choice-voucher-program-moderate-rehabilitation-single-room) |

Not re-opened in this session: the other entries of the source register (151 before this session). Their status is as recorded by the sessions that opened them.

## 4. Test for the stale rent benchmark

`rent-benchmark-test.cjs` reads the published model and changes only Property A's monthly rent by −10% and +10%. Output in `rent-benchmark-test.json`. At the published rent it reproduces the published results. Selling stays first in all nine cases (2040, 2045, 2050 × three rents). This is a test of sensitivity, not an estimate of the FY2027 amount.

## 5. Changes made to the site

Additions and corrections only; no model input, plan or recommendation changed. Listed in COORDINATION.md under session `f344fcd1`.
