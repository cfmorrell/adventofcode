import re
def part1():
    with open(filename) as f:
        mem = f.read().strip()
    pattern = "mul\(\d+,\d+\)"
    pattern2 = "\d+"
    matches = re.findall(pattern,mem)
    print(matches)
    total = 0
    for match in matches:
        digits = re.findall(pattern2,match)
        x,y = [int(i) for i in digits]
        total += (x*y)
    print(total)

def part2():
    with open(filename) as f:
        mem = f.read().strip()
    print(mem)
    pattern = "mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
    pattern2 = "\d+"
    matches = re.findall(pattern,mem)
    print(matches)
    total = 0
    calc = True
    for match in matches:
        if match == "do()":
            calc = True
            print("Start adding")
        elif match == "don't()":
            calc = False
            print("Stop adding")
        elif calc:
            digits = re.findall(pattern2,match)
            x,y = [int(i) for i in digits]
            total += (x*y)
            print(total)



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