from pathlib import Path
import os
cwd = os.getcwd()
births_txt_path = Path(cwd).parent / "Data" / "births" / "Births_per_year"

all_data = []
txt_files = list (births_txt_path.glob("*.txt"))
if txt_files:
    for txt_file in txt_files:
        with open(txt_file, "r") as f:
            country_line = f.readline().split()
            f.readline()  # empty line
            f.readline()  # header line
            country = country_line[0].rstrip(",")
            for line in f:
                if line:
                    add_line = f"{country},{",".join(line.split())}"
                    all_data.append(add_line)
else: print (f"No txt files found in {births_txt_path}")

with open ("births_per_year.csv", "w") as f:
    f.write("country,year,female,male,total\n")
    for row in all_data:
        f.write(row + "\n")


