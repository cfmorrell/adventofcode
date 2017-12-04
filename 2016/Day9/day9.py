#!/usr/bin/python

import sys
import re

filename = str(sys.argv[1])
f = open(filename, 'r').read()

regex = re.compile(u'(?<=\()[0-9]*x[0-9]*(?=\))')

decompressed = ''
loc = 0
while 1:
    marker = regex.findall(f,loc)[0]
    length = int(marker.split('x')[0])
    repeats = int(marker.split('x')[1])
    copyStartIndex = f.find(marker,loc)+len(marker)+1
    beforeCopyIndex = copyStartIndex-len(marker)-2
#    print 'Just add this stuff:',f[loc:beforeCopyIndex]
    decompressed += f[loc:beforeCopyIndex]
#    print 'Copy this stuff:',f[copyStartIndex:copyStartIndex+length]
    decompressed += f[copyStartIndex:copyStartIndex+length]*repeats
    print len(decompressed)
    loc = copyStartIndex+length
    if loc >= len(f):
        break
