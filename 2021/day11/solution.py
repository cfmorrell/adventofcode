import numpy as np
from numpy.lib.index_tricks import ndenumerate
from pandas import DataFrame
# from operator import xor

def neighbors(matrix, rowNumber, colNumber):
    result = []
    for rowAdd in range(-1, 2):
        newRow = rowNumber + rowAdd
        if newRow >= 0 and newRow <= len(matrix)-1:
            for colAdd in range(-1, 2):
                newCol = colNumber + colAdd
                if newCol >= 0 and newCol <= len(matrix[0])-1:
                    # if xor(newCol==colNumber,newRow==rowNumber):
                    result.append((newRow,newCol))
    result.remove((rowNumber,colNumber))
    return result

def part1(filename):
    with open(filename) as f:
        octopuses = np.array([[int(l) for l in i] for i in f.read().strip().split()])
        # print("Starting Point:\n{}".format(octopuses))
        flashcounter = 0
        for i in range(1,101):
            octopuses += 1
            while(len(np.where(octopuses > 9)[0] >= 0)):
                flashes = np.where(octopuses > 9)
                flashcounter += len(flashes[0])
                octopuses = np.where(octopuses > 9,-100,octopuses)
                for flashrow,flashcol in zip(flashes[0],flashes[1]):
                    for n in neighbors(octopuses,flashrow,flashcol):
                        octopuses[n[0]][n[1]] += 1
            octopuses = np.where(octopuses <= 0,0,octopuses)
            # print("After Step {}: \n {}".format(i,octopuses))
        print(flashcounter)

def part2(filename):
    with open(filename) as f:
        octopuses = np.array([[int(l) for l in i] for i in f.read().strip().split()])
        for i in range(1,1000):
            octopuses += 1
            while(len(np.where(octopuses > 9)[0] >= 0)):
                flashes = np.where(octopuses > 9)
                octopuses = np.where(octopuses > 9,-100,octopuses)
                for flashrow,flashcol in zip(flashes[0],flashes[1]):
                    for n in neighbors(octopuses,flashrow,flashcol):
                        octopuses[n[0]][n[1]] += 1
            octopuses = np.where(octopuses <= 0,0,octopuses)
            flatoctopuses = np.ravel(octopuses)
            if np.all(flatoctopuses == flatoctopuses[0]):
                print("After Step {}: \n {}".format(i,octopuses))
                break

# part1('sampleinput.txt')
# part1('input.txt')
# part2('sampleinput.txt')
part2('input.txt')