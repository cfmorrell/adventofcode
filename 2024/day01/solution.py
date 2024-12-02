def part1():
    left = []
    right = []
    with open(filename) as f:
        for line in f:
            nums = [int(i) for i in line.strip().split()]
            left.append(nums[0])
            right.append(nums[1])
    distance = 0
    left.sort()
    right.sort()
    for i in range(len(left)):
        distance += abs(left[i] - right[i])
    print(distance)

def part2():
    with open(filename) as f:
        left = []
        right = []
        with open(filename) as f:
            for line in f:
                nums = [int(i) for i in line.strip().split()]
                left.append(nums[0])
                right.append(nums[1])
    similarity = 0
    for item in left:
        similarity += item * right.count(item)
    print(similarity)        











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