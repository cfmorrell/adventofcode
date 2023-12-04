def part1():
    value = 0
    with open(filename) as f:
        for line in f:
            winningnumbers = set([int(i) for i in line.split('|')[0].split(':')[1].split()])
            mynumbers = set([int(i) for i in line.split('|')[1].split()])
            # print(winningnumbers)
            # print(mynumbers)
            score = int(2**(len(winningnumbers & mynumbers)-1))
            value += score
    print(value)

def part2():
    with open(filename) as f:
        cards = f.readlines()
    numcards = [1]*len(cards)
    for index,card in enumerate(cards):
        winningnumbers = set([int(i) for i in card.strip().split('|')[0].split(':')[1].split()])
        mynumbers = set([int(i) for i in card.strip().split('|')[1].split()])
        score = len(winningnumbers & mynumbers)
        for i in range(index+1,index+score+1):
            numcards[i] += numcards[index]
        # print(score)
        # print(numcards)
    print(sum(numcards))



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