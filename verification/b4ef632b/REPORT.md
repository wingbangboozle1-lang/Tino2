# Verification report — session `b4ef632b` — 17 Nov 2026

## Scope
Periodic recheck of the load-bearing official authorities the guide relies on, as of 17 Nov 2026, distinguishing enacted law from proposals, per the brief. No household figures or personal identifiers are involved. This session changed no model input and no published figure.

## Sources re-opened and read on 17 Nov 2026

| Authority | Item | Passage read | Result |
|---|---|---|---|
| IRS IR-2026-133 (5 Nov 2026) | Estate basic exclusion; annual gift exclusion | Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from $15,000,000 for 2026. For calendar 2027 the first $20,000 of gifts to any person are not taxable gifts, up from $19,000 for 2026; gifts to a non-citizen spouse $201,000 for 2027, up from $194,000 for 2026. | MATCH — guide tax page and Questions register carry these exact amounts |
| BOE LTA 2025/009 (7 Mar 2025) | Proposition 19 $1M allowance adjustment | For transfers 16 Feb 2025–15 Feb 2027, the value cap is the factored base year value plus $1,044,586. The next adjustment occurs in February 2027; the amount is unknown until the Board publishes it. | MATCH — guide tax page and property page carry $1,044,586 and mark later windows as not yet published |
| FTB 2025 Form 540 instructions | Line 62 Behavioral Health Services Tax; capital-gain treatment | Line 62: if taxable income is more than $1,000,000, compute the Behavioral Health Services Tax at 1% of the excess over $1,000,000. California taxes capital gains as ordinary income under the graduated schedule; no preferential long-term rate. | MATCH — guide tax page carries 1% BHST above $1,000,000 on line 62 and the 12.30%/13.30% sensitivity |
| Santa Clara County Clerk-Recorder | Documentary transfer tax; PCOR | $0.55 per $500 ($110 per $100,000); additional $20 if a PCOR is required but not submitted at recording. The city triple rate ($1.65/$500) applies to San Jose, Palo Alto and Mountain View only; Cupertino is not named. | MATCH — guide tax page carries these terms and marks the Cupertino city add-on unverified |
| U.S. Treasury Daily Par Yield Curve (Nov 2026) | 3-month and 2-year yields cited as phased-model examples | 11/16/2026: 3 Mo 4.34%, 2 Yr 4.83%. (11/13/2026: 3 Mo 4.32%, 2 Yr 4.88%.) | OBSERVED DRIFT — yields moved slightly versus the 11/13 figures cited as labelled examples in the phased-model text; these are examples, not model inputs, and no model arithmetic uses spot yields |

## Conclusion
No enacted figure changed since the 13–16 Nov 2026 review. The Treasury spot-yield examples drifted by a few basis points; because they are labelled examples (not model inputs), no page or generator change is required and the published recommendation does not move.

## Suite run on the current tree, 17 Nov 2026
- build-guide: no diff (generated pages already current)
- check-generated.py: PASS — 19 pages
- check-figures.py: PASS — 44/44 ledger records
- package-site.py: PASS — 33 reviewed files; legacy site excluded
- check-publication.py --self-test: PASS
- privacy-gate.py: PASS — 254 tracked text files; --self-test PASS
- privacy-audit.cjs: PASS
- test-guide.cjs: PASS — 19 pages / 1,231 source-linked rows / 13,783 checks
- test-model-reference.py: PASS — 20,736 comparisons
- test-phased.py: PASS — 200 checks
- validate.js: PASS — 1,613 checks / 19 pages / 178 official sources
- stress-test.js: PASS — 50-year paths

`test-browser.cjs` cannot launch Chromium in this sandbox (missing `libnss3.so`); it runs in CI.

## Related
- Stale PR #137 (`arena/e3f08d9e-tino2`) is behind `main`; its content is already contained in `main` via PR #138. Closed with this handoff, nothing discarded.
