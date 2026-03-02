def part1():
    spoiled = []
    fresh = []
    with open(filename) as f:
        freshids,ingredients = f.read().strip().split('\n\n')
        ids = []
        for id in freshids.split('\n'):
            ids.append([int(x) for x in id.split('-')])
        print(ids)
        for ingredient in [int(x) for x in ingredients.split('\n')]:
            print(ingredient)
            for id in ids:
                if id[0] <= ingredient <= id[1]:
                    fresh.append(ingredient)
                    break
                else:
                    spoiled.append(ingredient)
        print(fresh,spoiled)
        print(len(fresh))

def part2():
    with open(filename) as f:
        freshids,_ = f.read().strip().split('\n\n')
        id_ranges = []
        for id in freshids.split('\n'):
            begin,end = ([int(x) for x in id.split('-')])
            if len(id_ranges) == 0:
                id_ranges.append([begin,end])
            else:
                added = False
                for i in range(len(id_ranges)):
                    if begin <= id_ranges[i][1] + 1 and end >= id_ranges[i][0] - 1:
                        id_ranges[i][0] = min(begin,id_ranges[i][0])
                        id_ranges[i][1] = max(end,id_ranges[i][1])
                        added = True
                        break
                if not added:
                    id_ranges.append([begin,end])
        id_ranges.sort()
        for i in range(len(id_ranges)-1,0,-1):
            if id_ranges[i][0] <= id_ranges[i-1][1] + 1:
                id_ranges[i-1][0] = min(id_ranges[i][0],id_ranges[i-1][0])
                id_ranges[i-1][1] = max(id_ranges[i][1],id_ranges[i-1][1])
                del id_ranges[i]
        total = 0
        for r in id_ranges:
            total += r[1] - r[0] + 1
        print(id_ranges)
        print(total)









import sys,time,string
try:
    if sys.argv[1] not in ['T','F']:
        raise
    filename = 'sampleinput.txt' if sys.argv[1] == 'T' else 'input.txt'
    part = int(sys.argv[2])
except:
    print('Usage: solution.py [T|F] [1|2] (Testing & Part)')
    exit()


start = time.perf_counter()
if part == 1:
    part1()
else:
    part2()
end = time.perf_counter()
ms = (end-start)# * 10**6
print(f"Elapsed {ms:.03f} seconds.")
print(f"Elapsed {ms*10**3:.03f} milliseconds.")
print(f"Elapsed {ms*10**6:.03f} microsecondss.")