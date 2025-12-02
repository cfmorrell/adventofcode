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
            print("Turn",turn)
            direction = turn[0]
            distance = int(turn[1:])
            if direction == "L":
                newnum = num - distance
            else:
                newnum = num + distance
            if newnum >= 0:
                print("Started at",num,", ended at",newnum)
            else:
                print("Started at",num,", ended at",newnum%100,"-",newnum)
            if direction == "L" and newnum <= 0:
                print("Passed Zero Left!!!")
                passes = 1 + abs(newnum) // 100
                if num == 0:
                    passes -= 1
                print("Passed",passes,"times")
                count += passes
            elif direction == "R" and newnum >= 100:
                print("Passed Zero Right!!!")
                passes = newnum // 100
                count += passes
                print("Passed",passes,"times")

            print("Count: ",count)
            num = newnum % 100






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