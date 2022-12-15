import string
import numpy as np
def part1():
    with open(filename) as f:
        stoppoints = [20,60,100,140,180,220]
        valuesum = 1
        addcycleone = True
        sigstrengthsum = 0
        for cycle in range(1,223):
            if addcycleone == True:
                line = f.readline()
            if cycle in stoppoints:
                signalstrength = cycle * valuesum
                sigstrengthsum += signalstrength
                print('{}: Cycle: {}, Sum: {}, Signal Strength: {}, Sum: {}'.format(line.strip(), cycle, valuesum, signalstrength, sigstrengthsum))
            if 'noop' in line:
                addcycleone = True
            else:
                if addcycleone == True:
                    addcycleone = False
                else:
                    valuesum += int(line.strip().split()[1])
                    addcycleone = True
            

def part2():
    crt = np.full((6,40),'.')
    regx = 1
    with open(filename) as f:
        addcycleone = True
        for cycle in range(1,241):
            if (cycle-1)%40 in range(regx-1,regx+2):
                x = (cycle-1) % 40
                y = (cycle-1) // 40
                crt[y,x] = '#'
            # print('RegX: {}, Range: {} to {}, Cycle: {}, Pos: ({},{})'.format(regx,regx-1,regx+1,cycle,y,x))
            if addcycleone == True:
                line = f.readline()
            if 'noop' in line:
                addcycleone = True
            else:
                if addcycleone == True:
                    addcycleone = False
                else:
                    regx += int(line.strip().split()[1])
                    addcycleone = True
            for row in crt:
                print(''.join(row))
            print('----------------------------------------')









import sys
try:
    if sys.argv[1] not in ['T','F']:
        raise
    filename = 'sampleinput.txt' if sys.argv[1] == 'T' else 'input.txt'
    part = int(sys.argv[2])
except:
    print('Usage: solution.py [T|F] [1|2] (Testing & Part)')
    exit()


if part == 1:
    part1()
else:
    part2()