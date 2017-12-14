#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10000)

def knothash(plain):
    size = 256
    li = range(size)
    pos = skip = 0
    plainlst = [ord(i) for i in plain] + [17, 31, 73, 47, 23]
    for _ in range(64):
        for n in plainlst:
            new_li = []
            for i in range(n):
                new_li.append(li[(pos+i)%size])

            new_li = new_li[::-1]
            for i in range(n):
                li[(pos+i)%size] = new_li[i]

            pos += (n + skip)
            skip += 1
    h = [0]*16
    hi = 0
    for i in range(0, 256, 16):
        for j in range(i, i+16):
            h[hi] ^= li[j]
        hi += 1

    shex = ['%0.2x'%i for i in h]
    return ''.join(shex)

def part1(f):
    c = 0
    for j in range(128):
        string = f+'-'+str(j)
        h = knothash(string)
        b = ''
        for i in h:
            b += bin(int(i,16))[2:].zfill(4)
        c += b.count('1')
    return c
        
class Graph:
 
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g
 
    # A function to check if a given cell 
    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1 
        # and not yet visited
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])
             
 
    def DFS(self, i, j, visited):
        rowNbr = [-1,  0, 0, 1];
        colNbr = [ 0, -1, 1, 0];
         
        visited[i][j] = True
 
        # Recur for all connected neighbours
        for k in range(4):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)

    def countIslands(self):
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]

        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] == False and self.graph[i][j] ==1:
                    self.DFS(i, j, visited)
                    count += 1
        return count

def part2(f):
    mem = []
    for j in range(128):
        string = f+'-'+str(j)
        h = knothash(string)
        b = []
        for i in h:
            b.extend([int(i) for i in list(bin(int(i,16))[2:].zfill(4))])
        mem.append(b)
    print(mem)
    g = Graph(128,128,mem)
    return g.countIslands()

testkey = 'flqrgnkx'
realkey = 'ffayrhll'
# print(part1(realkey))
print(part2(realkey))