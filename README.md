
# TableGen 

### Quickly convert a list of dictionaries to human readable tables

## Install
```
pip install tablegen
```

## Create Table Object

```
from TableGen import Table

dict = [
    {"name": "Joseph" ,"age": 45, "favorite Animal": "Zebra" },
    {"name": "Jane" ,"age": 39, "favorite Animal": "Cat" },
    {"name": "Alex" ,"age": 57, "favorite Animal": "Black Bear" }
        ]

table = Table(dict)

``` 
now 

``` 
print(table.TableString)
``` 

will print
```
----------------------------------
| name   | age | favorite Animal |
----------------------------------
| Joseph | 45  | Zebra           |
----------------------------------
| Jane   | 39  | Cat             |
----------------------------------
| Alex   | 57  | Black Bear      |
----------------------------------
```

## add index with the index option

```
dict = [
    {"name": "Joseph" ,"age": 45, "favorite Animal": "Zebra" },
    {"name": "Jane" ,"age": 39, "favorite Animal": "Cat" },
    {"name": "Alex" ,"age": 57, "favorite Animal": "Black Bear" }
        ]

table = Table(dict,index=True)


print(table.TableString)
```
output is:
```
--------------------------------------
| # | name   | age | favorite Animal |
--------------------------------------
| 1 | Joseph | 45  | Zebra           |
--------------------------------------
| 2 | Jane   | 39  | Cat             |
--------------------------------------
| 3 | Alex   | 57  | Black Bear      |
--------------------------------------
```
## Limit Rows

you can limit the number of rows contained in the string and HTML table:
```
from TableGen import Table  
  
dict = [  
    {"name": "Joseph" ,"age": 45, "favorite Animal": "Zebra" },  
  {"name": "Jane" ,"age": 39, "favorite Animal": "Cat" },  
  {"name": "Alex" ,"age": 57, "favorite Animal": "Black Bear" }  
        ]  
  
table = Table(dict ,rowlimit= 2)  
  
print(table.TableString)  
```

output is :
```
----------------------------------
| name   | age | favorite Animal |
----------------------------------
| Joseph | 45  | Zebra           |
----------------------------------
| Jane   | 39  | Cat             |
----------------------------------

```
## change appearance of the text table

### change the vertical and horizontal lines with yLineChar and xLineChar:

```
from TableGen import Table  
  
dict = [  
    {"name": "Joseph" ,"age": 45, "favorite Animal": "Zebra" },  
  {"name": "Jane" ,"age": 39, "favorite Animal": "Cat" },  
  {"name": "Alex" ,"age": 57, "favorite Animal": "Black Bear" }  
        ]  
  
table = Table(dict ,xLineChar= "++", yLineChar="║")  
  
print(table.TableString)
```
output:
```
++++++++++++++++++++++++++++++++++
║ name   ║ age ║ favorite Animal ║
++++++++++++++++++++++++++++++++++
║ Joseph ║ 45  ║ Zebra           ║
++++++++++++++++++++++++++++++++++
║ Jane   ║ 39  ║ Cat             ║
++++++++++++++++++++++++++++++++++
║ Alex   ║ 57  ║ Black Bear      ║
++++++++++++++++++++++++++++++++++
```


### Change header with headertop, headerbottom and headery:
```
from TableGen import Table  
  
dict = [  
    {"name": "Joseph" ,"age": 45, "favorite Animal": "Zebra" },  
  {"name": "Jane" ,"age": 39, "favorite Animal": "Cat" },  
  {"name": "Alex" ,"age": 57, "favorite Animal": "Black Bear" }  
        ]  
  
table = Table(dict ,headertop= "_-+-_",headerbottom= "══.══",headerY= "{}" )  
  
print(table.TableString)
```

output:
```
_-+-__-+-__-+-__-+-__-+-__-+-__-+-__-+
{} name   {} age {} favorite Animal {}
══.════.════.════.════.════.════.════.
|  Joseph  | 45   | Zebra            |
--------------------------------------
|  Jane    | 39   | Cat              |
--------------------------------------
|  Alex    | 57   | Black Bear       |
--------------------------------------
```

