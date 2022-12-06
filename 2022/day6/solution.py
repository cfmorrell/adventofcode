import string
def part1():
    with open(filename) as f:
        stream = f.read().strip()
        pos = 4
        while True:
            frame = stream[pos-4:pos]
            # print(frame)
            dupfound = False
            for c in frame:
                if frame.count(c) > 1:
                    dupfound = True

            if not dupfound:
                print(pos)
                print(frame)
                break
            pos += 1


def part2():
    with open(filename) as f:
        stream = f.read().strip()
        pos = 14
        while True:
            frame = stream[pos-14:pos]
            # print(frame)
            dupfound = False
            for c in frame:
                if frame.count(c) > 1:
                    dupfound = True

            if not dupfound:
                print(pos)
                print(frame)
                break
            pos += 1










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