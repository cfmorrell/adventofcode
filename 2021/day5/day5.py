def part1(filename):
    with open(filename) as f:
        locations = {}
        for line in f:
            x1,y1 = [int(i) for i in line.split(' -> ')[0].split(',')]
            x2,y2 = [int(i) for i in line.split(' -> ')[1].split(',')]
            if x1 == x2:
                for y in range(min(y1,y2),max(y1,y2)+1):
                    if (x1,y) not in locations:
                        locations[(x1,y)] = 1
                    else:
                        locations[(x1,y)] += 1
            elif y1 == y2:
                for x in range(min(x1,x2),max(x1,x2)+1):
                    if (x,y1) not in locations:
                        locations[(x,y1)] = 1
                    else:
                        locations[(x,y1)] += 1
        v = locations.values()
        print(len(v) - v.count(1))

def part2(filename):
    with open(filename) as f:
        locations = {}
        for line in f:
            x1,y1 = [int(i) for i in line.split(' -> ')[0].split(',')]
            x2,y2 = [int(i) for i in line.split(' -> ')[1].split(',')]
            if x1 == x2:
                for y in range(min(y1,y2),max(y1,y2)+1):
                    if (x1,y) not in locations:
                        locations[(x1,y)] = 1
                    else:
                        locations[(x1,y)] += 1
            elif y1 == y2:
                for x in range(min(x1,x2),max(x1,x2)+1):
                    if (x,y1) not in locations:
                        locations[(x,y1)] = 1
                    else:
                        locations[(x,y1)] += 1
            elif abs(x1-x2) == abs(y1-y2):
                x,y = x1,y1
                for i in range(abs(x1-x2)+1):
                    if (x,y) not in locations:
                        locations[(x,y)] = 1
                    else:
                        locations[(x,y)] += 1
                    if x2 > x1:
                        x += 1
                    else:
                        x -= 1
                    if y2 > y1:
                        y += 1
                    else:
                        y -= 1


        v = locations.values()
        print(len(v) - v.count(1))

# part1('sampleinput.txt')
# part1('input.txt')
# part2('sampleinput.txt')
part2('input.txt')