## Save as txt file
the savetxt() methood can be used to save the table string in a file . this will open a tkinter save dialog.
![save dialog](https://i.ibb.co/TWXkBdY/2020-02-09-15-22-14-Save-As.png)

## HTML Tables
A Table object also contains an html string of this table.
```
from TableGen import Table  
  
dict = [  
    {"name": "Joseph" ,"age": 45, "favorite Animal": "Zebra" },  
  {"name": "Jane" ,"age": 39, "favorite Animal": "Cat" },  
  {"name": "Alex" ,"age": 57, "favorite Animal": "Black Bear" }  
        ]  
  
table = Table(dict)  
  
print(table.HTMLString)
```
output:

```
<!DOCTYPE html>
<html>
<head>
<style>
 table.gen-table {
 font-family: Tahoma, Geneva, sans-serif;
 border: 1px solid #1C6EA4;
 background-color: #EEEEEE;
 width: 100%;
 text-align: left;
 border-collapse: collapse;
 }
 table.gen-table td, table.gen-table th {
 border: 1px solid #AAAAAA;
 padding: 3px 2px;
 }
 table.gen-table tbody td {
 font-size: 13px;
 }
 table.gen-table tr:nth-child(even) {
 background: #F88888;
 }
 table.gen-table thead {
 background: #900C3F ;
 border-bottom: 2px solid #444444;
 }
 table.gen-table thead th {
 font-size: 15px;
 font-weight: bold;
 color: #FFFFFF;
 border-left: 2px solid #D0E4F5;
 }
 table.gen-table thead th:first-child {
 border-left: none;
 }
 table.gen-table tfoot td {
 font-size: 14px;
 }
 table.gen-table tfoot .links {
 text-align: right;
 }
 table.gen-table tfoot .links a{
 display: inline-block;
 background: #1C6EA4;
 color: #FFFFFF;
 padding: 2px 8px;
 border-radius: 5px;
 }
 </style>
<title>Generated Table</title>
</head>
<body>
<table class="gen-table">
<thead>
<tr>
<th>name</th>
<th>age</th>
<th>favorite Animal</th>

</tr>
</thead>
<tbody>

<tr>
<td>Joseph</td>
<td>45</td>
<td>Zebra</td>
</tr>

<tr>
<td>Jane</td>
<td>39</td>
<td>Cat</td>
</tr>

<tr>
<td>Alex</td>
<td>57</td>
<td>Black Bear</td>
</tr>

</tbody>
</table>
</body>
</html>

```
the viewHTML() method can be used to open the html in browser using the webbrowser module.
```
from TableGen import Table  
  
dict = [  
    {"name": "Joseph" ,"age": 45, "favorite Animal": "Zebra" },  
  {"name": "Jane" ,"age": 39, "favorite Animal": "Cat" },  
  {"name": "Alex" ,"age": 57, "favorite Animal": "Black Bear" }  
        ]  
  
table = Table(dict)  
  
table.viewHTML()
```

this will open the default web browser  with the table

![](https://i.ibb.co/SV2CJVL/2020-02-09-15-22-14-Save-As.png)

## Change table css
you can insert custom css and change the class of the table in the HTML by using the options HTMLstyle and HTMLtableclass
```
from TableGen import Table  
  
dict = [  
    {"name": "Joseph" ,"age": 45, "favorite Animal": "Zebra" },  
  {"name": "Jane" ,"age": 39, "favorite Animal": "Cat" },  
  {"name": "Alex" ,"age": 57, "favorite Animal": "Black Bear" }  
        ]  
style = '''  
.changedtable{  
border: solid;  
border-color : black;  
}  
  
.changedtable th{  
padding: 5px;  
background-color: #cce6ff;  
}  
  
.changedtable td{  
padding: 5px;  
background-color: #f2ffcc;  
}  
  
'''  
  
table = Table(dict,HTMLstyle=style,HTMLtableclass='changedtable')  
  
table.viewHTML()
```
this is the table generated from this code.

![](https://i.ibb.co/JrFH7y4/2020-02-10-14-08-35-Generated-Table.png)

## Get Table Directly from CSV 
a Table object can be created from a CSV file using the fromCsv() method.
```
from TableGen import Table  
  
table = Table.fromCsv("pokemon.csv", rowlimit= 20,index=True)  
  
print(table.TableString)
``` 
output:
```
-----------------------------------------------------------------------------------------------------------------------------------------------
| #   | Name                      | Type 1   | Type 2   | Total | HP  | Attack | Defense | Sp. Atk | Sp. Def | Speed | Generation | Legendary |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 1   | Bulbasaur                 | Grass    | Poison   | 318   | 45  | 49     | 49      | 65      | 65      | 45    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 2   | Ivysaur                   | Grass    | Poison   | 405   | 60  | 62     | 63      | 80      | 80      | 60    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 3   | Venusaur                  | Grass    | Poison   | 525   | 80  | 82     | 83      | 100     | 100     | 80    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 4   | VenusaurMega Venusaur     | Grass    | Poison   | 625   | 80  | 100    | 123     | 122     | 120     | 80    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 5   | Charmander                | Fire     |          | 309   | 39  | 52     | 43      | 60      | 50      | 65    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 6   | Charmeleon                | Fire     |          | 405   | 58  | 64     | 58      | 80      | 65      | 80    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 7   | Charizard                 | Fire     | Flying   | 534   | 78  | 84     | 78      | 109     | 85      | 100   | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 8   | CharizardMega Charizard X | Fire     | Dragon   | 634   | 78  | 130    | 111     | 130     | 85      | 100   | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 9   | CharizardMega Charizard Y | Fire     | Flying   | 634   | 78  | 104    | 78      | 159     | 115     | 100   | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 10  | Squirtle                  | Water    |          | 314   | 44  | 48     | 65      | 50      | 64      | 43    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 11  | Wartortle                 | Water    |          | 405   | 59  | 63     | 80      | 65      | 80      | 58    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 12  | Blastoise                 | Water    |          | 530   | 79  | 83     | 100     | 85      | 105     | 78    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 13  | BlastoiseMega Blastoise   | Water    |          | 630   | 79  | 103    | 120     | 135     | 115     | 78    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 14  | Caterpie                  | Bug      |          | 195   | 45  | 30     | 35      | 20      | 20      | 45    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 15  | Metapod                   | Bug      |          | 205   | 50  | 20     | 55      | 25      | 25      | 30    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 16  | Butterfree                | Bug      | Flying   | 395   | 60  | 45     | 50      | 90      | 80      | 70    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 17  | Weedle                    | Bug      | Poison   | 195   | 40  | 35     | 30      | 20      | 20      | 50    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 18  | Kakuna                    | Bug      | Poison   | 205   | 45  | 25     | 50      | 25      | 25      | 35    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 19  | Beedrill                  | Bug      | Poison   | 395   | 65  | 90     | 40      | 45      | 80      | 75    | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
| 20  | BeedrillMega Beedrill     | Bug      | Poison   | 495   | 65  | 150    | 40      | 15      | 80      | 145   | 1          | FALSE     |
-----------------------------------------------------------------------------------------------------------------------------------------------
```
