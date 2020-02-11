from tkinter.filedialog import asksaveasfile
import sys
import webbrowser
import datetime
import os
import time
import csv
from subprocess import Popen

DeafultHTMLStyle ="<style>\n table.gen-table {\n font-family: Tahoma, Geneva, sans-serif;\n border: 1px solid #1C6EA4;\n background-color: #EEEEEE;\n width: 100%;\n text-align: left;\n border-collapse: collapse;\n }\n table.gen-table td, table.gen-table th {\n border: 1px solid #AAAAAA;\n padding: 3px 2px;\n }\n table.gen-table tbody td {\n font-size: 13px;\n }\n table.gen-table tr:nth-child(even) {\n background: #F88888;\n }\n table.gen-table thead {\n background: #900C3F ;\n border-bottom: 2px solid #444444;\n }\n table.gen-table thead th {\n font-size: 15px;\n font-weight: bold;\n color: #FFFFFF;\n border-left: 2px solid #D0E4F5;\n }\n table.gen-table thead th:first-child {\n border-left: none;\n }\n table.gen-table tfoot td {\n font-size: 14px;\n }\n table.gen-table tfoot .links {\n text-align: right;\n }\n table.gen-table tfoot .links a{\n display: inline-block;\n background: #1C6EA4;\n color: #FFFFFF;\n padding: 2px 8px;\n border-radius: 5px;\n }\n </style>\n"


#invoked if some of the values are not string values
def castValuesToStr(dict):
    for item in dict:
        for key in item.keys():
            item[key] = str(item[key])


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
    #remove the file - listen with a subprocess when the browser is done with loading
   Popen([sys.executable,"./TempFileListener.py",url])



#helper function to make an index for the dictionary
def makeindex(leng):
    templist = ['#']
    for i in range(1,leng+1):
        templist.append(str(i))
    return templist

#helper function to make a string table
def listify(dict, index = False):
    final = {'totallen@#':0}
    #add an index if the index option is true
    if index:
        indexlist = makeindex(len(dict))
        final["#"] =  {'list':indexlist,'maxlen':getMaxLen(indexlist)}
    #convert the dictionary list to one dictionary of columns that includes the header
    for key in list(dict[0].keys()):
        final[key] = {'list':[key] }
        #append values to the list
        for row in dict:
            final[key]['list'].append(str(row[key]).replace("\n"," ").replace("\t"," "))
        #get max cell and row length
        final[key]['maxlen'] = getMaxLen(final[key]['list'])
        final['totallen@#'] = final['totallen@#'] + getMaxLen(final[key]['list'])
    return final

#helper function to get the maximum lenght of items in a list
def getMaxLen(listofstr):
    max = 0
    for strng in listofstr:
        if max < len(str(strng)):
            max =len(str(strng))
    return max

#function to generate a string pretty table from dict list
def stringTableFromDict(dict ,xLineChar = "-", yLineChar = "|", index = False , rowlimit = "all" , headerbottom = None , headertop = None ,headerY = None ):


    #listfy the object and set global vars
    fixY = ''
    fixHeaderY = ''
    listObj = listify(dict, index =index)
    linelen = 0
    rowlist = []
    line = ''
    final = ''
    if headerbottom is None:
        headerbottom = xLineChar
    if headertop is None:
        headertop = xLineChar
    if headerY is None:
        headerY = yLineChar
    #make a string to make up for length diffrences beetween headerY & yLineChar
    if len(headerY) > len(yLineChar):
        fixY = " " * (len(headerY) - len(yLineChar))
    elif len(headerY) < len(yLineChar):
        fixHeaderY = " " * (len(yLineChar) - len(headerY))





    #for each index in the original object make a line string
    for i in list(range(0,len(dict)+1)):
        #init the line string with Ychar
        tempstr = yLineChar + fixY
        for key in listObj.keys():

            #ignore the total lenght key in the listObj and fro every other key create a cell acording to the index
            if key != 'totallen@#':
                tempstr = tempstr +" "+ str(listObj[key]['list'][i]).replace('\n'," ").replace("\t"," ") + " " *(listObj[key]['maxlen'] - len(str(listObj[key]['list'][i]))) + " " +fixY+ yLineChar

        #only for the first loop get the length of rows and init the line seprator string
        if i == 0:
            line = xLineChar *round(len(tempstr)/len(xLineChar))
            headertopline = headertop*round(len(tempstr)/len(headertop))
            headerbottomline = headerbottom*round(len(tempstr)/len(headerbottom))
            tempstr = headerY+fixHeaderY+ tempstr[len(yLineChar + fixY):len(tempstr)-len(yLineChar+fixY)].replace(fixY+yLineChar,fixHeaderY + headerY)+fixHeaderY+ headerY
            #fix lenghts
            if len(line) >  len(tempstr):
                line = line[0:len(tempstr)]
            if len(line) <  len(tempstr):
                line = line + xLineChar[0:len(tempstr)-len(line)]
            if len(headertopline) >  len(tempstr):
                headertopline = headertopline[0:len(tempstr)]
            if len(headertopline) <  len(tempstr):
                headertopline = headertopline + headertop[0:len(tempstr)-len(headertopline)]
            if len(headerbottomline) >  len(tempstr):
                headerbottomline = headerbottomline[0:len(tempstr)]
            if len(headerbottomline) <  len(headertopline):
                headerbottomline = headerbottomline + headerbottom[0:len(tempstr)-len(headerbottomline)]

            #make final string
            tempstr = headertopline + "\n" + tempstr +"\n"+ headerbottomline
            rowlist.append(tempstr)
        else:
            #final line sting
            tempstr = tempstr +"\n" +line
            #append the final string to a list
            rowlist.append(tempstr)


    #if the rowlimit var is set to "all"(default) return a string with all row using the join function
    if rowlimit == "all":
        return    ("\n").join(rowlist)

    # if the rowlimit var is set to "all"(default) return a string with all row using the join function
    else:
        return   ("\n").join(rowlist[0:rowlimit+1])

