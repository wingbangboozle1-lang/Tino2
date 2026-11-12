#!/usr/bin/env python3
"""Transcription of the California Department of Insurance 2026 Homeowners Premium Survey
for the two survey locations that match this project, plus summary statistics.

Every figure below was read on 2026-11-12 (UTC) directly from the Department's own comparison
tool at interactive.web.insurance.ca.gov. The survey prices HYPOTHETICAL risks; it is not a quote
and none of these figures is a premium for either property in this project.

Run:  python3 research/60ca3e1f/build_insurance_survey.py
Writes insurance-survey-2026.json next to this file and prints the summary table.
"""
import json, os, statistics, urllib.parse

BASE = "https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:21::SUBMIT:NO::"

def url(location, cover, age=None, amount=None):
    q = urllib.parse.quote
    if age is None:
        return f"{BASE}P21_LOCATION,P21_TYPE,P21_SUBMIT:{q(location)},{q(cover)},Y"
    return (f"{BASE}P21_LOCATION,P21_TYPE,P21_HOME_AGE,P21_INSURANCE_AMOUNT,P21_SUBMIT:"
            f"{q(location)},{q(cover)},{q(age)},{amount},Y")

CUP = "SANTA CLARA CUPERTINO"
SUN = "SAN FRANCISCO SAN FRANCISCO-Sunset District"
NA = None

