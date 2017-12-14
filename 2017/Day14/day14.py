#!/usr/bin/env python3
import sys

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
        

def part2(f):
    mem = []
    for j in range(128):
        string = f+'-'+str(j)
        h = knothash(string)
        b = []
        for i in h:
            b.extend(list(bin(int(i,16))[2:].zfill(4)))
        mem.append(b)
    return mem


testkey = 'flqrgnkx'
realkey = 'ffayrhll'
#print(part1(realkey))
print(part2(testkey))