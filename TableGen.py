from tkinter.filedialog import asksaveasfile
import tkinter
import webbrowser
import datetime
import os
import time
import asyncio

DeafultHTMLStyle ="<style>\n table.gen-table {\n font-family: Tahoma, Geneva, sans-serif;\n border: 1px solid #1C6EA4;\n background-color: #EEEEEE;\n width: 100%;\n text-align: left;\n border-collapse: collapse;\n }\n table.gen-table td, table.gen-table th {\n border: 1px solid #AAAAAA;\n padding: 3px 2px;\n }\n table.gen-table tbody td {\n font-size: 13px;\n }\n table.gen-table tr:nth-child(even) {\n background: #D0E4F5;\n }\n table.gen-table thead {\n background: #1C6EA4;\n background: -moz-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);\n background: -webkit-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);\n background: linear-gradient(to bottom, #5592bb 0%, #327cad 66%, #1C6EA4 100%);\n border-bottom: 2px solid #444444;\n }\n table.gen-table thead th {\n font-size: 15px;\n font-weight: bold;\n color: #FFFFFF;\n border-left: 2px solid #D0E4F5;\n }\n table.gen-table thead th:first-child {\n border-left: none;\n }\n table.gen-table tfoot td {\n font-size: 14px;\n }\n table.gen-table tfoot .links {\n text-align: right;\n }\n table.gen-table tfoot .links a{\n display: inline-block;\n background: #1C6EA4;\n color: #FFFFFF;\n padding: 2px 8px;\n border-radius: 5px;\n }\n </style>\n"

#helper function to delete temp HTML file after the broser opened

async def removetemp(url):
    await asyncio.sleep(0.5) #delay for the browser to open
    os.remove(url)

#function to view HTML in the browser

def viewHTML(htmlstring):

    #make temp file name

   prefix = str(datetime.datetime.now().timestamp()*1000) +"_"
   filename = prefix +"temphtml.html"
   url = os.getcwd() + "\\" + filename
    #write to the file
   with open(filename, 'w', encoding="utf-8-sig") as tempfile:
       tempfile.write(htmlstring)
    #open the browser
   webbrowser.open(url)
    #remove the file
   asyncio.run(removetemp(url))

#helper function to make an index for the dictionary
def makeindex(leng):
    templist = ['#']
    for i in range(1,leng+1):
        templist.append(str(i))
    return templist


def listify(dict, index = False):
    final = {'totallen@#':0}
    if index:
        indexlist = makeindex(len(dict))
        final["#"] =  {'list':indexlist,'maxlen':getMaxLen(indexlist)}

    for key in list(dict[0].keys()):
        final[key] = {'list':[key] }
        for row in dict:
            final[key]['list'].append(row[key].replace("\n"," ").replace("\t"," "))
        final[key]['maxlen'] = getMaxLen(final[key]['list'])
        final['totallen@#'] = final['totallen@#'] + getMaxLen(final[key]['list'])
    return final

def getMaxLen(listofstr):
    max = 0
    for strng in listofstr:
        if max < len(str(strng)):
            max =len(str(strng))
    return max


def stringTableFromDict(dict ,xLineChar = "-", YLineChar = "|", index = False , rowlimit = "all"):

    listObj = listify(dict, index =index)
    linelen = 0
    rowlist = []
    line = ''
    final = ''
    for i in list(range(0,len(dict)+1)):
        tempstr = YLineChar
        for key in listObj.keys():
            if key != 'totallen@#':
                tempstr = tempstr +" " + str(listObj[key]['list'][i]).replace('\n'," ").replace("\t"," ") + " " *(listObj[key]['maxlen'] - len(str(listObj[key]['list'][i]))) + " " + YLineChar



        if i == 0:
            line = xLineChar *len(tempstr)





        tempstr = tempstr +"\n" +line

        rowlist.append(tempstr)


    final = line + final
    if rowlimit == "all":
        return  line+"\n" + ("\n").join(rowlist)
    else:
        return line+"\n" + ("\n").join(rowlist[0:rowlimit+1])

def HTMLTableFromDict(dict, style = DeafultHTMLStyle , title = "Generated Table" , index =False ,rowlimit = "all" ,HTMLtableclass = 'gen-table'):
    if index:
        tempdict = []
        for indx,row in enumerate(dict):
            temprow = {"#": str(indx +1)}
            for key in row.keys():
                temprow[key] = row[key]
            tempdict.append(temprow)
        dict = tempdict
            
    if rowlimit != "all":
        dict = dict[0:rowlimit]
    finalstring = "<!DOCTYPE html>\n<html>\n<head>\n" + style + "<title>" +title+"</title>\n" + "</head>\n" +"<body>\nTablePlaceHolder\n</body>\n</html>"
    finaltable =  "</table>"
    tablehead = "<table class=\""+HTMLtableclass+"\">\n<thead>\n<tr>\nHeaderPlaceHolder\n</tr>\n</thead>\n"
    innerhead  = ''
    rows = []
    for key in dict[0].keys():
        innerhead = innerhead + "<th>"+key+"</th>\n"
    tablehead = tablehead.replace("HeaderPlaceHolder", innerhead)
    for row in dict:
        tempstr = "<tr>\n<td>P</td>\n</tr>".replace("P","</td>\n<td>".join(list(row.values())))
        rows.append(tempstr)
    rowsstring = "".join(rows)
    finaltable = tablehead + "<tbody>" + rowsstring + "</tbody>" +finaltable
    finalstring = finalstring.replace("TablePlaceHolder",finaltable)


    return finalstring





class Table():
    def __init__(self,dict ,xLineChar = "-", YLineChar = "|", index = False , rowlimit = "all" , title = "Generated Table" ,HTMLstyle = DeafultHTMLStyle , HTMLtableclass = 'gen-table'):
        self.dict = dict
        self.TableString = stringTableFromDict(dict ,xLineChar = xLineChar, YLineChar = YLineChar, index = index , rowlimit = rowlimit)
        self.HTMLString = HTMLTableFromDict(dict , style = HTMLstyle , title=title  , rowlimit=rowlimit , index = index ,HTMLtableclass=HTMLtableclass)
    def savetxt(self):
        filename = asksaveasfile(mode = 'w' ,defaultextension = '.txt').name
        print(filename)
        with open(filename , 'w' , encoding = 'utf-8-sig') as saveHere:
            saveHere.write(self.TableString)
    def viewHTML(self):
        viewHTML(self.HTMLString)

    def saveHTML(self):
        filename = asksaveasfile(mode='w', defaultextension='.html').name
        with open(filename, 'w', encoding='utf-8-sig') as saveHere:
            saveHere.write(self.HTMLString)



