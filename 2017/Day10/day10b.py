#!/usr/bin/python

import sys
import copy

filename = str(sys.argv[1])

lengths = [ord(i) for i in open(filename, 'r').read().strip()] + [17, 31, 73, 47, 23]
print 'Lengths:',lengths

lstlen = 256
lst = list(range(lstlen))
curpos = 0
skip = 0

for i in range(64):
	print 'Round:',i,'Pos:',curpos,'Skip:',skip
	print lengths
	print lst
	for length in lengths:
		sublstend = curpos + length
		if sublstend < lstlen:
			lst[curpos:length] = lst[curpos:length][::-1]
		else:
			endlen = lstlen - curpos
			beglen = length - endlen
			revsublst = list(reversed(lst[curpos:] + lst[:beglen]))
			lst[curpos:] = revsublst[:endlen]
			lst[:beglen] = revsublst[endlen:]
		curpos = (sublstend + skip) % lstlen
		skip += 1
		print lst

print 'Sparse Hash:',lst
ans = ''
for i in range(0,256,16):
	print 'Block:',i/16,'Sublist:',lst[i:i+16]
	print 'Xor:',eval('^'.join([str(j) for j in lst[i:i+17]]))
	print 'To Hex:',hex(eval('^'.join([str(j) for j in lst[i:i+17]])))[2:].zfill(2)
	ans += hex(eval('^'.join([str(j) for j in lst[i:i+17]])))[2:].zfill(2)
print ans