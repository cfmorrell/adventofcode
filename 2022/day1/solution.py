testing = False
part = 2
filename = 'sampleinput.txt' if testing else 'input.txt'


def part1():
    with open(filename) as f:
        biggest = 0
        elves = [i.split() for i in f.read().split('\n\n')]
        print(elves)
        for elf in elves:
            weight = sum([int(i) for i in elf])
            print(weight,biggest)
            if weight > biggest:
                biggest = weight
        print(biggest)

def part2():
    with open(filename) as f:
        elves = [i.split() for i in f.read().split('\n\n')]
        elvweights = []
        for elf in elves:
            weight = sum([int(i) for i in elf])
            elvweights.append(weight)
        print(sum(sorted(elvweights)[-3:]))

if part == 1:
    part1()
else:
    part2()