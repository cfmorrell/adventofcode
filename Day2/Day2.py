#!/usr/bin/python

import sys

filename = str(sys.argv[1])
f = open(filename, 'r')

keypad = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]

loc = [0,2]

for line in f:
    for dir in line:
        if dir == 'U' and ((loc[0] == 1 and loc[1] > 1) or 
                           (loc[0] == 2 and loc[1] > 0) or 
                           (loc[0] == 3 and loc[1] > 1)):
                loc[1] -= 1
        elif dir == 'D' and ((loc[0] == 1 and loc[1] < 3) or 
                           (loc[0] == 2 and loc[1] < 4) or 
                           (loc[0] == 3 and loc[1] < 3)):
                loc[1] += 1
        elif dir == 'L' and ((loc[1] == 1 and loc[0] > 1) or 
                           (loc[1] == 2 and loc[0] > 0) or 
                           (loc[1] == 3 and loc[0] > 1)):
                loc[0] -= 1
        elif dir == 'R' and ((loc[1] == 1 and loc[0] < 3) or 
                           (loc[1] == 2 and loc[0] < 4) or 
                           (loc[1] == 3 and loc[0] < 3)):
                loc[0] += 1
#        print dir,loc
    print keypad[loc[1]][loc[0]]
