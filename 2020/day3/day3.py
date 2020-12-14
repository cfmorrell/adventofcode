def part1(filename):
    m = []
    with open(filename) as f:
        for line in f:
            line = list(line.strip())
            m.append(line)

    x = 0
    y = 0
    treecount = 0
    for row in m:
        print(x,row)
        if row[x%len(row)] == '#':
            treecount += 1
        x += 3
    print(treecount)
        
def part2(filename):
    m = []
    with open(filename) as f:
        for line in f:
            line = list(line.strip())
            m.append(line)
    total = 1
    changes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    for change in changes:
        x,y,treecount = 0,0,0
        x_change,y_change = change
        while y < len(m):
            # print(x,m[y])
            if m[y][x%len(m[y])] == '#':
                treecount += 1
            x += x_change
            y += y_change
        total *= treecount
        print(treecount,total)

#part1('input.txt')
part2('input.txt')