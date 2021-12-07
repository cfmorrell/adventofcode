import statistics
def part1(filename):
    with open(filename) as f:
        positions = [int(i) for i in f.read().strip().split(',')]
        targetpos = statistics.median(positions)
        totaldistance = 0
        for i in positions:
            totaldistance += abs(targetpos-i)
        print(totaldistance)

import datetime
def part2(filename):
    start = datetime.datetime.now()
    print(start)
    with open(filename) as f:
        positions = [int(i) for i in f.read().strip().split(',')]
        # print(positions)
        totaldistance = 0
        for i in positions:
            totaldistance += sum(list(range(1,abs(positions[0]-i+1))))
            # print(positions[0],i,list(range(1,abs(positions[0]-i+1))))
            # print(totaldistance)
        mindistance = totaldistance
        for targetpos in range(min(positions),max(positions)+1):
            totaldistance = 0
            for i in positions:
                thisdistance = sum(list(range(1,max(targetpos,i)-min(targetpos,i)+1)))
                # print("From {} to {} is distance {}".format(targetpos,i,thisdistance))
                totaldistance += thisdistance
            # print("Total distance for {} is {}".format(targetpos,totaldistance))
            if totaldistance < mindistance:
                mindistance = totaldistance
            elif totaldistance > mindistance:
                print("Best distance is {} at {}".format(mindistance,targetpos))
                break
    end = datetime.datetime.now()
    print(end)
    delta = end - start
    print(delta)

# part1('sampleinput.txt')
# part1('input.txt')
# part2('sampleinput.txt')
part2('input.txt')