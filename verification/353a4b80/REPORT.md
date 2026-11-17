# Session `353a4b80` — verification report

Branch `arena/353a4b80-tino2`, base `dcf2b34`. All work is on this branch only.

## What this session was looking for

The brief asks, among other things, for an imputed-rent input for the living paths
("*Add an imputed-rent input for living paths*"), for decisions to be comparable at
common horizons, and for nothing on the site to be stated in a way that misleads a
reader. The review below began as a line-by-line read of what the guide says it omits,
and found that one of the stated omissions was not an omission at all.

## Finding 1 — the living paths carry an imputed rent the site said they did not (corrected)

`analysis_model.simulate()` has always added, to the living paths' annual cash flow, a
rent the owner avoids by occupying the home:

```
avoided = imp0 * 12 * cf * cpi_lvl if living else 0.0        # scripts/analysis_model.py
```

with `imp0` taken from `p['rent_mo']` — the same input the rent path receives as gross
rent. Before this session that line was unnamed and undeclared, and four published
statements said the opposite of what it does:

| Page (before) | Statement |
|---|---|
| `guide/decision.html` | "No estate-tax allocation or value of housing services is included." |
| `guide/questions.html` (Q2) | "the financial ranking on the comparison page deliberately omits the value of housing services" |
| `guide/brief.html` | "the model credits no value for living there" |
| `guide/suggestions.html` (S19) | "Living paths currently credit no rent avoided." |

**Measured on the guide's own synthetic example inputs** (`analysis_pages.EXAMPLE_A`,
`EXAMPLE_PARAMS`, transfer 2045, unrounded, recomputed by `scripts/test-imputed-rent.py`):

| Live path, 25 years | Total wealth |
|---|---|
| With the credit as the engine computed it | $11,619,761 |
| With the credit set to zero | $6,600,131 |
| **The credit itself** | **$5,019,630, about 43% of the live total** |
| Sell at inheritance, invest at once | $12,408,330 |

So the credit is not a rounding detail: it is the difference between living finishing
$789,000 behind selling and $5.8 million behind it. At 10 years it is decisive:

| 10-year horizon | With credit | Without credit |
|---|---|---|
| Live in it | $5,355,600 | $4,158,380 |
| Sell and invest at once | $5,177,560 | $5,177,560 |
| Which leads | **living** | **selling** |

That is the exact question the brief's standing item was about, and the site was
answering it silently.

### What changed

1. `analysis_model.DEFAULT_PARAMS` now carries `imputed_rent_mo: None`, documented as
   "*None means use rent_mo*". `simulate()` derives `imp0` from it and reports it back
   as `imputed_rent_mo`, alongside the existing `avoided_rent` total. **No published
   figure moved**: all 84 scenario × horizon × path totals were compared before and
   after the change and all were identical.
2. The What-if page gains a **"Rent the living paths avoid"** control (modelled rent, or
   no value), precomputed across all 288 existing control combinations. Setting it to
   *no value* moves only the four living/mixed-living paths and moves no sell or rent
   path — asserted in the test.
3. The four statements are corrected in the direction the engine computes, and the
   comparison page now states the credit's size, its share of the live total, and the
   fact that it decides the 10-year ranking. The percentages and dollars are computed at
   build time from the model, so they cannot drift from the engine.
4. S19 moves to **Done 17 Nov 2026**, keeping its open remainder: the figure is the
   modelled rent, not an independent rent opinion for a real property.
5. `scripts/test-imputed-rent.py` (new, 43 checks) pins the arithmetic on both settings,
   fails if any of the four old statements is republished, checks that the what-if data
   agrees with the model, and checks that the disclosure quotes the model's own figure.
6. The figure ledger gains `MODEL-IMPUTED-RENT-25Y`, deliberately recorded with
   `verified: false` and no `source_url`, because it is a model output and not an
   official amount. The ledger's own rule ("an unverified record must not carry a
   source_url") is satisfied, and the guide's prose treats it as an assumption.

## Finding 2 — the site's two engines give opposite recommendations (flagged, not fixed)

The site publishes two independent calculators on the same synthetic inputs:

* `guide/data/model.js` → `annualA()` gives the living path **no** avoided rent
  (`grossRent: 0, vacancyCost: 0, managementCost: 0`; `afterTaxCash = -operatingCost`).
* `scripts/analysis_model.py` → `simulate()` credits it, as above.

