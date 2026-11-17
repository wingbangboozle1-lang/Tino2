# Source verification — depreciation, recapture and the home-sale exclusion

Session `62576bfc`, branch `arena/62576bfc-tino2`. Every document below was opened and read on
**17 November 2026** from this session's own fetches. Nothing here is quoted from a search result,
a summary page or another session's report: each passage was read at the URL printed beside it.

The rule of this repository is *never infer*. Where a value could not be read at the official page,
it is left blank or marked as an assumption on the page, and that is recorded below too.

## What this pass was for

The brief asks three times for rental tax the published model does not compute: *"Model depreciation
and recapture"*, *"Add an imputed-rent input for living paths"*, and *"Switch on the
primary-residence exclusion for living-then-sell paths"*. `guide/data/model.js` states that no
depreciation or passive-loss benefit is invented, and `guide/review.html` carries
*"omitted depreciation/recapture"* as a standing limitation. This pass establishes the rules those
three items rest on, so the new page publishes nothing that was not read at source.

## 1. IRS Publication 527 (2025), Residential Rental Property

<https://www.irs.gov/publications/p527> — read 17 Nov 2026 (HTML, chapters 2 and the basis
sections). Publication 527 is already the site's `rental` source; the passages below are the ones
the new page now quotes.

| Claim | Passage read at the source | Where the site uses it |
|---|---|---|
| 27.5-year recovery period | "Residential rental property (buildings or structures) and structural components such as furnaces, waterpipes, venting, etc. \| 27.5 years \| 30 years1" | Recovery-period row; the engine's `RECOVERY_YEARS` |
| Straight line and mid-month are required | "You must use the straight line method and a mid-month convention for residential rental property. In the first year that you claim depreciation for residential rental property, you can claim depreciation only for the number of months the property is in use." | Method-and-convention row; the schedule's first-year fraction |
| What the mid-month convention does | "A mid-month convention is used for all residential rental property and nonresidential real property. Under this convention, you treat all property placed in service, or disposed of, during any month as placed in service, or disposed of, at the midpoint of that month." | The 11.5-of-12 months fraction used in year 1 and the disposal year |
| Land is not depreciable | "You can't depreciate the cost of land because land generally doesn't wear out, become obsolete, or get used up. The costs of clearing, grading, planting, and landscaping are usually all part of the cost of land and can't be depreciated." | The land/building split control and the rule row |
| Splitting land from building | "you must divide the cost between the land and the buildings to figure the basis for depreciation of the buildings. The part of the cost that you allocate to each asset is the ratio of the FMV of that asset to the FMV of the whole property at the time you buy it." and "If you aren't certain of the FMVs of the land and the buildings, you can divide the cost between them based on their assessed values for real estate tax purposes." | The building-share control's explanation |
| When depreciation starts | "You begin to depreciate your rental property when you place it in service for the production of income." and "You place property in service in a rental activity when it is ready and available for a specific use in that activity. Even if you aren't using the property, it is in service when it is ready and available for its specific use." | Placed-in-service rule row |
| Conversion from personal use | "If you used the property for personal purposes before changing it to rental use, its basis for depreciation is the lesser of its adjusted basis or its FMV when you change it to rental use." | The basis row and a flagged limitation |
| Depreciation reduces basis | "Depreciation reduces your basis for figuring gain or loss on a later sale or exchange." and "you must stop depreciating property when the total of your yearly depreciation deductions equals your cost or other basis of your property … include any depreciation that you were allowed to claim, even if you didn't claim it." | Adjusted-basis row and the recapture arithmetic |

Not stated anywhere in this publication, and therefore **not published**: the $25,000 rental real
estate loss allowance and its phase-out. That lives in Publication 925, which the page links as a
limitation only, with no figure taken from it.

## 2. IRS Publication 946 (2025), How To Depreciate Property

<https://www.irs.gov/publications/p946> — read 17 Nov 2026 (HTML, Appendix A).

| Claim | Passage | Use |
|---|---|---|
| The official percentage tables exist and where | "Table A-6 is for Residential Rental Property using Mid-Month Convention and Straight Line depreciation--27.5 Years and lists the percentages for years 1 through 29 by month placed in service." | The percentage-table rule row |

