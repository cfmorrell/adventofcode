import string
import numpy as np
from collections import deque
import os
import time

AB = string.ascii_lowercase

def bfs(map, pos):
    w, h = len(map[0]), len(map)
    q = deque([[pos]])
    seen = set([pos])
    while q:
        path = q.popleft()
        x, y = path[-1]
        if map[y][x] == "E":
            return path
        e = AB.index(map[y][x])
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < w and 0 <= y2 < h and (x2, y2) not in seen:
                e2 = AB.index(map[y2][x2]) if map[y2][x2] != "E" else 26
                if e2 <= e + 1:
                    q.append(path + [(x2, y2)])
                    seen.add((x2, y2))


def part1():
    with open(filename) as f:
        map = np.array([list(i) for i in f.read().strip().split()])
        # print(map)
        y,x = [i[0] for i in np.where(map == 'S')]
        # y2,x2 = [i[0] for i in np.where(map == 'E')]
        map[y,x] = "a"
        # print(map)
        path = bfs(map, (x,y))
        # for stop in path:
        #     os.system('clear')
        #     map[stop[1],stop[0]] = '.'
        #     for row in map:
        #         print(''.join(row))
        #     time.sleep(.1)
        #     # os.system('clear')
        print(path)
        print(len(path))

def part2():
    with open(filename) as f:
        map = np.array([list(i) for i in f.read().strip().split()])
        y,x = [i[0] for i in np.where(map == 'S')]
        map[y,x] = "a"
        startpoints = np.where(map == 'a')
        startpoints = list(zip(startpoints[1],startpoints[0]))
        print(startpoints)
        shortestpath = len(map) * len(map[0])
        for startpoint in startpoints:
            thispath = bfs(map, startpoint)
            if thispath == None:
                continue
            print("Length:",len(thispath)-1, "from",startpoint)
            if len(thispath)-1 < shortestpath:
                shortestpath = len(thispath) - 1
        print(shortestpath)











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