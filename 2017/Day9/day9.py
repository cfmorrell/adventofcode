#!/usr/bin/python

import sys
import re

filename = str(sys.argv[1])
f = open(filename, 'r')

totalgarbage = 0
for line in f:
	holdline = line.strip()
	line = re.sub('!.','',line.strip())
	matches = re.findall('<.*?>', line)
	for match in matches:
		totalgarbage += len(match) - 2

print totalgarbage

# 	line = re.sub('<.*?>','',line)
# 	line = re.sub(',','',line)
# 	tally = 0
# 	score = 0
# 	for char in line:
# 	    if char == '{':
# 	        score += 1 + tally
# 	        tally += 1
# 	    elif char == '}':
# 	        tally -= 1
# 	totalscore += score
# 	print score,holdline
# print totalscore