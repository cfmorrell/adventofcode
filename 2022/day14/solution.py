import string
import numpy as np
from itertools import product
import os
import time

def part1():
    caves = np.full((200,600),'.')
    bottomrow = 0
    minx,maxx,miny,maxy = 1000,-1000,1000,-1000
    with open(filename) as f:
        for line in f:
            numpairs = line.count('->')
            line = line.strip().split(' -> ')
            for i in range(numpairs):
                leftx,lefty = [int(j) for j in line[i].split(',')]
                rightx,righty = [int(j) for j in line[i+1].split(',')]
                if max(lefty,righty) > maxy:
                    maxy = max(lefty,righty)
                if min(lefty,righty) < miny:
                    miny = min(lefty,righty)
                if max(leftx,rightx) > maxx:
                    maxx = max(leftx,rightx)
                if min(leftx,rightx) < minx:
                    minx = min(leftx,rightx)
                rocks = product(range(min(leftx,rightx),max(leftx,rightx)+1),range(min(lefty,righty),max(lefty,righty)+1))
                for rock in rocks:
                    caves[rock[1],rock[0]] = '#'

    felldown = False
    grains = 0
    while not felldown:
        y,x = 0,500
        grains += 1
        blocked = False

        while not blocked or felldown:
            # os.system('clear')
            # print(miny,maxy,minx,maxx)
            # for row in caves[miny-10:maxy+1]:
            #     print(''.join(row[minx-5:maxx+6]))
            # print("Grain Location: {},{}".format(y,x))
            # time.sleep(.01)
            y += 1
            if y >= maxy + 1:
                felldown = True
                break
            if caves[y,x] == '.':
                continue
            if caves[y,x-1] == '.':
                x -= 1
                continue
            if caves[y,x+1] == '.':
                x += 1
                continue
            caves[y-1,x] = 'O'
            blocked = True
    print(grains - 1)

def part2():
    caves = np.full((200,1000),'.')
    maxy = 0
    with open(filename) as f:
        for line in f:
            numpairs = line.count('->')
            line = line.strip().split(' -> ')
            for i in range(numpairs):
                leftx,lefty = [int(j) for j in line[i].split(',')]
                rightx,righty = [int(j) for j in line[i+1].split(',')]
                if max(lefty,righty) > maxy:
                    maxy = max(lefty,righty)
                rocks = product(range(min(leftx,rightx),max(leftx,rightx)+1),range(min(lefty,righty),max(lefty,righty)+1))
                for rock in rocks:
                    caves[rock[1],rock[0]] = '#'

    minx = 300
    maxx = 700
    miny = 0

    for x in range(minx,maxx+1):
        caves[maxy+2,x] = '#'

    hitorigin = False
    grains = 0
    while not hitorigin:
        y,x = 0,500
        grains += 1
        blocked = False

        while not blocked or hitorigin:
            if grains % 500 == 0:
                os.system('clear')
                for row in caves[miny:maxy+4]:
                    print(''.join(row[minx:maxx]))
            # print("Grain Location: {},{}".format(y,x))
            if caves[0,500] == 'O':
                hitorigin = True
                break

            y += 1
            if caves[y,x] == '.':
                continue
            if caves[y,x-1] == '.':
                x -= 1
                continue
            if caves[y,x+1] == '.':
                x += 1
                continue
            caves[y-1,x] = 'O'
            blocked = True
    print(grains - 1)









import sys
try:
    if sys.argv[1] not in ['T','F']:
        raise
    filename = 'sampleinput.txt' if sys.argv[1] == 'T' else 'input.txt'
    part = int(sys.argv[2])
except:
    print('Usage: solution.py [T|F] [1|2] (Testing & Part)')
    exit()


if part == 1:
    part1()
else:
    part2()