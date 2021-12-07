def part1(numbers):
    counter = 2020 - len(numbers)
    while counter > 0:
        r = list(reversed(numbers[:-1]))
        try:
            l = r.index(numbers[-1])
            numbers.append(l+1)
        except:
            numbers.append(0)
        counter -= 1
    print(numbers[-1])

def part2(numbers):
    d = {}
    end = 30000000
    for i,v in enumerate(numbers[:-1]):
        d[v] = i+1
    lastpair = (len(numbers),numbers[-1])
    for turnnumber in range(len(numbers)+1,end+1):
        # print("Turn #{}, looking for {} in {}".format(turnnumber,lastpair[1],d))
        lastseen = d.get(lastpair[1])
        if lastseen == None:
            diff = 0
            thispair = (turnnumber,diff)
            # print("Didn't find {}, adding 0 to dictionary next turn".format(lastpair[1]))
        else:
            diff = turnnumber - lastseen - 1
            thispair = (turnnumber,diff)
            # print("Found {} on previous turn {}, adding {} to dictionary next turn".format(lastpair[1],d[lastpair[1]],diff))
        d[lastpair[1]] = lastpair[0]
        lastpair = thispair
    print(thispair,len(d))

#I struggled with doing this in constant space.  The 3000000 element list wasn't going to work, so a 
#dictionary that only maintained the last time a number was seen got me there.


#part1([0,12,6,13,20,1,17])
#part1([0,3,6])
# part2([0,3,6])
# part2([3,1,2])
part2([0,12,6,13,20,1,17])