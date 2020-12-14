def part1(filename):
    with open(filename) as f:
        f = f.read().split('\n\n')
        total = 0
        for group in f:
            g = [i for i in group if i != '\n']
            total += len(set(g))
            print(total)

def part2(filename):
    with open(filename) as f:
        f = f.read().split('\n\n')
        total = 0
        for group in f:
            g = [set(list(i)) for i in group.split()]
            s = g[0]
            for p in g:
                s &= p
            # print(len(s))
            total += len(s)
        print(total)



# part1('input.txt')
part2('input.txt')