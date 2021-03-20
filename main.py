import csv

# fonction avec les operateur or ou and .
f = open("nfl_data.csv")
nfl = csv.reader(f)

def nfl_wins(team,year):
  count = 0
  for row in nfl:
    if row[2] == team and row[0]==year:
      count += 1
  return(count)

#en argument il suffit du nom de l'equipe et de l'annee rechercher.
victoire = nfl_wins(input(),input())
print(victoire,"victoire")