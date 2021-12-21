#!/usr/local/bin/python3
import numpy as np

def part1(filename):
    with open(filename) as f:
        enhancement = f.readline().strip()
        f.readline()
        image = np.array([list(i.strip()) for i in f.readlines()])
        for i in range(50):
            if i == 0:
                padval = '.'
            else:
                padval = image[0][0]
            image = np.pad(image,2,'constant',constant_values=padval)
            newimage = []
            for row in range(len(image)-2):
                for col in range(len(image[0])-2):
                    subimage = (image[row:row+3,col:col+3]).flatten()
                    value = int(''.join(['0' if i == '.' else '1' for i in subimage]),2)
                    newimage.append(enhancement[value])
            image = (np.reshape(newimage,(-1,len(image)-2)))
            trimval = image[0][0]
            trimrows = np.where(np.isin(image,trimval).any(axis=1))
            trimcols = np.where(np.isin(image,trimval).any(axis=0))
            image = image[trimrows[0][0]:trimrows[0][-1]+1,trimcols[0][0]:trimcols[0][-1]+1]
        # for j,row in enumerate(image):
        #     print(j,''.join(row))
        # print("Num Rows: {} Num Cols: {}".format(len(image),len(image[0])))
        print(np.count_nonzero(image == '#'))


# def part2(filename):


# part1('sampleinput.txt')
part1('input.txt')
# part2('sampleinput.txt')
# part2('input.txt')