def part1(filename):
    with open(filename) as f:
        total = 0
        for line in f:
            for num in line.strip().split('|')[1].split():
                if len(num) in [2,3,4,7]:
                    total += 1
        print(total)

def part2(filename):
    with open(filename) as f:
        total = 0
        for line in f:
            input,output = [[set(j) for j in i.split()] for i in line.strip().split('|')]
            input = sorted(input, key=len)
            numbers = ['']*10
            #1
            numbers[1] = input[0]
            #7
            numbers[7] = input[1]
            #4
            numbers[4] = input[2]
            #8
            numbers[8] = input[9]
            #3
            if numbers[1] <= input[3]:
                numbers[3] = input[3]
            elif numbers[1] <= input[4]:
                numbers[3] = input[4]
            elif numbers[1] <= input[5]:
                numbers[3] = input[5]
            #9
            if numbers[3] <= input[6]:
                numbers[9] = input[6]
            elif numbers[3] <= input[7]:
                numbers[9] = input[7]
            elif numbers[3] <= input[8]:
                numbers[9] = input[8]
            #6
            if not input[6].issuperset(numbers[1]):
                numbers[6] = input[6]
            elif not input[7].issuperset(numbers[1]):
                numbers[6] = input[7]
            elif not input[8].issuperset(numbers[1]):
                numbers[6] = input[8]
            #0
            if input[6] not in numbers:
                numbers[0] = input[6]
            elif input[7] not in numbers:
                numbers[0] = input[7]
            elif input[8] not in numbers:
                numbers[0] = input[8]
            #5
            # print("Nine: {}".format(''.join(list(numbers[9]))))
            # print("Three: {}".format(''.join(list(numbers[3]))))
            # print()),input[3:6])
            if input[3].union(numbers[1]) == numbers[9]:
                numbers[5] = input[3]
            elif input[4].union(numbers[1]) == numbers[9]:
                numbers[5] = input[4]
            elif input[5].union(numbers[1]) == numbers[9]:
                numbers[5] = input[5]
            #2
            if input[3] not in numbers:
                numbers[2] = input[3]
            elif input[4] not in numbers:
                numbers[2] = input[4]
            elif input[5] not in numbers:
                numbers[2] = input[5]
                
            result = [str(numbers.index(item)) for item in output]
            total += int(''.join(result))
            print(total)


# part1('sampleinput.txt')
# part1('input.txt')
# part2('sampleinput.txt')
part2('input.txt')