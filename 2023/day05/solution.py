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
        seeddata = [int(i) for i in f.readline().strip().split(': ')[1].split()]
        seedranges = []
        for i in range(0,len(seeddata),2):
            seedranges.append((seeddata[i],seeddata[i] + seeddata[i+1]-1))
        seedranges.sort()
        print(seedranges)
        transforms = [i.strip().split('\n')[1:] for i in f.read().strip().split('\n\n')]
        print(transforms)
        for transform in transforms:
            newseedranges = []
            for conversion in transform:
                deststart,sourcestart,rangelength = [int(i) for i in conversion.split()]
                shift = deststart - sourcestart
                sourcerange = (sourcestart, sourcestart + rangelength - 1)
                print("Source Range:",sourcerange)
                print("Destination Start:",deststart)
                print("Shift:",shift)
                for seedrange in seedranges:
                    print("Checking seed range:",seedrange)
                    if sourcerange[0] <= seedrange[0] <= sourcerange[1] and seedrange[1] > sourcerange[1]:
                        print("Starts in range, ends past range")
                        newrange1 = (sourcerange[0],seedrange[0]-1)
                        newrange2 = (seedrange[0] + shift, sourcerange[1]+ shift)
                        newrange3 = (sourcerange[1]+1,seedrange[1])
                        newseedranges.extend([newrange1,newrange2,newrange3])
                    elif sourcerange[0] <= seedrange[0] <= sourcerange[1] and sourcerange[0] <= seedrange[1] <= sourcerange[1]:
                        print("Starts and ends in range")
                        newseedranges.append((seedrange[0] + shift, seedrange[1]+ shift))
                    elif seedrange[0] < sourcerange[0] and sourcerange[0] <= seedrange[1] <= sourcerange[1]:
                        print("Starts before, ends in range")
                        newrange1 = (seedrange[0],sourcerange[0]-1)
                        newrange2 = (sourcerange[0] + shift, seedrange[1] + shift)
                        newrange3 = (seedrange[1]+1,sourcerange[1])
                        newseedranges.extend([newrange1,newrange2,newrange3])
                    elif seedrange[0] < sourcerange[0] and seedrange[1] > sourcerange[1]:
                        print("Stars before, ends after")
                        newrange1 = (seedrange[0],sourcerange[0]-1)
                        newrange2 = (sourcerange[0] + shift, sourcerange[1] + shift)
                        newrange3 = (sourcerange[1]+1,seedrange[1])
                        newseedranges.extend([newrange1,newrange2,newrange3])
                    else:
                        print("No impact to range")
                        newseedranges.append(seedrange)
            print(newseedranges)
            quit()

            print(seedranges)
            seedranges = newseedranges.copy()
            print('Transform Complete')
            end = time.perf_counter()
            ms = (end-start)# * 10**6
            print(f"Elapsed {ms:.03f} seconds.")
        print(seedranges)










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