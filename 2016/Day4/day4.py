#!/usr/bin/python

import sys
import re
import operator
import string

filename = str(sys.argv[1])
f = open(filename, 'r')

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

sum = 0
for line in f:
    count = {}
    #print line
    room = re.search('^[a-z\-]+(?=[0-9])',line).group(0)
    #print room
    room2 = re.sub('-','',room)
    #print 'Room:',room
    sectionid = int(re.search('(?!-)[0-9]+(?=\[)',line).group(0))
    #print 'Section:',sectionid
    rot = sectionid % 26
    #print 'Rot:',rot
    checksum = re.search('(?!\[)[a-z]{5}(?=\])',line).group(0)
    #print 'Checksum:',checksum
    for c in room2:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    value = ''.join(sorted(count, key=lambda k: (-count[k], k))[:5])
    #print 'Value:',value
    if value == checksum:
#        print 'Valid Room'
#        print room, str(sectionid), checksum
        print re.sub('-',' ',caesar(room,rot)),str(sectionid)
        sum += sectionid
    #else:
    #    print 'Invalid Room'

#print sum
