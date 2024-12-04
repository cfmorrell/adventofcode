import numpy as np
import re

def part1():
    with open(filename) as f:
        lines = np.array([list(line.strip()) for line in f.readlines()])
    checks = []
    for row in lines:
        checks.append(''.join(row))
    for i in range(len(lines[0])):
        checks.append(''.join(lines[:,i]))
    for i in range(-len(lines)+1,len(lines[0])):
        checks.append(''.join(np.diag(lines,k=i)))
    for i in range(-len(lines)+1,len(lines[0])):
        checks.append(''.join(np.diag(np.fliplr(lines),k=i)))

    pattern = "XMAS"
    pattern2 = "SAMX"
    count = 0
    for check in checks:
        count += len(re.findall(pattern,check))
        count += len(re.findall(pattern2,check))
        # print(check)
        # print(re.findall(pattern,check),count)
        # print(re.findall(pattern2,check),count)        
    print(count)

def part2():
    count = 0
    with open(filename) as f:
        lines = np.array([list(line.strip()) for line in f.readlines()])
    for i in range(lines.shape[0] - 2):
        for j in range(lines.shape[1] - 2):
            found = False
            sub_array = lines[i:i+3,j:j+3]
            for k in range(4):
                diag1,diag2 = ''.join(np.diag(sub_array)),''.join(np.diag(np.fliplr(sub_array)))
                # print(diag1,diag2)
                if (diag1 == 'MAS' or diag1 == 'SAM') and (diag2== 'MAS' or diag2 == 'SAM'):
                    found = True
                    # print(found)
                    break
                sub_array = np.rot90(sub_array)
            if found:
                count += 1
    print(count)










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