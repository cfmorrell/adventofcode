from itertools import product, starmap, islice
import copy

def findNeighbors1(grid, x, y):
    xi = (0, -1, 1) if 0 < x < len(grid) - 1 else ((0, -1) if x > 0 else (0, 1))
    yi = (0, -1, 1) if 0 < y < len(grid[0]) - 1 else ((0, -1) if y > 0 else (0, 1))
    return islice(starmap((lambda a, b: grid[x + a][y + b]), product(xi, yi)), 1, None)

def findNeighbors2(grid,x,y):
    neighbors = []
    x1,y1 = x,y
    for dir in ['u','ur','r','dr','d','dl','l','ul']:
        while 1:
            if dir == 'u':
                x1 -= 1
            elif dir == 'ur':
                x1 -= 1
                y1 += 1
            elif dir == 'r':
                y1 += 1
            elif dir == 'dr':
                y1 += 1
                x1 += 1
            elif dir == 'd':
                x1 += 1
            elif dir == 'dl':
                x1 += 1
                y1 -= 1
            elif dir == 'l':
                y1 -= 1
            elif dir == 'ul':
                x1 -= 1
                y1 -= 1
            if x1 >= len(grid) or x1 < 0 or y1 < 0 or y1 >= len(grid[0]):
                break
            if grid[x1][y1] != '.':
                neighbors.append(grid[x1][y1])
                break
        x1,y1 = x,y
    return neighbors

def printmatrix(matrix):
    for row in matrix:
        print(''.join(row))


def day11(filename):
    with open(filename) as f:
        seats = []
        for line in f:
            line = list(line.strip())
            seats.append(line)
    while 1:
        newseats = []
        for rownum,rowval in enumerate(seats):
            newrow = []
            for colnum,colval in enumerate(rowval):
                neighbors = list(findNeighbors2(seats,rownum,colnum))
                if colval == 'L' and neighbors.count('#') == 0:
                    newrow.append('#')
                elif colval == '#' and neighbors.count('#') >= 5:
                    newrow.append('L')
                else:
                    newrow.append(colval)
            newseats.append(newrow[:])
        # printmatrix(seats)
        # printmatrix(newseats)
        if seats == newseats:
            break
        seats = copy.deepcopy(newseats)
        newseats = []
    count = 0
    for row in seats:
        count += sum([1 for i in row if i == '#'])
    print(count)

day11('smallinput.txt')
day11('input.txt')