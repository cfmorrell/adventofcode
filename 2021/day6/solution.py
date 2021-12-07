def part1(filename,numdays):
    with open(filename) as f:
        startingfish = [int(i) for i in f.read().strip().split(',')]
        fishlist = [0]*9
        for i in startingfish:
            fishlist[i] += 1
        print("Start: {}".format(fishlist))
        for i in range(1,numdays+1):
            tempfishlist = fishlist[::]
            fishlist = [0]*9
            for j in range(8):
                fishlist[j] = tempfishlist[j+1]
            fishlist[8] = tempfishlist[0]
            fishlist[6] += tempfishlist[0]
            print("After {} days: {}".format(i,fishlist))
        print("Total fish: {}".format(sum(fishlist)))


def part2(filename):
    part1(filename,256)

# part1('sampleinput.txt')
# part1('input.txt')
# part2('sampleinput.txt')
part2('input.txt')