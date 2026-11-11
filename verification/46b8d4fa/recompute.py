#!/usr/bin/env python3
"""
Session 46b8d4fa - task K-2: independent recomputation of the published model.

What this does
--------------
The published pages compute their tables in the browser from site/data/model.js
(JavaScript, binary floating point). This script recomputes the same tables a second
time, in another language and with another arithmetic (Python `decimal`, 50
significant digits), from the *method stated on the pages*:

  market value      = input x (1 + home-price growth)^(year - 2026)
  assessed value    = input x (1 + 2 %)^(years)                 (Prop 13 ceiling scenario)
  property tax      = assessed value x scenario levy
  Prop 19 new value = market value - exclusion amount, when market value exceeds
                      (prior factored value + exclusion amount); otherwise the prior value
  Prop 19 amount    = official amount, multiplied by ONE year of home-price growth at each
                      biennial adjustment (February 2027, 2029, ...), as the pages state
  federal exclusion = official 2026 and 2027 amounts; 2027 amount x 1.02^(year - 2027) after
  sell              = market value x (1 - sale cost), compounded at the net portfolio return
  rent / live       = yearly after-tax cash carried at the net portfolio return, plus the
                      net sale at the endpoint after capital-gain tax on (amount realized - basis)

It then compares every dollar cell it knows how to derive with the cell the page
actually renders (exported by tools/export_published.cjs) and reports each difference.

It reads its inputs at run time from the export, so no household figure is stored in
this file. Rounding rule checked: nearest $10, halves up (JavaScript Math.round).

Usage
-----
  npm install --prefix .cache/test jsdom --no-audit --no-fund     # once
  node verification/46b8d4fa/tools/export_published.cjs
  python3 verification/46b8d4fa/recompute.py            # prints a summary, exit 1 on any difference
  python3 verification/46b8d4fa/recompute.py --json out.json
"""
from __future__ import annotations

import json
import re
import sys
from decimal import Decimal as D, getcontext, ROUND_FLOOR
from pathlib import Path

getcontext().prec = 50
REPO = Path(__file__).resolve().parents[2]
EXPORT = REPO / ".cache" / "46b8d4fa" / "published.json"


# ----------------------------------------------------------------------------- helpers
def d(x) -> D:
    """Exact decimal from a JSON number (via its shortest repr, e.g. 0.035 -> 0.035)."""
    return D(repr(x)) if isinstance(x, float) else D(x)


def round10(x: D) -> int:
    """Nearest $10, halves toward +infinity (what JavaScript Math.round(v/10)*10 does)."""
    return int((x / 10 + D("0.5")).to_integral_value(rounding=ROUND_FLOOR)) * 10


def near_half(x: D) -> bool:
    """True when x sits within one cent of a $10 rounding boundary (a float could tip it)."""
    frac = (x / 10) % 1
    return abs(frac - D("0.5")) < D("0.001")


MONEY = re.compile(r"([+\-\u2212]?)\s*\$\s?([\d,]+(?:\.\d+)?)")


def parse_money(text: str):
    """First dollar amount in a cell, as int. U+2212 or '-' means negative. None if absent."""
    m = MONEY.search(text)
    if not m:
        return None
    value = D(m.group(2).replace(",", ""))
    if m.group(1) in ("-", "\u2212"):
        value = -value
    return int(value)


