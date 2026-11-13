
# ---------------------------------------------------------------- discovery register
# Each row: (id, priority, question, why_it_blocks, document_or_source, holder, lead_time, official_link_key, gate)
# The gate marks whether the answer can change the ranking on the comparison page.
DISCOVERY=[
 ('D01','1','What kind of trust is it, who is trustee, and does the instrument give the trustee power to sell the residence?',
  'Selling may not be a decision available to the beneficiary at all. If the trustee must sell, or must keep the property for another beneficiary, the comparison is moot.',
  'The signed trust instrument, every amendment, and the schedule of assets. Ask counsel to confirm the trustee’s powers and any requirement to hold or divide the property in kind.',
  'Settlor, trustee, or the estate-planning attorney who drafted it','Weeks; potentially months if the attorney is unavailable','notice','Ranking-changing'),
 ('D02','1','Is the residence actually titled in the trust, or is it still in individual names with a pour-over will?',
  'Title controls who can convey, and it drives both the basis question and the reassessment question. A trust that names the house but does not hold title can force probate.',
  'A current grant deed and a preliminary title report. A title company will produce the report for a modest fee, and it shows every recorded interest.',
  'County recorder; the trustee; a title company','Days for the recorded deed; one to two weeks for a title report','ownership','Ranking-changing'),
 ('D03','1','Did the decedent retain a power that causes the residence to be included in the gross estate, and therefore to receive a basis step-up?',
  'If basis does not step up, an immediate sale produces a taxable gain that can consume a large share of the proceeds. This single answer can flip sell from first to last.',
  'Trust instrument plus the decedent’s Forms 709 and 706 if any were filed, reviewed by a tax attorney. Rev. Rul. 2023-2 is the IRS example of a grantor-trust pattern that did not receive an adjustment.',
  'Tax counsel; the decedent’s accountant; the trustee’s records','One to three weeks for a written opinion','trustbasis','Ranking-changing'),
 ('D04','1','Was the residence the decedent’s principal residence, and can an eligible child occupy it within one year?',
  'Prop 19 family-home relief requires occupancy by an eligible transferee. Without it the base resets to market value and the annual tax can multiply.',
  'The decedent’s last filed homeowners’ exemption record at the county assessor, plus a documented occupancy plan from the recipient.',
  'Santa Clara County Assessor; the recipient’s own decision','Days for the exemption record; the occupancy plan is a family decision','prop19','Ranking-changing'),
 ('D05','1','What is the complete gross estate, including prior taxable gifts and any spousal exclusion available?',
  'Federal estate tax is assessed on the whole estate, not on this house. Without the total, no headroom exists and no tax can be estimated. Portability must be elected on a timely return.',
  'A confidential estate inventory prepared with counsel: every account, policy, real property, business interest, debt, prior gift and the decedent’s marital history.',
  'Personal representative or trustee; counsel; financial institutions','Two to six weeks, longer if accounts are hard to trace','estate','Ranking-changing'),
 ('D06','1','What is the date-of-death fair market value of the residence?',
  'Basis, reassessment and the estate filing all reference this value. An appraisal prepared for the estate is the defensible record; a later one is not the same number.',
  'A qualified retrospective appraisal as of the date of death, with the comparable sales attached.',
  'Licensed appraiser, engaged by the trustee or counsel','Two to four weeks after engagement','basis','Ranking-changing'),
 ('D07','1','What are the current leases, occupancy and rent-control status of each unit in the San Francisco property?',
  'Existing tenancy and coverage determine lawful rent, notice requirements and whether the owner can occupy a unit at all. The premise of two rents plus a free unit is unverified.',
  'Signed leases, rent history, security deposit records, and the Rent Board’s unit history. Relocation rules apply to some owner move-ins.',
  'The owner’s own files; SF Rent Board records','Days for the owner’s own files; one to two weeks for Rent Board history','sfRent','Ranking-changing'),
 ('D08','2','What are the actual assessed values, tax-rate areas and direct charges on both parcels?',
  'A single blended percentage hides parcel-specific direct charges, bond levies and any special assessments. It also hides the actual assessed value the county uses.',
  'The current secured tax bill for each parcel, showing the rate area and every direct charge as a separate line.',
  'Santa Clara County Tax Collector; SF Treasurer & Tax Collector','Days; both publish online bill lookup','prop13','Ranking-changing'),
 ('D09','2','What would it cost to insure each property, for each occupancy, including or excluding earthquake?',
  'Premium is a real recurring cost and, more importantly, coverage determines whether an earthquake or water loss is a balance-sheet event or an inconvenience.',
  'Binding quotes for a homeowners form on the residence and a landlord form on the multi-unit property, each with and without earthquake coverage, plus a FAIR Plan comparison if the standard market declines.',
  'Licensed brokers; the California FAIR Plan','One to three weeks; longer in a tight market','cdieq','Ranking-changing'),
 ('D10','2','What is the achievable market rent for the residence, and what would professional management cost?',
  'The rent break-even table shows the rental only works above a rent floor. Whether that floor is achievable is the single most important rental input.',
  'Three or more comparable active and recently signed leases within a short radius, plus two management quotes expressed as a percentage of collected rent.',
  'Licensed property managers; public listing data; HUD small-area fair market rents as a floor check only','One week','hud','Ranking-changing'),
 ('D11','2','Will the solar interconnection still produce a credit, and under which tariff?',
  'A credit today is a function of the interconnection date and the applicable tariff. A future true-up, fixed charge or export rate change can turn a small credit into a cost.',
  'The interconnection agreement, the annual true-up statement, and the current tariff sheet.',
  'PG&E; the system owner’s records','Days to weeks','solar','Cost-changing'),
 ('D12','2','What repairs, replacements and capital items are likely in the next ten years?',
  'Roof, foundation, sewer line, electrical panel and seismic retrofit are lumpy costs that a percentage-of-value maintenance assumption cannot capture.',
  'A professional inspection, plus a disclosed list of past permits and any retrofit records. Ask for a reserve study if available.',
  'Licensed inspector; permit records at the city','Two to four weeks','rental','Cost-changing'),
 ('D13','2','What are the recipients’ own income, filing status and other income sources?',
  'Capital-gain rates, passive-loss limits, net investment income tax and bracket effects are personal. A flat rate is a teaching assumption, not a tax computation.',
  'Prior-year returns and a scenario prepared by a CPA, not a public calculator.',
  'The recipients’ own CPA','One to two weeks','rental','Cost-changing'),
 ('D14','3','What is the family’s actual preference about living in the residence?',
  'Living there has real value that this model deliberately omits: imputed rent, proximity, continuity. A financial ranking can be correct and still be the wrong decision.',
  'A documented family discussion of needs, timeline and alternatives, written down before the numbers are shown.',
  'The family','Immediate, but must precede the decision','invest','Preference'),
 ('D15','3','What investment policy will govern the proceeds if the property is sold?',
  'A portfolio return assumption is doing enormous work in every result on this site. Without a written policy, the return is a guess dressed as a plan.',
  'A short written investment policy statement stating target allocation, risk tolerance, liquidity needs and rebalancing rule.',
  'The recipients, with an adviser if desired','One to two weeks','fdic','Preference'),
 ('D16','3','Which specific bills are moving, and what would each do?',
  'Proposed law is not law. A bill that changes family-home transfer rules or repeals the federal estate tax changes the answer, but only once enacted.',
  'The official status page for each bill, checked before the decision, not months earlier.',
  'Congress.gov and the California Legislature, via the links in the register','Ongoing; a few minutes each','hr1301','Watchlist'),
]
DISCOVERY_PRIORITY={
 '1':'<span class="tag">P1</span> Blocks the decision. A different answer can reverse the ranking.',
 '2':'<span class="tag">P2</span> Changes a cost materially but is unlikely to reverse the ranking alone.',
 '3':'<span class="tag">P3</span> Preference, policy or watchlist. Necessary for a real decision, not for the arithmetic.'
}
body='<div class="callout"><strong>This section exists to close the gap between a model and a decision.</strong> The comparison page is arithmetic on invented inputs. A real decision needs the facts below. For each one, this register states the question, why the answer can change the outcome, the specific document or source that answers it, who physically holds that document, and how long it usually takes. <strong>Do not enter any answer on this site.</strong> Keep the completed register offline.</div>'
body+=section('How to read the priority column',table(['Priority','Meaning','How to treat it'],[
 ('P1','Blocks the decision. A different answer can reverse the ranking.','Resolve before comparing strategies seriously. Eight items.'),
 ('P2','Changes a cost materially but is unlikely to reverse the ranking alone.','Resolve before committing capital or signing anything. Six items.'),
 ('P3','Preference, policy or watchlist. Necessary for a real decision, not for the arithmetic.','Resolve as part of the decision, not before the analysis. Three items.'),
 ]))
