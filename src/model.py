"""Projection + decision model for the inheritance dashboard.

Every input is either (a) an official figure with a source id, (b) a value supplied
in the project brief (rounded to the nearest $10 before it was stored here), or
(c) a clearly-labelled placeholder that is listed on the Flagged for Review page.
No personal identifiers are stored in this file.
"""
from __future__ import annotations

START, END = 2026, 2050
YEARS = list(range(START, END + 1))
INHERIT_YEARS = [2040, 2045, 2050]
HORIZON = 10

# ---------------------------------------------------------------- official inputs
# FHFA All-Transactions House Price Index (via FRED), index 1995Q1=100.
HPI = {
    "A": {"series": "ATNHPIUS41940Q", "1996Q2": 104.42, "2006Q2": 317.27, "2016Q2": 367.05, "2026Q2": 558.75},
    "B": {"series": "ATNHPIUS41884Q", "1996Q2": 100.83, "2006Q2": 306.74, "2016Q2": 385.01, "2026Q2": 506.53},
}


def cagr(a: float, b: float, years: float) -> float:
    return (b / a) ** (1.0 / years) - 1.0


GROWTH = {
    k: {
        "low": cagr(v["2006Q2"], v["2026Q2"], 20),   # 20-year window
        "base": cagr(v["2016Q2"], v["2026Q2"], 10),  # 10-year window
        "high": cagr(v["1996Q2"], v["2026Q2"], 30),  # 30-year window
    }
    for k, v in HPI.items()
}
# Property B's 20-year and 10-year windows are close; keep the rule identical for both.

PROP13_CAP = 0.02                 # BOE LTA 2026/002 (max annual factor)
PROP19_AMOUNT_2025_27 = 1_044_586  # BOE LTA 2025/009
HOE = 7_000                       # BOE homeowners' exemption
RATE_A = 0.011622                 # Santa Clara County FY2025-26 component sum (see sources)
RATE_B = 0.0118162182             # San Francisco FY2026-27 secured rate
RATE_B_2526 = 0.0118268325        # San Francisco FY2025-26 combined rate
CPI = 0.023                       # CBO long-run CPI-U
SF_RENT_SHARE_OF_CPI = 0.60       # SF Rent Board: 60% of Bay Area CPI-U
ESTATE_EXCL = {2026: 15_000_000, 2027: 15_480_000}  # IRS
ESTATE_RATE = 0.40
SAFMR = {"A_3br": 5_870, "A_4br": 6_390, "B_2br": 3_310}   # HUD FY2026 SAFMR, $/month
RETURNS = {"g": 0.0465, "mix": 0.0800, "c": 0.1134}        # TSP G / 50-50 / TSP C since inception

# ---------------------------------------------------------------- brief inputs (rounded to $10)
A = dict(
    fmv=3_100_000, av_2026=550_540, av_2025=539_740, tax_2025=7_210,
    water_mo=(100, 150), elec_mo=(-20, -10), insurance=1_500,
)
B = dict(
    fmv=1_800_000, av_2025=114_250, tax_2025=2_440,
    rent_mo=7_150, water_mo=(330, 400), elec_mo=(30, 70), insurance=1_500,
)
A_HISTORY = [  # year, property tax, assessed value (rounded to $10)
    (2026, None, 550_540), (2025, 7_210, 539_740), (2024, 7_000, 529_160), (2023, 6_920, 518_790),
    (2022, 6_760, 508_610), (2021, 6_660, 498_640), (2020, 6_570, 493_530), (2019, 6_570, 483_850),
    (2018, 6_380, 474_370), (2017, 6_380, 465_070), (2016, 6_410, 455_950), (2015, 6_130, 449_100),
    (2014, 5_970, 440_310),
]
B_HISTORY = [
    (2025, 2_440, 114_250), (2024, 2_320, 112_010), (2023, 2_180, 109_810), (2022, 2_110, 107_660),
    (2021, 2_070, 105_600), (2020, 2_200, 104_510), (2019, 2_130, 102_470), (2018, 2_060, 100_460),
    (2017, 1_740, 98_490), (2016, 1_680, 96_560),
]

