import numpy as np
from collections import defaultdict

def part1():
    beamlocations = set()
    totalsplits = 0
    with open(filename) as f:
        beamlocations.add(f.readline().index('S'))
        for line in f:
            splitterlocations = [i for i, c in enumerate(line) if c == '^']
            if len(splitterlocations) == 0:
                continue
            else:
                newbeamlocations = set()
                for loc in beamlocations:
                    if loc in splitterlocations:
                        totalsplits += 1
                        newbeamlocations.add(loc - 1)
                        newbeamlocations.add(loc + 1)
                    else:
                        newbeamlocations.add(loc)
                beamlocations = newbeamlocations
            # print(line)
            # print(beamlocations)
    print(totalsplits)


def part2():
    # beamlocations = set()
    totalpaths = 1
    with open(filename) as f:
        row = list(f.readline().strip())
        s_col = row.index('S')
        beams = {s_col: 1}      # column -> number of paths in this column
        print(''.join(row), "Path Count:", totalpaths)
        # beamlocations.add(row.index('S'))
        for line in f:
            row = list(line.strip())
            splitterlocations = {i for i, c in enumerate(row) if c == '^'}
            new_beams = defaultdict(int)
            for col, count in beams.items():
                if col in splitterlocations:
                    # split into two beams, each inheriting `count` paths
                    left = col - 1
                    right = col + 1
                    if 0 <= left < len(row):
                        new_beams[left] += count
                        row[left] = '|'
                    if 0 <= right < len(row):
                        new_beams[right] += count
                        row[right] = '|'
                else:
                    # just continues straight down
                    if 0 <= col < len(row):
                        new_beams[col] += count
                        row[col] = '|'
            beams = dict(new_beams)
            totalpaths = sum(beams.values())
            print(''.join(row), "Path Count:", totalpaths)












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