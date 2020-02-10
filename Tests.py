from TableGen import Table

table = Table.fromCsv("pokemon.csv", rowlimit= 20,index=True)

print(table.TableString)