# ----------------------------------------------------------------------------- the model, restated
class Model:
    def __init__(self, base: dict):
        self.b = {k: d(v) for k, v in base.items() if isinstance(v, (int, float))}
        self.start = int(base["startYear"])
        # older pages (before PR #16/#20) had no official 2027 exclusion and another Prop 19 step rule
        self.legacy_prop19 = "estateExclusion2027" not in base

    # --- series
    def market(self, prop: str, year: int, g: D | None = None) -> D:
        g = self.b["appreciation"] if g is None else g
        v0 = self.b["aValue"] if prop == "A" else self.b["bValue"]
        return v0 * (1 + g) ** (year - self.start)

    def assessed_before_transfer(self, prop: str, year: int) -> D:
        n = year - self.start
        if prop == "A":
            return self.b["aAssessed"] * (1 + self.b["assessmentGrowth"]) ** n
        # Property B input is a 2025 roll value, so 2026 is one factor later
        return self.b["bAssessed2025"] * (1 + self.b["assessmentGrowth"]) ** (n + 1)

    def prop19_amount(self, year: int, g: D | None = None) -> D:
        """Published scenario (as stated on the pages after PR #16/#20): BOE adjusts the amount
        every second February 16 (2027, 2029, ...) by ONE calendar year's change in the
        California house-price index; the scenario applies one year of home-price growth per
        adjustment. Until commit 240f255 the pages compounded two years per step instead;
        pass legacy=True to reproduce those older pages."""
        g = self.b["appreciation"] if g is None else g
        if self.legacy_prop19:
            return self.b["prop19Amount"] * (1 + g) ** (2 * max(0, (year - 2026) // 2))
        steps = max(0, (year - 2025) // 2)
        return self.b["prop19Amount"] * (1 + g) ** steps

    def transfer(self, year: int, g: D | None = None) -> dict:
        market = self.market("A", year, g)
        prior = self.assessed_before_transfer("A", year)
        amount = self.prop19_amount(year, g)
        primary = prior if market <= prior + amount else market - amount
        rate = self.b["aRate"]
        return dict(market=market, prior=prior, amount=amount, primary=primary,
                    primary_tax=primary * rate, full_tax=market * rate)

    # --- Property A, one year after a transfer in year T
    def a_year(self, year: int, option: str, T: int, g: D | None = None, rent_key: str = "aRent4BR") -> dict:
        b = self.b
        n = year - self.start
        k = max(0, year - T)
        tr = self.transfer(T, g)
        market = self.market("A", year, g)
        start_value = tr["primary"] if option == "live" else tr["market"]
        assessed = start_value * (1 + b["assessmentGrowth"]) ** k
        tax = assessed * b["aRate"]
        water = b["aWaterMonthly"] * 12 * (1 + b["expenseInflation"]) ** n
        solar = b["aSolarMonthlyCredit"] * 12                      # held flat on the published pages
        insurance = b["aInsuranceAnnual"] * (1 + b["expenseInflation"]) ** n
        maintenance = market * b["maintenanceA"]
        operating = tax + water + insurance + maintenance - solar
        row = dict(year=year, market=market, assessed=assessed, tax=tax, water=water, solar=solar,
                   insurance=insurance, maintenance=maintenance, operating=operating)
        if option == "live":
            row.update(gross=D(0), vacancy=D(0), management=D(0), noi=-operating, income_tax=D(0), cash=-operating)
            return row
        gross = b[rent_key] * (1 + b["rentGrowth"]) ** n * 12
        vacancy = gross * b["vacancy"]
        collected = gross - vacancy
        management = collected * b["management"]
        noi = collected - management - operating
        income_tax = max(D(0), noi) * b["ordinaryTax"]             # no refund on a loss
        row.update(gross=gross, vacancy=vacancy, management=management, noi=noi, income_tax=income_tax, cash=noi - income_tax)
        return row

    # --- the three strategies carried to the same endpoint
    def decision(self, T: int, H: int, g: D | None = None, r: D | None = None, rent_key: str = "aRent4BR") -> dict:
        b = self.b
        r = (b["portfolioGross"] - b["portfolioTaxDrag"]) if r is None else r
        tr = self.transfer(T, g)
        net_sale_now = tr["market"] * (1 - b["saleCost"])
        growth = (1 + r) ** H
        res = {"transfer": tr, "r": r}
        res["sell"] = dict(initial=net_sale_now, first_tax=D(0), first_cash=net_sale_now * r,
                           reserve=D(0), final_sale=D(0), cg_tax=D(0), terminal=net_sale_now * growth,
                           terminal_after_liquidation=net_sale_now * growth - max(D(0), net_sale_now * (growth - 1)) * b["capitalGainsTax"])
        for option in ("rent", "live"):
            reserve = D(0)
            rows = []
            for t in range(1, H + 1):
                row = self.a_year(T + t, option, T, g, rent_key)
                reserve = reserve * (1 + r) + row["cash"]
                rows.append(row)
            final_market = self.market("A", T + H, g)
            realized = final_market * (1 - b["saleCost"])
            gain = max(D(0), realized - tr["market"])               # basis = modeled value at death
            exclusion = min(b["primaryGainExclusion"], gain) if (option == "live" and H >= 2) else D(0)
            cg_tax = max(D(0), gain - exclusion) * b["capitalGainsTax"]
            final_sale = realized - cg_tax
            res[option] = dict(initial=D(0), first_tax=rows[0]["tax"], first_cash=rows[0]["cash"], reserve=reserve,
                               final_sale=final_sale, cg_tax=cg_tax, terminal=final_sale + reserve, realized=realized,
                               gain=gain, exclusion=exclusion, final_market=final_market, rows=rows)
        return res

    # --- Property B, continuing ownership
    def b_year(self, year: int) -> dict:
        b = self.b
        n = year - self.start
        market = self.market("B", year)
        assessed = self.assessed_before_transfer("B", year)
        tax = assessed * b["bRate"]
        infl = (1 + b["expenseInflation"]) ** n
        gross = b["bRentMonthly"] * 12 * (1 + b["sfRentGrowth"]) ** n
        vacancy = gross * b["vacancy"]
        management = (gross - vacancy) * b["management"]
        water = b["bWaterMonthly"] * 12 * infl
        electric = b["bElectricMonthly"] * 12 * infl
        insurance = b["bInsuranceAnnual"] * infl
        maintenance = market * b["maintenanceB"]
        fee = b["bRentBoardFeeAnnual"] * infl
        noi = gross - vacancy - management - tax - water - electric - insurance - maintenance - fee
        return dict(year=year, market=market, assessed=assessed, tax=tax, gross=gross, vacancy=vacancy,
                    management=management, water=water, electric=electric, insurance=insurance,
                    maintenance=maintenance, fee=fee, noi=noi)

    # --- estate headroom scenario
    def exclusion(self, year: int) -> D:
        b = self.b
        if "estateExclusion2027" not in b:                           # older pages: 2026 amount grown 2 %
            return b["estateExclusion"] * (1 + b["estateIndex"]) ** (year - self.start)
        if year <= 2026:
            return b["estateExclusion"]                              # official, deaths in 2026
        return b["estateExclusion2027"] * (1 + b["estateIndex"]) ** (year - 2027)   # 2027 official, then assumed

    # --- plan 4: live in A and rent out Property B's owner unit (constant-rate base path only)
    # Parameters as stated on the pages: HUD one-bedroom benchmark grown with costs (3 %) until the
    # inheritance; afterwards 60 % of (CPI 2.3 % + 0.4 pt), capped at 7 % (Sources and Flagged pages).
    CPI = D("0.023")
    SF_CONTROLLED_GROWTH = min(D("0.07"), max(D(0), D("0.6") * (D("0.023") + D("0.004"))))

    def b_unit_reserve(self, T: int, H: int, r: D) -> D:
        b = self.b
        unit = b["bRent1BR"] * 12 * (1 + b["expenseInflation"]) ** (T - self.start)
        reserve = D(0)
        for _ in range(H):
            unit *= 1 + self.SF_CONTROLLED_GROWTH
            net = unit * (1 - b["vacancy"]) * (1 - b["management"]) * (1 - b["ordinaryTax"])
            reserve = reserve * (1 + r) + net
        return reserve

    def deflator(self, year: int) -> D:
        return (1 + self.CPI) ** (year - self.start)

    def estate_year(self, year: int) -> dict:
        b = self.b
        a = self.market("A", year)
        exclusion = self.exclusion(year)
        return dict(a=a, b=self.market("B", year), included=a, exclusion=exclusion,
                    headroom=max(D(0), exclusion - a), excess=max(D(0), a - exclusion))


# ----------------------------------------------------------------------------- comparison
class Checker:
    def __init__(self):
        self.rows = []          # every comparison made
        self.unparsed = []      # published cells this script could not read
        self.missing = []       # tables it expected and did not find (layout changed)
        self.headline = {}

    def cell(self, page, table, row_label, column, published_text, expected: D, magnitude_only=False):
        pub = parse_money(published_text)
        exp = round10(expected)
        if pub is None:
            self.unparsed.append(dict(page=page, table=table, row=str(row_label), column=column, text=published_text[:80]))
            return
        if magnitude_only:
            pub, exp = abs(pub), abs(exp)
        self.rows.append(dict(page=page, table=table, row=str(row_label), column=column, published=pub,
                              recomputed=exp, diff=pub - exp, boundary=near_half(expected)))

    def text(self, page, table, row_label, column, published, expected):
        self.rows.append(dict(page=page, table=table, row=str(row_label), column=column, published=published,
                              recomputed=expected, diff=0 if published == expected else 1, boundary=False))

    @property
    def diffs(self):
        return [r for r in self.rows if r["diff"] != 0]


def find(pub, c, page, fragment, required_head=None):
    """Table on `page` whose nearest heading contains `fragment`. Records a note and returns None when absent."""
    for t in pub["pages"].get(page, {}).get("tables", []):
        if fragment.lower() in t["heading"].lower() and (required_head is None or required_head in t["head"]):
            return t
    c.missing.append(dict(page=page, heading_fragment=fragment))
    return None


def year_of(text):
    m = re.search(r"(20\d\d)", text)
    return int(m.group(1)) if m else None


def run(pub: dict) -> Checker:
    m = Model(pub["base"])
    c = Checker()
    b = m.b
    H = 10
    r = b["portfolioGross"] - b["portfolioTaxDrag"]
    dec = {T: m.decision(T, H) for T in (2040, 2045, 2050)}
    first = lambda T, opt: m.a_year(T + 1, opt, T)
    other = lambda row: row["water"] + row["insurance"] + row["maintenance"] - row["solar"]

    # ---------------------------------------------------------------- index.html
    page = "index.html"
    t = find(pub, c, page, "Three choices")
    if t:
        for row in t["rows"]:
            T = year_of(row["cells"][0]); dd = dec[T]; cells = row["cells"]
            c.cell(page, "Answer by inheritance year", T, "Value of A at inheritance", cells[1], dd["transfer"]["market"])
            c.cell(page, "Answer by inheritance year", T, "Sell and reinvest", cells[2], dd["sell"]["terminal"])
            c.cell(page, "Answer by inheritance year", T, "Rent out, then sell", cells[3], dd["rent"]["terminal"])
            c.cell(page, "Answer by inheritance year", T, "Live in, then sell", cells[4], dd["live"]["terminal"])
            c.cell(page, "Answer by inheritance year", T, "Selling ahead of renting", cells[5], dd["sell"]["terminal"] - dd["rent"]["terminal"])
            c.cell(page, "Answer by inheritance year", T, "Same, portfolio also taxed", cells[6], dd["sell"]["terminal_after_liquidation"] - dd["rent"]["terminal"])
    t = find(pub, c, page, "Four numbers decide it")
    if t:
        T = 2045; dd = dec[T]
        for row, val in zip(t["rows"], (D(0), first(T, "rent")["tax"], dd["sell"]["initial"] * r, -first(T, "live")["cash"])):
            c.cell(page, "Four numbers (2045)", row["cells"][0][:38], "Amount", row["cells"][1], val)
    t = find(pub, c, page, "costs to hold in the first year")
    if t:
        for row in t["rows"]:
            T = year_of(row["cells"][0]); rent, live = first(T, "rent"), first(T, "live")
            vals = (b["aAssessed"] * b["aRate"], live["tax"], rent["tax"], other(rent), live["tax"] + other(live), rent["tax"] + other(rent))
            for i, val in enumerate(vals, start=1):
                c.cell(page, "Costs upon inheriting", T, t["head"][i], row["cells"][i], val)
    t = find(pub, c, page, "Federal, state and local")
    if t:
        for row in t["rows"]:
            y = year_of(row["cells"][0])
            if row["cells"][0].startswith("Federal") and y:
                c.cell(page, "Tax on the inheritance", y, "Allowed before tax", row["cells"][2], m.exclusion(y))
                c.cell(page, "Tax on the inheritance", y, "Room left after Property A", row["cells"][3], m.exclusion(y) - m.market("A", y))

    # ---------------------------------------------------------------- site/decision.html (base case 2040 -> 2050)
    page = "site/decision.html"; T = 2040; dd = dec[T]
    t = find(pub, c, page, "2040 inheritance")
    if t:
        cols = [("Initial net sale", "initial"), ("First-year property tax", "first_tax"), ("First-year after-tax cash", "first_cash"),
                ("Cash reserve at endpoint", "reserve"), ("Net terminal property sale", "final_sale"),
                ("Terminal capital-gain tax", "cg_tax"), ("Financial position", "terminal")]
        for row, key in zip(t["rows"], ("sell", "rent", "live")):
            for i, (label, field) in enumerate(cols, start=1):
                c.cell(page, "Terminal wealth bridge", key, label, row["cells"][i], dd[key][field])
    t = find(pub, c, page, "Where the difference comes from")
    if t:
        for row in t["rows"]:
            y = int(row["cells"][0]); rent, live = m.a_year(y, "rent", T), m.a_year(y, "live", T)
            vals = (rent["market"], rent["assessed"], rent["tax"], rent["gross"], rent["noi"], rent["cash"], live["tax"], live["cash"])
            for i, val in enumerate(vals, start=1):
                c.cell(page, "Annual mechanics", y, t["head"][i], row["cells"][i], val)
    t = find(pub, c, page, "Does the financial winner change")
    if t:
        returns = [D(h.strip("%")) / 100 for h in t["head"][1:4]]
        for row in t["rows"]:
            g = D(row["cells"][0].split("%")[0]) / 100
            for i, rr in enumerate(returns, start=1):
                d2 = m.decision(T, H, g=g, r=rr)
                adv = d2["sell"]["terminal"] - d2["rent"]["terminal"]
                c.cell(page, "Two-way sensitivity", f"{g:.1%} growth", f"{rr:.0%} return", row["cells"][i], adv, magnitude_only=True)
                c.text(page, "Two-way sensitivity", f"{g:.1%} growth", f"{rr:.0%} return (which side leads)",
                       row["cells"][i].split()[0], "Sell" if adv >= 0 else "Rent")

    # ---------------------------------------------------------------- site/estate-tax.html
    page = "site/estate-tax.html"
    t = find(pub, c, page, "How much can be inherited")
    if t:
        for row in t["rows"]:
            y = year_of(row["cells"][0])
            if row["cells"][0].startswith("Federal") and y:
                c.cell(page, "Thresholds by level", y, "Allowed before tax", row["cells"][2], m.exclusion(y))
                c.cell(page, "Thresholds by level", y, "Room left after Property A", row["cells"][3], m.exclusion(y) - m.market("A", y))
    t = find(pub, c, page, "versus modeled exclusion")
    if t:
        for row in t["rows"]:
            y = int(row["cells"][0]); e = m.estate_year(y)
            for i, f in enumerate(("a", "b", "included", "exclusion", "headroom", "excess"), start=1):
                c.cell(page, "Estate headroom by year", y, t["head"][i], row["cells"][i], e[f])

    # ---------------------------------------------------------------- site/properties.html
    page = "site/properties.html"
    t = find(pub, c, page, "Partial relief")
    if t:
        for row in t["rows"]:
            y = year_of(row["cells"][0]); tr = m.transfer(y)
            for i, f in enumerate(("market", "prior", "amount", "primary", "primary_tax", "full_tax"), start=1):
                c.cell(page, "Prop 19 illustration", y, t["head"][i], row["cells"][i], tr[f])
    t = find(pub, c, page, "First full year after the inheritance")
    if t:
        for row in t["rows"]:
            T2 = year_of(row["cells"][0]); rent, live = first(T2, "rent"), first(T2, "live")
            vals = (m.market("A", T2), live["tax"], rent["tax"], rent["insurance"], rent["water"], -rent["solar"], rent["maintenance"],
                    live["tax"] + other(live), rent["tax"] + other(rent))
            for i, val in enumerate(vals, start=1):
                c.cell(page, "First year after inheritance", T2, t["head"][i], row["cells"][i], val)
    t = find(pub, c, page, "Before any inheritance event")
    if t:
        for row in t["rows"]:
            y = int(row["cells"][0]); n = y - m.start
            market = m.market("A", y); assessed = m.assessed_before_transfer("A", y); tax = assessed * b["aRate"]
            ins = b["aInsuranceAnnual"] * (1 + b["expenseInflation"]) ** n
            water_net = b["aWaterMonthly"] * 12 * (1 + b["expenseInflation"]) ** n - b["aSolarMonthlyCredit"] * 12
            maint = market * b["maintenanceA"]
            for i, val in enumerate((market, assessed, tax, ins, water_net, maint, tax + ins + water_net + maint), start=1):
                c.cell(page, "Property A baseline", y, t["head"][i], row["cells"][i], val)
    t = find(pub, c, page, "After a 2040 inheritance")
    if t:
        for row in t["rows"]:
            y = int(row["cells"][0]); rr = m.a_year(y, "rent", 2040)
            for i, val in enumerate((rr["gross"], rr["vacancy"], rr["management"], rr["tax"], other(rr), rr["noi"], rr["cash"]), start=1):
                c.cell(page, "Property A rental scenario", y, t["head"][i], row["cells"][i], val)
    t = find(pub, c, page, "Existing rent rolls")
    if t:
        for row in t["rows"]:
            y = int(row["cells"][0]); rr = m.b_year(y)
            vals = (rr["market"], rr["assessed"], rr["tax"], rr["gross"], rr["water"] + rr["electric"] + rr["insurance"], rr["maintenance"], rr["noi"])
            for i, val in enumerate(vals, start=1):
                c.cell(page, "Property B baseline", y, t["head"][i], row["cells"][i], val)

    # ---------------------------------------------------------------- site/san-francisco.html
    page = "site/san-francisco.html"
    t = find(pub, c, page, "Gross rent is not spendable income")
    if t:
        rr = m.b_year(2026)
        expected = [rr["gross"], -rr["vacancy"], -rr["management"], -rr["tax"], -rr["water"], -rr["electric"], -rr["insurance"],
                    -rr["maintenance"], -rr["fee"], rr["noi"]]
        for row, val in zip(t["rows"], expected):
            c.cell(page, "Property B 2026 cash flow", row["cells"][0][:40], "2026 amount", row["cells"][1], val)
    t = find(pub, c, page, "A stable contributor")
    if t:
        for row in t["rows"]:
            y = int(row["cells"][0]); rr = m.b_year(y)
            for i, val in enumerate((rr["market"], rr["tax"], rr["gross"], rr["noi"]), start=1):
                c.cell(page, "Property B selected years", y, t["head"][i], row["cells"][i], val)
    t = find(pub, c, page, "Potential upside")
    if t:
        for row, key in zip(t["rows"][:2], ("bRent1BR", "bRent2BR")):
            c.cell(page, "Owner-unit benchmark", row["cells"][0], "Monthly gross rent", row["cells"][1], b[key])
            c.cell(page, "Owner-unit benchmark", row["cells"][0], "Annual gross rent", row["cells"][2], b[key] * 12)

    # ---------------------------------------------------------------- site/plan.html (default selection: 2045 -> 2055)
    page = "site/plan.html"
    t = find(pub, c, page, "Four ways to use the two properties")
    if t:
        T = 2045; dd = dec[T]; defl = m.deflator(T + H)
        plan4 = dd["live"]["terminal"] + m.b_unit_reserve(T, H, r)
        results = (dd["sell"]["terminal"], dd["rent"]["terminal"], dd["live"]["terminal"], plan4)
        best = max(results)
        for row, val in zip(t["rows"], results):
            label = row["cells"][0][:28]
            c.cell(page, "Four plans (2045)", label, "Result after 10 years", row["cells"][3], val)
            c.cell(page, "Four plans (2045)", label, "In 2026 dollars", row["cells"][4], val / defl)
            if val != best:
                c.cell(page, "Four plans (2045)", label, "Gap to best", row["cells"][5], val - best)
            else:
                c.text(page, "Four plans (2045)", label, "Gap to best", row["cells"][5], "Best")
        c.headline["plan4_2045"] = round10(plan4)
    t = find(pub, c, page, "Where the gap comes from")
    if t:
        T = 2045; dd = dec[T]; rent, live = first(T, "rent"), first(T, "live"); tr = dd["transfer"]
        vals = (tr["market"], D(0), rent["tax"], rent["gross"], rent["noi"], dd["sell"]["initial"] * r, -live["cash"],
                (tr["market"] - tr["primary"]) * b["aRate"])
        for row, val in zip(t["rows"], vals):
            c.cell(page, "Drivers (2045)", row["cells"][0][:40], "Amount", row["cells"][1], val)

    d40 = dec[2040]
    c.headline.update({f"{T}->{T + H}": dict(sell=round10(dec[T]["sell"]["terminal"]), rent=round10(dec[T]["rent"]["terminal"]),
                                             live=round10(dec[T]["live"]["terminal"]),
                                             sell_if_portfolio_taxed=round10(dec[T]["sell"]["terminal_after_liquidation"]),
                                             prop19_amount=round10(dec[T]["transfer"]["amount"])) for T in (2040, 2045, 2050)})
    # what-if, pending H.R.7034 (no dollar limit on the main-home exclusion): live case with the whole gain excluded
    c.headline["live_2040_if_home_sale_gain_fully_excluded"] = round10(d40["live"]["terminal"] + d40["live"]["cg_tax"])
    return c


def summarise(c: Checker):
    by_table = {}
    for r in c.rows:
        agg = by_table.setdefault((r["page"], r["table"]), dict(cells=0, differences=0, max_abs=0, boundary=0))
        agg["cells"] += 1
        if r["diff"] != 0:
            agg["differences"] += 1
            agg["boundary"] += 1 if r["boundary"] else 0
            if isinstance(r["published"], int):
                agg["max_abs"] = max(agg["max_abs"], abs(r["diff"]))
    return by_table


def main(argv):
    if not EXPORT.exists():
        print("missing", EXPORT.relative_to(REPO), "- run: node verification/46b8d4fa/tools/export_published.cjs")
        return 2
    pub = json.loads(EXPORT.read_text(encoding="utf-8"))
    c = run(pub)
    by_table = summarise(c)
    print(f"commit checked: {pub.get('commit')}")
    print(f"{'page':26} {'table':30} {'cells':>6} {'diff':>5} {'max |diff|':>10}")
    for (page, tbl), agg in by_table.items():
        print(f"{page:26} {tbl:30} {agg['cells']:6d} {agg['differences']:5d} {agg['max_abs']:10d}")
    total, diffs = len(c.rows), c.diffs
    print(f"\nTOTAL cells recomputed and compared: {total}; differences: {len(diffs)} "
          f"(of which at a $10 rounding boundary: {sum(1 for r in diffs if r['boundary'])}); "
          f"cells not parsed: {len(c.unparsed)}; expected tables not found: {len(c.missing)}")
    for k, v in c.headline.items():
        print("  recomputed", k, v)
    for r in diffs:
        print("  DIFF", r)
    for u in c.unparsed:
        print("  UNPARSED", u)
    for u in c.missing:
        print("  TABLE NOT FOUND (layout changed?)", u)
    if "--json" in argv:
        dest = Path(argv[argv.index("--json") + 1])
        dest.write_text(json.dumps(dict(commit=pub.get("commit"), total=total, differences=diffs, unparsed=c.unparsed, missing=c.missing,
                                        by_table=[dict(page=p, table=t, **a) for (p, t), a in by_table.items()],
                                        headline=c.headline), indent=1), encoding="utf-8")
    return 1 if (diffs or c.unparsed or c.missing) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
