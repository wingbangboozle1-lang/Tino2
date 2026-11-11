#!/usr/bin/env python3
"""Independent recomputation of the live / rent / sell comparison for Property A.

Written by session 4e07c8e6 without reusing the site's calculation code. It reads only the
published inputs (already rounded to $10) from site/data/model.js, so no private figure is typed
here. Run from the repository root:

    python3 verification/4e07c8e6/recompute.py

Part 1 rebuilds the site's three headline results from first principles.
Part 2 changes one thing at a time to test whether the ranking survives.
Every number that is not a published input is a stated assumption, not an official figure.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = open(os.path.join(ROOT, "site", "data", "model.js"), encoding="utf-8").read()


def published_inputs():
    block = SRC[SRC.index("const BASE = {"):SRC.index("};", SRC.index("const BASE = {"))]
    vals = {k: float(v) for k, v in re.findall(r"(\w+):\s*([0-9.]+)", block)}
    for name in ("A_RATE", "B_RATE"):
        vals[name] = float(re.search(name + r"\s*=\s*([0-9.]+)", SRC).group(1))
    vals["aRate"], vals["bRate"] = vals["A_RATE"], vals["B_RATE"]
    return vals


P = published_inputs()
Y0 = int(P["startYear"])


def allowance(year, growth, p=P):
    """Prop 19 dollar amount: one year's price change applied at each two-year step (BOE LTA 2025/009)."""
    steps = max(0, (year - 2025) // 2)
    return p["prop19Amount"] * (1 + growth) ** steps


def run(inherit, hold=10, p=P, **o):
    """Return the end-of-period position of each plan.

    Options (all default to the site's own treatment):
      home      annual home-price growth          cost     annual cost and Property A rent growth
      net       portfolio return after annual tax a_rate   Property A tax rate after inheritance
      excl      home-sale gain exclusion          bshare   building share of value (None = no depreciation)
      rent      monthly rent in 2026 dollars      prop19   False = no parent-child relief at all
    """
    g = o.get("home", p["appreciation"]); c = o.get("cost", p["expenseInflation"])
    r = o.get("net", p["portfolioGross"] - p["portfolioTaxDrag"])
    rate = o.get("a_rate", p["aRate"]); excl = o.get("excl", p["primaryGainExclusion"])
    bshare = o.get("bshare"); rent0 = o.get("rent", p["aRent4BR"])
    cg, ordy = p["capitalGainsTax"], p["ordinaryTax"]
    k0 = inherit - Y0
    value0 = p["aValue"] * (1 + g) ** k0                 # market value on the date of death = new income-tax basis
    old_assessed = p["aAssessed"] * (1 + p["assessmentGrowth"]) ** k0
    allow = allowance(inherit, g, p)
    excess = max(0.0, value0 - (old_assessed + allow))   # BOE: amount above the value cap is added
    live_base = old_assessed + excess if o.get("prop19", True) else value0
    out = {"value_at_death": value0, "old_assessed": old_assessed, "allowance": allow, "live_taxable": live_base}

    # --- Sell at inheritance, invest the net proceeds ---
    net = value0 * (1 - p["saleCost"])
    out["sell"] = net * (1 + r) ** hold
    # (a) site's conservative bound: every dollar of growth taxed again at the end
    out["sell_all_growth_taxed"] = out["sell"] - (out["sell"] - net) * cg
    # (b) split: the annual tax drag is treated as tax already paid on the income part of the return;
    #     only the unrealised price growth (gross return minus an assumed 3-point income yield) is taxed at the end
    income_net = max(0.0, r - (p["portfolioGross"] - 0.03))
    v, basis = net, net
    for _ in range(hold):
        basis += v * income_net
        v *= 1 + r
    out["sell_unrealised_taxed"] = v - max(0.0, v - basis) * cg
    out["sale_cost_loss"] = value0 * p["saleCost"]       # capital loss if the trust holds the house for sale (IRS Pub. 559)
    out["sale_cost_loss_tax_value_max"] = out["sale_cost_loss"] * cg

    # --- Hold for `hold` years, then sell ---
    res = {"rent": 0.0, "live": 0.0, "liveB": 0.0}
    b_unit = p["bRent1BR"] * 12 * (1 + c) ** k0          # B's third unit let at the HUD 1-bedroom benchmark on move-out
    dep_per_year = (bshare * value0 / 27.5) if bshare else 0.0
    suspended, dep_taken, first = 0.0, 0.0, {}
    for t in range(1, hold + 1):
        k = k0 + t
        market = p["aValue"] * (1 + g) ** k
        upkeep = (p["aWaterMonthly"] * 12 + p["aInsuranceAnnual"]) * (1 + c) ** k + market * p["maintenanceA"] - p["aSolarMonthlyCredit"] * 12
        tax_full = value0 * (1 + p["assessmentGrowth"]) ** t * rate
        tax_live = live_base * (1 + p["assessmentGrowth"]) ** t * rate
        collected = rent0 * 12 * (1 + c) ** k * (1 - p["vacancy"])
        noi = collected * (1 - p["management"]) - tax_full - upkeep
        taxable = noi - dep_per_year
        dep_taken += dep_per_year
        if taxable < 0:                                   # passive loss: carried forward, not used against other income
            suspended += -taxable; income_tax = 0.0
        else:
            used = min(suspended, taxable); suspended -= used
            income_tax = (taxable - used) * ordy
        rent_cash = noi - income_tax
        live_cash = -(tax_live + upkeep)
        b_unit *= 1 + p["sfRentGrowth"]                    # then limited by the SF rent ordinance (site uses 60% of CPI)
        b_cash = b_unit * (1 - p["vacancy"]) * (1 - p["management"]) * (1 - ordy)
        for key, cash in (("rent", rent_cash), ("live", live_cash), ("liveB", live_cash + b_cash)):
            res[key] = res[key] * (1 + r) + cash
        if t == 1:
            first = {"tax_full": tax_full, "tax_live": tax_live, "noi": noi, "rent_cash": rent_cash, "live_cash": live_cash,
                     "gross_rent": rent0 * 12 * (1 + c) ** k, "market": market, "upkeep": upkeep, "b_unit_cash": b_cash}
    proceeds = p["aValue"] * (1 + g) ** (k0 + hold) * (1 - p["saleCost"])
    gain = proceeds - value0
    tax_rent = max(0.0, gain) * cg
    if bshare:                                            # depreciation lowers basis; that part of the gain is taxed at up to 25% federal
        recapture_rate = cg + 0.05
        tax_rent = max(0.0, gain) * cg + dep_taken * recapture_rate - suspended * ordy
    tax_live = max(0.0, gain - (excl if hold >= 2 else 0.0)) * cg
    out.update(rent=proceeds - tax_rent + res["rent"], live=proceeds - tax_live + res["live"],
               liveB=proceeds - tax_live + res["liveB"], first=first, proceeds=proceeds, gain=gain,
               reserves=res, dep_taken=dep_taken)
    return out


def r10(x):
    return int(round(x / 10.0) * 10)


def breakeven(inherit, plan, lo=0.0, hi=0.12, **o):
    """Home-price growth at which `plan` equals selling and investing (bisection)."""
    f = lambda g: run(inherit, home=g, **o)[plan] - run(inherit, home=g, **o)["sell"]
    if f(lo) > 0 or f(hi) < 0:
        return None
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    return (lo + hi) / 2


def main():
    rows = {"inputs_read_from": "site/data/model.js", "part1": {}, "part2": {}}
    for y in (2040, 2045, 2050):
        b = run(y)
        rows["part1"][y] = {k: r10(b[k]) for k in ("value_at_death", "old_assessed", "allowance", "live_taxable", "sell",
                                                   "sell_all_growth_taxed", "sell_unrealised_taxed", "rent", "live", "liveB",
                                                   "sale_cost_loss", "sale_cost_loss_tax_value_max")}
        rows["part1"][y]["first_year"] = {k: r10(v) for k, v in b["first"].items()}
        tests = {
            "site treatment": {},
            "A tax rate 1.1636% (sum of published components) instead of 1.2%": {"a_rate": 0.011636},
            "joint return: $500,000 home-sale exclusion": {"excl": 500000},
            "depreciation, building = 20% of value (assumption)": {"bshare": 0.2},
            "depreciation, building = 40% of value (assumption)": {"bshare": 0.4},
            "rent 25% above the HUD benchmark (assumption)": {"rent": P["aRent4BR"] * 1.25},
            "home prices +5.0% a year (assumption)": {"home": 0.05},
            "home prices +6.7% a year (recorded San Jose-area average 1976-2025), portfolio unchanged": {"home": 0.067},
            "portfolio +7.0% a year after tax (assumption)": {"net": 0.07},
            "portfolio +3.0% a year after tax (assumption)": {"net": 0.03},
            "no Prop 19 relief": {"prop19": False},
        }
        part2 = {}
        for label, opt in tests.items():
            x = run(y, **opt)
            plans = {"sell": x["sell_unrealised_taxed"], "rent": x["rent"], "live": x["live"], "liveB": x["liveB"]}
            best = max(plans, key=plans.get)
            part2[label] = {**{k: r10(v) for k, v in plans.items()}, "best": best,
                            "sell_untaxed": r10(x["sell"]), "sell_all_growth_taxed": r10(x["sell_all_growth_taxed"])}
        rows["part2"][y] = part2
        rows["part1"][y]["breakeven_home_growth"] = {
            plan: (None if breakeven(y, plan) is None else round(breakeven(y, plan), 4)) for plan in ("rent", "live", "liveB")}
    json.dump(rows, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "recompute.json"), "w"), indent=1)
    for y in (2040, 2045, 2050):
        a = rows["part1"][y]
        print(f"\n== Inheritance {y}, endpoint {y + 10} ==")
        print("value at death", a["value_at_death"], "| carried assessed", a["old_assessed"], "| Prop 19 amount", a["allowance"], "| taxable if lived in", a["live_taxable"])
        print("first year:", a["first_year"])
        print("sell (site headline, growth untaxed)", a["sell"], "| all growth taxed", a["sell_all_growth_taxed"], "| unrealised part taxed", a["sell_unrealised_taxed"])
        print("rent", a["rent"], "| live", a["live"], "| live + B unit rented", a["liveB"])
        print("sale-cost capital loss", a["sale_cost_loss"], "worth at most", a["sale_cost_loss_tax_value_max"])
        print("break-even home growth:", a["breakeven_home_growth"])
        for label, v in rows["part2"][y].items():
            print(f"  {label:92s} sell {v['sell']:>11,} rent {v['rent']:>11,} live {v['live']:>11,} live+B {v['liveB']:>11,}  best: {v['best']}")


if __name__ == "__main__":
    main()
