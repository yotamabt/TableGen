


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
                tempstr = tempstr +" " + str(listObj[key]['list'][i]) + " " *(listObj[key]['maxlen'] - len(str(listObj[key]['list'][i]))) + " " + YLineChar

               
                
        if i == 0:
            line = xLineChar *len(tempstr)
            linelen  = len(tempstr)



             
        tempstr = tempstr +"\n" +line
        
        rowlist.append(tempstr)
       
    final = line + final
    if rowlimit == "all":
        return line+"\n" + ("\n").join(rowlist)
    else:
        return