They therefore disagree about the headline answer:

| Transfer 2045, horizon | Python engine (`/guide/paths.html`, `/guide/decision.html` distribution table) | Browser engine (`/guide/whatif.html`, `/guide/decision.html` comparison table) |
|---|---|---|
| 10 years | living leads | selling leads |
| 25 years | selling leads | selling leads |
| 50 years | selling leads | selling leads |

Rendered in a browser, the What-if page's own status line says *"Highest total under
these controls: Live in it (never sell)"* at the 25-year default, while the same page's
sibling table (`/guide/paths.html`) says selling leads at 25 years. A reader who moves
one control at a time across the site can be told two different things.

**Why this session did not fix it.** Aligning either engine changes published seven-figure
outputs across several pages, and the browser engine's numbers are frozen by
`scripts/test-model-reference.py` (108 configurations) and `scripts/test-guide.cjs`
(model invariants on `guide/decision.html`). Those are shared gates owned by other
sessions; editing them from this branch would be a scope collision under the board's
rules. The item is logged in `COORDINATION.md` as a request with the proposed fix and the
files it touches. It is also published on the site's Flagged page so the reader is not
left with a silent contradiction.

## Finding 3 — a duplicate `source` key in the generator (cosmetic, left in place)

`scripts/build-guide.py` defines `'rp2532'` twice in its source dictionary (lines ~9 and
~20 at the base commit). Python keeps the last value; both point at Rev. Proc. 2025-32,
so no link is wrong. Recorded, not changed, because the file is touched by every session.

## Official sources re-opened on 17 November 2026

Each was fetched live today and the passage the guide relies on was read again.

| Source | Passage read | Result |
|---|---|---|
| [IRS, IR-2026-133 (5 Nov 2026), 2027 inflation adjustments](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) | "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from a total of $15,000,000 for estates of decedents who died in 2026"; annual exclusion "$20,000 … up from $19,000"; non-citizen spouse "$201,000 … up from $194,000" | MATCH — no change to `FED-EXCLUSION-2026/2027`, `FED-GIFT-EXCLUSION-2026/2027`, `GIFT-ANNUAL-2026`, `FED-GIFT-SPOUSE-NONCITIZEN-2026/2027` |
| [BOE, Proposition 19](https://www.boe.ca.gov/prop19/) | The Proposition 58/193 vs Proposition 19 comparison: value limit "current taxable value plus $1,000,000 (as biennially adjusted)"; "File for homeowners' exemption within 1 year of transfer"; "File claim for exclusion within 3 years or before transfer to third party"; R&TC §63.2 | MATCH |
| [BOE, Letter to Assessors 2025/009 (7 Mar 2025)](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) | "the $1 million amount is adjusted to **$1,044,586**"; "for transfers that occur February 16, 2025 through February 15, 2027"; the enclosed table of all three windows; "The next adjustment … will occur in February 2027" | MATCH — `PROP19-ALLOWANCE` and the three enacted windows are exactly as published |
| [FTB, 2025 Instructions for Form 540](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html), line 62 | "Line 62 – Behavioral Health Services Tax. If your taxable income is more than $1,000,000 … Tax rate – 1%: .01 … Multiply line 3 by line 4" | MATCH — `CA-BHST` (the brief's "1% tax above one million dollars") |
| Same, line 19 as the base of the schedules | Rate schedules apply to Form 540 line 19 (taxable income), which includes capital gains; the instructions contain no separate capital-gain rate | MATCH on the rates; the "no separate capital-gain rate" point remains an inference from the schedules, and the Flagged page already says so |

Not re-opened today (no claim in this session depends on them): the FTB rate-schedule
PDF (the fetch failed; the amounts it carries were re-read on 14–16 Nov 2026 and are
carried at their original `checked` dates), the county assessor pages, FRED series,
BLS, HUD and the SF sources.

## Verification performed

Recomputations are in `scripts/test-imputed-rent.py`; the suite results and the
publication result are recorded in the `COORDINATION.md` block for this session.

## What a reader should take from this

*The comparison between living in an inherited home and selling it turns on a number the
household has to supply: what occupying the home is worth to them.* The model can price
the rent avoided; it cannot price proximity, continuity, or the willingness to be a
landlord. Before this session the guide took a silent position on that number. It now
states it, sizes it, and lets the reader take it away — which is what the original brief
asked for, and what makes the ranking reviewable instead of inherited.
