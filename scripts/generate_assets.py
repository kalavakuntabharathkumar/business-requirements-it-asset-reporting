from pathlib import Path
import pandas as pd

OUT = Path("data/assets_120k.csv")
OUT.parent.mkdir(parents=True, exist_ok=True)
types = ["Laptop", "Monitor", "Mobile", "Server", "Tablet", "Printer"]
departments = ["Engineering", "Finance", "Sales", "IT Operations", "Human Resources", "Marketing"]
locations = ["Bengaluru", "Hyderabad", "Chennai", "Pune", "Delhi"]
statuses = ["In Use", "In Storage", "Under Repair", "Retired"]
criticalities = ["Low", "Medium", "High", "Critical"]

rows = []
for i in range(1, 120001):
    rows.append({
        "asset_id": f"AST-{i:06d}",
        "asset_type": types[i % len(types)],
        "department": departments[i % len(departments)],
        "owner": f"User {((i - 1) % 8500) + 1}",
        "location": locations[i % len(locations)],
        "purchase_date": pd.Timestamp("2019-01-01") + pd.Timedelta(days=(i * 13) % 2800),
        "last_seen": pd.Timestamp("2026-10-14") - pd.Timedelta(days=(i * 7) % 180),
        "asset_status": statuses[i % len(statuses)],
        "criticality": criticalities[i % len(criticalities)],
        "cost": [18000, 28000, 42000, 78000, 250000, 310000][i % 6],
    })
pd.DataFrame(rows).to_csv(OUT, index=False, date_format="%Y-%m-%d")
print(f"Generated {len(rows):,} synthetic asset records at {OUT}")
