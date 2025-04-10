import csv
from pathlib import Path
import os
from datetime import datetime, timedelta
cwd = os.getcwd()
euro_path = Path(cwd).parent / "Data" / "euro" / "All_matches"
world_matches = Path(cwd).parent /"Data"/"World"/ "matches_1930_2022.csv"

euro_semi_finals = {}
if euro_path.exists() and euro_path.is_dir():
    csv_files = list(euro_path.glob("*.csv"))
    if csv_files:
        for file in csv_files:
            with open(file, "r") as f:
                csv_file = csv.reader(f)
                next(csv_file)
                for row in csv_file:
                    if "SEMIFINAL" in row[26]:
                        euro_semi_finals[row[1]] = euro_semi_finals.get(row[1], []) + [row[14]] #row 14 = Date, row 13 = Year
                        euro_semi_finals[row[2]] = euro_semi_finals.get(row[2], []) + [row[14]]
    else:
        print("Geen CSV-bestanden gevonden in de map.")
else:
    print(f"Map '{euro_path}' bestaat niet of is geen directory.")

# with open("euro_semi_finals_date.txt", "w") as f:
#     for team, years in euro_semi_finals.items():
#         f.write(f"{team},{years}\n")

world_semi_finals = {}
with open(world_matches, "r") as f:
    csv_file = csv.reader(f)
    next(csv_file)
    for row in csv_file:
        if "Semi-finals" in row[15]:
            world_semi_finals[row[0]] = world_semi_finals.get(row[0], []) + [row[16]] #row 16 = Date, row 21 = year
            world_semi_finals[row[1]] = world_semi_finals.get(row[1], []) + [row[16]]

# with open("world_semi_finals_date.txt", "w") as f:
#     for team, years in world_semi_finals.items():
#         f.write(f"{team},{years}\n")

combi_semi_finals = euro_semi_finals.copy()
for key, values in world_semi_finals.items():
    combi_semi_finals[key] = combi_semi_finals.get(key, []) + values
sorted_combi_semi_finals = {key: sorted(values) for key, values in combi_semi_finals.items()}
print(sorted_combi_semi_finals)

# with open("combi_semi_finals_date.txt", "w") as f:
#     for team, years in sorted_combi_semi_finals.items():
#         f.write(f"{team}, {years}\n")

combi_plus_9_months = {}
for key, values in sorted_combi_semi_finals.items():
    for value in values:
        date = datetime.strptime(value, "%Y-%m-%d")
        datetime_9months = date + timedelta(days=266)
        date_9months = datetime_9months.strftime("%Y-%m-%d")
        combi_plus_9_months[key] = combi_plus_9_months.get(key, []) + [date_9months]

# with open ("combi_plus_266days.txt", "w") as f:
#     for team, dates in combi_plus_9_months.items():
#         f.write(f"{team}, {dates}\n")



