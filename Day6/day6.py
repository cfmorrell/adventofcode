#!/usr/bin/python

import sys
import operator

filename = str(sys.argv[1])
f = open(filename, 'r')

first = True
data = []
for line in f:
    row = line.strip()
    if first:
        for i in row:
            col = {}
            col[i] = 1
            data.append(col)
        first = False
    else:
        count = 0
        for i in row:
            if i in data[count]:
                data[count][i] += 1
            else:
                data[count][i] = 1
            count += 1
print data

for row in data:
    print sorted(row.items(), key=operator.itemgetter(1))[0]

