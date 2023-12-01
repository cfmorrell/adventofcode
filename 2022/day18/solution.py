import numpy as np
from matplotlib import pyplot as plt

def part1():
    space = []
    with open(filename) as f:
        for line in f:
            space.append([int(i) for i in line.strip().split(',')])
    # print(space)
    surfacecount = 0
    for loc in space:
        neighbors = [[loc[0]+1,loc[1],loc[2]],[loc[0]-1,loc[1],loc[2]],\
                     [loc[0],loc[1]+1,loc[2]],[loc[0],loc[1]-1,loc[2]],\
                     [loc[0],loc[1],loc[2]+1],[loc[0],loc[1],loc[2]-1]]
        startingsurfaces = 6
        for neighbor in neighbors:
            if neighbor in space:
                startingsurfaces -= 1
        surfacecount += startingsurfaces
        # print('Adding {} surfaces. Total is now: {}'.format(startingsurfaces,surfacecount))
    print('Original Surface Count: ',surfacecount)
    
    # plt.rcParams["figure.figsize"] = [10, 10]
    # plt.rcParams["figure.autolayout"] = True
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')

    # x = [i[0] for i in space]
    # y = [i[1] for i in space]
    # z = [i[2] for i in space]
    # ax.scatter(x,y,z,c=z,alpha=1)
    # plt.show()

    return((space,surfacecount))

def genneighbors(loc):
    neighbors = [[loc[0]+1,loc[1],loc[2]],[loc[0]-1,loc[1],loc[2]],\
                 [loc[0],loc[1]+1,loc[2]],[loc[0],loc[1]-1,loc[2]],\
                 [loc[0],loc[1],loc[2]+1],[loc[0],loc[1],loc[2]-1]]    
    return neighbors


def part2():
    visibleset = set()
    space,surfacecount = part1()
    maxcorner = max((max([i[0] for i in space]),max([i[1] for i in space]),max([i[2] for i in space]))) + 1
    grid = np.full((maxcorner,maxcorner,maxcorner),0)
    for loc in space:
        grid[loc[0],loc[1],loc[2]] = 1
    # print(grid)
    newsurfacecount = 0
    
    for loc in space:
        print('Checking:',loc)
        visible = False
        if sum(grid[:loc[0],loc[1],loc[2]]) == 0:
            print('Visible from x=0')
            visibleset.add((loc,('x0')))
            newsurfacecount += 1
            neighbors = genneighbors((loc[0]-1,loc[1],loc[2]))
            newsurfacecount -= 1
            for n in neighbors:
                if n in space:
                    newsurfacecount += 1
        if sum(grid[loc[0]+1:,loc[1],loc[2]]) == 0:
            print('Visible from x=max')
            newsurfacecount += 1
            neighbors = genneighbors((loc[0]+1,loc[1],loc[2]))
            newsurfacecount -= 1
            for n in neighbors:
                if n in space:
                    newsurfacecount += 1
        if sum(grid[loc[0],:loc[1],loc[2]]) == 0:
            print('Visible from y=0')
            newsurfacecount += 1
            neighbors = genneighbors((loc[0],loc[1]-1,loc[2]))
            newsurfacecount -= 1
            for n in neighbors:
                if n in space:
                    newsurfacecount += 1
        if sum(grid[loc[0],loc[1]+1:,loc[2]]) == 0:
            print('Visible from y=max')
            newsurfacecount += 1
            neighbors = genneighbors((loc[0],loc[1]+1,loc[2]))
            newsurfacecount -= 1
            for n in neighbors:
                if n in space:
                    newsurfacecount += 1
        if sum(grid[loc[0],loc[1],:loc[2]]) == 0:
            print('Visible from z=0')
            newsurfacecount += 1
            neighbors = genneighbors((loc[0],loc[1],loc[2]-1))
            newsurfacecount -= 1
            for n in neighbors:
                if n in space:
                    newsurfacecount += 1
        if sum(grid[loc[0],loc[1],loc[2]+1:]) == 0:
            print('Visible from z=max')
            newsurfacecount += 1
            neighbors = genneighbors((loc[0],loc[1],loc[2]+1))
            newsurfacecount -= 1
            for n in neighbors:
                if n in space:
                    newsurfacecount += 1
        print('Checked visibility:',loc,newsurfacecount)
        # if visible:
        #     neighbors = [[loc[0]+1,loc[1],loc[2]],[loc[0]-1,loc[1],loc[2]],\
        #                     [loc[0],loc[1]+1,loc[2]],[loc[0],loc[1]-1,loc[2]],\
        #                     [loc[0],loc[1],loc[2]+1],[loc[0],loc[1],loc[2]-1]]
        #     for n in neighbors:
        #         if n in space:
        #             newsurfacecount += 1
        #     print("Checked neighbors too",loc,newsurfacecount)

    # emptyspaces = []
    # for x in range(maxcorner+2):
    #     for y in range(maxcorner+2):
    #         for z in range(maxcorner+2):
    #             emptyspaces.append([x,y,z])
    # # print(emptyspaces)
    # for s in space:
    #     emptyspaces.remove(s)
    # # print(emptyspaces)
    # for loc in emptyspaces:
    #     neighbors = [[loc[0]+1,loc[1],loc[2]],[loc[0]-1,loc[1],loc[2]],\
    #                  [loc[0],loc[1]+1,loc[2]],[loc[0],loc[1]-1,loc[2]],\
    #                  [loc[0],loc[1],loc[2]+1],[loc[0],loc[1],loc[2]-1]]
    #     contained = True
    #     for n in neighbors:
    #         if n not in space:
    #             contained = False
    #     if contained:
    #         print('Surrounded Location:',loc)
    #         surfacecount -= 6
    # print('Updated Surface Count:',surfacecount)
    









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