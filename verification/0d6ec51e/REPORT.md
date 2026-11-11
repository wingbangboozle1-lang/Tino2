# Verification record — session 0d6ec51e (11 November 2026)

Repository-only; not published. No household figure is typed in this folder: `options.cjs` reads every input from `site/data/model.js` at run time, and `options.json` holds only its rounded outputs.

## What was checked

| Check | How | Result |
|---|---|---|
| The independent calculation reproduces the three published choices | `options.cjs` rebuilds sell, rent and live for 2040, 2045 and 2050 from the yearly rows and compares with `MODEL.decision` | 12 of 12 equal to the dollar |
| The published engine (`site/data/options.js`) agrees with the independent calculation | `scripts/validate.js` compares 63 hold-then-sell figures, 9 depreciation figures, 6 old-rule figures, 24 estate-tax figures, 4 probate figures and 4 Property B figures | all equal after rounding to $10 |
| The two were written by different routes | Published engine: calls `MODEL.decision` with a shorter horizon and compounds the result; empty house = rental case with rent set to zero. Independent: loops the yearly rows itself and builds the sale | the agreement is therefore a real cross-check of the arithmetic |
| Arithmetic that does not depend on the model | Probate schedule on $1,000,000 = $23,000 and on $10,000,000 = $113,000; estate tax zero at the exclusion; 40% on the first $1,000,000 above it | pass |
| Whole suite on the final tree | `validate.js`, `stress-test.js`, `package-site.py`, `check-publication.py --self-test`, `runtime-test.cjs`, `qa/tools/gate.cjs`, `src/check_links.py`, `integration/tools/privacy_scan.py` | see the board block for the counts |

## Limits of this verification (read before relying on it)

1. Both calculations use the published model's own functions for yearly costs and values. They cross-check the new arithmetic, not the model's inputs. An error inside `MODEL.annualA` would pass both.
2. The depreciation figures use three assumed building shares, full-year deductions, no $25,000 allowance and the highest possible tax rate on the deduction at sale. The page states each assumption and also gives the opposite extreme.
3. The old-rule test changes one thing only: the assessed value carried by the heir. It does not model any other part of the failed measure.
4. The estate-tax table assumes no prior taxable gifts, no unused exclusion from a parent who died first, and no deductions. The exclusion after 2027 is the model's projection.
5. Eight official documents were read from the official site's search-result text only (marked "extract" in `research/0d6ec51e/completeness-ledger.md`). They are flagged on the site.

## Irregularities

| ID | Finding | Status |
|---|---|---|
| N-I1 | The published rental case contains no depreciation, although the checklist page tells the reader to reconcile it | Quantified on the new page; ranking unchanged; published figures left as they are |
| N-I2 | No plan includes estate tax on the money, and the amount of money is not in the record | Flagged High; table by amount published |
| N-I3 | The recommendation depends on the current reassessment rule | Flagged High; test published; initiative status verified |
| N-I4 | Eight documents not opened, read from extracts | Flagged Medium |
| N-I5 | The source register labels those entries "Carried forward · needs revalidation"; they were not carried forward, they were read from extracts | Cosmetic; the register's rule was not changed because another session wrote it |
| N-I6 | This session's first board entry gave its claim time as 13:27 UTC; the push was at 13:18 UTC | Corrected in the block |
| N-I7 | Steps for which no official page was opened (affidavit of death of trustee, preliminary change of ownership report, supplemental-bill timing) | Not published; listed in the ledger as open |
