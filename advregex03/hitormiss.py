#!/usr/bin/env python3
import re
mytxt = open('grimm.txt') # open file ojbect

allLines = mytxt.readlines() # read out of buffer into list

mytxt.close() # close file

lookingfor = re.compile(r'wol[vf][es]?\w+') # compile
                               ## a search expression
lookfor2 = re.compile(r'gut[en][i]?\w+',re.IGNORECASE)
lookfor3 = re.compile(r'mi?\w+')
l2 = []
l3 = []
for oneline in allLines:   # search through the lines
    mymatchobj = lookingfor.search(oneline) # call
                      ## search() and pass oneline 
    myobj2 = lookfor2.search(oneline)
    if myobj2:
        l2.append(myobj2.group())
    myobj3 = lookfor3.search(oneline)
    if myobj3:
        l3.append(myobj3.group())

    if mymatchobj: # if mymatchobj has a value (if a match, then...)
            print(mymatchobj.group(), '***', oneline, end='') # Print
                 ## what was matched on, ***, then the string matched

print("\n\n\n",l2)
print("\n\n\n",l3)

