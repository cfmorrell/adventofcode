#!/usr/local/bin/python3

def part1(filename):
    with open(filename) as f:
        l = f.read().strip().split(',')
        maxx = int(l[0].split('..')[1])
        minx = int(l[0].split('..')[0].split('=')[1])
        maxy = int(l[1].split('..')[1])
        miny = int(l[1].split('..')[0].split('=')[1])
        print(minx, maxx, miny, maxy)
    realbiggesty = 0
    count = 0
    for dx in range(maxx+1):
        for dy in range(miny,1000):
            thisdx, thisdy, biggesty = dx,dy,0
            x,y = 0,0
            for t in range(1,500):
                x += thisdx
                y += thisdy
                if thisdx < 0:
                    thisdx += 1
                elif thisdx > 0:
                    thisdx -= 1
                thisdy -= 1
                if y >= biggesty:
                    biggesty = y
                # print('t:{} x,y:({},{}) dx,dy:({},{})'.format(t,x,y,thisdx,thisdy))
                if minx <= x <= maxx and miny <= y <= maxy:
                    count += 1
                    if biggesty > 0:
                        print("Hit coordinate ({},{}) with dx,dy: {},{} at time {} with biggest y {}".format(x,y,dx,dy,t,biggesty))
                    if biggesty >= realbiggesty:
                        realbiggesty = biggesty
                    break
    print("Part1: {}".format(realbiggesty))
    print("Part2: {}".format(count))

# def part2(filename):


# part1('sampleinput.txt')
from datetime import datetime
start = datetime.now()
part1('input.txt')
end = datetime.now()
print(end-start)
# part2('sampleinput.txt')
# part2('input.txt')