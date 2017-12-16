#!/usr/bin/env python3

import sys

def dance(reps,programs):
    seen = []
    for i in range(reps):
        s = ''.join(programs)
        if s in seen:
            return(seen[reps % i])
        seen.append(s)
        for move in moves:
            whichmove = move[0]
            if whichmove == 's':
                programs[0:0] = programs[move[1]:]
                programs[move[1]:] = []
            elif whichmove == 'x':
                hold = programs[move[1]]
                programs[move[1]],programs[move[2]] = programs[move[2]],programs[move[1]]
            elif whichmove == 'p':
                indexa = programs.index(move[1])
                indexb = programs.index(move[2])
                programs[indexa],programs[indexb] = programs[indexb],programs[indexa]
    return ''.join(programs)




testfile = 'sample.txt'
realfile = 'input.txt'
#programs = list('abcde')
programs = list('abcdefghijklmnop')

moves = []
f = open(realfile,'r').read().strip().split(',')
for move in f:
    if move[0] == 's':
        moves.append((move[0],0-int(move[1:])))
    elif move[0] == 'x':
        a,b = [int(i) for i in move[1:].split('/')]
        moves.append((move[0],a,b))
    elif move[0] == 'p':
        a,b = move[1:].split('/')
        moves.append((move[0],a,b))


#part1
print('Part1:',dance(1,programs[:]))
print('Part2a:',dance(10000,programs[:]))
print('Part2:',dance(1000000000,programs[:]))
