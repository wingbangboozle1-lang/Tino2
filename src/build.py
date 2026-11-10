"""Builds the static dashboard in ./dashboard from src/model.py and src/data/sources.json.

Rules enforced here:
  * every dollar figure goes through money() -> rounded to the nearest $10;
  * every table row must carry at least one source link (assert in table());
  * no personal identifiers anywhere: placeholders only.
"""
from __future__ import annotations
import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import model as m

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "dashboard")
SRC = {s["id"]: s for s in json.load(open(os.path.join(ROOT, "src", "data", "sources.json")))}
ASOF = "November 10, 2026"
FLAGS: list[tuple[str, str, str, str]] = []   # (area, item, why, link html)

SHORT = {"irs_2027": "IRS IR-2026-133", "irs_rp2635": "Rev. Proc. 2026-35", "irs_estate": "IRS estate tax", "irs_i706": "IRS Form 706 instr.",
         "irs_gifts": "IRS inheritance FAQ", "irs_p551": "IRS Pub. 551", "irs_tc701": "IRS Topic 701", "irs_tc409": "IRS Topic 409",
         "irs_tc559": "IRS Topic 559", "irs_p527": "IRS Pub. 527", "congress_hr1301": "Congress.gov H.R.1301", "cbo": "CBO outlook",
         "tsp": "TSP fund returns", "fred_sj": "FHFA HPI San Jose", "fred_sf": "FHFA HPI San Francisco", "hud_a": "HUD SAFMR 95014",
         "hud_b": "HUD SAFMR 94122", "ftb_cg": "FTB capital gains", "ftb_5805": "FTB rate schedules", "sco": "State Controller",
         "rtc13301": "RTC §13301", "boe_p19": "BOE Prop 19", "lta25009": "BOE LTA 2025/009", "lta26026": "BOE LTA 2026/026",
         "lta26002": "BOE LTA 2026/002", "pub800": "BOE Pub. 800-1", "boe_hoe": "BOE homeowners' exemption", "boe502d": "BOE-502-D",
         "prob16061": "Probate Code §16061.7", "sos_ccrov": "SOS memo 26138", "sos_results": "SOS returns", "vg3": "Voter guide Prop 3",
         "vg40": "Voter guide Prop 40", "vg42": "Voter guide Prop 42", "ab942": "AB 942 status", "cpuc_nem": "CPUC net metering",
         "cdi_study": "CDI reports", "cdi_tool": "CDI premium tool", "sf_tax": "SF Treasurer", "sf_death": "SF.gov after-death guide",
         "sf_transfer": "SF transfer tax", "sf_rent": "SF Rent Board 2026", "sf_rent60": "SF Rent Board rule", "sfpuc": "SFPUC plan",
         "sjw": "San Jose Water", "scc_asr": "SCC Assessor", "scc_ratebook": "SCC Tax Rate Book", "scc_archive": "SCC rate-book archive"}
USED: set[str] = set()


def L(*ids: str) -> str:
    out = []
    for i in ids:
        s = SRC[i]; USED.add(i)
        out.append(f'<a href="{html.escape(s["url"])}" target="_blank" rel="noopener noreferrer">{SHORT[i]}</a>')
    return " · ".join(out)


def money(x) -> str:
    if x is None:
        return "—"
    r = m.r10(x)
    return ("−$" if r < 0 else "$") + f"{abs(r):,}"


def pct(x, d=2) -> str:
    return f"{x * 100:.{d}f}%"


BADGE = {"V": ("v", "Verified"), "E": ("e", "Official · re-check"), "U": ("u", "User-provided"),
         "M": ("m", "Model"), "X": ("x", "Unverified · blank")}


def B(k: str) -> str:
    c, t = BADGE[k]
    return f'<span class="b b-{c}">{t}</span>'


def auto(*ids: str) -> str:
    """Badge from the access status of the cited sources (worst one wins)."""
    acc = [SRC[i]["access"] for i in ids]
    return B("V") if all(a == "opened" for a in acc) else B("E")


def table(head: list[str], rows: list[list[str]], cls: str = "") -> str:
    for r in rows:
        assert len(r) == len(head), (head, r)
        assert "<a " in r[-1], f"row without a source link: {r}"
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tw"><table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def flag(area: str, item: str, why: str, link: str) -> None:
    FLAGS.append((area, item, why, link))


NAV = [("index.html", "Summary"), ("properties.html", "Properties"), ("projections.html", "Projections"),
       ("property-tax.html", "Property tax"), ("decision.html", "Decision"), ("estate-tax.html", "Estate tax"),
       ("process.html", "Trust process"), ("law-watch.html", "Law watch"), ("flagged.html", "Flagged for review"),
       ("sources.html", "Sources")]


