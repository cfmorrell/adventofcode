from itertools import product
def findneighbors(x,y,z):
    neighbors = list(product([x-1,x,x+1],[y-1,y,y+1],[z-1,z,z+1]))
    neighbors.remove((x,y,z))
    return set(neighbors)



def part1(filename):
    activeset = set()
    with open(filename) as f:
        for y,line in enumerate(f):
            for x,val in enumerate(line):
                if val == '#':
                    activeset.add((x,y,0))
    for _ in range(6):
        nextturnactiveset = set()
        minx = min([i[0] for i in list(activeset)])
        miny = min([i[1] for i in list(activeset)])
        minz = min([i[2] for i in list(activeset)])
        maxx = max([i[0] for i in list(activeset)])
        maxy = max([i[1] for i in list(activeset)])
        maxz = max([i[2] for i in list(activeset)])
        fullset = set(product(range(minx-1,maxx+2),range(miny-1,maxy+2),range(minz-1,maxz+2)))
        for i in fullset:
            if len(activeset.intersection(findneighbors(*i))) == 3:
                nextturnactiveset.add(i)
            elif i in activeset and len(activeset.intersection(findneighbors(*i))) == 2:
                nextturnactiveset.add(i)
        activeset = nextturnactiveset
        print("Num Active:",len(activeset))


def findneighbors2(x,y,z,w):
    neighbors = list(product([x-1,x,x+1],[y-1,y,y+1],[z-1,z,z+1],[w-1,w,w+1]))
    neighbors.remove((x,y,z,w))
    return set(neighbors)

def part2(filename):
    activeset = set()
    with open(filename) as f:
        for y,line in enumerate(f):
            for x,val in enumerate(line):
                if val == '#':
                    activeset.add((x,y,0,0))
    for _ in range(6):
        nextturnactiveset = set()
        minx = min([i[0] for i in list(activeset)])
        miny = min([i[1] for i in list(activeset)])
        minz = min([i[2] for i in list(activeset)])
        minw = min([i[3] for i in list(activeset)])
        maxx = max([i[0] for i in list(activeset)])
        maxy = max([i[1] for i in list(activeset)])
        maxz = max([i[2] for i in list(activeset)])
        maxw = max([i[3] for i in list(activeset)])

        fullset = set(product(range(minx-1,maxx+2),range(miny-1,maxy+2),range(minz-1,maxz+2),range(minw-1,maxw+2)))
        for i in fullset:
            if len(activeset.intersection(findneighbors2(*i))) == 3:
                nextturnactiveset.add(i)
            elif i in activeset and len(activeset.intersection(findneighbors2(*i))) == 2:
                nextturnactiveset.add(i)
        activeset = nextturnactiveset
        print("Num Active:",len(activeset))



# findneighbors(2,2,2)
# part1('smallinput.txt')
# part1('input.txt')
# part2('smallinput.txt')
part2('input.txt')