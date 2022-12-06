import string
def part1():
    with open(filename) as f:
        f = f.read()
        towers,moves = f.split('\n\n')
        towers = towers.split('\n')
        print(towers)
        tlist = []
        for i in range(10):
            if str(i) in towers[-1]:
                col = []
                loc = towers[-1].find(str(i))
                print(loc)
                for j in reversed(towers[:-1]):
                    if j[loc] != ' ':
                        col.insert(0,j[loc])
                        print(j[loc])
                tlist.append(col)
        print(tlist)

        for move in moves.split('\n'):
            m = move.split(' ')
            num = int(m[1])
            src = int(m[3])
            dst = int(m[-1])
            for i in range(num):
                tlist[dst-1].insert(0,tlist[src-1].pop(0))
        result = ''.join([col[0] for col in tlist])
        print(result)
            
def part2():
    with open(filename) as f:
        f = f.read()
        towers,moves = f.split('\n\n')
        towers = towers.split('\n')
        tlist = []
        for i in range(10):
            if str(i) in towers[-1]:
                col = []
                loc = towers[-1].find(str(i))
                for j in reversed(towers[:-1]):
                    if j[loc] != ' ':
                        col.insert(0,j[loc])
                tlist.append(col)
        # print(tlist)

        for move in moves.split('\n'):
            # print(move)
            m = move.split(' ')
            num = int(m[1])
            src = int(m[3])
            dst = int(m[-1])
            # for i in range(num):
            tlist[dst-1][:0] = tlist[src-1][0:num]
            del tlist[src-1][0:num]
            # print(tlist)



        result = ''.join(['' if len(col) == 0 else col[0] for col in tlist])
        print(result)










import sys
try:
    if sys.argv[1] not in ['T','F']:
        raise
    filename = 'sampleinput.txt' if sys.argv[1] == 'T' else 'input.txt'
    part = int(sys.argv[2])
except:
    print('Usage: solution.py [T|F] [1|2] (Testing & Part)')
    exit()


if part == 1:
    part1()
else:
    part2()