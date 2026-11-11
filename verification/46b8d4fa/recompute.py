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
        """Published scenario: the official amount, then compounded at home-price growth
        once per completed two-year step after 2026 (no look-ahead)."""
        g = self.b["appreciation"] if g is None else g
        steps = max(0, (year - 2026) // 2)
        return self.b["prop19Amount"] * (1 + g) ** (2 * steps)

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
    def estate_year(self, year: int) -> dict:
        b = self.b
        a = self.market("A", year)
        exclusion = b["estateExclusion"] * (1 + b["estateIndex"]) ** (year - self.start)
        return dict(a=a, b=self.market("B", year), included=a, exclusion=exclusion,
                    headroom=max(D(0), exclusion - a), excess=max(D(0), a - exclusion))


# ----------------------------------------------------------------------------- comparison
class Checker:
    def __init__(self):
        self.rows = []          # every comparison
        self.unparsed = []

    def cell(self, page, table, row_label, column, published_text, expected: D, magnitude_only=False):
        pub = parse_money(published_text)
        exp = round10(expected)
        if pub is None:
            self.unparsed.append(dict(page=page, table=table, row=row_label, column=column, text=published_text))
            return
        if magnitude_only:
            pub, exp = abs(pub), abs(exp)
        self.rows.append(dict(page=page, table=table, row=str(row_label), column=column, published=pub,
                              recomputed=exp, diff=pub - exp, boundary=near_half(expected)))

    @property
    def diffs(self):
        return [r for r in self.rows if r["diff"] != 0]


def table(pub, page, heading_fragment):
    for t in pub["pages"][page]["tables"]:
        if heading_fragment.lower() in t["heading"].lower():
            return t
    raise SystemExit(f"table not found on {page}: {heading_fragment!r} (the page layout changed; update this script)")


def run(pub: dict) -> Checker:
    m = Model(pub["base"])
    c = Checker()
    b = m.b
    T, H = 2040, 10                                   # the base case the pages state: 2040 transfer, 2050 endpoint
    dec = m.decision(T, H)
    best = max(("sell", "rent", "live"), key=lambda k: dec[k]["terminal"])

    # index.html - decision preview
    page = "index.html"
    t = table(pub, page, "2040 inheritance, 2050 endpoint")
    for row, key in zip(t["rows"], ("sell", "rent", "live")):
        cells = row["cells"]
        c.cell(page, "Decision preview", key, "First-year property tax", cells[1], dec[key]["first_tax"])
        c.cell(page, "Decision preview", key, "First-year after-tax cash", cells[2], dec[key]["first_cash"])
        c.cell(page, "Decision preview", key, "2050 financial position", cells[3], dec[key]["terminal"])
        if key != best:
            c.cell(page, "Decision preview", key, "Difference vs. best", cells[4], dec[key]["terminal"] - dec[best]["terminal"])

    # site/decision.html - terminal bridge
    page = "site/decision.html"
    t = table(pub, page, "2040 inheritance")
    cols = [("Initial net sale", "initial"), ("First-year property tax", "first_tax"), ("First-year after-tax cash", "first_cash"),
            ("Cash reserve at endpoint", "reserve"), ("Net terminal property sale", "final_sale"),
            ("Terminal capital-gain tax", "cg_tax"), ("Financial position", "terminal")]
    for row, key in zip(t["rows"], ("sell", "rent", "live")):
        for i, (label, field) in enumerate(cols, start=1):
            c.cell(page, "Terminal wealth bridge", key, label, row["cells"][i], dec[key][field])

    # site/decision.html - annual mechanics
    t = table(pub, page, "Where the difference comes from")
    for row in t["rows"]:
        y = int(row["cells"][0])
        rent, live = m.a_year(y, "rent", T), m.a_year(y, "live", T)
        for i, (label, val) in enumerate([("Market value", rent["market"]), ("Rent-case assessment", rent["assessed"]),
                                          ("Rent-case property tax", rent["tax"]), ("Gross rent", rent["gross"]),
                                          ("Rental NOI", rent["noi"]), ("Rent after-tax cash", rent["cash"]),
                                          ("Live-case property tax", live["tax"]), ("Live annual net cost", live["cash"])], start=1):
            c.cell(page, "Annual mechanics", y, label, row["cells"][i], val)

    # site/decision.html - two-way sensitivity (sell minus rent; label says which side leads)
    t = table(pub, page, "Does the financial winner change")
    returns = [D(h.strip("%")) / 100 for h in t["head"][1:4]]
    for row in t["rows"]:
        g = D(row["cells"][0].split("%")[0]) / 100
        for i, r in enumerate(returns, start=1):
            dd = m.decision(T, H, g=g, r=r)
            adv = dd["sell"]["terminal"] - dd["rent"]["terminal"]
            text = row["cells"][i]
            c.cell(page, "Two-way sensitivity", f"{g:.1%} growth", f"{r:.0%} return", text, adv, magnitude_only=True)
            leader = "Sell" if adv >= 0 else "Rent"
            if not text.startswith(leader):
                c.rows.append(dict(page=page, table="Two-way sensitivity", row=f"{g:.1%} growth", column=f"{r:.0%} return (leader)",
                                   published=text.split()[0], recomputed=leader, diff=1, boundary=False))

    # site/estate-tax.html - headroom by year
    page = "site/estate-tax.html"
    t = table(pub, page, "versus modeled exclusion")
    for row in t["rows"]:
        y = int(row["cells"][0])
        e = m.estate_year(y)
        for i, f in enumerate(("a", "b", "included", "exclusion", "headroom", "excess"), start=1):
            c.cell(page, "Estate headroom", y, t["head"][i], row["cells"][i], e[f])

    # site/properties.html - Prop 19 illustrations
    page = "site/properties.html"
    t = table(pub, page, "Partial relief")
    for row in t["rows"]:
        y = int(row["cells"][0][:4])
        tr = m.transfer(y)
        for i, f in enumerate(("market", "prior", "amount", "primary", "primary_tax", "full_tax"), start=1):
            c.cell(page, "Prop 19 illustration", y, t["head"][i], row["cells"][i], tr[f])

    # site/properties.html - Property A before any inheritance
    t = table(pub, page, "Before any inheritance event")
    for row in t["rows"]:
        y = int(row["cells"][0]); n = y - m.start
        market = m.market("A", y); assessed = m.assessed_before_transfer("A", y); tax = assessed * b["aRate"]
        ins = b["aInsuranceAnnual"] * (1 + b["expenseInflation"]) ** n
        water_net = b["aWaterMonthly"] * 12 * (1 + b["expenseInflation"]) ** n - b["aSolarMonthlyCredit"] * 12
        maint = market * b["maintenanceA"]
        for i, val in enumerate((market, assessed, tax, ins, water_net, maint, tax + ins + water_net + maint), start=1):
            c.cell(page, "Property A baseline", y, t["head"][i], row["cells"][i], val)

    # site/properties.html - Property A rental scenario after a 2040 inheritance
    t = table(pub, page, "After a 2040 inheritance")
    for row in t["rows"]:
        y = int(row["cells"][0])
        r = m.a_year(y, "rent", T)
        other = r["water"] + r["insurance"] + r["maintenance"] - r["solar"]
        for i, val in enumerate((r["gross"], r["vacancy"], r["management"], r["tax"], other, r["noi"], r["cash"]), start=1):
            c.cell(page, "Property A rental scenario", y, t["head"][i], row["cells"][i], val)

    # site/properties.html - Property B baseline
    t = table(pub, page, "Existing rent rolls")
    for row in t["rows"]:
        y = int(row["cells"][0])
        r = m.b_year(y)
        for i, val in enumerate((r["market"], r["assessed"], r["tax"], r["gross"], r["water"] + r["electric"] + r["insurance"],
                                 r["maintenance"], r["noi"]), start=1):
            c.cell(page, "Property B baseline", y, t["head"][i], row["cells"][i], val)

    # site/san-francisco.html - 2026 cash-flow lines and selected years
    page = "site/san-francisco.html"
    t = table(pub, page, "Gross rent is not spendable income")
    r = m.b_year(2026)
    expected = [r["gross"], -r["vacancy"], -r["management"], -r["tax"], -r["water"], -r["electric"], -r["insurance"],
                -r["maintenance"], -r["fee"], r["noi"]]
    for row, val in zip(t["rows"], expected):
        c.cell(page, "Property B 2026 cash flow", row["cells"][0][:40], "2026 amount", row["cells"][1], val)
    t = table(pub, page, "A stable contributor")
    for row in t["rows"]:
        y = int(row["cells"][0]); r = m.b_year(y)
        for i, val in enumerate((r["market"], r["tax"], r["gross"], r["noi"]), start=1):
            c.cell(page, "Property B selected years", y, t["head"][i], row["cells"][i], val)
    t = table(pub, page, "Potential upside")
    for row, key in zip(t["rows"][:2], ("bRent1BR", "bRent2BR")):
        c.cell(page, "Owner-unit benchmark", row["cells"][0], "Monthly gross rent", row["cells"][1], b[key])
        c.cell(page, "Owner-unit benchmark", row["cells"][0], "Annual gross rent", row["cells"][2], b[key] * 12)

    c.headline = dict(sell=round10(dec["sell"]["terminal"]), rent=round10(dec["rent"]["terminal"]),
                      live=round10(dec["live"]["terminal"]), best=best,
                      sell_after_liquidation=round10(dec["sell"]["terminal_after_liquidation"]),
                      transfer_market=round10(dec["transfer"]["market"]), prop19_amount=round10(dec["transfer"]["amount"]),
                      primary_assessed=round10(dec["transfer"]["primary"]))
    return c


def main(argv):
    if not EXPORT.exists():
        print("missing", EXPORT.relative_to(REPO), "- run: node verification/46b8d4fa/tools/export_published.cjs")
        return 2
    pub = json.loads(EXPORT.read_text(encoding="utf-8"))
    c = run(pub)
    by_table = {}
    for r in c.rows:
        key = (r["page"], r["table"])
        agg = by_table.setdefault(key, dict(cells=0, differences=0, max_abs=0))
        agg["cells"] += 1
        if r["diff"] != 0:
            agg["differences"] += 1
            if isinstance(r["diff"], int):
                agg["max_abs"] = max(agg["max_abs"], abs(r["diff"]))
    print(f"commit checked: {pub.get('commit')}")
    print(f"{'page':26} {'table':30} {'cells':>6} {'diff':>5} {'max |diff|':>10}")
    for (page, tbl), agg in by_table.items():
        print(f"{page:26} {tbl:30} {agg['cells']:6d} {agg['differences']:5d} {agg['max_abs']:10d}")
    total, diffs = len(c.rows), c.diffs
    print(f"\nTOTAL cells recomputed and compared: {total}; differences: {len(diffs)}; cells not parsed: {len(c.unparsed)}")
    print("base case (2040 transfer, 2050 endpoint), recomputed:", c.headline)
    for r in diffs:
        print("  DIFF", r)
    for u in c.unparsed:
        print("  UNPARSED", u)
    if "--json" in argv:
        dest = Path(argv[argv.index("--json") + 1])
        dest.write_text(json.dumps(dict(commit=pub.get("commit"), total=total, differences=diffs, unparsed=c.unparsed,
                                        by_table=[dict(page=p, table=t, **a) for (p, t), a in by_table.items()],
                                        headline=c.headline), indent=1), encoding="utf-8")
    return 1 if (diffs or c.unparsed) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