The page computes the schedule from the mid-month rule in Pub. 527 rather than transcribing the
percentage grid, and says so. The arithmetic (11.5/12 of a full year in the first and disposal
years, a full year in between, over 27.5 years) is shown on the page and reproduced by
`scripts/test-tax-realism.py`, which recomputes it independently in Python.

## 3. IRS Topic 409, Capital gains and losses

<https://www.irs.gov/taxtopics/tc409> — read 17 Nov 2026.

| Claim | Passage | Use |
|---|---|---|
| Unrecaptured section 1250 gain, 25% maximum | "There are a few other exceptions where capital gains may be taxed at rates greater than 20%: 1. The taxable part of a gain from selling section 1202 qualified small business stock is taxed at a maximum 28% rate. 2. Net capital gains from selling collectibles (such as coins or art) are taxed at a maximum 28% rate. 3. **The portion of any unrecaptured section 1250 gain from selling section 1250 real property is taxed at a maximum 25% rate.**" | The recapture rate, the 25% line in the engine, and the ledger record `UNREC-1250-RATE-MAX` |
| The ordinary capital-gain rates | "For taxable years beginning in 2025, the tax rate on most net capital gain is no higher than 15% for most individuals", with the 0% and 20% thresholds listed by filing status | The 15% / 20% control on the page |

The IRS states 25% as a **maximum**, and the page says maximum. It is not modelled as a flat rate
anywhere.

## 4. Instructions for Schedule D (Form 1040) (2025)

<https://www.irs.gov/instructions/i1040sd> and <https://www.irs.gov/pub/irs-pdf/i1040sd.pdf> — read
17 Nov 2026 (the PDF, "Line 19" and the Unrecaptured Section 1250 Gain Worksheet).

| Claim | Passage | Use |
|---|---|---|
| When the worksheet applies | "Line 19 … complete the Unrecaptured Section 1250 Gain Worksheet in these instructions if any of the following apply for 2025. • You sold or otherwise disposed of section 1250 property (generally, real property that you depreciated) held more than 1 year. …" | The "where it is worked out" rule row |

## 5. Instructions for Form 4797 (2025)

<https://www.irs.gov/instructions/i4797> — read 17 Nov 2026.

| Claim | Passage | Use |
|---|---|---|
| Where the recapture is reported | Part III of the form covers the ordinary-income recapture; the instructions list "Section 1250 property" under Line 26, and the publication pages for 523 and 544 both route the sale of depreciable rental property through Form 4797 | The "where it is reported" rule row |

No dollar figure is taken from this document. It is cited for the reporting route only.

## 6. IRS Publication 523 (2025), Selling Your Home

<https://www.irs.gov/publications/p523> — read 17 Nov 2026 (HTML; the eligibility steps, the
business-or-rental-use section and Worksheet 3). This is the document the whole §121 layer rests on.

