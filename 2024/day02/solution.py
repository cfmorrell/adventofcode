def part1():
    counter = 0
    with open(filename) as f:
        for line in f:
            report = [int(i) for i in line.strip().split()]
            safe = True
            if sorted(report) != report and list(reversed(sorted(report))) != report:
                safe = False
            if safe:
                for index,item in enumerate(report):
                    if report.count(item) > 1:
                        safe = False
                    if index < len(report) - 1:
                        if abs(item - report[index + 1]) > 3:
                            safe = False
            if safe:
                counter += 1
    print(counter)

def checkifsafe(report):
    # print(report)
    safe = True
    if sorted(report) != report and list(reversed(sorted(report))) != report:
        safe = False
    if safe:
        for index,item in enumerate(report):
            if report.count(item) > 1:
                safe = False
            if index < len(report) - 1:
                if abs(item - report[index + 1]) > 3:
                    safe = False
    return safe

def part2():
    counter = 0
    with open(filename) as f:
        for line in f:
            report = [int(i) for i in line.strip().split()]
            safe = False
            if not checkifsafe(report):
                for i in range(len(report)):
                    if checkifsafe(report[:i]+report[i+1:]):
                        safe = True
            else:
                safe = True
            if safe:
                counter += 1
        print(counter)


    print(counter)







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