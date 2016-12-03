#!/usr/bin/python

import sys

filename = str(sys.argv[1])
f = open(filename, 'r')

count = 0
group1 = []
group2 = []
group3 = []
allSides = []
for line in f:
    row = [int(x) for x in line.split()]
    group1.append(row[0])
    group2.append(row[1])
    group3.append(row[2])
    if len(group1) == 3:
        allSides.append(group1)
        allSides.append(group2)
        allSides.append(group3)
        group1 = []
        group2 = []
        group3 = []

for sides in allSides:
    if sides.index(max(sides)) == 0:
        if sides[1] + sides[2] > sides[0]:
            count += 1
    elif sides.index(max(sides)) == 1:
        if sides[0] + sides[2] > sides[1]:
            count += 1
    elif sides.index(max(sides)) == 2:
        if sides[0] + sides[1] > sides[2]:
            count += 1
print count

        
