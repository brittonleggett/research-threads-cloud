import csv
from collections import defaultdict

rows = defaultdict(dict)  # (year) -> {item: [values]}

with open("USDA_ERS_Historical_Meat_Price_Spreads_1970-present.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for r in reader:
        year = int(r["Year"])
        item = r["Data_Item"]
        try:
            val = float(r["Value"])
        except ValueError:
            continue
        rows[(year, item)].setdefault("vals", []).append(val)

def annual_avg(year, item):
    key = (year, item)
    if key not in rows:
        return None
    vals = rows[key]["vals"]
    return sum(vals) / len(vals)

years = sorted(set(y for (y, i) in rows.keys()))
print("Year,BeefFarmShare%,PorkFarmShare%")
beef_series = []
pork_series = []
for y in years:
    beef_net = annual_avg(y, "Choice beef net farm value")
    beef_retail = annual_avg(y, "Choice beef retail value")
    pork_net = annual_avg(y, "Pork net farm value")
    pork_retail = annual_avg(y, "Pork retail value")
    beef_share = round(100 * beef_net / beef_retail, 1) if beef_net and beef_retail else None
    pork_share = round(100 * pork_net / pork_retail, 1) if pork_net and pork_retail else None
    if beef_share is not None:
        beef_series.append((y, beef_share))
    if pork_share is not None:
        pork_series.append((y, pork_share))
    print(f"{y},{beef_share if beef_share is not None else ''},{pork_share if pork_share is not None else ''}")

def decade_avg(series, y0, y1):
    vals = [v for (y, v) in series if y0 <= y <= y1]
    return round(sum(vals) / len(vals), 1) if vals else None

print("\n--- Decade averages, beef farm share % of retail ---")
for y0 in range(1970, 2030, 10):
    y1 = y0 + 9
    a = decade_avg(beef_series, y0, y1)
    if a is not None:
        print(f"{y0}-{min(y1,2026)}: {a}%")

print("\n--- Decade averages, pork farm share % of retail ---")
for y0 in range(1970, 2030, 10):
    y1 = y0 + 9
    a = decade_avg(pork_series, y0, y1)
    if a is not None:
        print(f"{y0}-{min(y1,2026)}: {a}%")

print("\n--- First 5 vs last 5 years available ---")
print("Beef first5:", beef_series[:5])
print("Beef last5:", beef_series[-5:])
print("Pork first5:", pork_series[:5])
print("Pork last5:", pork_series[-5:])
