import copy

class Tile(object):
    def __init__(self,number):
        self.number = number
        self.sides = []
        self.neighbors = 0

    def append(self,other):
        return self.sides.append(other)

    def __str__(self):
        return "{} {} {}".format(self.number,self.neighbors, self.sides)

def rotate90Clockwise(matrix):
    A = copy.deepcopy(matrix)
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    return A

def printmatrix(matrix):
    for line in matrix:
        print(line)
    print('')

def part1(filename):
    tiles = []
    allsides = []
    with open(filename) as f:
        for tile in f.read().split('\n\n'):
            thistileobject = Tile(int(tile[4:9]))
            thistile = [list(i) for i in tile.split('\n')[1:]]
            thistileobject.sides.append(thistile[0])
            thistileobject.sides.append(thistile[0][::-1])
            for _ in range(3):
                thistile = rotate90Clockwise(thistile)
                thistileobject.sides.append(thistile[0])
                thistileobject.sides.append(thistile[0][::-1])
            allsides.extend(thistileobject.sides)
            tiles.append(thistileobject)

    total = 1
    for tile in tiles:
        count = sum([1 for i in tile.sides if allsides.count(i) > 1])
        tile.neighbors = count
        # print('{} {}'.format(tile.number,tile.neighbors))
        if count == 4:
            total *= tile.number
            print(tile)
    print(total)

part1('smallinput.txt')
part1('input.txt')