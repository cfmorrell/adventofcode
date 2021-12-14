import collections
def part1(filename):
    with open(filename) as f:
        ruledict = {}
        polymer = ''
        for line in f:
            if '->' in line:
                ruledict[line.split('->')[0].strip()] = line.split('->')[1].strip()
            elif len(line.strip()) > 0:
                polymer = line.strip()
        # print(polymer,ruledict)
        for j in range(10):
            temppolymer = ''
            for i in range(len(polymer)):
                if polymer[i:i+2] in ruledict:
                    temppolymer += polymer[i] + ruledict[polymer[i:i+2]]
                else:
                    temppolymer += polymer[i]
            # print(temppolymer)
            polymer = temppolymer
        frequency = collections.Counter(polymer).most_common()
        print(frequency[0][1]-frequency[-1][1])


def part2(filename):
    with open(filename) as f:
        ruledict = {}
        polymer = ''
        for line in f:
            if '->' in line:
                ruledict[line.split('->')[0].strip()] = line.split('->')[1].strip()
            elif len(line.strip()) > 0:
                polymer = line.strip()


# part1('sampleinput.txt')
# part1('input.txt')
part2('sampleinput.txt')
# part2('input.txt')