| Claim | Passage | Use |
|---|---|---|
| The exclusion amounts | "you may exclude the first $250,000 of gain from the sale of your home from your income and avoid paying taxes on it. The exclusion is increased to $500,000 for a married couple filing jointly." | The filing-status control and ledger record `S121-EXCLUSION-AMOUNT` |
| Ownership test | "If you owned the home for at least 24 months (2 years) out of the last 5 years leading up to the date of sale (date of the closing), you meet the ownership requirement. For a married couple filing jointly, only one spouse has to meet the ownership requirement." | Ownership row |
| Residence test | "If you owned the home and used it as your residence for at least 24 months of the previous 5 years, you meet the residence requirement. The 24 months of residence can fall anywhere within the 5-year period, and it doesn't have to be a single block of time. All that is required is a total of 24 months (730 days) of residence during the 5-year period. Unlike the ownership requirement, each spouse must meet the residence requirement individually for a married couple filing jointly to get the full exclusion." | Residence row, and the engine's `residenceInWindow` test |
| One main home | "You may take the exclusion, whether maximum or partial, only on the sale of a home that is your principal residence, meaning your main home. An individual has only one main home at a time." | The one-main-home row, which matters here because the planning premise is that the heir already owns and lives in another property |
| Look-back | "You may take the exclusion only once during a 2-year period." | Look-back row |
| Depreciation is never excluded | "If you were entitled to take depreciation deductions because you used your home for business purposes or as rental property, you cannot exclude the part of your gain equal to any depreciation allowed or allowable as a deduction for periods after May 6, 1997." | The carve-out row and the engine's subtraction of depreciation before the exclusion is applied |
| Nonqualified use | "Gain from the sale or exchange of your main home isn't excludable from income if it is allocable to periods of nonqualified use. Nonqualified use means any period after 2008 when neither you nor your spouse (or former spouse) used the property as your main home, with certain exceptions." | The nonqualified-use row and the allocation in the engine |
| The exception | "A period of nonqualified use does not include: 1. Any portion of the 5-year period ending on the date of the sale or exchange after the last date you or your spouse (or former spouse) used the property as your main home; …" | The exception row; the engine applies a zero factor for `live_then_rent` |
| Worksheet 3, the allocation method | Section B: "Divide the nonuse days by the days owned. This number is your nonresidence factor" and "Multiply the decimal from Section B, Step 4, by the amount listed in Section B, Step 1. This number is your nonqualified use gain" | The engine's `worksheet3()` |
| Worked example: Finley | "Finley buys a property on January 1, 2020, for $400,000 and uses the entire property as rental property for 2 years, claiming $20,000 of depreciation deductions … Finley allocates 40% (2/5 …) of the remaining $300,000 gain, or $120,000, to nonqualified use … The $180,000 of the remaining gain is excluded from gross income … The $20,000 attributable to the depreciation deduction is subject to recapture under section 1250." | Printed on the page and frozen in `scripts/test-tax-realism.py` |
| Worked example: Taylor | "Taylor had deducted $27,000 for depreciation for the period of rental to a third party. Taylor can't exclude the part of the gain equal to the depreciation claimed after May 6, 1997, for renting the house ($27,000). This is unrecaptured section 1250 gain. … Taylor entered $200,000 in Step 3 of Section A. … The entire $200,000 gain is excludable from gross income because any period after the last qualified use doesn't constitute nonqualified use." | Printed on the page and frozen in `scripts/test-tax-realism.py` |

Those two examples are the reason the page is trustworthy: the site's worksheet code reproduces the
IRS's own published outcomes ($320,000 gain, $20,000 recaptured, $120,000 nonqualified, $180,000
excluded; and $227,000 gain, $27,000 recaptured, $0 nonqualified, $200,000 excluded), and
`scripts/test-tax-realism.py` fails if it ever stops doing so.

## 7. IRS Publication 925, Passive Activity and At-Risk Rules

<https://www.irs.gov/publications/p925> — **linked, not read in this pass.** The page links it as a
limitation only: that a rental loss is not automatically usable in the year it arises. No figure,
allowance or threshold from it is published, so nothing was verified against it. Recorded here so
the gap is visible rather than implied away.

## 8. Documents opened that produced no claim

- <https://www.irs.gov/pub/irs-pdf/i1040sd.pdf> chunks 2, 5, 6 and 8 were read to locate line 19;
  the intervening material (QSB stock, collectibles, demutualisation) is not used by this site.
- Search results returned several secondary tax sites stating the 25% rate; none is cited. The
  statutory rate was read at Topic 409 instead, and the worksheet route at the Schedule D
  instructions.

## What is deliberately not published

- The passive-activity allowance, its income phase-out, and the year a suspended loss is released.
- California's treatment of the same gain and the 3.8% net investment income tax. The page is
  labelled federal-only; the guide's existing ledger record `CA-CAPITAL-GAINS-ORDINARY` is the
  basis for the California sentence, and Topic 559 for the NIIT sentence.
- Any land/building ratio for a real parcel. The page's building-share control is a synthetic input
  and the page says so.
- Any statement about what the household should do. The page compares patterns on a synthetic house
  and states the traps; it does not rank them for a real family.

## Irregularities found

1. The `ftb` source key in `scripts/build-guide.py` is labelled "CA Controller · estate tax" but the
   ledger record `CA-CAPITAL-GAINS-ORDINARY` cites it with the FTB Form 540 instructions URL. The
   two disagree, so the new page uses the `ftb540` key (which carries the FTB instructions URL and
   label) for the California capital-gain sentence. **The mismatch in the ledger record is left as
   it is** — correcting another session's record is not this session's scope, and the record's
   source URL is correct; only its `source_id` label is off. Flagged here for the board.
2. Nothing else. Every passage the new page attributes to an IRS document was read at that document
   on 17 November 2026 and is transcribed above.
