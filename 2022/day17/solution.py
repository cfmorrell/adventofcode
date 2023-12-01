import numpy as np
import os
def part1():
    with open(filename) as f:
        ventqueue = list(f.read().strip())
    piece1 = [(0,0),(0,1),(0,2),(0,3)]
    piece2 = [(0,1),(1,0),(1,1),(1,2),(2,1)]
    piece3 = [(0,0),(0,1),(0,2),(1,2),(2,2)]
    piece4 = [(0,0),(1,0),(2,0),(3,0)]
    piece5 = [(0,0),(0,1),(1,0),(1,1)]
    piecequeue = [piece1, piece2, piece3, piece4, piece5]
    board = np.full((10,7),'.')
    rockcount = 0
    highestpoint = 0
    while rockcount < 1000000000000:
        currentpiece = piecequeue.pop(0)
        piecequeue.append(currentpiece)
        piecebottomleft = [highestpoint + 3,2]
        if len(board) < highestpoint + max([i[0] for i in currentpiece]) + 4:
            board = np.append(board,np.full((max([i[0] for i in currentpiece]) + 4,7),'.'),axis=0)
        while 1:
            #clear old spot
            for i in currentpiece:
                board[i[0]+piecebottomleft[0],i[1]+piecebottomleft[1]] = '.'

            #Move left or right
            driftdir = ventqueue.pop(0)
            ventqueue.append(driftdir)
            if driftdir == '>' and max([i[1]+piecebottomleft[1] for i in currentpiece]) < 6:
                # print('Checking Right')
                clearright = True
                for pos in currentpiece:
                    if board[piecebottomleft[0] + pos[0], piecebottomleft[1] + pos[1]+1] != '.':
                        clearright = False
                if clearright:
                    # print('Clear right')
                    piecebottomleft[1] += 1
                # else:
                #     print('Not clear right')
            elif driftdir == '<' and min([i[1]+piecebottomleft[1] for i in currentpiece]) > 0:
                # print('Checking Left')
                clearleft = True
                for pos in currentpiece:
                    if board[piecebottomleft[0] + pos[0], piecebottomleft[1] + pos[1]-1] != '.':
                        clearleft = False
                if clearleft:
                    # print('Clear left')
                    piecebottomleft[1] -= 1
                # else:
                #     print('Not clear left')
            #draw new spot
            for i in currentpiece:
                board[i[0]+piecebottomleft[0],i[1]+piecebottomleft[1]] = '#'

            #print board, wait
            # os.system('clear')
            # for line in reversed(board):
            #     print(''.join(line))
            # print('-----------------')
            # time.sleep(0.1)

            #clear old spot
            for i in currentpiece:
                board[i[0]+piecebottomleft[0],i[1]+piecebottomleft[1]] = '.'
            #Move Down
            # print('Checking Below')
            clearbelow = True
            if piecebottomleft[0] <= 0:
                clearbelow = False
            for pos in currentpiece:
                if board[piecebottomleft[0] + pos[0] - 1, piecebottomleft[1] + pos[1]] != '.':
                    clearbelow = False
            if clearbelow:
                # print('Clear below')
                piecebottomleft[0] -= 1
            else:
                for i in currentpiece:
                    board[i[0]+piecebottomleft[0],i[1]+piecebottomleft[1]] = '#'                
                if rockcount % 1000 == 0:
                    print('Highest Point:',highestpoint)
                # print('Bottom Left Corner:',piecebottomleft)
                for i,row in enumerate(board):
                    if '#' not in row:
                        highestpoint = i
                        break
                # highestpoint += max([i[0] for i in currentpiece]) + 1
                rockcount += 1
                # print('New Highest Point:',highestpoint)
                # print('Rock Count:',rockcount)
                break
            for i in currentpiece:
                board[i[0]+piecebottomleft[0],i[1]+piecebottomleft[1]] = '#'

            #print board, wait
            # os.system('clear')
            # for line in reversed(board):
            #     print(''.join(line))
            # print('-----------------')
            # time.sleep(0.1)            




def part2():
    with open(filename) as f:
        pass











import sys,time,string
try:
    if sys.argv[1] not in ['T','F']:
        raise
    filename = 'sampleinput.txt' if sys.argv[1] == 'T' else 'input.txt'
    part = int(sys.argv[2])
except:
    print('Usage: solution.py [T|F] [1|2] (Testing & Part)')
    exit()


start = time.perf_counter()
if part == 1:
    part1()
else:
    part2()
end = time.perf_counter()
ms = (end-start)# * 10**6
print(f"Elapsed {ms:.03f} seconds.")
print(f"Elapsed {ms*10**3:.03f} milliseconds.")
print(f"Elapsed {ms*10**6:.03f} microsecondss.")