#!/usr/bin/python

import sys

filename = str(sys.argv[1])
f = open(filename, 'r').read()

repeat = False
loc = [0,0]
locHist = [str(loc)]
dir = 'N'
dirs = ['N','E','S','W']
for move in f.split(','):
    thisMove = move.strip()
    print loc, 'to', thisMove
    if thisMove[0] == 'L':
        dir = dirs[(dirs.index(dir) - 1) % 4]
    elif thisMove [0] == 'R':
        dir = dirs[(dirs.index(dir) + 1) % 4]

    if dir == 'N':
        for i in range(0,int(thisMove[1:])):
            loc[1] += 1
            if str(loc) in locHist:
                repeat = True
                break
            locHist.append(str(loc))
    elif dir == 'S':
        for i in range(0,int(thisMove[1:])):
            loc[1] -= 1
            if str(loc) in locHist:
                repeat = True
                break
            locHist.append(str(loc))
    elif dir == 'E':
        for i in range(0,int(thisMove[1:])):
            loc[0] += 1
            if str(loc) in locHist:
                repeat = True
                break
            locHist.append(str(loc))
    elif dir == 'W':
        for i in range(0,int(thisMove[1:])):
            loc[0] -= 1
            if str(loc) in locHist:
                repeat = True
                break
            locHist.append(str(loc))
    if repeat:
        break
print locHist
    #print dir
    #print loc
print abs(loc[0]) + abs(loc[1])
