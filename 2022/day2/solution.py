testing = False
part = 2
filename = 'sampleinput.txt' if testing else 'input.txt'


def part1():
    with open(filename) as f:
        scoredict = {'X':1, 'Y':2, 'Z':3}
        scoremapping = {'X':'A','Y':'B','Z':'C'}
        score = 0
        for line in f:
            elf,me = [i.strip() for i in line.split()]
            score += scoredict[me]
            if elf == scoremapping[me]:
                score += 3
            elif (elf == 'A' and me == 'Y') or (elf == 'B' and me == 'Z') or (elf == 'C' and me == 'X'):
                score += 6
            print(elf,me,score)

def part2():
    with open(filename) as f:
        scoredict = {'A':1, 'B':2, 'C':3}
        scoremapping = {'X':'A','Y':'B','Z':'C'}
        score = 0
        for line in f:
            elf,me = [i.strip() for i in line.split()]
            if me == 'Y':
                score += 3 + scoredict[elf]
            elif me == 'X':
                if elf == 'A':
                    score += 3
                elif elf == 'B':
                    score += 1
                elif elf == 'C':
                    score += 2
            elif me == 'Z':
                if elf == 'A':
                    score += 8
                elif elf == 'B':
                    score += 9
                elif elf == 'C':
                    score += 7
            print(elf,me,score)

if part == 1:
    part1()
else:
    part2()