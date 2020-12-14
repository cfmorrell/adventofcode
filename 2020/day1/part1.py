def part1():
    with open('input.txt') as f:
        l = [int(i) for i in f.read().split()]
        for i,v in enumerate(l):
            for i2,v2 in enumerate(l):
                if i == i2:
                    continue
                elif (v+v2) == 2020:
                    print(v,v2,v*v2)

def part2():
    with open('input.txt') as f:
        l = [int(i) for i in f.read().split()]
        for i,v in enumerate(l):
            for i2,v2 in enumerate(l):
                for i3,v3 in enumerate(l):
                    if i == i2 or i == i3 or i2 == i3:
                        continue
                    elif (v+v2+v3) == 2020:
                        print(v,v2,v3,v*v2*v3)

part2()