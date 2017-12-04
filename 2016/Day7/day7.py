#!/usr/bin/python

import sys
import re

filename = str(sys.argv[1])
f = open(filename, 'r')

abbaPresent = re.compile(u'([a-z])(?!\\1)([a-z])\\2\\1')
insideBrackets = re.compile(u'\\[[a-z]*([a-z])(?!\\1)([a-z])\\2\\1[a-z]*\\]')
#Part 2: cat input.txt | sed 's/\(.\)\1\{2,\}/\1 \1/g' | grep -Ec '(^|\])[a-z ]*(.)(.)\2.*\[[a-z ]*\3\2\3|\[[a-z ]*(.)(.)\4.*\][a-z ]*\5\4\5'


sum = 0
for line in f:
    print 'Start:',line.strip()
#    present = abbaPresent.search(line)
#    inside = insideBrackets.search(line)
#    if present != None and inside == None:
#        print 'TLS!!'
#        sum += 1
    temp = re.sub(u'\\[[a-z]*\\]','.',line)
    abaList = []
    for j in range(0,2):
        for i in re.finditer(u'([a-z])(?!\\1)[a-z]\\1',temp[j:]):
            abaList.append(i.group(0))
    for aba in abaList:
        bab = aba[1]+aba[0]+aba[1]
#        print aba,modmatched
        if re.search('\\[[a-z]*' + bab + '[a-z]*\\]',line):
            sum += 1
            print 'Match:',aba, bab
            break


print 'Total:',sum