def page(fn: str, title: str, lead: str, body: str) -> None:
    nav = "".join(f'<a href="{f}"{" class=on" if f == fn else ""}>{t}</a>' for f, t in NAV)
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title} · Inheritance decision dashboard</title>
<link rel="stylesheet" href="static/style.css"></head>
<body>
<header><div class="wrap"><a class="brand" href="index.html">Inheritance decision dashboard</a>
<span class="tag">Property A · Cupertino 95014 &nbsp;|&nbsp; Property B · San Francisco 94122</span></div>
<nav><div class="wrap">{nav}</div></nav></header>
<main class="wrap">
<h1>{title}</h1><p class="lead">{lead}</p>
{body}
</main>
<footer><div class="wrap"><p>Data as of {ASOF}. All dollar figures are rounded to the nearest $10; statutory amounts are shown as published.
No names, addresses or parcel numbers are used: the people are "Parent", "Trustee" and "Heir".
This is an organized research file, not legal, tax or investment advice; have a California estate attorney and a CPA confirm it before acting.</p>
<p><a href="flagged.html">Flagged for review</a> · <a href="sources.html">Sources</a> · <a href="../index.html">Repository home page (other dashboards)</a></p></div></footer>
</body></html>"""
    with open(os.path.join(OUT, fn), "w") as f:
        f.write(doc)


def legend() -> str:
    return ('<p class="legend">' + B("V") + ' official page opened and read for this file &nbsp; ' + B("E") +
            ' official page, figure seen only in a search excerpt or page not opened: confirm by hand &nbsp; ' + B("U") +
            ' from the project brief, not checked against records &nbsp; ' + B("M") +
            ' calculated from the linked inputs &nbsp; ' + B("X") + ' no official figure found, left blank</p>')


def cards(items) -> str:
    return '<div class="cards">' + "".join(
        f'<div class="card"><div class="k">{k}</div><div class="v">{v}</div><div class="n">{n}</div></div>' for k, v, n in items) + "</div>"


def callout(kind: str, text: str) -> str:
    return f'<div class="call {kind}">{text}</div>'


G = m.GROWTH
SC = [("low", "Low"), ("base", "Base"), ("high", "High")]
RL = [("g", "4.65% (TSP G Fund)"), ("mix", "8.00% (50/50 mix)"), ("c", "11.34% (TSP C Fund)")]
OPT = {"sell": "Sell and reinvest", "rent": "Keep and rent out", "live": "Move in"}

# ------------------------------------------------------------------ numbers reused in prose
be = {(o, Y, s): m.breakeven(o, Y, s) for o in ("rent", "live") for Y in m.INHERIT_YEARS for s, _ in SC}
wins = {k: 0 for k in OPT}
grid = {}
for Y in m.INHERIT_YEARS:
    for s, _ in SC:
        for rk, _ in RL:
            w, d = m.best(Y, s, m.RETURNS[rk]); wins[w] += 1; grid[(Y, s, rk)] = (w, d)
sell_wins_mix = sum(1 for (Y, s, rk), (w, _) in grid.items() if rk in ("mix", "c") and w == "sell")
sell_wins_g = sum(1 for (Y, s, rk), (w, _) in grid.items() if rk == "g" and w == "sell")
be_rent_base = [be[("rent", Y, "base")] for Y in m.INHERIT_YEARS]
be_live_base = [be[("live", Y, "base")] for Y in m.INHERIT_YEARS]
be_all = [v for (o, Y, s), v in be.items() if o == "rent"]
Y0 = 2045
f_rent, f_live = m.option_flows("rent", Y0, "base")[0], m.option_flows("live", Y0, "base")[0]


# ====================================================================== PROPERTIES
def history(rows, key):
    out, prev = [], None
    for y, tax, av in sorted(rows):
        dav = dtax = None; note = []
        if prev:
            dav = av / prev[2] - 1
            if tax and prev[1]:
                dtax = tax / prev[1] - 1
                if tax == prev[1]:
                    note.append("tax identical to prior year")
                elif dtax < 0:
                    note.append("tax fell while assessed value rose")
                elif dtax - dav > 0.05:
                    note.append("tax rose much faster than assessed value")
            if dav < 0.0199:
                note.append("assessed value rose less than 2%")
        if tax is None:
            note.append("tax not supplied")
        for n in note:
            flag("Brief data", f"Property {key}, {y}: {n}",
                 "Rounded brief figures: " + (f"tax {money(tax)}, " if tax else "") + f"assessed value {money(av)}" +
                 (f", change {pct(dav)}" if dav is not None else "") + (f", tax change {pct(dtax, 1)}" if dtax is not None else "") +
                 ". Compare with the county bill for that year.", L("scc_asr") if key == "A" else L("sf_tax"))
        out.append([str(y), money(av), pct(dav) if dav is not None else "—", money(tax), pct(dtax, 1) if dtax is not None else "—",
                    pct(tax / av) if tax else "—", "; ".join(note) or "—", B("U"), L("scc_asr") if key == "A" else L("sf_tax")])
        prev = (y, tax, av)
    return out[::-1]


def build_properties():
    head = ["Item", "Property A · Cupertino 95014", "Property B · San Francisco 94122", "Status", "Source / where to confirm"]
    rows = [
        ["Estimated market value, Nov 2026", money(m.A["fmv"]), money(m.B["fmv"]), B("U"), L("scc_asr", "sf_tax")],
        ["Latest assessed value in the brief", money(m.A["av_2026"]) + " (2026)", money(m.B["av_2025"]) + " (2025)", B("U"), L("scc_asr", "sf_tax")],
        ["Latest property tax bill in the brief", money(m.A["tax_2025"]) + " (2025)", money(m.B["tax_2025"]) + " (2025)", B("U"), L("scc_asr", "sf_tax")],
        ["Assessed value as a share of market value", pct(m.A["av_2026"] / m.A["fmv"], 1), pct(m.B["av_2025"] / m.B["fmv"], 1), B("M"), L("boe_p19")],
        ["Use today", "Single home, solar", "3 units: 2 rented, 1 available to the family", B("U"), L("lta26026")],
        ["Rent collected", "—", money(m.B["rent_mo"]) + " / month (2 units)", B("U"), L("sf_rent60")],
        ["Water", f"{money(m.A['water_mo'][0])}–{money(m.A['water_mo'][1])} / month", f"{money(m.B['water_mo'][0])}–{money(m.B['water_mo'][1])} / month (3 units)", B("U"), L("sjw", "sfpuc")],
        ["Electricity", f"credit of {money(-m.A['elec_mo'][1])}–{money(-m.A['elec_mo'][0])} / month (solar)", f"{money(m.B['elec_mo'][0])}–{money(m.B['elec_mo'][1])} / month", B("U"), L("cpuc_nem")],
        ["Insurance, owner's estimate", money(m.A["insurance"]) + " / year", money(m.B["insurance"]) + " / year", B("U"), L("cdi_tool")],
        ["Insurance, official premium for the ZIP", "", "", B("X"), L("cdi_tool", "cdi_study")],
        ["Repairs and maintenance records", "", "", B("X"), L("irs_p527")],
        ["Benchmark market rent (HUD FY2026)", f"{money(m.SAFMR['A_3br'])} (3 bedrooms) · {money(m.SAFMR['A_4br'])} (4 bedrooms) / month", f"{money(m.SAFMR['B_2br'])} (2 bedrooms) / month", B("V"), L("hud_a", "hud_b")],
    ]
    flag("Insurance", "No official premium for either ZIP", "The Department of Insurance comparison tool is form-driven and returned no figure. The owner's estimate is used and grown with inflation; get real quotes (primary-residence policy for A, landlord policy for B).", L("cdi_tool"))
    flag("Maintenance", "No repair history and no official benchmark", f"Placeholders of {money(m.PLACEHOLDER['maint_A'])} (A) and {money(m.PLACEHOLDER['maint_B'])} (B) per year in 2026 dollars are used only so the totals are not understated. Replace with real records.", L("irs_p527"))
    flag("Rent", "Bedroom count of Property A is unknown", "The 4-bedroom HUD benchmark is used for the rent option; the 3-bedroom figure is shown as a sensitivity. HUD FY2027 figures were not reachable, FY2026 is used.", L("hud_a"))
    flag("Utilities", "Water provider for Property A not confirmed", "San Jose Water's increase is quoted only as an example; the bill itself names the provider.", L("sjw"))
    ha, hb = history(m.A_HISTORY, "A"), history(m.B_HISTORY, "B")
    hh = ["Year", "Assessed value", "Change", "Property tax", "Change", "Tax ÷ assessed value", "Check", "Status", "Where to confirm"]
    body = legend() + callout("warn", "<b>Privacy.</b> Figures come from the project brief and are rounded to the nearest $10. No parcel was looked up and no name, address or parcel number is stored. A multi-year assessed-value history together with a ZIP code can still be matched to public county records by a determined reader; see <a href='flagged.html'>Flagged for review</a>.") + \
        "<h2>Inputs side by side</h2>" + table(head, rows) + \
        "<h2>Property A: tax and assessment history</h2><p>Assessed value rose by no more than 2% in every year, the Proposition 13 pattern for a property that has not changed hands (" + L("lta26002") + "). The property tax bill is larger than rate × assessed value because bills also carry fixed charges.</p>" + table(hh, ha) + \
        "<h2>Property B: tax and assessment history</h2>" + table(hh, hb)
    page("properties.html", "The two properties", "What the brief says about each home, with every line labelled by how far it has been confirmed.", body)


# ====================================================================== PROJECTIONS
def build_projections():
    ha = ["Year", "Value low", "Value base", "Value high", "Assessed value", "Property tax", "Insurance", "Water", "Electricity", "Maintenance", "Total yearly cost", "Inputs"]
    ra = []
    for y in m.YEARS:
        c = m.costs_A(y); t = m.tax_current_owner("A", y)
        ra.append([str(y)] + [money(m.fmv("A", y, s)) for s, _ in SC] + [money(m.fbyv("A", y)), money(t), money(c["insurance"]), money(c["water"]),
                   money(c["electricity"]), money(c["maintenance"]), money(t + sum(c.values())), L("fred_sj", "lta26002", "scc_ratebook", "cbo")])
    hb = ["Year", "Value low", "Value base", "Value high", "Assessed value", "Property tax", "Insurance", "Water", "Electricity", "Maintenance", "Rent, 2 units", "Net income", "Inputs"]
    rb = []
    for y in m.YEARS:
        c = m.costs_B(y); t = m.tax_current_owner("B", y)
        rb.append([str(y)] + [money(m.fmv("B", y, s)) for s, _ in SC] + [money(m.fbyv("B", y)), money(t), money(c["insurance"]), money(c["water"]),
                   money(c["electricity"]), money(c["maintenance"]), money(m.rent_B(y)), money(m.noi_B(y)), L("fred_sf", "sf_tax", "sf_rent60", "cbo")])
    assum = [
        ["Home value growth, Property A", f"low {pct(G['A']['low'])} · base {pct(G['A']['base'])} · high {pct(G['A']['high'])} a year", "Annualized change in the FHFA index for the San Jose metro over the last 20 / 10 / 30 years (Q2 to Q2)", B("M"), L("fred_sj")],
        ["Home value growth, Property B", f"low {pct(G['B']['low'])} · base {pct(G['B']['base'])} · high {pct(G['B']['high'])} a year", "Same method, San Francisco metro division index", B("M"), L("fred_sf")],
        ["Assessed value growth while the owner is unchanged", "2.00% a year", "The maximum factor; the 2026-27 factor is 1.02. Any year with inflation under 2% would be lower", auto("lta26002"), L("lta26002")],
        ["Tax rate on assessed value, Property A", pct(m.RATE_A, 4), "Sum of the FY2025-26 county-wide 1% levy and the bond rates for the Cupertino-area districts", B("E"), L("scc_ratebook", "scc_archive")],
        ["Tax rate on assessed value, Property B", pct(m.RATE_B, 4), "FY2026-27 secured rate", auto("sf_tax"), L("sf_tax")],
        ["Fixed charges on the bill", f"A {money(m.FIXED_A_2025)} · B {money(m.FIXED_B_2025)} (2025)", "2025 bill minus rate × assessed value; grown with inflation", B("M"), L("scc_ratebook", "sf_tax")],
        ["Inflation for costs and market rent", pct(m.CPI, 1) + " a year", "CBO long-run CPI-U projection", auto("cbo"), L("cbo")],
        ["Rent growth for sitting tenants in Property B", pct(m.SF_RENT_SHARE_OF_CPI * m.CPI), "60% of inflation, the San Francisco Rent Board formula", auto("sf_rent60"), L("sf_rent60")],
        ["Electricity, Property A", money(m.costs_A(2026)["electricity"]) + " a year, held flat", "Solar credit from the brief; no escalation assumed", B("U"), L("cpuc_nem")],
        ["Maintenance", f"A {money(m.PLACEHOLDER['maint_A'])} · B {money(m.PLACEHOLDER['maint_B'])} a year in 2026 dollars", "Placeholder, not from any source", B("X"), L("irs_p527")],
    ]
    flag("Property tax", "Cupertino-area tax rate", f"{pct(m.RATE_A, 4)} is a sum of FY2025-26 component rates from the summary pages of the county rate book. The exact tax-rate area of the parcel is unknown and the FY2026-27 book was not posted. The rate on the actual bill governs.", L("scc_ratebook", "scc_archive"))
    flag("Property tax", "Fixed charges are derived, not read from a bill", "Computed as bill minus rate × assessed value from rounded brief figures. The itemized bill lists the real charges.", L("sf_tax", "scc_ratebook"))
    flag("Utilities", "Water grown at general inflation", "The San Francisco utility's published plan shows +7.0% water and +15.0% wastewater for the year ending June 2027, well above inflation; long-run water costs here are probably understated.", L("sfpuc"))
    flag("Utilities", "Solar credit after the legacy net-metering period", "Net-metering 2.0 customers keep the tariff for 20 years from interconnection. The interconnection date is unknown, so the credit is held flat in the yearly table and set to $0 in the decision model.", L("cpuc_nem"))
    flag("Projections", "Home-value scenarios are history, not forecasts", "Low, base and high are the 20-, 10- and 30-year annualized changes in a metro-wide index. A single house can differ widely.", L("fred_sj", "fred_sf"))
    body = legend() + "<h2>Assumptions behind every row</h2>" + table(["Assumption", "Value", "Basis", "Status", "Source"], assum) + \
        "<h2>Property A · Cupertino 95014, year by year</h2><p>Costs as they would be for the <b>current owner</b>, with no change of ownership. What happens to the tax at inheritance is on the <a href='property-tax.html'>property tax page</a>. Negative electricity is a credit.</p>" + table(ha, ra, "num") + \
        "<h2>Property B · San Francisco 94122, year by year</h2><p>Net income = rent from two units minus property tax, insurance, water, electricity and maintenance, before income tax, for the current owner.</p>" + table(hb, rb, "num")
    page("projections.html", "Year-by-year projections, 2026–2050", "House value, assessed value, property tax, insurance, water, electricity and maintenance for each year, under stated assumptions.", body)


# ====================================================================== PROPERTY TAX
def build_ptax():
    rules = [
        ["Annual increase while ownership is unchanged", "Assessed value rises by an inflation factor capped at 2%; the 2026-27 factor is 1.02", auto("lta26002"), L("lta26002")],
        ["Inheritance is a change in ownership", "Since Feb 16, 2021 a parent-to-child transfer is reassessed to market value unless the family-home exclusion applies", auto("boe_p19"), L("boe_p19")],
        ["Family-home exclusion: who", "The home must be the parent's principal residence and become the child's principal residence within one year of the transfer", auto("lta26026"), L("lta26026", "scc_asr")],
        ["Family-home exclusion: how much", "If market value is at most the old assessed value + $1,044,586, the old assessed value continues. If it is more, the excess is added to the old assessed value", auto("lta25009"), L("lta25009")],
        ["The $1,044,586 amount", "Applies Feb 16, 2025 to Feb 15, 2027; adjusted every second Feb 16 by a California house-price index", auto("lta25009"), L("lta25009")],
        ["Moving out later", "The exclusion ends and the home is reassessed when it stops being the child's principal residence", auto("lta26026"), L("lta26026")],
        ["Multi-unit property", "Only the unit that was the parent's principal residence can qualify", auto("lta26026"), L("lta26026")],
        ["Claim forms", "Homeowners' exemption (BOE-266) within 1 year; exclusion claim (BOE-19-P) within 3 years", B("E"), L("pub800", "sf_death", "lta26026")],
        ["Homeowners' exemption", "$7,000 off assessed value for an owner-occupied principal residence", auto("boe_hoe"), L("boe_hoe")],
    ]
    head = ["If inherited in", "Scenario", "Market value", "Old assessed value", "Exclusion amount (projected)", "Taxable value if Heir moves in", "Tax if Heir moves in", "Tax if rented or kept empty", "Tax under current owner", "Inputs"]
    rows = []
    for y in (2026, 2030, 2035, 2040, 2045, 2050):
        for s, sl in (SC if y in m.INHERIT_YEARS else [("base", "Base")]):
            rows.append([str(y), sl, money(m.fmv("A", y, s)), money(m.fbyv("A", y)), money(m.prop19_amount(y, s)), money(m.prop19_taxable(y, s)),
                         money(m.tax_A_live(y, s)), money(m.tax_full("A", y, s)), money(m.tax_current_owner("A", y)), L("lta25009", "fred_sj", "scc_ratebook")])
    rb = [[str(y), money(m.fmv("B", y)), money(m.fbyv("B", y)), money(m.tax_current_owner("B", y)), money(m.tax_full("B", y)),
           money(m.tax_full("B", y) - m.tax_current_owner("B", y)), L("lta26026", "sf_tax", "fred_sf")] for y in (2026, 2040, 2045, 2050)]
    flag("Property tax", "Future exclusion amount is a projection", "The amount after Feb 15, 2027 is not published. The model raises it every second year by one year of the scenario growth rate, which mirrors how the last two adjustments worked; the Board of Equalization figure will differ.", L("lta25009"))
    flag("Property tax", "Which home is the Parent's principal residence", "The family-home exclusion can only apply to the Parent's principal residence. The tables assume that is Property A. If it is a unit of Property B instead, Property A is fully reassessed whatever the Heir does.", L("lta26026"))
    flag("Property tax", "Whether Property B is in the same inheritance", "The brief does not say. A separate table shows the tax if Property B is also inherited and fully reassessed.", L("lta26026"))
    y = 2040
    body = legend() + cards([
        ("Tax today (2025 bill)", money(m.A["tax_2025"]), "Property A, current owner"),
        (f"Inherited {y}, Heir moves in", money(m.tax_A_live(y)), "a year, base scenario"),
        (f"Inherited {y}, rented or empty", money(m.tax_full("A", y)), "a year, base scenario"),
        ("Exclusion amount today", "$1,044,586", "through Feb 15, 2027"),
    ]) + "<h2>The rules</h2>" + table(["Rule", "What it says", "Status", "Source"], rules) + \
        f"<h2>Property A: the tax bill after inheritance</h2><p>The low assessed value does not pass to the Heir intact. Because the house is worth far more than the old assessed value plus the exclusion amount, moving in only takes about {money(m.prop19_amount(y))} off the taxable value in {y}; not moving in means tax on the full market value. Worked example at today's values: {money(m.A['fmv'])} − $1,044,586 = {money(m.prop19_taxable(2026))} taxable if the Heir moves in, against {money(m.A['av_2026'])} now.</p>" + table(head, rows, "num") + \
        "<h2>Property B: if it is inherited too</h2><p>With two rented units and no Parent living there, the exclusion would not apply and the whole building would be reassessed.</p>" + \
        table(["If inherited in", "Market value (base)", "Old assessed value", "Tax under current owner", "Tax after full reassessment", "Increase per year", "Inputs"], rb, "num")
    page("property-tax.html", "Property tax and Proposition 19", "How the tax bill changes the day the house is inherited, and what moving in does and does not save.", body)


# ====================================================================== DECISION
def build_decision():
    opts = [
        ["Sell and reinvest", "Sale soon after death is at or near the stepped-up basis, so little or no capital gain", "None after sale", "Investment returns", auto("irs_gifts"), L("irs_gifts", "irs_tc409")],
        ["Keep and rent out", "Rent is taxable income; 3.8% net investment income tax can apply", "Reassessed to full market value", "Market rent on Property A", B("V"), L("boe_p19", "irs_tc559", "hud_a")],
        ["Move in", "Up to $250,000 / $500,000 of later gain can be excluded after owning and living there 2 of 5 years", "Market value minus the exclusion amount, if moved in within 1 year", "Rent on the unit vacated in Property B", B("V"), L("lta26026", "irs_tc701", "hud_b")],
        ["Keep empty", "No income", "Reassessed to full market value", f"None; costs about {money(m.tax_full('A', Y0) + m.infl(m.A['insurance'], Y0) + m.infl(m.PLACEHOLDER['maint_A'], Y0))} a year from {Y0}", B("M"), L("boe_p19")],
    ]
    cf = []
    for Y in m.INHERIT_YEARS:
        for o in ("rent", "live"):
            f = m.option_flows(o, Y, "base")[0]
            cf.append([str(Y), OPT[o], money(m.fmv("A", Y)), money(f["income"]), money(f["tax"]), money(f["insurance"]), money(f["maintenance"]),
                       money(f["utilities"]), money(f["net"]), pct(f["net"] / m.fmv("A", Y)), L("hud_a" if o == "rent" else "hud_b", "lta25009", "scc_ratebook")])
    bt = []
    for Y in m.INHERIT_YEARS:
        for s, sl in SC:
            bt.append([str(Y), f"{sl} ({pct(G['A'][s])})", money(m.fmv("A", Y, s) * (1 - m.PLACEHOLDER["sell_cost"])), pct(be[("rent", Y, s)]), pct(be[("live", Y, s)]), L("fred_sj", "tsp")])
    wt = []
    for Y in m.INHERIT_YEARS:
        for s, sl in SC:
            for rk, rl in RL:
                w, d = grid[(Y, s, rk)]
                wt.append([str(Y), sl, rl, money(d["sell"]), money(d["rent"]), money(d["live"]), f"<b>{OPT[w]}</b>", L("tsp", "fred_sj", "hud_a")])
    # sensitivity
    sens = []
    def with_(name, val, fn):
        d = m.PLACEHOLDER if name in m.PLACEHOLDER else m.SAFMR
        old = d[name]; d[name] = val
        try:
            return fn()
        finally:
            d[name] = old
    base_be = m.breakeven("rent", Y0, "base")
    for lab, name, vals, fmt, src in [
        ("Maintenance, Property A (per year, 2026 dollars)", "maint_A", [0, m.PLACEHOLDER["maint_A"], 2 * m.PLACEHOLDER["maint_A"]], money, L("irs_p527")),
        ("Selling costs (share of price)", "sell_cost", [0.04, 0.06, 0.08], lambda v: pct(v, 0), L("sf_transfer")),
        ("Market rent, Property A (per month)", "A_4br", [m.SAFMR["A_3br"], m.SAFMR["A_4br"], round(m.SAFMR["A_4br"] * 1.25 / 10) * 10], money, L("hud_a")),
    ]:
        for v in vals:
            sens.append([lab, fmt(v), pct(with_(name, v, lambda: m.breakeven("rent", Y0, "base"))), pct(with_(name, v, lambda: m.breakeven("live", Y0, "base"))), src])
    comp = []
    for Y in m.INHERIT_YEARS:
        a = m.total_return("A", Y); b1 = m.total_return("B", Y, reassessed=False); b2 = m.total_return("B", Y, reassessed=True)
        comp.append([str(Y), "A, rented (reassessed)", money(a["value"]), money(a["net"]), pct(a["yield_"]), pct(a["growth"]), pct(a["total"]), L("hud_a", "fred_sj")])
        comp.append([str(Y), "B, not inherited yet (old tax base)", money(b1["value"]), money(b1["net"]), pct(b1["yield_"]), pct(b1["growth"]), pct(b1["total"]), L("sf_tax", "fred_sf")])
        comp.append([str(Y), "B, inherited and reassessed", money(b2["value"]), money(b2["net"]), pct(b2["yield_"]), pct(b2["growth"]), pct(b2["total"]), L("sf_tax", "fred_sf")])
    taxes = [
        ["Basis of an inherited house", "Fair market value at the date of death (or alternate valuation date)", auto("irs_gifts"), L("irs_gifts")],
        ["Federal long-term capital gain rates", "0%, 15% or 20% depending on taxable income", auto("irs_tc409"), L("irs_tc409")],
        ["Depreciation taken while rented", "Taxed at up to 25% on sale (unrecaptured section 1250 gain)", auto("irs_tc409"), L("irs_tc409")],
        ["Net investment income tax", "3.8% on rents and gains above $200,000 (single) or $250,000 (joint) of modified adjusted gross income", auto("irs_tc559"), L("irs_tc559")],
        ["Home-sale exclusion", "$250,000 single / $500,000 joint if owned and lived in 2 of the last 5 years", auto("irs_tc701"), L("irs_tc701")],
        ["Community property held by spouses", "When one spouse dies, the whole property can take a new basis if at least half is included in that spouse's estate", B("E"), L("irs_p551")],
        ["California tax on gains", "Taxed as ordinary income, plus 1% on taxable income over $1,000,000", B("E"), L("ftb_cg", "ftb_5805")],
        ["California top income tax rate", "", B("X"), L("ftb_5805")],
        ["Whether California follows the federal step-up in basis", "", B("X"), L("ftb_cg")],
        ["Depreciation period for a rental house", "", B("X"), L("irs_p527")],
        ["Transfer tax when selling Property B", "0.75% of the full price for a sale of $1,000,000 to under $5,000,000", B("E"), L("sf_transfer")],
        ["Transfer tax when selling Property A", "", B("X"), L("scc_asr")],
        ["Agent commission, escrow and title costs", "", B("X"), L("sf_transfer")],
    ]
    flag("Decision model", "Selling costs of 6% are a placeholder", "No official figure exists for agent fees, escrow and title; the county transfer tax for Property A was not confirmed from an official page. Sensitivity at 4% and 8% is shown.", L("sf_transfer"))
    flag("Decision model", "Results are before income tax", "The Heir's filing status, bracket and other income are unknown. Rent, dividends and interest are all taxable; rental depreciation was not modeled because the official publication was not opened.", L("irs_p527", "irs_tc559"))
    flag("Decision model", "Reinvestment returns are past returns", "4.65% and 11.34% are the since-inception annual returns of the federal Thrift Savings Plan's government-securities and S&P 500 index funds to Dec 31, 2025. The 8.00% line is simply the midpoint, a modeling choice. None is a forecast.", L("tsp"))
    flag("Decision model", "California tax items left blank", "Top state rate, state treatment of stepped-up basis and the rental depreciation period were not confirmed from an official page.", L("ftb_cg", "irs_p527"))
    flag("Decision model", "Keeping the house is not charged a future selling cost", "The 10-year comparison counts the kept house at full market value. This favors keeping, so the case for selling is, if anything, understated.", L("fred_sj"))
    lo, hi = min(be_rent_base), max(be_rent_base)
    body = legend() + cards([
        ("Break-even return, keep and rent", f"{pct(lo, 1)}–{pct(hi, 1)}", "base scenario: selling wins if reinvested money earns more than this"),
        ("Break-even return, move in", f"{pct(min(be_live_base), 1)}–{pct(max(be_live_base), 1)}", "base scenario"),
        (f"Net rent on Property A, {Y0}", money(f_rent["net"]), f"a year, {pct(f_rent['net'] / m.fmv('A', Y0))} of its value"),
        ("Selling comes out ahead in", f"{wins['sell']} of {len(grid)}", "combinations of year, growth and return"),
    ]) + f"""
