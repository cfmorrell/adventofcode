#!/usr/bin/python

import sys
import hashlib
    
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

testdoorid = 'abc'
realdoorid = 'ffykfhsq'

doorid = realdoorid

password = ['_','_','_','_','_','_','_','_']
found = [0,0,0,0,0,0,0,0]
count = 0
while 1:
    index = doorid + str(count)
    thisHash = hashlib.md5(index).hexdigest()
    if thisHash.startswith('00000') and RepresentsInt(thisHash[5]) and int(thisHash[5]) <= 7 and found[int(thisHash[5])] == 0:
        password[int(thisHash[5])] = thisHash[6]
        found[int(thisHash[5])] = 1 
        print ''.join(password)
    if 0 not in found:
        break
    count += 1