# ---------------------------------------------------------------- placeholders (FLAGGED)
PLACEHOLDER = dict(
    maint_A=6_000,      # $/yr, 2026 dollars -- no official source, no records supplied
    maint_B=9_000,      # $/yr, 2026 dollars -- brief says B needs more upkeep than A
    sell_cost=0.06,     # share of sale price: agent fees, escrow/title, transfer tax
)

# Fixed (non-ad-valorem) charges implied by the bills in the brief: bill - rate x assessed value.
FIXED_A_2025 = A["tax_2025"] - RATE_A * A["av_2025"]
FIXED_B_2025 = B["tax_2025"] - RATE_B_2526 * B["av_2025"]


def r10(x: float) -> int:
    """Round to the nearest $10 (project rule)."""
    return int(round(x / 10.0)) * 10


def infl(base: float, year: int, base_year: int = 2026, rate: float = CPI) -> float:
    return base * (1 + rate) ** (year - base_year)


def mid(pair):
    return (pair[0] + pair[1]) / 2.0


def fmv(prop: str, year: int, scen: str = "base") -> float:
    p = A if prop == "A" else B
    return p["fmv"] * (1 + GROWTH[prop][scen]) ** (year - START)


def fbyv(prop: str, year: int) -> float:
    """Factored base year value if ownership never changes (2% assumed every year)."""
    if prop == "A":
        return A["av_2026"] * (1 + PROP13_CAP) ** (year - 2026)
    return B["av_2025"] * (1 + PROP13_CAP) ** (year - 2025)


def fixed(prop: str, year: int) -> float:
    return infl(FIXED_A_2025 if prop == "A" else FIXED_B_2025, year, 2025)


def rate(prop: str) -> float:
    return RATE_A if prop == "A" else RATE_B


def tax_current_owner(prop: str, year: int) -> float:
    return rate(prop) * fbyv(prop, year) + fixed(prop, year)