<h2>Recommendation</h2>
<div class="call good"><p><b>Sell Property A within about a year of inheriting it, reinvest the proceeds in a diversified mix, and keep Property B as the family home and income property.</b></p>
<ol>
<li><b>The tax reset makes the day of inheritance the cheapest day to sell.</b> The Heir's basis becomes the market value at death, so a prompt sale leaves little or no capital gain to tax.</li>
<li><b>The low property tax does not survive.</b> In {Y0} (base scenario) the bill goes from about {money(m.tax_current_owner('A', Y0))} to {money(m.tax_full('A', Y0))} a year if rented, or {money(m.tax_A_live(Y0))} if the Heir moves in.</li>
<li><b>As a rental, Property A earns very little on its value.</b> Benchmark rent of {money(f_rent['income'])} less tax, insurance and upkeep leaves about {money(f_rent['net'])} a year, {pct(f_rent['net'] / m.fmv('A', Y0))} of a {money(m.fmv('A', Y0))} asset. Nearly all its return would have to come from price growth.</li>
<li><b>Selling wins unless the money is parked in savings.</b> With the mixed or stock-index return, selling is ahead in {sell_wins_mix} of 18 cases. At the 4.65% government-securities return it is ahead in only {sell_wins_g} of 9, the low-growth ones.</li>
<li><b>Property B already covers housing and income.</b> It houses the family in the third unit and collects {money(m.rent_B(Y0))} a year by {Y0}; holding both homes would leave almost everything in Bay Area real estate.</li>
</ol>
<p><b>When the answer changes.</b> Keep and rent if the proceeds would only go into savings or Treasury-type holdings earning less than about {pct(lo, 1)}–{pct(hi, 1)}, or if you expect Cupertino prices to keep rising near {pct(G['A']['high'], 1)} a year (break-even then rises to {pct(max(be_all), 1)}). Moving in is the weakest choice on money alone: in {Y0} it leaves the family about {money(f_rent['net'] - f_live['net'])} a year worse off than renting Property A out, so it only makes sense if living there is worth that much to the family.</p></div>
<h2>The four options</h2>""" + table(["Option", "Income tax position", "Property tax after inheritance", "Income", "Status", "Source"], opts) + \
        "<h2>First-year cash flow of keeping Property A</h2><p>Base growth scenario. For <i>move in</i>, income is the market rent on the Property B unit the family would vacate, since the family's own housing is covered either way.</p>" + \
        table(["Inherited in", "Option", "Market value", "Income", "Property tax", "Insurance", "Maintenance", "Water", "Net per year", "Net ÷ value", "Inputs"], cf, "num") + \
        f"<h2>Break-even reinvestment return</h2><p>The yearly return the sale proceeds must earn, over {m.HORIZON} years, for selling to tie with keeping. Above it, selling wins.</p>" + \
        table(["Inherited in", "Home-value growth", "Sale proceeds after 6% costs", "Break-even vs. renting", "Break-even vs. moving in", "Inputs"], bt, "num") + \
        f"<h2>Wealth after {m.HORIZON} years, all 27 combinations</h2><p>Sell: proceeds compounded at the return shown. Keep: house value after {m.HORIZON} years plus each year's net cash reinvested at the same return (a negative net is money the family pays in). Before income tax.</p>" + \
        table(["Inherited in", "Growth", "Reinvestment return", "Sell and reinvest", "Keep and rent out", "Move in", "Highest", "Inputs"], wt, "num") + \
        f"<h2>How sensitive is the answer?</h2><p>Break-even for inheritance in {Y0}, base growth ({pct(base_be)} with the standard inputs), changing one unconfirmed input at a time.</p>" + \
        table(["Input changed", "Value", "Break-even vs. renting", "Break-even vs. moving in", "Related source"], sens, "num") + \
        "<h2>Property A and Property B as investments</h2><p>First-year net income as a share of value, plus the scenario's price growth. Property B also houses the family, which is not counted.</p>" + \
        table(["Year", "Property", "Value (base)", "Net income", "Income yield", "Price growth", "Total", "Inputs"], comp, "num") + \
        "<h2>Tax rules that apply to each choice</h2>" + table(["Rule", "What it says", "Status", "Source"], taxes)
    page("decision.html", "Live in, rent, or sell?", "The numbers behind the choice for Property A, with Property B kept in view.", body)


# ====================================================================== ESTATE TAX
def build_estate():
    lv = [
        ["Federal", "Basic exclusion, deaths in 2026", "$15,000,000 per person", auto("irs_estate"), L("irs_estate")],
        ["Federal", "Basic exclusion, deaths in 2027", "$15,480,000 per person", auto("irs_2027"), L("irs_2027", "irs_rp2635")],
        ["Federal", "Tax rate on the amount above the exclusion", "40% top rate", B("E"), L("irs_i706")],
        ["Federal", "Unused exclusion of a spouse who died first", "Can be carried to the surviving spouse only if an estate tax return is filed on time for the first death", auto("irs_estate"), L("irs_estate")],
        ["Federal", "Return due", "9 months after the date of death", B("E"), L("irs_i706")],
        ["Federal", "Gifts that use none of the exclusion", "$19,000 per recipient in 2026; $20,000 in 2027", auto("irs_2027"), L("irs_2027")],
        ["Federal", "Tax paid by the Heir on receiving an inheritance", "None: an inheritance is not income to the recipient; later income from it is taxable", auto("irs_gifts"), L("irs_gifts")],
        ["Federal", "Whether the current exclusion level is permanent law", "", B("X"), L("irs_estate")],
        ["California", "Estate tax", "None for deaths on or after Jan 1, 2005", auto("sco"), L("sco")],
        ["California", "Inheritance and gift tax", "None; barred by statute", auto("rtc13301"), L("rtc13301")],
        ["Santa Clara County / Cupertino", "Local inheritance or estate tax", "None; the same statute should be read for its wording on local governments", B("E"), L("rtc13301")],
        ["San Francisco", "Local inheritance or estate tax", "None; same statute", B("E"), L("rtc13301")],
    ]
    hr = []
    for y in (2026, 2027, 2030, 2035, 2040, 2045, 2050):
        ex = m.estate_exclusion(y); a, b = m.fmv("A", y), m.fmv("B", y)
        hr.append([str(y), money(ex), money(a), money(b), money(ex - a), money(ex - a - b), money(2 * ex - a - b),
                   (B("V") if y <= 2027 else B("M")), L("irs_estate", "irs_2027", "cbo", "fred_sj")])
    hs = []
    for y in m.INHERIT_YEARS:
        ex = m.estate_exclusion(y)
        for s, sl in SC:
            a, b = m.fmv("A", y, s), m.fmv("B", y, s)
            hs.append([str(y), sl, money(a + b), money(ex - a - b), money(max(0, a + b - ex) * m.ESTATE_RATE), money(2 * ex - a - b), L("irs_i706", "fred_sj", "fred_sf")])
    flag("Estate tax", "Size of the cash and investments in the estate is unknown", "The tables show room left under the exclusion instead of a tax bill. Subtract the estate's other assets (cash, investments, retirement accounts, life insurance owned by the Parent) from the room shown.", L("irs_estate"))
    flag("Estate tax", "Exclusion after 2027 is a projection", f"Grown at {pct(m.CPI, 1)} a year and rounded to $10,000. The law indexes it with a different inflation measure, and Congress can change it.", L("irs_2027", "cbo"))
    flag("Estate tax", "Permanence of the current exclusion", "Described as permanent by non-government sources only; the IRS page that would confirm the wording was not opened.", L("irs_estate"))
    flag("Estate tax", "40% rate and 9-month deadline seen in excerpt only", "Both come from the IRS Form 706 instructions as shown in search excerpts; open the instructions to confirm.", L("irs_i706"))
    flag("Estate tax", "Local-government wording of the statute", "The section was opened, but the exact wording covering counties and cities should be re-read before relying on it.", L("rtc13301"))
    all_under = all(m.fmv("A", yy, s) + m.fmv("B", yy, s) < m.estate_exclusion(yy) for yy in m.INHERIT_YEARS for s, _ in SC)
    y = 2045; ex = m.estate_exclusion(y)
    body = legend() + cards([
        ("Federal exclusion, 2026", "$15,000,000", "per person"),
        ("Federal exclusion, 2027", "$15,480,000", "per person"),
        ("California estate / inheritance tax", "$0", "no state or local tax"),
        (f"Room for other assets, {y}", money(ex - m.fmv("A", y) - m.fmv("B", y)), "one exclusion, after both homes, base scenario"),
    ]) + "<h2>Thresholds at each level of government</h2>" + table(["Level", "Item", "Amount or rule", "Status", "Source"], lv) + \
        f"""<h2>How much room is left before any estate tax</h2>
