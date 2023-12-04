def part1():
    diemax = {'red':12,'green':13,'blue':14}
    gamesum = 0
    with open(filename) as f:
        for line in f:
            nogo = False
            gamenum = int(line.split(':')[0].split()[1])
            # print(gamenum)
            rounds = line.split(':')[1].split(';')
            # print(rounds)
            for round in rounds:
                for color in round.split(', '):
                    if int(color.split()[0]) > diemax[color.split()[1]]:
                        nogo = True
            if not nogo:
                gamesum += gamenum
    print(gamesum)

def part2():
    powersum = 0
    with open(filename) as f:
        for line in f:
            diemin = {'red':0,'green':0,'blue':0}
            gamenum = int(line.split(':')[0].split()[1])
            rounds = line.split(':')[1].split(';')
            for round in rounds:
                for color in round.split(', '):
                    if int(color.split()[0]) > diemin[color.split()[1]]:
                        diemin[color.split()[1]] = int(color.split()[0])
            power = diemin['red'] * diemin['green'] * diemin['blue']
            powersum += power                        
    print(powersum)








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