def prop19_amount(year: int, scen: str = "base") -> float:
    """$1M amount in effect after Feb 16 of `year`; adjusted every odd year by one year of HPI."""
    n = max(0, (year - 2025) // 2)
    return PROP19_AMOUNT_2025_27 * (1 + GROWTH["A"][scen]) ** n


def prop19_taxable(year: int, scen: str = "base") -> float:
    """New taxable value of A if the heir moves in within a year and claims the exclusion."""
    f, m = fbyv("A", year), fmv("A", year, scen)
    cap = f + prop19_amount(year, scen)
    return f if m <= cap else f + (m - cap)


def tax_A_live(year: int, scen: str = "base", k: int = 0) -> float:
    tv = prop19_taxable(year, scen) * (1 + PROP13_CAP) ** k
    return RATE_A * (tv - HOE) + fixed("A", year + k)


def tax_full(prop: str, year: int, scen: str = "base", k: int = 0) -> float:
    tv = fmv(prop, year, scen) * (1 + PROP13_CAP) ** k
    return rate(prop) * tv + fixed(prop, year + k)


def estate_exclusion(year: int) -> float:
    if year in ESTATE_EXCL:
        return ESTATE_EXCL[year]
    return round(ESTATE_EXCL[2027] * (1 + CPI) ** (year - 2027) / 10_000) * 10_000


# ---------------------------------------------------------------- annual cost lines
def costs_A(year: int) -> dict:
    return dict(
        insurance=infl(A["insurance"], year),
        water=infl(mid(A["water_mo"]) * 12, year),
        electricity=mid(A["elec_mo"]) * 12,   # negative = credit; held flat (NEM legacy end date unknown)
        maintenance=infl(PLACEHOLDER["maint_A"], year),
    )


def costs_B(year: int) -> dict:
    return dict(
        insurance=infl(B["insurance"], year),
        water=infl(mid(B["water_mo"]) * 12, year),
        electricity=infl(mid(B["elec_mo"]) * 12, year),
        maintenance=infl(PLACEHOLDER["maint_B"], year),
    )


def rent_B(year: int) -> float:
    return B["rent_mo"] * 12 * (1 + SF_RENT_SHARE_OF_CPI * CPI) ** (year - START)


def noi_B(year: int, reassessed_in: int | None = None, scen: str = "base") -> float:
    c = costs_B(year)
    if reassessed_in is not None and year >= reassessed_in:
        t = tax_full("B", reassessed_in, scen, year - reassessed_in)
    else:
        t = tax_current_owner("B", year)
    return rent_B(year) - t - sum(c.values())


# ---------------------------------------------------------------- decision model
def option_flows(option: str, Y: int, scen: str):
    """Yearly net cash flow (k = 1..HORIZON) of keeping Property A under `option`."""
    out = []
    for k in range(1, HORIZON + 1):
        yr = Y + k - 1
        ins, maint = infl(A["insurance"], yr), infl(PLACEHOLDER["maint_A"], yr)
        if option == "rent":
            income = infl(SAFMR["A_4br"] * 12, yr)
            tax = tax_full("A", Y, scen, k - 1)
            other = 0.0                       # tenant pays water / power (assumption)
        elif option == "live":
            income = infl(SAFMR["B_2br"] * 12, Y) * (1 + SF_RENT_SHARE_OF_CPI * CPI) ** (k - 1)
            tax = tax_A_live(Y, scen, k - 1)
            other = infl(mid(A["water_mo"]) * 12, yr)   # electricity taken as $0 (NEM status unknown)
        else:
            raise ValueError(option)
        out.append(dict(year=yr, income=income, tax=tax, insurance=ins, maintenance=maint,
                        utilities=other, net=income - tax - ins - maint - other))
    return out


def wealth(option: str, Y: int, scen: str, r: float) -> float:
    """Wealth attributable to Property A at the end of year Y+HORIZON-1, before income tax."""
    if option == "sell":
        return fmv("A", Y, scen) * (1 - PLACEHOLDER["sell_cost"]) * (1 + r) ** HORIZON
    flows = option_flows(option, Y, scen)
    acc = sum(f["net"] * (1 + r) ** (HORIZON - i - 1) for i, f in enumerate(flows))
    return fmv("A", Y + HORIZON, scen) + acc


def breakeven(option: str, Y: int, scen: str) -> float:
    """Reinvestment return at which selling ties with keeping the house under `option`."""
    lo, hi = -0.05, 0.40
    for _ in range(80):
        m = (lo + hi) / 2
        if wealth("sell", Y, scen, m) < wealth(option, Y, scen, m):
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


def total_return(prop: str, Y: int, scen: str = "base", reassessed: bool = True) -> dict:
    """Year-1 net income as a share of market value, plus the scenario appreciation rate."""
    v = fmv(prop, Y, scen)
    if prop == "A":
        net = option_flows("rent", Y, scen)[0]["net"]
    else:
        net = noi_B(Y, Y if reassessed else None, scen)
    return dict(value=v, net=net, yield_=net / v, growth=GROWTH[prop][scen], total=net / v + GROWTH[prop][scen])


def best(Y: int, scen: str, r: float):
    w = {o: wealth(o, Y, scen, r) for o in ("sell", "rent", "live")}
    return max(w, key=w.get), w


if __name__ == "__main__":
    print("growth", {k: {s: round(g * 100, 2) for s, g in v.items()} for k, v in GROWTH.items()})
    print("fixed A/B", round(FIXED_A_2025), round(FIXED_B_2025))
    for y in (2026, 2040, 2045, 2050):
        print(y, "A fmv", r10(fmv("A", y)), "fbyv", r10(fbyv("A", y)), "p19", r10(prop19_amount(y)),
              "p19 taxable", r10(prop19_taxable(y)), "tax live", r10(tax_A_live(y)),
              "tax full", r10(tax_full("A", y)), "tax now", r10(tax_current_owner("A", y)),
              "excl", estate_exclusion(y))
        print("   B fmv", r10(fmv("B", y)), "tax now", r10(tax_current_owner("B", y)), "tax full",
              r10(tax_full("B", y)), "rent", r10(rent_B(y)), "noi", r10(noi_B(y)), "noi reass", r10(noi_B(y, y)))
    for Y in INHERIT_YEARS:
        for s in ("low", "base", "high"):
            print(Y, s, "BE rent %.2f%% live %.2f%%" % (breakeven("rent", Y, s) * 100, breakeven("live", Y, s) * 100),
                  {k: (best(Y, s, r)[0], [r10(x) for x in best(Y, s, r)[1].values()]) for k, r in RETURNS.items()})
    print(option_flows("rent", 2045, "base")[0]); print(option_flows("live", 2045, "base")[0])