#function to generate an HTML string from dictlist
def HTMLTableFromDict(dict, style = DeafultHTMLStyle , title = "Generated Table" , index =False ,rowlimit = "all" ,HTMLtableclass = 'gen-table'):

    if "<style>" not in style:
        style = "<style>\n" + style +"\n</style>"
    #create an index if the index option is set to True
    if index:
        tempdict = []
        for indx,row in enumerate(dict):
            temprow = {"#": str(indx +1)}
            for key in row.keys():
                temprow[key] = row[key]
            tempdict.append(temprow)
        dict = tempdict

    #set the row limit if its not set to all
    if rowlimit != "all":
        dict = dict[0:rowlimit]

    #set vars containig html tags with palceholders
    finalstring = "<!DOCTYPE html>\n<html>\n<head>\n" + style + "<title>" +title+"</title>\n" + "</head>\n" +"<body>\nTablePlaceHolder\n</body>\n</html>"
    finaltable =  "</table>"
    tablehead = "<table class=\""+HTMLtableclass+"\">\n<thead>\n<tr>\nHeaderPlaceHolder\n</tr>\n</thead>\n"
    innerhead  = ''
    rows = []
    #create the headers
    for key in dict[0].keys():
        innerhead = innerhead + "<th>"+key+"</th>\n"
    tablehead = tablehead.replace("HeaderPlaceHolder", innerhead)

    #for each row create a matching <tr> tag and append it to a list
    for row in dict:
        tempstr = ''
        try:
            tempstr = "\n<tr>\n<td>P</td>\n</tr>\n".replace("P","</td>\n<td>".join(list(row.values())))
        except TypeError:
            #one type error will trigger the function for all the rows.
            castValuesToStr(dict)
            tempstr = "\n<tr>\n<td>P</td>\n</tr>".replace("P", "</td>\n<td>".join(list(row.values())))
        rows.append(tempstr)

    #join the list
    rowsstring = "".join(rows)
    #create the final string and return it
    finaltable = tablehead + "<tbody>\n" + rowsstring + "\n</tbody>\n" +finaltable
    finalstring = finalstring.replace("TablePlaceHolder",finaltable)


    return finalstring




#the table class recives a dictionary list Object and returns a Table object containing a human readable string table and a html string
class Table():
    #init the table and use the parameters to make the TableString and HTMLString
    def __init__(self,dict ,xLineChar = "-", yLineChar = "|", index = False,headerbottom = None, headertop = None ,headerY = None  , rowlimit = "all" , title = "Generated Table" ,HTMLstyle = DeafultHTMLStyle , HTMLtableclass = 'gen-table'):
        self.dict = dict
        self.TableString = stringTableFromDict(dict ,xLineChar = xLineChar, yLineChar = yLineChar, index = index,headerbottom = headerbottom, headertop = headertop ,headerY = headerY  , rowlimit = rowlimit)
        self.HTMLString = HTMLTableFromDict(dict , style = HTMLstyle , title=title  , rowlimit=rowlimit , index = index ,HTMLtableclass=HTMLtableclass)
    #the fromCsv methood recives a csv path and returns a Table Object
    @classmethod
    def fromCsv(cls,csvpath,xLineChar = "-", yLineChar = "|",headerbottom = None, headertop = None ,headerY = None , index = False , rowlimit = "all" , title = "Generated Table" ,HTMLstyle = DeafultHTMLStyle , HTMLtableclass = 'gen-table'):
        tempdictlist = []
        if csvpath.split(".")[-1] == "csv":
            with open(csvpath , 'r' , encoding = 'utf-8-sig') as csvfile:
                for row in csv.DictReader(csvfile):
                    tempdictlist.append(row)
            return cls(tempdictlist,xLineChar =xLineChar ,yLineChar = yLineChar,index=index ,rowlimit=rowlimit,HTMLstyle =HTMLstyle , HTMLtableclass = HTMLtableclass)

    #save the TableString as a txt file using tkinter's asksaveasfile
    def savetxt(self):
        filename = asksaveasfile(mode = 'w' ,defaultextension = '.txt').name
        print(filename)
        with open(filename , 'w' , encoding = 'utf-8-sig') as saveHere:
            saveHere.write(self.TableString)

    #open a browser to view html table
    def viewHTML(self):
        viewHTML(self.HTMLString)

    # save the HTMLString as an html file using tkinter's asksaveasfile
    def saveHTML(self):
        filename = asksaveasfile(mode='w', defaultextension='.html').name
        with open(filename, 'w', encoding='utf-8-sig') as saveHere:
            saveHere.write(self.HTMLString)





