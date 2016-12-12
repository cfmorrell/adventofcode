#!/usr/bin/python

import sys
import os
import time

filename = str(sys.argv[1])
f = open(filename, 'r')

def updateScreen():
    os.system('clear')
    for y in range(0,screenHeight):
        print ''.join(screen[y])

def rotateCol(column, distance):
    tempCol = []
    for i in range(screenHeight-distance,screenHeight):
        tempCol.append(screen[i][column])
    for i in range(0,screenHeight-distance):
        tempCol.append(screen[i][column])
    for i in range(0,len(tempCol)):
        screen[i][column] = tempCol[i]
    updateScreen()

def rotateRow(row, distance):
    tempRow = []
    for i in range(screenWidth-distance,screenWidth):
        tempRow.append(screen[row][i])
    for i in range(0,screenWidth-distance):
        tempRow.append(screen[row][i])
    screen[row] = tempRow
    updateScreen()

def addRect(width, height):
    for y in range(0,height):
        for x in range(0,width):
            screen[y][x] = '#'
    updateScreen()

screenHeight = 6
screenWidth = 50

screen = [['.' for x in range(screenWidth)] for y in range(screenHeight)] 
updateScreen()

for line in f:
    time.sleep(0.05)
    if 'rect' in line:
        rect = line.split()[1]
        width= int(rect.split('x')[0])
        height = int(rect.split('x')[1])
        addRect(width,height)
    elif 'column' in line:
        col = int(line.split()[2].split('=')[1])
        distance = int(line.split()[4])
        rotateCol(col,distance)
    elif 'row' in line:
        row = int(line.split()[2].split('=')[1])
        distance = int(line.split()[4])
        rotateRow(row,distance)

sum = 0
for y in range(0,screenHeight):
    for x in range(0,screenWidth):
        if screen[y][x] == '#':
            sum += 1

print 'Total:',sum
