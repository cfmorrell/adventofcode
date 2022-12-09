import numpy as np
import string

def printfield(hpos,tpos,tlocs):
    xs = [i[0] for i in tlocs]
    ys = [i[1] for i in tlocs]
    xs.append(hpos[0])
    xs.append(tpos[0])
    ys.append(hpos[1])
    ys.append(tpos[1])
    width = max(xs) - min(xs) + 2
    height = max(ys) - min(xs) + 2
    dim = max(width,height)
    field = np.full((dim,dim),'.')
    shiftx = abs(min(xs))
    shifty = abs(min(ys))
    print(hpos,tpos)
    print(tlocs)
    for loc in tlocs:
        field[loc[0]+shiftx,loc[1]+shifty] = '#'
    field[hpos[0]+shiftx,hpos[1]+shifty] = 'H'
    field[tpos[0]+shiftx,tpos[1]+shifty] = 'T'
    field[shiftx,shifty] = 's'
    field = np.rot90(field)
    print(str(field).replace(' [', '').replace('[', '').replace(']', '').replace("'",''))    

def part1():
    with open(filename) as f:
        hpos = [0,0]
        tpos = [0,0]
        tlocs = set()
        for line in f:
            # print(line)
            direction = line.split(' ')[0]
            distance = int(line.split(' ')[1])
            for step in range(distance):
                if direction == 'R':
                    hpos[0] += 1
                elif direction == 'L':
                    hpos[0] -= 1
                elif direction == 'U':
                    hpos[1] += 1
                elif direction == 'D':
                    hpos[1] -= 1
                if abs(hpos[0]-tpos[0]) > 1 or abs(hpos[1]-tpos[1]) > 1:
                    if hpos[0] == tpos[0] and hpos[1] > tpos[1]:
                        tpos[1] += 1
                    elif hpos[0] == tpos[0] and hpos[1] < tpos[1]:
                        tpos[1] -= 1
                    elif hpos[1] == tpos[1] and hpos[0] > tpos[0]:
                        tpos[0] += 1
                    elif hpos[1] == tpos[1] and hpos[0] < tpos[0]:
                        tpos[0] -= 1
                    elif hpos[0] > tpos[0] and hpos[1] > tpos[1]:
                        tpos[0] += 1
                        tpos[1] += 1
                    elif hpos[0] > tpos[0] and hpos[1] < tpos[1]:
                        tpos[0] += 1
                        tpos[1] -= 1
                    elif hpos[0] < tpos[0] and hpos[1] < tpos[1]:
                        tpos[0] -= 1
                        tpos[1] -= 1
                    elif hpos[0] < tpos[0] and hpos[1] > tpos[1]:
                        tpos[0] -= 1
                        tpos[1] += 1
                tlocs.add(tuple(tpos))
                # printfield(hpos,tpos,tlocs)
            # print('---------------')
        print(len(tlocs))
                


def moverope(hpos,tpos):
    if abs(hpos[0]-tpos[0]) > 1 or abs(hpos[1]-tpos[1]) > 1:
        if hpos[0] == tpos[0] and hpos[1] > tpos[1]:
            tpos[1] += 1
        elif hpos[0] == tpos[0] and hpos[1] < tpos[1]:
            tpos[1] -= 1
        elif hpos[1] == tpos[1] and hpos[0] > tpos[0]:
            tpos[0] += 1
        elif hpos[1] == tpos[1] and hpos[0] < tpos[0]:
            tpos[0] -= 1
        elif hpos[0] > tpos[0] and hpos[1] > tpos[1]:
            tpos[0] += 1
            tpos[1] += 1
        elif hpos[0] > tpos[0] and hpos[1] < tpos[1]:
            tpos[0] += 1
            tpos[1] -= 1
        elif hpos[0] < tpos[0] and hpos[1] < tpos[1]:
            tpos[0] -= 1
            tpos[1] -= 1
        elif hpos[0] < tpos[0] and hpos[1] > tpos[1]:
            tpos[0] -= 1
            tpos[1] += 1


def part2():
    with open(filename) as f:
        pos = [[0,0] for i in range(10)]
        # print(pos)
        tlocs = set()
        for line in f:
            direction = line.split(' ')[0]
            distance = int(line.split(' ')[1])
            for step in range(distance):
                if direction == 'R':
                    pos[0][0] += 1
                elif direction == 'L':
                    pos[0][0] -= 1
                elif direction == 'U':
                    pos[0][1] += 1
                elif direction == 'D':
                    pos[0][1] -= 1
                # print('Head:',pos[0])
                for i in range(1,10):
                    moverope(pos[i-1],pos[i])
                tlocs.add(tuple(pos[9]))
        print(len(tlocs))
                











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