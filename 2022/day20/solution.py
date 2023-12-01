def part1():
    with open(filename) as f:
        nums = [[int(i),False] for i in f.read().strip().split()]
    print(nums)
    while False in [i[1] for i in nums]:
        pointer = [i[1] for i in nums].index(False)
        # print(pointer)
        numtomove = nums.pop(pointer)
        numtomove[1] = True
        if numtomove[0] < 0:
            pointer -= 1
        print('Moving {} to {}'.format(numtomove[0],(pointer+numtomove[0])%(len(nums)+1)))
        nums.insert((pointer+numtomove[0])%(len(nums)+1),numtomove)
        # print(nums)
        print([i[0] for i in nums])

    # for i in range(len(nums)):
    #     numtomove=nums.pop(i + adjuster)
    #     destination = (i+adjuster+numtomove)%(len(nums)+1)
    #     print('Moving {} to {}'.format(numtomove,destination))
    #     nums.insert(numtomove,destination)
    #     if destination <= i - 1:
    #         adjuster -= 1
    #     # elif destination == i + 1:
    #     #     adjuster = 1
    #     else:
    #         adjuster = 0
    #     # print('Next Location {} for value {}'.format(pointer,nums[pointer]))
    #     print(nums)
    #     print('Round {} with adjuster {}'.format(i,adjuster))
    #     print('---------------------')

def part2():
    with open(filename) as f:
        pass











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