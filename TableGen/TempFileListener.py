import sys
import time
import os

def removetemp(url):
    try:
        time.sleep(0.5) #delay for the browser to open
        os.remove(url)
    #if the browser is still loading give it more time
    except PermissionError:
        removetemp(url)

try:
    time.sleep(0.5)
    removetemp(sys.argv[1])
except IndexError:
    pass