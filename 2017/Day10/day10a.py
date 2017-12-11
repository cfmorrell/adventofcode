#!/usr/bin/python

import sys

filename = str(sys.argv[1])
lengths = [int(i) for i in open(filename, 'r').read().strip().split(',')]

lstlen = 256
lst = list(range(lstlen))
curpos = 0
skip = 0

for length in lengths:
	sublst = []
	newpos = curpos + length
	if newpos < lstlen:
		lst[curpos:length] = lst[curpos:length][::-1]
	else:
		endlen = lstlen - curpos
		beglen = length - endlen
		sublst = lst[curpos:] + lst[:beglen]
		sublst.reverse()
		lst[curpos:] = sublst[:endlen]
		lst[:beglen] = sublst[endlen:]
	curpos = (newpos + skip) % lstlen
	skip += 1
print 'Finished:',lst
print 'Answer:',lst[0]*lst[1]
