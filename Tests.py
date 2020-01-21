from TableGen import Table,HTMLTableFromDict,viewHTML
import csv
import array
TEST =[]


with open('annual-enterprise-survey-2018-financial-year-provisional-csv.csv' , 'r' ,encoding='utf-8-sig',newline= '') as testfile:
    read = csv.DictReader(testfile)
    for row in read:
        TEST.append(row)


table = Table(TEST ,index =True ,rowlimit = 100)
print(table.TableString)
table.viewHTML()




