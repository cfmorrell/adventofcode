import numpy as np
from operator import xor
import cv2 as cv

def neighbors(matrix, rowNumber, colNumber):
    result = []
    for rowAdd in range(-1, 2):
        newRow = rowNumber + rowAdd
        if newRow >= 0 and newRow <= len(matrix)-1:
            for colAdd in range(-1, 2):
                newCol = colNumber + colAdd
                if newCol >= 0 and newCol <= len(matrix[0])-1:
                    if xor(newCol==colNumber,newRow==rowNumber):
                        result.append(matrix[newRow][newCol])
    return result

def part1(filename):
    with open(filename) as f:
        localmins = []
        heightmap = np.array([list(i) for i in f.read().strip().split()])
        print(DataFrame(heightmap))
        for row in range(len(heightmap)):
            for col in range(len(heightmap[0])):
                n = neighbors(heightmap,row,col)
                v = heightmap[row,col]
                if len(n) > 0 and v < min(n):
                    localmins += v
                    # print((row,col),v,n)
        print(localmins,sum([int(i) for i in localmins])+len(localmins))

def part2(filename):
    with open(filename) as f:
        localmins = []
        heightmap = np.array([[int(l) for l in i] for i in f.read().strip().split()])
        # print(heightmap)
        boundedheightmap = np.pad(heightmap, (1,1), constant_values=9)
        # print(boundedheightmap)
        basin_nine = (boundedheightmap == 9).astype('uint8')
        # print(basin_nine)
        mask = np.pad(basin_nine, (1,1))
        # print(mask)

        basins = []

        for (x,y),_ in np.ndenumerate(basin_nine):
            if basin_nine[x,y] == 0:
                fillings,_,_,_ = cv.floodFill(basin_nine, mask, (y,x), 1)
                basins.append(fillings)
                # print(fillings)
        print(np.prod(sorted(basins)[-3:]))




# part1('sampleinput.txt')
# part1('input.txt')
# part2('sampleinput.txt')
part2('input.txt')