# company: (premium with $2,500 deductible, premium with $5,000 deductible)
HOMEOWNERS = {
 "cupertino_40y_1000000": {
  "location": CUP, "home_age": "40 Years", "coverage": 1000000, "profiles": [377, 477],
  "rows": {
   "Aegis Security Ins Co": (4082, 3608),
   "Amica Mutual Ins Co": (3116, 2731),
   "Armed Forces Ins Exch": (3268, 3028),
   "ASI Select Ins Corp": (2911, 2654),
   "California Automobile Ins Co (Mercury Group)": (1784, 1569),
   "California Capital Ins Co (Auto Owners Group)": (1767, 1629),
   "California Cas Indemnity Exch": (4135, 3656),
   "CSAA Ins Exch": (2127, 1939),
   "DB Ins Co. LTD (U.S. Branch)": (4202, 3722),
   "Farmers Ins Exchange (Farmers Group)": (3659, 3438),
   "Federal Ins Co (Chubb Group)": (4677, 4247),
   "General Ins Co of Amer": (3415, 2962),
   "Grange Ins Association": (6430, 5942),
   "Homesite Ins Co of the Midwest": (2025, 1918),
   "Horace Mann Ins Co": (3968, 3185),
   "Horace Mann Prop & Cas Ins Co": (4739, 3803),
   "Incline Cas Co": (2581, 2274),
   "Integon National Ins Co": (2162, 1651),
   "Interins Exch of the Automobile Club (AAA)": (NA, 3994),
   "MAPFRE Ins Co": (2405, 2084),
   "Metromile Ins Co": (4132, 3927),
   "Nationwide Mutual Ins Co": (2690, 2240),
   "Obsidian Pacific Ins Co": (2581, 2274),
   "Pacific Specialty Ins Co": (1543, 1355),
   "Privilege Underwriters Reciprocal Exch (PURE)": (4433, 3534),
   "Residence Mutual Ins Co (Western Mutual Group)": (4095, 3604),
   "Safeco Ins Co of America (Safeco Group)": (2473, 2061),
   "Spinnaker Ins Co": (2044, 1802),
   "Standard Fire Ins Co (Travelers Group)": (2598, 2460),
   "Stillwater Ins Co": (2275, 2041),
   "Stillwater Prop & Cas Co": (2345, 2104),
   "Sutton National Ins Co": (2581, 2274),
   "United Serv Automobile Assn (USAA)": (NA, 2698),
   "Universal N Amer (DBA One Alliance N Amer Ins Co)": (4968, 4471),
   "US Coastal P&C Ins Co (DBA Pacific Coastal P&C)": (1785, 1632),
   "Wawanesa General Ins Co": (2741, 2545),
   "Zurich American Ins Co": (2008, 1895),
  }},
 "cupertino_70y_1000000": {
  "location": CUP, "home_age": "70 Years", "coverage": 1000000, "profiles": [387, 487],
  "rows": {
   "Aegis Security Ins Co": (4158, 3674),
   "Amica Mutual Ins Co": (3461, 3033),
   "Armed Forces Ins Exch": (3033, 2823),
   "ASI Select Ins Corp": (2956, 2694),
   "California Automobile Ins Co (Mercury Group)": (1671, 1479),
   "California Capital Ins Co (Auto Owners Group)": (1625, 1508),
   "California Cas Indemnity Exch": (3964, 3510),
   "CSAA Ins Exch": (2127, 1939),
   "DB Ins Co. LTD (U.S. Branch)": (3942, 3492),
   "Farmers Ins Exchange (Farmers Group)": (3448, 3258),
   "Federal Ins Co (Chubb Group)": (4677, 4247),
   "General Ins Co of Amer": (3415, 2962),
   "Homesite Ins Co of the Midwest": (2132, 2019),
   "Horace Mann Ins Co": (3968, 3185),
   "Horace Mann Prop & Cas Ins Co": (4739, 3803),
   "Incline Cas Co": (2741, 2429),
   "Integon National Ins Co": (2162, 1651),
   "Interins Exch of the Automobile Club (AAA)": (NA, 3656),
   "MAPFRE Ins Co": (2524, 2188),
   "Metromile Ins Co": (4040, 3865),
   "Nationwide Mutual Ins Co": (2625, 2201),
   "Obsidian Pacific Ins Co": (2741, 2429),
   "Pacific Specialty Ins Co": (1642, 1450),
   "Privilege Underwriters Reciprocal Exch (PURE)": (4433, 3534),
   "Residence Mutual Ins Co (Western Mutual Group)": (4095, 3604),
   "Safeco Ins Co of America (Safeco Group)": (2473, 2061),
   "Spinnaker Ins Co": (1598, 1418),
   "Standard Fire Ins Co (Travelers Group)": (2551, 2429),
   "Stillwater Ins Co": (2182, 1958),
   "Stillwater Prop & Cas Co": (2250, 2019),
   "Sutton National Ins Co": (2741, 2429),
   "United Serv Automobile Assn (USAA)": (NA, 2636),
   "Universal N Amer (DBA One Alliance N Amer Ins Co)": (4968, 4471),
   "US Coastal P&C Ins Co (DBA Pacific Coastal P&C)": (1909, 1745),
   "Wawanesa General Ins Co": (2526, 2351),
   "Zurich American Ins Co": (1969, 1859),
  }},
 "sunset_40y_1000000": {
  "location": SUN, "home_age": "40 Years", "coverage": 1000000, "profiles": [377, 477],
  "rows": {
   "Aegis Security Ins Co": (4749, 4196),
   "Amica Mutual Ins Co": (4016, 3504),
   "Armed Forces Ins Exch": (3353, 3105),
   "ASI Select Ins Corp": (4107, 3727),
   "California Automobile Ins Co (Mercury Group)": (3062, 2699),
   "California Capital Ins Co (Auto Owners Group)": (2628, 2483),
   "California Cas Indemnity Exch": (4926, 4354),
   "CSAA Ins Exch": (2632, 2393),
   "DB Ins Co. LTD (U.S. Branch)": (5409, 4789),
   "Farmers Ins Exchange (Farmers Group)": (3776, 3539),
   "Federal Ins Co (Chubb Group)": (4883, 4208),
   "General Ins Co of Amer": (4991, 4329),
   "Grange Ins Association": (6836, 6317),
   "Homesite Ins Co of the Midwest": (2018, 1912),
   "Horace Mann Ins Co": (8961, 7192),
   "Horace Mann Prop & Cas Ins Co": (10384, 8333),
   "Incline Cas Co": (2739, 2412),
   "Integon National Ins Co": (2982, 2277),
   "Interins Exch of the Automobile Club (AAA)": (NA, 3941),
   "MAPFRE Ins Co": (4227, 3664),
   "Metromile Ins Co": (2972, 2757),
   "Nationwide Mutual Ins Co": (3653, 3039),
   "Obsidian Pacific Ins Co": (2739, 2412),
   "Pacific Specialty Ins Co": (1328, 1166),
   "Privilege Underwriters Reciprocal Exch (PURE)": (7698, 6076),
   "Residence Mutual Ins Co (Western Mutual Group)": (6345, 5583),
   "Safeco Ins Co of America (Safeco Group)": (3342, 2785),
   "Spinnaker Ins Co": (2684, 2372),
   "Standard Fire Ins Co (Travelers Group)": (2216, 2065),
   "Stillwater Ins Co": (1874, 1680),
   "Stillwater Prop & Cas Co": (2318, 2080),
   "Sutton National Ins Co": (2739, 2412),
   "United Serv Automobile Assn (USAA)": (NA, 2733),
   "Universal N Amer (DBA One Alliance N Amer Ins Co)": (9833, 8842),
   "US Coastal P&C Ins Co (DBA Pacific Coastal P&C)": (2754, 2545),
   "Wawanesa General Ins Co": (3094, 2887),
   "Zurich American Ins Co": (3353, 3162),
  }},
 "sunset_70y_1000000": {
  "location": SUN, "home_age": "70 Years", "coverage": 1000000, "profiles": [387, 487],
  "rows": {
   "Aegis Security Ins Co": (4837, 4274),
   "Amica Mutual Ins Co": (4461, 3892),
   "Armed Forces Ins Exch": (3095, 2879),
   "ASI Select Ins Corp": (4169, 3783),
   "California Automobile Ins Co (Mercury Group)": (2985, 2642),
   "California Capital Ins Co (Auto Owners Group)": (2572, 2447),
   "California Cas Indemnity Exch": (4729, 4183),
   "CSAA Ins Exch": (2632, 2393),
   "DB Ins Co. LTD (U.S. Branch)": (5072, 4491),
   "Farmers Ins Exchange (Farmers Group)": (3424, 3238),
   "Federal Ins Co (Chubb Group)": (4883, 4208),
   "General Ins Co of Amer": (4991, 4329),
   "Homesite Ins Co of the Midwest": (2117, 2005),
   "Horace Mann Ins Co": (8961, 7192),
   "Horace Mann Prop & Cas Ins Co": (10384, 8333),
   "Incline Cas Co": (2908, 2576),
   "Integon National Ins Co": (2982, 2277),
   "Interins Exch of the Automobile Club (AAA)": (NA, 3605),
   "MAPFRE Ins Co": (4437, 3845),
   "Metromile Ins Co": (2669, 2491),
   "Nationwide Mutual Ins Co": (3563, 2985),
   "Obsidian Pacific Ins Co": (2908, 2576),
   "Pacific Specialty Ins Co": (1413, 1248),
   "Privilege Underwriters Reciprocal Exch (PURE)": (7698, 6076),
   "Residence Mutual Ins Co (Western Mutual Group)": (6345, 5583),
   "Safeco Ins Co of America (Safeco Group)": (3342, 2785),
   "Spinnaker Ins Co": (2143, 1907),
   "Standard Fire Ins Co (Travelers Group)": (2079, 1947),
   "Stillwater Ins Co": (1797, 1611),
   "Stillwater Prop & Cas Co": (2224, 1995),
   "Sutton National Ins Co": (2908, 2576),
   "United Serv Automobile Assn (USAA)": (NA, 2658),
   "Universal N Amer (DBA One Alliance N Amer Ins Co)": (9833, 8842),
   "US Coastal P&C Ins Co (DBA Pacific Coastal P&C)": (2841, 2628),
   "Wawanesa General Ins Co": (2896, 2710),
   "Zurich American Ins Co": (3287, 3101),
  }},
}

