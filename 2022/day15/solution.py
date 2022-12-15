import string
from scipy.spatial.distance import cityblock
import numpy as np
import os

def part1():
    shift = 10000000
    rowinquestion = 2000000
    row = [0]*shift
    beaconsinrow = set()
    with open(filename) as f:
        for line in f:
            sx = int(line.split('=')[1].split(',')[0]) + shift
            sy = int(line.split('y=')[1].split(':')[0])
            bx = int(line.split('x=')[2].split(',')[0]) + shift
            by = int(line.split('y=')[-1])
            if by == rowinquestion:
                beaconsinrow.add((bx,by))
            mandist = cityblock([sx,sy],[bx,by])
            disttorow = abs(sy-rowinquestion)
            # print(sx,sy,bx,by,mandist,disttorow)
            if len(row) <= sx+(mandist-disttorow)+1:
                row.extend([0]*((sx+(mandist-disttorow)+1)-len(row)+1))
            row[sx-(mandist-disttorow):sx+(mandist-disttorow)+1] = [1]*(((mandist-disttorow)*2)+1)
        print(sum(row)-len(beaconsinrow))


#https://www.geeksforgeeks.org/merging-intervals/
def mergeIntervals(rows,row):
    arr = rows[row]
    arr.sort(key=lambda x: x[0])
    index = 0
    for i in range(1, len(arr)):
        if (arr[index][1] >= arr[i][0]-1):
            arr[index][1] = max(arr[index][1], arr[i][1])
        else:
            index = index + 1
            arr[index] = arr[i]
    rows[row] = [arr[i] for i in range(index+1)][::]


global rows

def part2():
    maxsize = 4000001
    rows = [[] for _ in range(maxsize)]
    # print(rows)
    with open(filename) as f:
        for line in f:
            if len(line.strip()) < 3:
                break
            sx = int(line.split('=')[1].split(',')[0])
            sy = int(line.split('y=')[1].split(':')[0])
            bx = int(line.split('x=')[2].split(',')[0])
            by = int(line.split('y=')[-1])
            mandist = cityblock([sx,sy],[bx,by])
            top = max(sy-mandist,0)
            bottom = min(sy+mandist+1,maxsize)
            for row in range(top,bottom):
                disttorow = abs(sy-row)
                left = max(0,sx-(mandist-disttorow))
                right = min(maxsize,sx+(mandist-disttorow))
                rows[row].append([left,right])
    for row in range(len(rows)):
        mergeIntervals(rows,row)
        if len(rows[row]) > 1:
            y = row
            x = rows[row][0][1] + 1
            break
    print((4000000*x)+y)        

            # for r in rows:
            #     print(r)
                    # print(''.join([str(i) for i in r]))
    # for i,r in enumerate(rows):
    #     if len(r) > 1:
    #         y = i
    #         x = r[0][1] + 1
    #         break
    # print((4000000*x)+y)
    







import sys
import time
try:
    if sys.argv[1] not in ['T','F']:
        raise
    filename = 'sampleinput.txt' if sys.argv[1] == 'T' else 'input.txt'
    part = int(sys.argv[2])
except:
    print('Usage: solution.py [T|F] [1|2] (Testing & Part)')
    exit()


start = time.perf_counter()
if part == 1:
    part1()
else:
    part2()
end = time.perf_counter()
ms = (end-start)# * 10**6
print(f"Elapsed {ms:.03f} seconds.")
print(f"Elapsed {ms*10**3:.03f} milliseconds.")
print(f"Elapsed {ms*10**6:.03f} microsecondss.")
