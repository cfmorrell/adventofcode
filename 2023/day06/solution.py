def part1():
    with open(filename) as f:
        times = [int(i) for i in f.readline().split(':')[1].split()]
        distances = [int(i) for i in f.readline().split(':')[1].split()]
    rounds = dict(zip(times, distances))
    print(rounds)
    winningoptions = []
    for time,recorddistance in rounds.items():
        thiswinningoption = 0
        for buttontime in range(time):
            speed = buttontime
            movetime = time - buttontime
            movedistance = movetime * speed
            if movedistance > recorddistance:
                thiswinningoption += 1
        winningoptions.append(thiswinningoption)
    print(winningoptions)
    result = 1
    for option in winningoptions:
        result *= option
    print(result)



def part2():
    with open(filename) as f:
        time = int(f.readline().split(':')[1].replace(' ',''))
        recorddistance = int(f.readline().split(':')[1].replace(' ',''))
    print(time, recorddistance)
    result = 0
    for buttontime in range(time):
        if time%1000 == 0:
            print(time)
        speed = buttontime
        movetime = time - buttontime
        movedistance = movetime * speed
        if movedistance > recorddistance:
            result += 1

    print(result)










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