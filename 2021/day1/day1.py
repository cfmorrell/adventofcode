def part1():
    with open('input.txt') as f:
        l = [int(i) for i in f.read().split()]
        increases = 0
        previous = l[0]
        for i in l:
            if i > previous:
                increases += 1
            previous = i
    print(increases)

def part2():
    with open('input.txt') as f:
        l = [int(i) for i in f.read().split()]
        increases = 0
        previous = l[0] + l[1] + l[2]
        for i,v in enumerate(l):
            if i >= len(l)-2:
                break
            s = l[i] + l[i+1] + l[i+2]
            if s > previous:
                increases += 1
            previous = s
    print(increases)

part2()