def part1():
    with open(filename) as f:
        instructions = list(f.readline().strip())
        instructions = [0 if i=='L' else 1 for i in instructions]
        f.readline()
        map = {}
        for line in f:
            location = line.split(' = ')[0].strip()
            left = line.split('(')[1].split(',')[0]
            right = line.split(', ')[1].strip(')\n')
            map[location] = (left,right)
        location = 'AAA'
        print(instructions,map)
    counter = 0
    while location != 'ZZZ':
        location = map[location][instructions[0]]
        instructions.append(instructions.pop(0))
        counter += 1
    print(counter)


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