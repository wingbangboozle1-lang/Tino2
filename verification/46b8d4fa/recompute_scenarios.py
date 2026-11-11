#!/usr/bin/env python3
"""
Session 46b8d4fa - task K-2, part 2: independent replication of the black-swan numbers.

The landing page and the Best plan page show (a) twelve scenarios - six replays of recorded
official annual series and six stated assumptions - and (b) 2,000 random 50-year histories
built by re-ordering five-year blocks of the recorded years 1977-2025. The pages compute
them in the browser (site/data/history-engine.js). This script computes them again in
Python and compares every figure the two pages render.

Inputs read at run time:
  * the base settings the pages use (from the export written by tools/export_published.cjs);
  * the official annual series shipped with the site (site/data/history.js: BLS CPI-U, FHFA
    house-price indexes, Treasury 10-year yield, OECD share prices, via FRED). No household data.

The scenario definitions below are the ones the Recorded data page states in words.
The random histories reuse the page's published seed (20261111), so the same 2,000 histories
are drawn; the generator is re-implemented here with explicit 32-bit arithmetic.

Usage:  node verification/46b8d4fa/tools/export_published.cjs
        python3 verification/46b8d4fa/recompute_scenarios.py        # exit 1 on any difference
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
EXPORT = REPO / ".cache" / "46b8d4fa" / "published.json"
START, N = 2026, 50
CPI, EQ, BOND = 0.023, 0.07, 0.045            # baseline stated on the Sources page (CBO-anchored CPI; equities and yield assumptions)
EQ_WEIGHT, DIVIDEND = 0.6, 0.02               # 60/40 portfolio; +2.0 points for dividends missing from the price index


def round10(x: float) -> int:
    return int(math.floor(x / 10 + 0.5)) * 10


def money(text: str):
    m = re.search(r"([\-\u2212]?)\s*\$\s?([\d,]+)", text)
    if not m:
        return None
    v = int(m.group(2).replace(",", ""))
    return -v if m.group(1) else v


def load_history():
    src = (REPO / "site" / "data" / "history.js").read_text(encoding="utf-8")
    data = json.loads(src[src.index("{"): src.rindex("}") + 1])
    cols = data["columns"]
    return {row[0]: dict(zip(cols, row)) for row in data["rows"]}


class Engine:
    def __init__(self, base: dict, hist: dict):
        self.B, self.H = base, hist
        self.home0 = base["appreciation"]
        self.spread = base["expenseInflation"] - CPI
        self.drag = base["portfolioTaxDrag"]

    # ---- recorded data
    def g(self, col, y):
        a, b = self.H.get(y), self.H.get(y - 1)
        if a is None or b is None or a.get(col) is None or b.get(col) is None:
            return None
        return a[col] / b[col] - 1

    def hist_year(self, y):
        cpi = self.g("cpi", y)
        first = lambda *xs: next(x for x in xs if x is not None)
        return dict(home=first(self.g("sj", y), self.g("ca", y), cpi), homeB=first(self.g("sf", y), self.g("ca", y), cpi),
                    cpi=cpi, eq=self.g("eq", y) + DIVIDEND, bond=self.H[y]["gs10"] / 100)

    def window(self, a, b):
        return [self.hist_year(y) for y in range(a, b + 1)]

    # ---- the twelve scenarios, as described on the Recorded data page
    def scenarios(self):
        base = dict(cpi=CPI, eq=EQ, bond=BOND)
        flat = lambda **kw: dict(base, **kw)
        return [
            dict(id="baseline", name="Smooth baseline", seq=[]),
            dict(id="replay50", name="Replay of the last 49 years", seq=self.window(1977, 2025), fixed=2027),
            dict(id="stagflation", name="1970s-style stagflation", seq=self.window(1973, 1982)),
            dict(id="gfc", name="2008-style housing and equity crash", seq=self.window(2006, 2012)),
            dict(id="bust90", name="Early-1990s Bay Area bust", seq=self.window(1990, 1996)),
            dict(id="dotcom", name="Equity-only crash (2000–2003 style)", seq=self.window(2000, 2003)),
            dict(id="infl2123", name="2021–23 inflation spike", seq=self.window(2021, 2023)),
            dict(id="lost", name="Lost decades (flat nominal prices)", seq=[dict(home=0, homeB=0, cpi=0.005, eq=0.03, bond=0.015)] * 15),
            dict(id="insurance", name="Insurance and climate-cost shock",
                 seq=[flat(home=-0.03 if i < 5 else self.home0, homeB=-0.03 if i < 5 else self.home0, insExtra=0.12) for i in range(10)]),
            dict(id="policyTax", name="Property-tax regime change (assessments track market)", seq=[], flags=dict(assessFollowsMarket=True)),
            dict(id="noProp19", name="Prop 19 inheritance relief repealed", seq=[], flags=dict(noProp19=True)),
            dict(id="perfect", name="Compound shock: stagflation → 2008-style crash + insurance shock",
                 seq=[dict(r, insExtra=0.08) for r in self.window(1973, 1982)] + self.window(2006, 2012)),
        ]

    def build_path(self, sc, shock_start=None):
        p = dict(home=[self.home0] * (N + 1), homeB=[self.home0] * (N + 1), cpi=[CPI] * (N + 1), eq=[EQ] * (N + 1),
                 bond=[BOND] * (N + 1), insExtra=[0.0] * (N + 1))
        start = sc.get("fixed") or shock_start or 2042
        for k, r in enumerate(sc["seq"]):
            i = start - START + k
            if 1 <= i <= N:
                for key in ("home", "homeB", "cpi", "eq", "bond"):
                    p[key][i] = r[key]
                p["insExtra"][i] = r.get("insExtra", 0)
        p["flags"] = dict(sc.get("flags", {}))
        p["shockStart"] = start
        return p

    # ---- derived series and the four strategies
    def derive(self, p):
        B = self.B
        d = dict(cpiI=[1.0], mA=[B["aValue"]], mB=[B["bValue"]], fbA=[B["aAssessed"]], costI=[1.0], rentI=[1.0], insI=[1.0], sfg=[0.0], port=[0.0])
        for i in range(1, N + 1):
            cpi = p["cpi"][i]
            d["cpiI"].append(d["cpiI"][-1] * (1 + cpi))
            d["mA"].append(d["mA"][-1] * (1 + p["home"][i]))
            d["mB"].append(d["mB"][-1] * (1 + p["homeB"][i]))
            d["fbA"].append(d["fbA"][-1] * (1 + min(0.02, cpi)))               # Prop 13: lower of CPI and 2 %
            cost_g = max(-0.5, cpi + self.spread)                              # costs and market rent: CPI + 0.7 pt
            d["costI"].append(d["costI"][-1] * (1 + cost_g))
            d["rentI"].append(d["rentI"][-1] * (1 + cost_g))
            d["insI"].append(d["insI"][-1] * (1 + cost_g + (p["insExtra"][i] or 0)))
            d["sfg"].append(min(0.07, max(0, 0.6 * (cpi + 0.004))))            # SF covered units: 60 % of CPI (+0.4 pt regional), cap 7 %
            d["port"].append(EQ_WEIGHT * p["eq"][i] + (1 - EQ_WEIGHT) * p["bond"][i] - self.drag)
        return d

    def prop19_cap(self, d, year):
        amount = self.B["prop19Amount"]
        for j in range(1, max(0, (year - 2025) // 2) + 1):                     # one year's price change per biennial adjustment
            i = min(N, 2 * j - 1)
            amount *= d["mA"][i] / d["mA"][i - 1]
        return amount

    def simulate(self, p, inherit_year, hold=10, rent_key="aRent4BR"):
        B, d = self.B, self.derive(p)
        flags = p.get("flags", {})
        shock = p.get("shockStart") or START
        follows = lambda yr: bool(flags.get("assessFollowsMarket")) and yr >= shock
        Y = inherit_year - START
        T = Y + hold
        MY, fb, cap = d["mA"][Y], d["fbA"][Y], self.prop19_cap(d, inherit_year)
        primary = MY if flags.get("noProp19") else (fb if MY <= fb + cap else MY - cap)
        net = MY * (1 - B["saleCost"])
        sell = net
        for t in range(Y + 1, T + 1):
            sell *= 1 + d["port"][t]
        lad_rent, lad_live = MY, primary
        res_rent = res_live = res_live_sf = 0.0
        sf_unit = B["bRent1BR"] * 12 * d["rentI"][Y]
        for t in range(Y + 1, T + 1):
            yr = START + t
            f = 1 + min(0.02, p["cpi"][t])
            lad_rent *= f
            lad_live *= f
            a_rent = d["mA"][t] if follows(yr) else min(lad_rent, d["mA"][t])
            a_live = d["mA"][t] if follows(yr) else min(lad_live, d["mA"][t])
            fixed = (B["aWaterMonthly"] * 12 * d["costI"][t] + B["aInsuranceAnnual"] * d["insI"][t]
                     + d["mA"][t] * B["maintenanceA"] - B["aSolarMonthlyCredit"] * 12)
            gross = B[rent_key] * 12 * d["rentI"][t]
            noi = gross * (1 - B["vacancy"]) * (1 - B["management"]) - a_rent * B["aRate"] - fixed
            rent_cash = noi - max(0, noi) * B["ordinaryTax"]
            live_cash = -(a_live * B["aRate"] + fixed)
            sf_unit *= 1 + d["sfg"][t]
            sf_net = sf_unit * (1 - B["vacancy"]) * (1 - B["management"]) * (1 - B["ordinaryTax"])
            res_rent = res_rent * (1 + d["port"][t]) + rent_cash
            res_live = res_live * (1 + d["port"][t]) + live_cash
            res_live_sf = res_live_sf * (1 + d["port"][t]) + live_cash + sf_net
        realized = d["mA"][T] * (1 - B["saleCost"])
        gain = max(0, realized - MY)
        excl = min(B["primaryGainExclusion"], gain) if hold >= 2 else 0
        tax_rent, tax_live = gain * B["capitalGainsTax"], max(0, gain - excl) * B["capitalGainsTax"]
        out = dict(sell=sell, sellLiq=sell - max(0, sell - net) * B["capitalGainsTax"], rent=realized - tax_rent + res_rent,
                   live=realized - tax_live + res_live, liveSF=realized - tax_live + res_live_sf)
        best = "sell"
        for k in ("sell", "rent", "live", "liveSF"):
            if out[k] > out[best]:
                best = k
        out["best"] = best
        return out

    # ---- 2,000 random histories (seeded block bootstrap of 1977-2025)
    @staticmethod
    def mulberry32(seed):
        a = seed & 0xFFFFFFFF
        imul = lambda x, y: (x * y) & 0xFFFFFFFF

        def rnd():
            nonlocal a
            a = (a + 0x6D2B79F5) & 0xFFFFFFFF
            t = imul(a ^ (a >> 15), 1 | a)
            t = ((t + imul(t ^ (t >> 7), 61 | t)) & 0xFFFFFFFF) ^ t
            return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296
        return rnd

    def monte_carlo(self, paths=2000, block=5, seed=20261111, years=(2040, 2045, 2050), hold=10):
        vec = self.window(1977, 2025)
        geo = lambda key: math.exp(sum(math.log(1 + r[key]) for r in vec) / len(vec)) - 1
        shift = dict(home=self.home0 - geo("home"), homeB=self.home0 - geo("homeB"), cpi=CPI - geo("cpi"), eq=EQ - geo("eq"), bond=BOND - geo("bond"))
        rnd = self.mulberry32(seed)
        keys = ("sell", "sellLiq", "rent", "live", "liveSF")
        R = {y: {k: [] for k in keys} for y in years}
        for _ in range(paths):
            p = dict(home=[0.0], homeB=[0.0], cpi=[0.0], eq=[0.0], bond=[0.0], insExtra=[0.0], flags={})
            while len(p["home"]) <= N:
                s = int(math.floor(rnd() * (len(vec) - block + 1)))
                for j in range(block):
                    if len(p["home"]) > N:
                        break
                    r = vec[s + j]
                    p["home"].append(max(-0.6, r["home"] + shift["home"]))
                    p["homeB"].append(max(-0.6, r["homeB"] + shift["homeB"]))
                    p["cpi"].append(max(-0.05, r["cpi"] + shift["cpi"]))
                    p["eq"].append(max(-0.9, r["eq"] + shift["eq"]))
                    p["bond"].append(max(0, r["bond"] + shift["bond"]))
                    p["insExtra"].append(0.0)
            for y in years:
                out = self.simulate(p, y, hold)
                for k in keys:
                    R[y][k].append(out[k])

        def q(arr, pr):
            s = sorted(arr)
            return s[min(len(s) - 1, max(0, int(math.floor(pr * (len(s) - 1)))))]
        summary = {}
        for y in years:
            n = len(R[y]["sell"])
            best = {k: 0 for k in ("sell", "rent", "live", "liveSF")}
            for i in range(n):
                b = "sell"
                for k in ("sell", "rent", "live", "liveSF"):
                    if R[y][k][i] > R[y][b][i]:
                        b = k
                best[b] += 1
            summary[y] = dict(p10={k: q(R[y][k], 0.1) for k in keys}, p50={k: q(R[y][k], 0.5) for k in keys}, p90={k: q(R[y][k], 0.9) for k in keys},
                              best={k: v / n for k, v in best.items()},
                              sellLiqBeatsRent=sum(1 for i in range(n) if R[y]["sellLiq"][i] > R[y]["rent"][i]) / n)
        return summary


def table(pub, page, fragment):
    for t in pub["pages"].get(page, {}).get("tables", []):
        if fragment.lower() in t["heading"].lower():
            return t
    return None


def main():
    if not EXPORT.exists():
        print("missing export - run: node verification/46b8d4fa/tools/export_published.cjs")
        return 2
    pub = json.loads(EXPORT.read_text(encoding="utf-8"))
    eng = Engine(pub["base"], load_history())
    scs = eng.scenarios()
    checks, diffs, missing = 0, [], []

    def cmp(where, label, published, expected):
        nonlocal checks
        checks += 1
        if published != expected:
            diffs.append(dict(where=where, item=label, published=published, recomputed=expected))

    results = {y: [(sc, eng.simulate(eng.build_path(sc), y)) for sc in scs] for y in (2040, 2045, 2050)}
    mc = eng.monte_carlo()

    # Best plan page, default selection 2045: twelve scenarios x four plans, and the random-history table
    t = table(pub, "site/plan.html", "Does the ranking survive")
    if t:
        label = dict(sell="Sell", rent="Rent", live="Live", liveSF="Live + rent B unit")
        for row, (sc, out) in zip(t["rows"], results[2045]):
            cmp("plan.html scenarios 2045", sc["name"] + " · name", row["cells"][0], sc["name"])
            for i, k in enumerate(("sell", "rent", "live", "liveSF"), start=2):
                cmp("plan.html scenarios 2045", f"{sc['name']} · {k}", money(row["cells"][i]), round10(out[k]))
            cmp("plan.html scenarios 2045", sc["name"] + " · best is sell?", row["cells"][6].strip().startswith("Sell"), out["best"] == "sell")
    else:
        missing.append("site/plan.html: scenario table")
    t = table(pub, "site/plan.html", "2,000 random")
    if t:
        for row, key in zip(t["rows"], ("p10", "p50", "p90")):
            for i, k in enumerate(("sell", "rent", "live"), start=1):
                cmp("plan.html random histories 2045", f"{key} {k}", money(row["cells"][i]), round10(mc[2045][key][k]))
    else:
        missing.append("site/plan.html: random-history table")

    # Landing page: black-swan check by inheritance year
    t = table(pub, "index.html", "Growth and inflation are never steady")
    if t:
        for row in t["rows"]:
            y = int(re.search(r"(20\d\d)", row["cells"][0]).group(1))
            sell_best = [sc["name"] for sc, out in results[y] if out["best"] == "sell"]
            keep_best = [sc["name"] for sc, out in results[y] if out["best"] != "sell"]
            cmp("index.html black-swan check", f"{y} scenarios where selling is best", row["cells"][1], f"{len(sell_best)} of {len(scs)}")
            cmp("index.html black-swan check", f"{y} scenarios where keeping wins", row["cells"][2], "; ".join(keep_best) if keep_best else "None")
            cmp("index.html black-swan check", f"{y} random histories selling best", row["cells"][3], f"{mc[y]['best']['sell'] * 100:.0f}%")
            cmp("index.html black-swan check", f"{y} poor decade sell", money(row["cells"][4]), round10(mc[y]["p10"]["sell"]))
            cmp("index.html black-swan check", f"{y} poor decade rent", money(row["cells"][5]), round10(mc[y]["p10"]["rent"]))
    else:
        missing.append("index.html: black-swan table")

    print(f"commit checked: {pub.get('commit')}")
    print(f"scenario and random-history figures recomputed and compared: {checks}; differences: {len(diffs)}; tables not found: {len(missing)}")
    for y in (2040, 2045, 2050):
        n_sell = sum(1 for _, o in results[y] if o["best"] == "sell")
        print(f"  {y}: selling best in {n_sell} of {len(scs)} scenarios; random histories: sell first {mc[y]['best']['sell']:.1%}, rent first {mc[y]['best']['rent']:.1%}, "
              f"live first {(mc[y]['best']['live'] + mc[y]['best']['liveSF']):.1%}; sell still ahead of rent when the portfolio is also taxed: {mc[y]['sellLiqBeatsRent']:.1%}")
    for dd in diffs:
        print("  DIFF", dd)
    for mm in missing:
        print("  TABLE NOT FOUND", mm)
    return 1 if (diffs or missing) else 0


if __name__ == "__main__":
    sys.exit(main())
