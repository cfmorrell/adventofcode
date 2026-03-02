import numpy as np
import math

def dist(p1, p2):
    return math.sqrt(
        (p2[0] - p1[0])**2 +
        (p2[1] - p1[1])**2 +
        (p2[2] - p1[2])**2
    )

def part1():
    with open(filename) as f:
        arr = [tuple(int(i) for i in line.split(',')) for line in f.read().strip().split("\n")]
    total_points = len(arr)
    pairs = []
    for point in arr:
        for other_point in arr:
            d = dist(point, other_point)
            if point != other_point and ((other_point, point),d) not in pairs:
                pairs.append(((point, other_point),d))
    pairs.sort(key=lambda x: x[1])
    circuits = {pairs[0][0][0]: 1, pairs[0][0][1]: 1}
    for i in range(1,10):
        # for k,v in circuits.items():
        #     print(f"{k}: {v}")
        # print("Checking pair", i, pairs[i])
        if pairs[i][0][0] in circuits and pairs[i][0][1] in circuits:
            # print("Both in circuits")
            if circuits[pairs[i][0][0]] != circuits[pairs[i][0][1]]:
                val_to_replace = circuits[pairs[i][0][1]]
                val_to_keep = circuits[pairs[i][0][0]]
                # print("Merging circuits", val_to_replace, "into", val_to_keep)
                for k in circuits:
                    if circuits[k] == val_to_replace:
                        circuits[k] = val_to_keep
        elif pairs[i][0][0] not in circuits and pairs[i][0][1] not in circuits:
            # print("New circuit found")
            circuit_value = max(circuits.values()) + 1
            circuits[pairs[i][0][0]] = circuit_value
            circuits[pairs[i][0][1]] = circuit_value
        elif pairs[i][0][0] in circuits:
            # print(pairs[i][0][0], "in circuits")
            # print("Adding", pairs[i][0][1], "to circuit", circuits[pairs[i][0][0]])
            circuits[pairs[i][0][1]] = circuits[pairs[i][0][0]]
        elif pairs[i][0][1] in circuits:
            # print(pairs[i][0][1], "in circuits")
            # print("Adding", pairs[i][0][0], "to circuit", circuits[pairs[i][0][1]])
            circuits[pairs[i][0][0]] = circuits[pairs[i][0][1]]
    num_circuits = max(circuits.values())
    for pair in pairs:
        if pair[0][0] not in circuits:
            # print("Pair[0] not in circuits:", pair[0][0])
            num_circuits += 1
            circuits[pair[0][0]] = num_circuits
        if pair[0][1] not in circuits:
            # print("Pair[1] not in circuits:", pair[0][1])
            num_circuits += 1
            circuits[pair[0][1]] = num_circuits
    # for k,v in circuits.items():
        # print(f"{k}: {v}")    
    counts = []
    for i in set(circuits.values()):
        counts.append(list(circuits.values()).count(i))
    print(math.prod(sorted(counts)[-3:]))




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