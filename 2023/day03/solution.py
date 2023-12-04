import re
import numpy as np
def part1():
    total = 0
    numcount = 0
    with open(filename) as f:
        board = np.array([list(line.strip()) for line in f])
        print('\n'.join([''.join([i for i in row]) for row in board]))
        f.seek(0)
        # input()
        for index,line in enumerate(f):
            nums = [i.strip() for i in re.findall('\d+',line)]
            print('*******************************************')
            print('Numbers in row:',nums)
            for num in nums:
                print('==============================')
                print('Working on number:',num)
                start = line.find(num)
                end = start + len(num)
                rowabove = index-1 if index > 0 else 0
                rowbelow = index+2 if index < len(board) else len(board)
                colleft = start-1 if start > 0 else 0
                colright = end+1 if end < len(board[0]) else len(board[0])
                subboard = board[rowabove:rowbelow,colleft:colright]
                print('--------')
                print('\n'.join([''.join([i for i in row]) for row in subboard]))
                print('--------')
                keyvals = ''.join(subboard.flatten())
                print('Flat:',keyvals)
                if len(re.findall('[^\d.]',keyvals)) > 0:
                    print("Adding {} to the total".format(num))
                    total += int(num)
                else:
                    print('No symbol in',keyvals)
                    numcount += 1
                print('Total:',total)
                if num == '873':
                    input()
                print(numcount)
            # input()

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
print(f"Elapsed {ms*10**6:.03f} microseconds.")