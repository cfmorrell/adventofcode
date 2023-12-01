import re
def part1():
    with open(filename) as f:
        totalval = 0
        for line in f:
        ## Regular Expression Solution    
            digits = re.findall('\d+',line)

        ## Brute Force Solution##
            # digits = [i for i in line if i.isdigit()]
            thisval = int(digits[0] + digits[-1])
            totalval += thisval
            print(thisval,totalval)
        print(totalval)

def part2():
    dict = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8', 'nine':'9'}
    with open(filename) as f:
        totalval = 0
        for line in f:
            digits = re.findall('(?=(\d|one|two|three|four|five|six|seven|eight|nine))',line)
            totalval += int(dict.get(digits[0],digits[0]) + dict.get(digits[-1],digits[-1]))

        ## Naive Solution
            # leftval = findnum(line,dict,0,len(line),1)
            # rightval = findnum(line,dict,len(line)-2,-1,-1)
            # thisval = int(leftval + rightval)
            # totalval += thisval
        print(totalval)

def findnum(line,dict,start,stop,step):
    for index in range(start,stop,step):
        if line[index].isdigit():
            return line[index]
        else:
            for num in dict.keys():
                if line[index:].find(num) == 0:
                    return dict[num]


import sys,time,string
try:
    if sys.argv[1] not in ['T','F']:
        raise
    filename = 'sampleinput2.txt' if sys.argv[1] == 'T' else 'input.txt'
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