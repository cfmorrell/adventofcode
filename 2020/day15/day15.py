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
    end = 10
    for i,v in enumerate(numbers):
        if v in d:
            d[v].append(i)
        else:
            d[v] = [i]
    lastval = numbers.pop()
    print(d)
    for i in range(len(numbers),end):
        print("Looking for",lastval)
        if lastval not in d or max(d[lastval]) == i-1:
            print("Value not found")
            if 0 in d:
                d[0].append(i)
            else:
                d[0] = [i]
            lastval = 0
        else:
            lastoccurence = max(d[lastval])
            print("last occurence",lastoccurence)
            diff = i - lastoccurence
            print("Distance is",diff)
            if diff in d:
                d[diff].append(i)
            else:
                d[diff] = [i]
            lastval = diff
        print(lastval,d)



#part1([0,12,6,13,20,1,17])
#part1([0,3,6])
part2([0,3,6])