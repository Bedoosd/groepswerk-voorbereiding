import csv

with open ("euro_summary.csv", "r") as f:
    csv_euro = csv.reader(f)
    euro_winner_year = {}
    next(csv_euro)
    for row in csv_euro:
        euro_winner_year[row[1]] = euro_winner_year.get(row[1], []) + [row[0]]
    for winner, year in euro_winner_year.items():
        print (winner, year)

with open ("euro_winners", "w") as f:
    f.write(f"Euro Winners\n\n")
    for winner, years in euro_winner_year.items():
        f.write(f"{winner} : {years}\n")

# with open ("euro_summary.csv", "r") as f:
#     csv_file = csv.reader(f)
#     winner_year = {}
#     next(csv_file)
#     for row in csv_file:
#         winner_year[row[1]] = winner_year.get(row[1], "") + f"{row[0]}, "
#     print (winner_year)
#     for winner, year in winner_year.items():
#         print (winner, year)
#
# with open ("euro_winners_simple", "w") as f:
#     f.write(f"Euro Winners\n\n")
#     for winner, years in winner_year.items():
#         f.write(f"{winner} : {years}\n")

with open ("world_cup.csv", "r") as f:
    csv_world = csv.reader(f)
    next(csv_world)
    winner_year = {}
    for row in csv_world:
        winner_year[row[3]] = winner_year.get(row[3], []) + [row[0]]
    print (winner_year)
    for winner, year in winner_year.items():
        print (winner, year)

with open ("world_winners", "w") as f:
    f.write(f"World Cup Winners\n\n")
    for winner, years in winner_year.items():
        f.write(f"{winner} : {years}\n")

# with open ("world_cup.csv", "r") as f:
#     csv_world = csv.reader(f)
#     next(csv_world)
#     winner_year = {}
#     for row in csv_world:
#         winner_year[row[3]] = winner_year.get(row[3], "") + f"{row[0]}, "
#     print (winner_year)
#     for winner, year in winner_year.items():
#         print (winner, year)
#
# with open ("world_winners_simple", "w") as f:
#     f.write(f"World Cup Winners\n\n")
#     for winner, years in winner_year.items():
#         f.write(f"{winner} : {years}\n")