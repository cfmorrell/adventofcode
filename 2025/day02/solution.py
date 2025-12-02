def validaterange_part1(r):
    invalid_ids = []
    start = int(r.split('-')[0])
    end = int(r.split('-')[1])
    for i in range(start, end+1):
        id = str(i)
        doubles = False
        if len(id) % 2 == 1:
            continue
        else:
            half = len(id)//2
            firsthalf = id[:half]
            secondhalf = id[half:]
            if firsthalf == secondhalf:
                invalid_ids.append(i)
    return invalid_ids

def part1():
    invalid_ids = []
    with open(filename) as f:
        for r in f.read().split(','):
            invalid_ids += validaterange_part1(r)
            print(invalid_ids)
    print(sum(invalid_ids))

def validaterange_part2(r):
    invalid_ids = set()
    start = int(r.split('-')[0])
    end = int(r.split('-')[1])
    for i in range(start, end+1):
        # print("Checking ID:",i)
        id = str(i)
        for j in range(1, len(id)//2 + 1):
            if id.count(id[:j]) == len(id)/j:
                print("Invalid ID found:",i)
                invalid_ids.add(i)
    return invalid_ids

def part2():
    invalid_ids = set()
    with open(filename) as f:
        for r in f.read().split(','):
            invalid_ids.update(validaterange_part2(r))
            print(invalid_ids)
    print(sum(list(invalid_ids)))











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