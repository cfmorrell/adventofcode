### HELP!!!: https://github.com/tobstern/AoC2022/blob/master/day07.py#L68

from collections import defaultdict as dd

path = ''
dirs = dd(list)
ls_executed = False
with open('input.txt') as f:
    for line in f:
        cmd = line.strip().split(" ")
        if line[0] == "$":
            ls_executed = False
            # it is a command
            if cmd[1] == "cd":
                if cmd[2] != "..":
                    # go into directory
                    if cmd[2] != "/":
                        path += cmd[-1] + "/"
                    else:
                        path = "/"
                else:
                    # go out of directory
                    # here is an empty string occuring
                    # - select [:-2]
                    path = "/".join(path.split("/")[:-2]) + "/"
            elif cmd[1] == "ls":
                # second occuring command - ls:
                ls_executed = True
        elif ls_executed:
            # now see, if there are more directories and/or files
            if cmd[0] == "dir":
                # there is a directory
                dirs[path] += [cmd[1]]
            else:
                # there is a file
                fname = cmd[1]
                dirs[path] += [[int(cmd[0]), fname]]
for dir in dirs.keys():
    print(dir,dirs[dir])

def count_size(d, fs, s):
    # count the sizes of all files and containing directories
    # recursively
    # return list of sizes of those directories
    for f in fs:
        # print(f"for dir: {d} and the files: {fs} and the size: {s}")
        if len(f) == 2:
            # it is a file
            s += [f[0]]
        else:
            # it is a directory -> go into it and sum up its files
            new_d = d + f + "/"
            count_size(new_d, dirs[new_d], s)

    return s
            
def part1():
    siz = []
    for d, fs in dirs.items():
        siz += [sum(count_size(d, fs, []))]

    res1 = sum([s for s in siz if s <= 100000])

    print(f"Part 1 result is: {res1}")



def part2():
    siz = []
    for d, fs in dirs.items():
        siz += [sum(count_size(d, fs, []))]
    max_space = int(70e6)
    least_space = int(30e6)
    used_space = siz[0]
    available_space = max_space - used_space
    needed_space = least_space - available_space
    for d, fs in dirs.items():
        # find size of all directories (reuse siz of part 1)
        dsize = min([s for s in siz if s > needed_space])

    print(f"Part 2 result is: {dsize}")











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