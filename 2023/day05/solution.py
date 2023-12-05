def part1():
    with open(filename) as f:
        seeds = [int(i) for i in f.readline().strip().split(': ')[1].split()]
        transforms = [i.strip().split('\n')[1:] for i in f.read().strip().split('\n\n')]
        for transform in transforms:
            newseeds = seeds[::]
            for conversion in transform:
                deststart,sourcestart,rangelength = [int(i) for i in conversion.split()]
                sourcerange = (sourcestart, sourcestart + rangelength - 1)
                for index,seed in enumerate(seeds):
                    if sourcerange[0] <= seed <= sourcerange[1]:
                        newseeds[index] = deststart + seed - sourcerange[0]
            seeds = newseeds[::]
        print(min(seeds))

def part2():
    with open(filename) as f:
        seedranges = [int(i) for i in f.readline().strip().split(': ')[1].split()]
        seeds = list(range(seedranges[0],seedranges[0] + seedranges[1]))
        seeds.extend(list(range(seedranges[2],seedranges[2] + seedranges[3])))
        print('Number of seeds:',len(seeds))


        transforms = [i.strip().split('\n')[1:] for i in f.read().strip().split('\n\n')]
        for transform in transforms:
            newseeds = seeds[::]
            for conversion in transform:
                deststart,sourcestart,rangelength = [int(i) for i in conversion.split()]
                sourcerange = (sourcestart, sourcestart + rangelength - 1)
                for index,seed in enumerate(seeds):
                    if sourcerange[0] <= seed <= sourcerange[1]:
                        newseeds[index] = deststart + seed - sourcerange[0]
            seeds = newseeds[::]
            print('Transform Complete')
        print(min(seeds))










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