# Earthquake, single-family profile 901. Value = annual premium per $1,000 of coverage,
# or the text the survey shows instead ("CEA" = sold through the California Earthquake Authority).
EQ_ORDER = ["Aegis Security Ins Co","Amica Mutual Ins Co","Armed Forces Ins Exch","ASI Select Ins Corp",
 "California Automobile Ins Co (Mercury Group)","California Capital Ins Co (Auto Owners Group)",
 "California Cas Indemnity Exch","Coastal Select Ins Co","CSAA Ins Exch","DB Ins Co. LTD (U.S. Branch)",
 "Farmers Ins Exchange (Farmers Group)","Federal Ins Co (Chubb Group)","General Ins Co of Amer","Geovera Ins Co",
 "Grange Ins Association","Homesite Ins Co of CA","Horace Mann Ins Co","Horace Mann Prop & Cas Ins Co",
 "Incline Cas Co","Integon National Ins Co","Interins Exch of the Automobile Club (AAA)","MAPFRE Ins Co",
 "Metromile Ins Co","Nationwide Mutual Ins Co","Obsidian Pacific Ins Co","Pacific Specialty Ins Co",
 "Palomar Specialty Ins Co","Privilege Underwriters Reciprocal Exch (PURE)",
 "Residence Mutual Ins Co (Western Mutual Group)","Safeco Ins Co of America (Safeco Group)","Spinnaker Ins Co",
 "Standard Fire Ins Co (Travelers Group)","Stillwater Ins Co","Stillwater Prop & Cas Co","Sutton National Ins Co",
 "United Serv Automobile Assn (USAA)","Universal N Amer (DBA One Alliance N Amer Ins Co)",
 "US Coastal P&C Ins Co (DBA Pacific Coastal P&C)","Wawanesa General Ins Co","Zurich American Ins Co"]
