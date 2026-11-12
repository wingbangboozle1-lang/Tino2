# Executive-summary review — 12 November 2026

## Scope and honesty boundary

The inherited repository already implements the requested 15-page dashboard. This session inspected coordination records, the publishing workflow, README, landing page, review register and test scripts. It did **not** independently re-verify every historical research assertion or every external URL. Passing structural source-link tests does not prove that an external source supports a figure. Nine rendered calculated rows carry context links only, not evidence that their outputs are official facts. Household values remain unverified assumptions; projections are computed scenarios, not confirmed future amounts.

## Changes

- Recast the landing-page recommendation as a base-case leader, not an unconditional instruction.
- Put the missing estate-tax allocation warning next to the recommendation, not only deep in the review register.
- State that the model does not price housing services; acknowledge that other holding costs change too.
- Round the landing-page monthly water display to the nearest $10; preserve engine inputs and calculation precision.
- Add a dedicated, source-linked Suggestions section with priority, question, discovery route and approval gate. These are proposals only: no financial baseline, privacy setting, trust interpretation or history change is automatically implemented.
- Preserve the existing Flagged for Review disclosures, particularly public-history exposure. Do not claim that display rounding ensures anonymity.

## Official pages directly retrieved this session

| Source | What was checked | Limits |
|---|---|---|
| [IRS estate tax](https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax) | Gross estate includes real estate, cash, securities and certain other interests; deductions and adjusted taxable gifts matter; 2026 filing threshold $15,000,000; portability requires an election | This page's table ends in 2026. This session does not use it to independently validate the site's separate 2027 citation or household tax due. |
| [BOE Proposition 19](https://www.boe.ca.gov/prop19/) | Principal residence of transferor and transferee; value limit tied to taxable value plus adjusted exclusion; homeowner exemption within one year; exclusion claim within three years or before third-party transfer | Summary chart retrieved; not proof of this trust's eligibility or future law. |
| [CDI residential insurance](https://www.insurance.ca.gov/01-consumers/105-type/5-residential/) | Official guidance to shop and compare policies, coverage tools, limited FAIR Plan coverage | No property-specific premium confirmed; no new quote inferred. |
| [GitHub sensitive-data guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) | History rewrite has coordination and data-loss risks; cached references, forks and other clones can persist | No history rewrite authorized or performed. |

## Verification performed

- `python3 scripts/package-site.py`: PASS; public allowlist only.
- `python3 scripts/check-publication.py --self-test`: PASS; 28 public files; negative tests pass.
- `node scripts/validate.js`: PASS; 1,132 checks, 15 pages, 171 source-register entries.
- `node scripts/stress-test.js`: PASS; 50-year paths, ownership, real-dollar and shocks.
- `node scripts/runtime-test.cjs`: PASS; 1,331 rendered rows source-linked; no JavaScript errors or broken local file links.
- `node qa/tools/gate.cjs`: PASS; zero errors/warnings; 1,322 own-source rows, nine context-link calculated rows. Existing money gate primarily checks amounts at or above $1,000 and is not a universal guarantee for all smaller dollar displays.
- Regression check confirms the four new suggestion rows have HTTPS official references and approval gates; estate-tax caveat is adjacent to the recommendation.

The isolated jsdom test dependency is cached, not committed or published. The generated shared gate report was restored after inspection to avoid out-of-scope edits. No arithmetic or financial assumptions changed.

## Irregularities / follow-up

Existing unresolved items remain on `site/review.html`: historical privacy exposure, actual insurance quotes, estate inventory, trust eligibility, rent benchmark freshness, taxes and private bill reconciliation. This session cannot establish household facts from public official sources. They must not be silently filled. Broad prior “verified” labels must be read with the ledger's per-item qualifications. No exhaustive external-link availability claim is made.
