import TableGen
import csv
import array
TEST =[]

with open('AIRItemsResults207.csv' , 'r' ,encoding='utf-8-sig',newline= '') as testfile:
    read = csv.DictReader(testfile)
    for row in read:
        TEST.append(row)

print(TableGen.stringTableFromDict(TEST  , index =True))