<p>Room = exclusion − market value of the home(s). Whatever cash and investments the estate also holds must fit in that room; each $1,000,000 above it would cost about {money(1_000_000 * m.ESTATE_RATE)} in federal tax. "Two exclusions" applies when a spouse died earlier and the unused exclusion was claimed on a timely return.</p>""" + \
        table(["Year of death", "Exclusion per person", "Property A (base)", "Property B (base)", "Room after A only", "Room after A + B", "Room after A + B, two exclusions", "Exclusion figure", "Inputs"], hr, "num") + \
        "<h2>Same test under low, base and high home values</h2>" + \
        table(["Year", "Scenario", "A + B value", "Room, one exclusion", "Tax on the homes alone", "Room, two exclusions", "Inputs"], hs, "num") + \
        "<h2>Reading the result</h2><ul><li>" + ("The two homes alone stay under one person's exclusion in every scenario shown, so the homes by themselves do not trigger federal estate tax." if all_under else "In at least one scenario the two homes alone exceed one person's exclusion; see the table.") + "</li>" + \
        f"<li>In the base scenario for {y}, other assets above about {money(ex - m.fmv('A', y) - m.fmv('B', y))} (one exclusion) would be taxed at the top rate.</li>" + \
        "<li>Home values in the base and high scenarios grow faster than the exclusion is projected to, so the room shrinks over time as a share of the estate.</li>" + \
        "<li>Ways people stay under the line, all for an estate attorney to assess: annual gifts within the per-recipient amount, filing a return at the first spouse's death to preserve the unused exclusion, and charitable bequests.</li></ul>"
    page("estate-tax.html", "Estate tax thresholds and headroom", "What can pass tax-free at the federal, state and local level, and how much room the two homes leave for cash and investments.", body)


# ====================================================================== PROCESS
def build_process():
    steps = [
        ["1", "Now, while the Parent is living", "Confirm which home is the Parent's principal residence and that the trust holds title; keep solar interconnection papers, repair records and the trust document where the successor Trustee can find them", "The exclusion and the legacy solar tariff both depend on these facts", B("V"), L("lta26026", "cpuc_nem")],
        ["2", "At death", "Get a professional appraisal of each property as of the date of death", "That value becomes the Heir's basis for any later sale", auto("irs_gifts"), L("irs_gifts")],
        ["3", "Within 60 days", "Trustee sends the required notice to heirs and beneficiaries", "Starts the 120-day period to contest the trust", B("E"), L("prob16061")],
        ["4", "Within 150 days", "File the change-in-ownership statement for a deceased owner (BOE-502-D) with each county assessor", "Reports the transfer; triggers reassessment review", B("E"), L("boe502d")],
        ["5", "Within 9 months", "File the federal estate tax return if the estate exceeds the filing threshold, or to preserve a spouse's unused exclusion", "Tax, if any, is due with it", B("E"), L("irs_estate", "irs_i706")],
        ["6", "Within the first months", "Decide: sell, rent or move in (see Decision page)", "A sale close to the date-of-death value leaves little gain to tax", B("M"), L("irs_gifts")],
        ["7a", "If moving in: within 1 year", "Make the home the Heir's principal residence and file the homeowners' exemption claim (BOE-266)", "Required for the family-home exclusion; there are no exceptions to the one-year rule", B("E"), L("lta26026", "pub800")],
        ["7b", "If moving in: within 3 years", "File the parent-child exclusion claim (BOE-19-P)", "Applies the exclusion from the date of death", B("E"), L("lta26026", "pub800", "scc_asr")],
        ["7c", "If selling", "Trustee or Heir sells; report the sale using the date-of-death basis", "Gain is only the change since death", auto("irs_gifts", "irs_tc409"), L("irs_gifts", "irs_tc409")],
        ["7d", "If renting Property A", "Report rent as income; expect reassessment to market value", "Net investment income tax may apply", auto("irs_tc559"), L("irs_tc559", "boe_p19")],
        ["8", "Property B, ongoing", "Rent increases for sitting tenants follow the Rent Board's yearly figure (1.6% for Mar 2026 to Feb 2027)", "Limits rent growth to 60% of inflation", B("E"), L("sf_rent", "sf_rent60")],
        ["9", "Trust income tax return and tax ID number", "", "Not confirmed from an official page", B("X"), L("irs_estate")],
        ["10", "Property tax due dates and supplemental bills after reassessment", "", "Not confirmed from an official page", B("X"), L("sf_tax")],
    ]
    flag("Process", "Trust-administration deadlines seen in excerpts only", "The 60-day notice, 120-day contest period and 150-day assessor filing come from official pages as shown in search excerpts. Confirm each with the estate attorney.", L("prob16061", "boe502d"))
    flag("Process", "Trust income tax filing and property-tax due dates left blank", "No official page was opened for these.", L("irs_estate", "sf_tax"))
    body = legend() + "<h2>Step by step</h2>" + table(["Step", "When", "What to do", "Why it matters", "Status", "Source"], steps) + \
        callout("info", "A living trust normally passes real estate without probate court, but the Trustee still has duties and deadlines. The order above is a checklist to take to a California estate attorney, not a substitute for one.")
    page("process.html", "Inheriting through the trust: step by step", "What has to happen, in order, from today through the first three years after the Parent's death.", body)


# ====================================================================== LAW WATCH
def build_law():
    rows = [
        ["Federal estate exclusion", "In force", "$15,000,000 for 2026, rising to $15,480,000 for 2027", "More room before estate tax each year", B("V"), L("irs_estate", "irs_2027")],
        ["Death Tax Repeal Act (H.R.1301)", "Introduced Feb 13, 2025; no further action recorded", "Would repeal the federal estate tax", "No effect unless enacted", B("E"), L("congress_hr1301")],
        ["Proposals to end the step-up in basis", "", "", "Would make a sale at inheritance taxable on the Parent's full gain; watch closely", B("X"), L("irs_gifts")],
        ["Proposition 19 exclusion amount", "Next adjustment Feb 16, 2027", "$1,044,586 until then", "Small change in the taxable value if the Heir moves in", B("V"), L("lta25009")],
        ["Initiative to repeal Proposition 19's inheritance rules", "Failed to qualify for the ballot (May 2026)", "Rules unchanged", "Reassessment at inheritance stays", B("V"), L("sos_ccrov")],
        ["Proposition 3 (Nov 2026)", "Yes 60.6% in unofficial returns; results final Dec 11, 2026", "Makes the existing higher state income tax rates on high incomes permanent", "Raises California tax on a large gain or high rental income after 2030", B("V"), L("sos_results", "vg3")],
        ["Proposition 40 (Nov 2026)", "No 52.8% in unofficial returns", "One-time tax on covered assets over $1 billion; real property excluded", "No effect on this estate", B("E"), L("sos_results", "vg40")],
        ["Proposition 42 (Nov 2026)", "Yes 51.6% in unofficial returns", "Bars new state taxes on owning personal property, including financial assets", "Limits future state wealth-type taxes on reinvested sale proceeds", B("V"), L("sos_results", "vg42")],
        ["AB 942 (rooftop solar)", "Not enacted", "Language ending legacy net metering when a home is sold was removed", "Legacy solar terms are not cut off by this bill", B("V"), L("ab942")],
        ["Net metering legacy period", "In force", "Net-metering 2.0 terms last 20 years from interconnection", "The solar credit on Property A likely ends before or near inheritance", B("E"), L("cpuc_nem")],
        ["San Francisco rent increase", "In force", "1.6% for Mar 2026 to Feb 2027", "Caps rent growth on Property B's occupied units", B("E"), L("sf_rent")],
        ["San Francisco water and sewer rates", "Adopted plan", "+7.0% water, +15.0% wastewater for the year ending June 2027", "Property B's water bill rises faster than inflation", B("E"), L("sfpuc")],
        ["San Francisco vacant-unit tax", "", "", "Would matter only if a unit in Property B were left empty", B("X"), L("sf_tax")],
        ["California estate or inheritance tax proposals", "", "", "None confirmed from an official page", B("X"), L("sco")],
        ["Santa Clara County FY2026-27 tax rates", "Not yet posted", "", "Small change to the Property A rate", B("V"), L("scc_archive")],
    ]
    flag("Law watch", "Election results are unofficial", "Percentages were read on Nov 10, 2026. The Secretary of State certifies results by Dec 11, 2026.", L("sos_results"))
    flag("Law watch", "Three items left blank", "Step-up repeal proposals, the San Francisco vacant-unit tax and California estate-tax proposals were found only on non-government sites.", L("sos_results"))
    body = legend() + table(["Item", "Status", "What it does", "Effect on this decision", "Check", "Source"], rows) + \
        callout("info", "The inheritance is expected 14 to 24 years from now. Every rule on this site can change before then; the two that matter most for the plan are the step-up in basis and Proposition 19. Re-run the numbers when either changes.")
    page("law-watch.html", "Pending and recent law changes", "What is moving, what failed, and how each would change the plan.", body)


# ====================================================================== SUMMARY / FLAGGED / SOURCES
def build_index():
    y = Y0; ex = m.estate_exclusion(y)
    nav = "".join(f'<a class="tile" href="{f}"><b>{t}</b><span>{d}</span></a>' for f, t, d in [
        ("properties.html", "Properties", "Inputs and tax history for both homes"),
        ("projections.html", "Projections", "Every year 2026–2050: value, tax, insurance, utilities, upkeep"),
        ("property-tax.html", "Property tax", "Proposition 13 and 19: the bill after inheritance"),
        ("decision.html", "Decision", "Live in, rent or sell: cash flows, break-evens, sensitivity"),
        ("estate-tax.html", "Estate tax", "Thresholds and room left for cash"),
        ("process.html", "Trust process", "Step-by-step checklist with deadlines"),
        ("law-watch.html", "Law watch", "Pending changes and their effect"),
        ("flagged.html", "Flagged for review", f"{len(FLAGS) + 3} open items"),
        ("sources.html", "Sources", "Every official link, and how far each was checked")])
    keys = [
        ["Best plan for Property A", "Sell within about a year of inheriting and reinvest in a diversified mix; keep Property B", B("M"), '<a href="decision.html">Decision</a> · ' + L("irs_gifts")],
        ["Why selling at inheritance is cheap", "Basis resets to market value at death, so a prompt sale has little or no taxable gain", B("V"), L("irs_gifts")],
        [f"Property A value in {y}", f"{money(m.fmv('A', y, 'low'))} low · {money(m.fmv('A', y))} base · {money(m.fmv('A', y, 'high'))} high", B("M"), L("fred_sj")],
        [f"Property A tax in {y}: today's owner / Heir moves in / rented", f"{money(m.tax_current_owner('A', y))} / {money(m.tax_A_live(y))} / {money(m.tax_full('A', y))} a year", B("M"), L("lta25009", "scc_ratebook")],
        [f"Net rent from Property A in {y}", f"{money(f_rent['net'])} a year ({pct(f_rent['net'] / m.fmv('A', y))} of value)", B("M"), L("hud_a")],
        ["Return needed for selling to beat renting", f"{pct(min(be_rent_base), 1)}–{pct(max(be_rent_base), 1)} a year (base); {pct(min(be_all), 1)}–{pct(max(be_all), 1)} across scenarios", B("M"), L("tsp", "fred_sj")],
        ["Past returns for comparison", "4.65% government securities fund · 11.34% S&P 500 index fund, since inception", B("E"), L("tsp")],
        [f"Property B net income in {y}", f"{money(m.noi_B(y))} a year on today's tax base; {money(m.noi_B(y, y))} if inherited and reassessed", B("M"), L("sf_tax", "sf_rent60")],
        ["Federal estate tax exclusion", "$15,000,000 (2026) · $15,480,000 (2027) per person; 40% above it", B("E"), L("irs_estate", "irs_2027", "irs_i706")],
        [f"Room for cash and investments in {y}", f"{money(ex - m.fmv('A', y) - m.fmv('B', y))} after both homes (one exclusion, base)", B("M"), L("irs_2027", "cbo")],
        ["California estate or inheritance tax", "None", B("V"), L("sco", "rtc13301")],
    ]
    body = callout("warn", "<b>Privacy first.</b> This repository and website are public. People are called Parent, Trustee and Heir; the homes are Property A and Property B; dollar figures are rounded to the nearest $10. See the first item on <a href='flagged.html'>Flagged for review</a>.") + cards([
        ("Recommended", "Sell A · keep B", "sell Property A soon after inheriting, reinvest, keep Property B"),
        ("Break-even return", f"{pct(min(be_rent_base), 1)}–{pct(max(be_rent_base), 1)}", "selling wins if reinvested money earns more (base)"),
        (f"Property A tax after inheritance, {y}", f"{money(m.tax_A_live(y))}–{money(m.tax_full('A', y))}", f"a year, against {money(m.tax_current_owner('A', y))} for today's owner"),
        ("Federal estate exclusion", "$15,000,000", "2026, per person; no California tax"),
    ]) + f"""
