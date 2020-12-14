def part1(filename):
    with open(filename) as f:
        earliesttime = int(f.readline())
        buses = [int(i) for i in f.readline().split(',') if i.isdigit()]
    # print(earliesttime,buses)

    actualtime = earliesttime
    while 1:
        # print(actualtime)
        for bus in buses:
            if actualtime % bus == 0:
                return(bus * (actualtime - earliesttime))
        actualtime += 1


# def part2(filename):
#     with open(filename) as f:
#         f = f.readlines()
#     busvalues = f[1].strip().split(',')
#     busdict = {int(v):i for i,v in enumerate(busvalues) if v.isdigit()}
#     busids = list(busdict.keys())

#     print("BusIDs:",busids)
#     print("BusDict:",busdict)

#     step = busids[0]
#     start = 0
#     for busid in busids[1:]:
#         print("Looking at busid:",busid)
#         delta = busdict[busid]
#         for i in range(start,step*busid,step):
#             print(i)
#             if not (i+delta)%busid:
#                 step = step*busid
#                 start = i
    # print(start)




def mod_filter_seq(seq, a, b):
    return (x for x in seq if not (x+a) % b)

import itertools
def part2(filename):
    with open(filename) as f:
        f = f.readlines()
    buslist = [(i,int(v)) for i,v in enumerate(f[1].strip().split(',')) if v.isdigit()]
    seq = itertools.count(1)
    for (a, b) in buslist:
        seq = mod_filter_seq(seq, a, b)
    print(next(seq))
# 3417



# print(part1('smallinput.txt'))
# print(part1('input.txt'))
# part2('smallinput.txt')
part2('input.txt')