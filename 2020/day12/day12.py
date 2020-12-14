import math

def part1(filename):
    with open(filename) as f:
        inst = [(i[0],int(i[1:])) for i in  f.readlines()]

    direction = 90
    loc = [0,0]
    for i in inst:
        if i[0] == 'N':
            loc[1] += i[1]
        elif i[0] == 'E':
            loc[0] += i[1]
        elif i[0] == 'S':
            loc[1] -= i[1]
        elif i[0] == 'W':
            loc[0] -= i[1]
        elif i[0] == 'R':
            direction = (direction + i[1]) % 360
        elif i[0] == 'L':
            direction = (direction - i[1]) % 360
        elif i[0] == 'F':
            loc[0] += int(i[1] * math.sin(math.radians(direction)))
            loc[1] += int(i[1] * math.cos(math.radians(direction)))
    print(loc,sum([abs(i) for i in loc]))
        
def part2(filename):
    with open(filename) as f:
        inst = [(i[0],int(i[1:])) for i in  f.readlines()]

    loc = [0,0]
    wloc = [10,1]
    for i in inst:
        if i[0] == 'N':
            wloc[1] += i[1]
        elif i[0] == 'E':
            wloc[0] += i[1]
        elif i[0] == 'S':
            wloc[1] -= i[1]
        elif i[0] == 'W':
            wloc[0] -= i[1]
        elif i[0] == 'R':
            qx = int(round(math.cos(math.radians(-i[1])) * wloc[0] - math.sin(math.radians(-i[1])) * wloc[1]))
            qy = int(round(math.sin(math.radians(-i[1])) * wloc[0] + math.cos(math.radians(-i[1])) * wloc[1]))
            wloc[0] = qx
            wloc[1] = qy
        elif i[0] == 'L':
            qx = int(round(math.cos(math.radians(i[1])) * wloc[0] - math.sin(math.radians(i[1])) * wloc[1]))
            qy = int(round(math.sin(math.radians(i[1])) * wloc[0] + math.cos(math.radians(i[1])) * wloc[1]))
            wloc[0] = qx
            wloc[1] = qy
        elif i[0] == 'F':
            loc[0] = loc[0] + (wloc[0] * i[1])
            loc[1] = loc[1] + (wloc[1] * i[1])
        print(i,loc,wloc,sum([abs(i) for i in loc]))
        # input("")

part1('input.txt')
part2('input.txt')