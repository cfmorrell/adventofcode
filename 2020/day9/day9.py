def part1(filename,width):
    with open(filename) as f:
        data = [int(i) for i in f.read().split()]
    start = -1
    numbers = []
    for i in data[width:]:
        start += 1
        numbers = data[start:start+width]
        for x in range(width):
            # print("Checking if {} - {} ({}) is in {}".format(i,numbers[x],i-numbers[x],numbers))
            if i - numbers[x] in numbers:
                # print("It is, moving on.")
                break
            elif i - numbers[x] not in numbers and x == width - 1:
                return i

def part2(filename,input):
    with open(filename) as f:
        data = [int(i) for i in f.read().split()]    
    for i in range(3,len(data)):
        for j in range(len(data)):
            if sum(data[j:j+i]) == input:
                print('Found it',data[j:j+i],min(data[j:j+i]),max(data[j:j+i]))
                print('Weakness: {}'.format(max(data[j:j+i])+min(data[j:j+i])))


part2input = part1('smallinput.txt',5)
print(part2input)
part2('smallinput.txt',part2input)
part2input = part1('input.txt',25)
print(part2input)
part2('input.txt',part2input)
