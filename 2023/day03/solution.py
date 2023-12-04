import re
import numpy as np
def part1():
    total = 0
    with open(filename) as f:
        board = np.array([list(line.strip()) for line in f])
        # print('\n'.join([''.join([i for i in row]) for row in board]))
        f.seek(0)
        for index,line in enumerate(f):
            nums = re.finditer('\d+',line)
            # print('*******************************************')
            # print('Numbers in row:',[i.group() for i in nums])
            for num in nums:
                # print('==============================')
                # print('Working on number:',num.group())
                rowabove = (index-1 if index > 0 else 0)
                rowbelow = (index+2 if index < len(board) else len(board))
                colleft = (num.span()[0]-1 if num.span()[0] > 0 else 0)
                colright = (num.span()[1]+1 if num.span()[1] < len(board[0]) else len(board[0]))
                subboard = board[rowabove:rowbelow,colleft:colright]
                # print('--------')
                # print('\n'.join([''.join([i for i in row]) for row in subboard]))
                # print('--------')
                keyvals = ''.join(subboard.flatten())
                # print('Flat:',keyvals)
                if len(re.findall('[^\d.]',keyvals)) > 0:
                    # print("Adding {} to the total".format(num.group()))
                    total += int(num.group())
                # else:
                #     print('No symbol in',keyvals)
        print('Total:',total)

def part2():
    total = 0
    with open(filename) as f:
        board = np.array([list(line.strip()) for line in f])
        f.seek(0)
        gearlist = []
        for index,line in enumerate(f):
            gears = re.finditer('\*',line)
            for gear in gears:
                subboard = board[max(index-1,0):min(index+2,len(board)),max(gear.span()[0]-1,0):min(gear.span()[1]+1,len(board[0]))]
                # print('--------')
                # print('\n'.join([''.join([i for i in row]) for row in subboard]))
                # print('--------')
                gearsurrounds = ' '.join([''.join([i for i in row]) for row in subboard])
                # print(gearsurrounds)
                if len(re.findall('\d+',gearsurrounds)) == 2:
                    thisgearboard = board[max(index-1,0):min(index+2,len(board)),max(gear.span()[0]-3,0):min(gear.span()[1]+3,len(board[0]))]
                    gearlist.append(thisgearboard)#,index,gear.span()[0])
                    # print("Found a gear")
        totalratio = 0
        for gear in gearlist:
            nums = []
            for row in gear:
                row = ''.join(row)
                thesenums = re.finditer('\d+',row)
                for thisnum in thesenums:
                    if len(thisnum.group()) == 3:
                        nums.append(thisnum.group())
                        if len(nums) == 2:
                            break
                    elif len(thisnum.group()) == 2 and (thisnum.span()[0] in [1,2,3,4]):
                        nums.append(thisnum.group())
                        if len(nums) == 2:
                            break
                    elif len(thisnum.group()) == 1 and (thisnum.span()[0] in [2,3,4]):
                        nums.append(thisnum.group())
                        if len(nums) == 2:
                            break
            # print(nums)
            totalratio += int(nums[0]) * int(nums[1])
        print(totalratio)












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