#!/usr/bin/python
import sys

def knothash(plain):
    size = 256
    li = range(size)
    pos = skip = 0

    for _ in range(64):
        for n in [ord(i) for i in plain]:
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
    h = knothash(f+'-0')
    b = ''
    for i in range(0,len(h),2):
        b += bin(int(h[i:i+2],16))[2:]
    print(b)
        

def part2():
    pass

filename = str(sys.argv[1])
with open(filename) as f:
    f = f.read().strip()

print(part1(f))
#print(part2())