<h2>Executive summary</h2>
<p><b>The decision.</b> Property A (Cupertino 95014, about {money(m.A['fmv'])} today) is expected to pass through a trust between 2040 and 2050. On the numbers, the best plan is to <b>sell it within about a year of inheriting, reinvest the proceeds in a diversified mix, and keep Property B</b> (San Francisco 94122) as the family home and rental.</p>
<p><b>Why.</b> Three rules drive the result. First, an inherited house takes a new tax basis equal to its value at death, so selling promptly produces little or no capital gain. Second, California reassesses an inherited home: the tax bill of about {money(m.tax_current_owner('A', y))} a year in {y} becomes {money(m.tax_full('A', y))} if the house is rented and {money(m.tax_A_live(y))} even if the Heir moves in and claims the family-home exclusion. Third, at benchmark rents the house would net only about {money(f_rent['net'])} a year after that tax, insurance and upkeep, which is {pct(f_rent['net'] / m.fmv('A', y))} of a {money(m.fmv('A', y))} asset.</p>
<p><b>The test.</b> Selling beats renting whenever the reinvested money earns more than {pct(min(be_rent_base), 1)}–{pct(max(be_rent_base), 1)} a year (base home-price growth of {pct(G['A']['base'])}). Selling came out ahead in {wins['sell']} of {len(grid)} combinations of inheritance year, home-price growth and investment return. It lost only where the money earned the 4.65% government-securities return while Cupertino prices grew at the base or high rate, so <b>money that would sit in savings is better left in the house, rented out</b>.</p>
<p><b>Property B.</b> Keep it. It nets about {money(m.noi_B(2026))} a year today and houses the family in the third unit. If it is inherited as well it will be reassessed, lifting its tax from about {money(m.tax_current_owner('B', y))} to {money(m.tax_full('B', y))} a year in {y}; its income yield on value stays above Property A's (see the comparison table on the Decision page).</p>
<p><b>Estate tax.</b> California and its local governments charge none. The federal exclusion is $15,000,000 per person in 2026 and $15,480,000 in 2027. Both homes fit under one exclusion in every scenario; in {y} the base case leaves room for about {money(ex - m.fmv('A', y) - m.fmv('B', y))} of cash and investments before the 40% tax starts. The estate's cash total is not in the brief, so compare it with that room.</p>
<p><b>What is not settled.</b> {len(FLAGS) + 3} items are open, including the Heir's income tax position, real insurance quotes, repair costs, selling costs and several figures confirmed only from excerpts. They are listed on <a href="flagged.html">Flagged for review</a>. The sensitivity table on the <a href="decision.html">Decision page</a> shows how far maintenance, selling costs and market rent each move the break-even.</p>
<h2>Key numbers</h2>""" + legend() + table(["Finding", "Number", "Status", "Source"], keys) + '<h2>Sections</h2><div class="tiles">' + nav + "</div>"
    page("index.html", "Inheritance decision dashboard", "Two California homes, one decision: when Property A is inherited, live in it, rent it, or sell it?", body)


def build_flagged():
    top = [
        ("Privacy", "The repository and this website are public", "Anyone can read them. Rounded assessed-value histories plus a ZIP code can be matched against public assessor data. Other pages in this repository, built by parallel sessions, were checked for unrounded figures during integration (see COORDINATION.md). If this matters, make the repository private or remove the year-by-year history tables.", L("scc_asr")),
        ("Method", "External links could not be machine-checked", "The build environment cannot reach government sites. Each link was either opened through the research tool or taken from an official search result; the Sources page says which.", L("irs_estate")),
        ("Method", "Several dashboards exist in this repository", "Parallel sessions published their own pages at the repository root and under pages/. They use different growth assumptions (3% and 4% a year) and so show different projected values and taxes. This dashboard's assumptions are listed on the Projections page.", L("fred_sj")),
    ]
    allf = top + FLAGS
    excerpt = [(s["publisher"], s["title"], ("Figure seen in a search excerpt only" if s["access"] == "excerpt" else "Page not opened") + ": " + s["used_for"], L(i))
               for i, s in SRC.items() if s["access"] != "opened" and i in USED]
    rows = [[str(n + 1), a, i, w, B("X") if "blank" in i.lower() else '<span class="b b-x">Needs review</span>', l] for n, (a, i, w, l) in enumerate(allf)]
    rows2 = [[a, i, w, B("E"), l] for a, i, w, l in excerpt]
    body = f"<p>{len(allf)} open items and {len(excerpt)} sources that need a manual re-check. None blocks publication; each is listed so it can be settled by hand.</p>" + \
        "<h2>Open items</h2>" + table(["#", "Area", "Item", "Why it is flagged / what to do", "Status", "Where to check"], rows) + \
        "<h2>Official sources not read in full</h2>" + table(["Publisher", "Page", "What was taken from it", "Status", "Link"], rows2)
    page("flagged.html", "Flagged for review", "Everything that is unverified, left blank, irregular or assumed.", body)


def build_sources():
    lab = {"opened": B("V") + " opened and read", "excerpt": B("E") + " search excerpt only", "not-opened": B("E") + " not opened"}
    rows = [[s["publisher"], s["title"], s["used_for"], lab[s["access"]], L(i)] for i, s in sorted(SRC.items(), key=lambda kv: kv[1]["publisher"]) if i in USED]
    body = f"<p>{len(rows)} sources, all government or government-regulated publishers. Accessed {ASOF}. Links open in a new tab and were not machine-checked from the build environment.</p>" + \
        table(["Publisher", "Page", "Used for", "How far it was checked", "Link"], rows)
    page("sources.html", "Sources", "Every official page behind the tables, with an honest note on how far each was checked.", body)


CSS = """:root{--bg:#f6f7f9;--card:#fff;--ink:#1c2430;--mute:#5b6676;--line:#dfe3ea;--brand:#14532d;--accent:#0f766e}
*{box-sizing:border-box}body{margin:0;font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--ink);background:var(--bg)}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px}header{background:var(--brand);color:#fff}header .wrap{display:flex;flex-wrap:wrap;gap:6px 18px;align-items:baseline;padding-top:14px;padding-bottom:10px}
.brand{color:#fff;font-weight:700;font-size:1.15rem;text-decoration:none}.tag{font-size:.85rem;opacity:.85}
nav{background:#0f3f22}nav .wrap{display:flex;flex-wrap:wrap;gap:2px;padding-top:0;padding-bottom:0}nav a{color:#e7f3ea;text-decoration:none;padding:9px 12px;font-size:.92rem}nav a:hover,nav a.on{background:#fff;color:var(--brand)}
main{padding-top:26px;padding-bottom:40px}h1{font-size:1.8rem;margin:0 0 6px}h2{font-size:1.25rem;margin:34px 0 10px;padding-top:6px;border-top:2px solid var(--line)}.lead{color:var(--mute);font-size:1.05rem;margin:0 0 18px;max-width:75ch}
p,li{max-width:85ch}a{color:var(--accent)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px;margin:18px 0}.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.card .k{font-size:.8rem;color:var(--mute);text-transform:uppercase;letter-spacing:.04em}.card .v{font-size:1.5rem;font-weight:700;margin:4px 0;color:var(--brand)}.card .n{font-size:.88rem;color:var(--mute)}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}.tile{display:block;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;text-decoration:none;color:var(--ink)}.tile:hover{border-color:var(--accent)}.tile b{display:block;color:var(--brand)}.tile span{font-size:.9rem;color:var(--mute)}
.tw{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:10px;margin:10px 0 18px}table{border-collapse:collapse;width:100%;font-size:.9rem}
th,td{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}th{background:#eef1f5;font-size:.8rem;text-transform:uppercase;letter-spacing:.03em;color:var(--mute);position:sticky;top:0}
tbody tr:hover{background:#fafbfc}table.num td{white-space:nowrap;font-variant-numeric:tabular-nums}table.num td:last-child{white-space:normal;min-width:150px;font-size:.82rem}
.b{display:inline-block;padding:1px 8px;border-radius:999px;font-size:.75rem;font-weight:600;white-space:nowrap}.b-v{background:#dcfce7;color:#166534}.b-e{background:#fef3c7;color:#92400e}.b-u{background:#e0e7ff;color:#3730a3}.b-m{background:#e0f2fe;color:#075985}.b-x{background:#fee2e2;color:#991b1b}
.legend{font-size:.85rem;color:var(--mute);line-height:2;max-width:none}.call{border-left:4px solid var(--accent);background:var(--card);padding:12px 16px;border-radius:0 10px 10px 0;margin:14px 0}.call.warn{border-color:#b45309;background:#fffbeb}.call.good{border-color:var(--brand);background:#f0fdf4}.call p,.call li{max-width:90ch}
footer{border-top:1px solid var(--line);background:var(--card);padding:18px 0;font-size:.85rem;color:var(--mute)}footer p{max-width:none}
@media(max-width:640px){h1{font-size:1.4rem}nav a{padding:8px 9px;font-size:.85rem}.card .v{font-size:1.25rem}}
"""


def main():
    os.makedirs(os.path.join(OUT, "static"), exist_ok=True)
    open(os.path.join(OUT, "static", "style.css"), "w").write(CSS)
    for fn in (build_properties, build_projections, build_ptax, build_decision, build_estate, build_process, build_law):
        fn()
    build_index()      # after the content pages so the flag count is complete
    build_flagged()
    build_sources()
    json.dump({"as_of": ASOF, "growth": G, "breakeven": {f"{o}-{Y}-{s}": round(v, 4) for (o, Y, s), v in be.items()},
               "wins": wins, "flags": len(FLAGS) + 3}, open(os.path.join(ROOT, "src", "data", "model_outputs.json"), "w"), indent=1)
    print("built", len(NAV), "pages;", len(FLAGS) + 3, "flags;", len(USED), "sources used; unused:", sorted(set(SRC) - USED))


if __name__ == "__main__":
    main()