rows=[]
for (i,p,q,why,doc,who,lead,link,gate) in DISCOVERY:
    rows.append((DISCOVERY_PRIORITY[p],'<strong>'+q+'</strong>',why,doc,who,lead,source(link),gate))
body+=section('Discovery register',table(['Priority','Question','Why it blocks the decision','Document or source that answers it','Who holds it','Typical lead time','Official framework','Gate'],rows))
body+=section('The four facts that decide the ranking','''<p>Most of the register above improves accuracy. Four items can change which strategy wins, and they should be resolved in this order.</p>''')
body+=section('Order of resolution','<div class="grid two">'+''.join(
 '<div class="card"><div class="eyebrow">Step %d</div><h3>%s</h3><p class="muted">%s</p></div>'%(n,t,d)
 for n,t,d in [
  (1,'Does the trust permit a sale?','D01 and D02. If the trustee cannot or must not sell, the rest of the comparison is academic.'),
  (2,'Is there a basis step-up?','D03. An unadjusted basis turns an immediate sale from a low-tax event into a large one, which can lose the sale its first place.'),
  (3,'Is family-home relief available?','D04. Without occupancy, the assessed base resets to market value and the annual property tax roughly multiplies.'),
  (4,'Is the estate over the filing threshold?','D05. If it is, estate tax and liquidity become constraints that no strategy comparison on this site models.')]
)+'</div>')
body+=section('What to do with the answers','table(['If the answer is…','Then…','Because','Official context'],[
 ('The trustee must sell','Stop comparing. The decision is about timing, price and net proceeds.','The comparison assumes a choice that does not exist.','notice'),
 ('No basis step-up','Re-run every sell scenario with a large taxable gain before ranking anything.','The sale strategy loses much of its advantage when the gain is taxed.','trustbasis'),
 ('No family-home relief','Model the residence at full market reassessment, which is what the comparison page’s rent column already does.','The live column understates tax if relief is unavailable.','prop19'),
 ('The estate exceeds the filing threshold','Add a liquidity review before choosing to keep the property.','Estate tax can force a sale regardless of preference.','estate'),
 ('The rent floor is not achievable','Treat renting as a cost-carrying choice, not an income strategy.','The break-even table on the real-conditions page shows the floor.','prop13'),
 ]))
page('questions','What must be answered first?','A register of the facts that are missing, why each one can change the answer, the exact document that resolves it, who holds that document, and how long it takes.',body)
