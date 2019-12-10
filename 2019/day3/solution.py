#!/usr/bin/python

import sys


def func(fn):
    """
    >>> func("test1.txt")
    6
    >>> func("test2.txt")
    159
    >>> func("test3.txt")
    135
    """
    f = open(fn, 'r')
    moves = [{}, {}]
    for num, line in enumerate(f):
        line = line.strip().split(",")
        currentlocation = (0, 0)
        steps = 1
        for movement in line:
            direction = movement[0]
            distance = int(movement[1:])
            for i in range(distance):
                if direction == 'R':
                    currentlocation = (currentlocation[0]+1, currentlocation[1])
                elif direction == 'L':
                    currentlocation = (currentlocation[0]-1, currentlocation[1])
                elif direction == 'U':
                    currentlocation = (currentlocation[0], currentlocation[1]+1)
                elif direction == 'D':
                    currentlocation = (currentlocation[0], currentlocation[1]-1)
                if currentlocation not in moves[num]:
                    moves[num][currentlocation] = steps
                # print(currentlocation, steps)
                steps += 1
    intersections = (moves[0].keys() & moves[1].keys())
    # print(intersections)
    # dist = sum(abs(i) for i in intersections.pop())
    pickone = intersections.pop()
    steps = moves[0][pickone] + moves[1][pickone]
    for ints in intersections:
        s = moves[0][ints] + moves[1][ints]
        if s < steps:
            steps = s
    return(steps)
    f.close()

if __name__ == "__main__":
    filename = str(sys.argv[1])
    print(func(filename))
