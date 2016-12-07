#!/usr/bin/python

import sys
import re

filename = str(sys.argv[1])
f = open(filename, 'r')
newfile = open('out.txt','w')
abbaPresent = re.compile(u'([a-z])(?!\\1)([a-z])\\2\\1')
insideBrackets = re.compile(u'\\[[a-z]*([a-z])(?!\\1)([a-z])\\2\\1[a-z]*\\]')
abaBefore = re.compile(u'([a-z])(?!\\1)([a-z])\\1.*\\[.*\\2\\1\\2.*\\]')
abaAfter = re.compile(u'\\[.*([a-z])(?!\\1)([a-z])\\1.*\\].*\\2\\1\\2')
aba = re.compile(u'(\\[[a-z]*([a-z])(?!\\2)([a-z])\\2[a-z]*\\].*\\3\\2\\3|([a-z])(?!\\4)([a-z])\\4.*\\[[a-z]*\\5\\4\\5[a-z]*\\])')

sum = 0
for line in f:
    print line
#    present = abbaPresent.search(line)
#    inside = insideBrackets.search(line)
#    if present != None and inside == None:
#        print 'TLS!!'
#        sum += 1
   # before = abaBefore.search(line)
   # after = abaAfter.search(line)
    result = aba.search(line)
    if result:
        newfile.write(line.strip()+'\n')
        sum += 1


print 'Total:',sum
