import string
def part1():
    with open(filename) as f:
        overlapcount = 0
        for line in f:
            halves = line.strip().split(',')
            first = [int(i) for i in halves[0].split('-')]
            second = [int(i) for i in halves[1].split('-')]
            if (first[0] <= second[0] and first[1] >= second[1]) or (first[0] >= second[0] and first[1] <= second[1]):
                overlapcount += 1
                print("overlap",first[0],second[0],first[1],second[1],line)
        print(overlapcount)

def part2():
    with open(filename) as f:
        overlapcount = 0
        for line in f:
            oldhalves = line.strip().split(',')
            halves = []
            for half in oldhalves:
                temp = [int(i) for i in half.split('-')]
                halves.append(temp)
            halves.sort()
            starta,enda = halves[0]
            startb,endb = halves[1]
            if enda >= startb:
                overlapcount += 1
                # print("overlap",halves)
        print(overlapcount)






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