F, C = "See Footnotes", "CEA"
EQ_CUP = [F,C,C,C,C,5.08,7.40,1.88,C,15,C,2.19,C,2.75,1.86,F,2.51,2.51,F,3.40,C,C,F,C,F,8,3.10,2.00,1.15,C,F,3.08,7.50,7.50,F,C,3.25,F,C,3.10]
EQ_SUN = [F,C,C,C,C,6.46,4.48,2.49,C,15,C,2.23,C,6.17,1.86,F,3.29,3.29,F,3.40,C,C,F,C,F,8,3.10,2.24,1.13,C,F,6.17,7.50,7.50,F,C,3.25,F,C,3.10]
assert len(EQ_ORDER) == len(EQ_CUP) == len(EQ_SUN) == 40

def stats(values):
    v = sorted(x for x in values if x is not None)
    return {"priced": len(v), "lowest": v[0], "median": statistics.median(v), "highest": v[-1],
            "at_or_below_1500": sum(1 for x in v if x <= 1500)}

out = {"read_on": "2026-11-12", "effective": "2026-05-01",
       "tool": "https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:20",
       "not_a_quote": True, "homeowners": {}, "earthquake_single_family": {}}
print(f"{'profile':24} {'ded.':>6} {'priced':>6} {'lowest':>7} {'median':>8} {'highest':>8} {'<=1500':>6}")
for key, block in HOMEOWNERS.items():
    rows = block["rows"]
    s2500 = stats([a for a, b in rows.values()])
    s5000 = stats([b for a, b in rows.values()])
    out["homeowners"][key] = {
        "location": block["location"], "home_age": block["home_age"], "coverage": block["coverage"],
        "profiles": {"deductible_2500": block["profiles"][0], "deductible_5000": block["profiles"][1]},
        "companies_listed": len(rows),
        "url": url(block["location"], "HOMEOWNERS", block["home_age"], block["coverage"]),
        "deductible_2500": s2500, "deductible_5000": s5000,
        "rows": [{"company": c, "deductible_2500": a, "deductible_5000": b} for c, (a, b) in rows.items()],
    }
    print(f"{key:24} {2500:>6} {s2500['priced']:>6} {s2500['lowest']:>7} {s2500['median']:>8} {s2500['highest']:>8} {s2500['at_or_below_1500']:>6}")
    print(f"{'':24} {5000:>6} {s5000['priced']:>6} {s5000['lowest']:>7} {s5000['median']:>8} {s5000['highest']:>8} {s5000['at_or_below_1500']:>6}")

for key, loc, vals in (("cupertino", CUP, EQ_CUP), ("sunset", SUN, EQ_SUN)):
    nums = sorted(v for v in vals if isinstance(v, (int, float)))
    out["earthquake_single_family"][key] = {
        "location": loc, "profile": 901, "companies_listed": len(vals),
        "url": url(loc, "EARTHQUAKE - Single Family"),
        "rate_per_1000": {"priced": len(nums), "lowest": nums[0], "median": statistics.median(nums), "highest": nums[-1]},
        "through_cea": vals.count(C), "see_footnotes": vals.count(F),
        "rows": [{"company": c, "value": v} for c, v in zip(EQ_ORDER, vals)],
    }
    print(f"earthquake {key:10} listed {len(vals)}  rate/1000 priced {len(nums)} low {nums[0]} median {statistics.median(nums)} high {nums[-1]}  CEA {vals.count(C)}  footnotes {vals.count(F)}")

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "insurance-survey-2026.json")
with open(path, "w") as fh:
    json.dump(out, fh, indent=1)
    fh.write("\n")
print("wrote", os.path.relpath(path))
