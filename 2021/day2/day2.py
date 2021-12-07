def part1():
    with open('input.txt') as f:
        l = [i for i in f.read().split('\n')]
        depth = 0
        hpos = 0
        for i in l:
            direction,distance = i.split()
            if direction == 'forward':
                hpos += int(distance)
            elif direction == 'down':
                depth += int(distance)
            elif direction == 'up':
                depth -= int(distance)
    print(depth*hpos)

def part2():
    with open('input.txt') as f:
        l = [i for i in f.read().split('\n')]
        depth = 0
        hpos = 0
        aim = 0
        for i in l:
            direction,distance = i.split()
            if direction == 'forward':
                hpos += int(distance)
                depth += (aim * int(distance))
            elif direction == 'down':
                aim += int(distance)
            elif direction == 'up':
                aim -= int(distance)
    print(depth*hpos)

part2()