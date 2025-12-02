def part1():
    num = 50
    count = 0
    with open(filename) as f:
        turns = f.read().split()
        for turn in turns:
            direction = turn[0]
            distance = int(turn[1:])
            if direction == "L":
                num = (num - distance) % 100
            else:
                num = (num + distance) % 100
            if num == 0:
                count += 1
        print(count)

def part2():
    num = 50
    count = 0
    with open(filename) as f:
        turns = f.read().split()
        for turn in turns:
            direction = turn[0]
            distance = int(turn[1:])
            if direction == "L":
                newnum = num - distance
            else:
                newnum = num + distance
            if direction == "L" and newnum <= 0:
                passes = 1 + abs(newnum) // 100
                if num == 0:
                    passes -= 1
                count += passes
            elif direction == "R" and newnum >= 100:
                passes = newnum // 100
                count += passes

            num = newnum % 100
        print("Count: ",count)







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