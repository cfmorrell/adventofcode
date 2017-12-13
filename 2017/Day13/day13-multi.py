#!/usr/bin/env python3

import sys
import copy
from multiprocessing import Pool

def movescanners(fw):
    for layer in fw:
        if layer[0] > 0:
            if layer[2] == 'D': 
                layer[1] += 1
                if layer[1] == layer[0] - 1:
                    layer[2] = 'U'
            elif layer[2] == 'U':
                layer[1] -= 1
                if layer[1] == 0:
                    layer[2] = 'D'


def part1(f):
    maxdepth = 100
    fw = [[0,0,'D'] for i in range(maxdepth+1)]
    for line in f:
        depth,rng = [int(i) for i in line.strip().split(':')]
        fw[depth][0] = rng
    score = 0
    for i,d in enumerate(fw):
        if d[1] == 0 and d[0] > 0:
            score += d[0] * i
        # print(i,d,score)
        movescanners(fw)
    return score


def calcscore(data):
    fw,delay = data
    if delay%1000 == 0:
        print("Delay",delay)
    for i in range(delay):
        movescanners(fw)
 #   score = 0
    for i,d in enumerate(fw):
        if d[1] == 0 and d[0] > 0:
            return
            # score += (d[0] * i) + 1
        movescanners(fw)
    # print('Score:',score)
#    if score == 0:
    print(delay)

def foundit(delay):
    print(delay)

def part2(f):
    maxdepth = 100
    origfw = [[0,0,'D'] for i in range(maxdepth+1)]
    for line in f:
        depth,rng = [int(i) for i in line.strip().split(':')]
        origfw[depth][0] = rng

    data = [(copy.deepcopy(origfw),delay) for delay in range(10000)]

    pool = Pool(processes=None)
    pool.map(calcscore, data)


    # delay = 0
    # while 1:
    #     if delay % 1000 == 0:
    #         print('Delay:',delay)

    #     result = pool.apply_async(calcscore, (copy.deepcopy(origfw), delay, ))
    #     if result:
    #         return result.get
    #     delay += 1


filename = str(sys.argv[1])
f = open(filename, 'r')


# print(part1(f))
print(part2(f))

