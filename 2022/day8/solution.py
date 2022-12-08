import string
import numpy as np

def part1():
    treecount = 0
    with open(filename) as f:
        rows = []
        for index,line in enumerate(f):
            rows.append([int(i) for i in list(line.strip())])
    trees = np.array(rows)

    print(trees)

    for y in range(1,len(trees)-1):
        for x in range(1,len(trees[0])-1):
            visible = False
            if trees[y,x] > max(trees[y,:x]):
                visible = True
            if trees[y,x] > max(trees[y,x+1:]):
                visible = True
            if trees[y,x] > max(trees[y+1:,x]):
                visible = True
            if trees[y,x] > max(trees[:y,x]):
                visible = True
            if visible == True:
                treecount += 1
    treecount += (len(trees) * 2) + ((len(trees[0]) - 2) * 2)
    print('Total trees:',treecount)


def part2():
    with open(filename) as f:
        rows = []
        for index,line in enumerate(f):
            rows.append([int(i) for i in list(line.strip())])
    trees = np.array(rows)

    print(trees)
    highestscore = 0
    for y in range(1,len(trees)-1):
        for x in range(1,len(trees[0])-1):
            l,r,u,d = 0,0,0,0
            scenicscore = 1
            # print('Looking from: ({},{}) with value {}'.format(x,y,trees[y,x]))
            #Look left
            for left in range(x-1,-1,-1):
                if trees[y,left] >= trees[y,x] or left == 0:
                    l = x-left
                    scenicscore *= (x-left)
                    # print('Distance Left:',x-left)
                    break
            #Look right
            for right in range(x+1,len(trees[y])):
                if trees[y,right] >= trees[y,x] or right == len(trees[y])-1:
                    scenicscore *= (right-x)
                    # r = right-x
                    # print('Distance Right:',right-x)
                    break
            #Look up
            for up in range(y-1,-1,-1):
                # print('Compare {} >= {}, index: {}'.format(trees[up,x],trees[y,x],up))
                if trees[up,x] >= trees[y,x] or up == 0:
                    scenicscore *= (y-up)
                    # u = y-up
                    # print('Distance Up:',y-up)
                    break
            #Look down
            for down in range(y+1,len(trees)):
                if trees[down,x] >= trees[y,x] or down == len(trees)-1:
                    scenicscore *= (down-y)
                    # d = down-y
                    # print('Distance Down:',down-y)
                    break
            if scenicscore > highestscore:
                highestscore = scenicscore
                print('Looking from: ({},{}) with value {} and scenic score {}'.format(x,y,trees[y,x],scenicscore))











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