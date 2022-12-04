import string
def part1():
    with open(filename) as f:
        priority = 0
        dupes = []
        for line in f:
            line = line.strip()
            midpoint = len(line)//2
            firsthalf = line[:midpoint]
            secondhalf = line[midpoint:]
            for c in firsthalf:
                if c in secondhalf:
                    dupes.append(c)
                    break
        for i in dupes:
            if i in string.ascii_lowercase:
                priority += string.ascii_lowercase.index(i)+1
            else:
                priority += string.ascii_uppercase.index(i)+27
    print(priority)

def part2():
    priority = 0
    with open(filename) as f:
        lines = f.readlines()
        numlines = len(lines)
        for i in range(0,numlines,3):
            a,b,c = lines[i].strip(),lines[i+1].strip(),lines[i+2].strip()
            for j in a:
                if j in a and j in b and j in c:
                    if j in string.ascii_lowercase:
                        priority += string.ascii_lowercase.index(j)+1
                    else:
                        priority += string.ascii_uppercase.index(j)+27
                    print(priority)
                    break






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