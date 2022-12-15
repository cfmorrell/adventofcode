import string
import numpy as np
from math import lcm
def part1():
    monkeys = []
    with open(filename) as f:
        monkeydata = f.read().split('\n\n')
        for m in monkeydata:
            thismonkey = {}
            lines = m.split('\n')
            for line in lines:
                if 'Starting' in line:
                    thismonkey['items'] = [int(i) for i in line.strip().split(': ')[1].split(', ')]
                elif 'Operation' in line:
                    thismonkey['operation'] = line.strip().split('= ')[-1]
                elif 'Test:' in line:
                    thismonkey['test'] = int(line.strip().split(' ')[-1])
                elif 'true:' in line:
                    thismonkey['destiftrue'] = int(line.strip().split(' ')[-1])
                elif 'false:' in line:
                    thismonkey['destiffalse'] = int(line.strip().split(' ')[-1])
            thismonkey['itemcount'] = 0
            monkeys.append(thismonkey)
    for round in range(20):
        # print('Round #{}'.format(round+1))
        for m in range(len(monkeys)):
            for i in range(len(monkeys[m]['items'])):
                monkeys[m]['itemcount'] += 1
                old = monkeys[m]['items'].pop(0)
                worrylevel = eval(monkeys[m]['operation'])//3
                if worrylevel % monkeys[m]['test'] == 0:
                    monkeys[monkeys[m]['destiftrue']]['items'].append(worrylevel)
                else:
                    monkeys[monkeys[m]['destiffalse']]['items'].append(worrylevel)
    itemcounts = list(reversed(sorted([m['itemcount'] for m in monkeys])))
    print(itemcounts)
    # print(itemcounts[0] * itemcounts[1])


def part2():
    monkeys = []
    with open(filename) as f:
        monkeydata = f.read().split('\n\n')
        for m in monkeydata:
            thismonkey = {}
            lines = m.split('\n')
            for line in lines:
                if 'Starting' in line:
                    thismonkey['items'] = [int(i) for i in line.strip().split(': ')[1].split(', ')]
                elif 'Operation' in line:
                    thismonkey['operation'] = line.strip().split('= ')[-1]
                elif 'Test:' in line:
                    thismonkey['test'] = int(line.strip().split(' ')[-1])
                elif 'true:' in line:
                    thismonkey['destiftrue'] = int(line.strip().split(' ')[-1])
                elif 'false:' in line:
                    thismonkey['destiffalse'] = int(line.strip().split(' ')[-1])
            thismonkey['itemcount'] = 0
            monkeys.append(thismonkey)
    totaltest = np.prod([j['test'] for j in monkeys])
    # multiple = lcm(*[j['test'] for j in monkeys])
    # print(totaltest)
    checkvals = [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
    for round in range(1,10001):
        # print('Round #{}'.format(round+1))
        for m in range(len(monkeys)):
            for i in range(len(monkeys[m]['items'])):
                monkeys[m]['itemcount'] += 1
                old = monkeys[m]['items'].pop(0)
                worrylevel = eval(monkeys[m]['operation']) % totaltest
                if worrylevel % monkeys[m]['test'] == 0:
                    # if worrylevel % multiple == 0:
                        # worrylevel = multiple
                        # print('lined up')
                    # worrylevel = monkeys[m]['test']
                    monkeys[monkeys[m]['destiftrue']]['items'].append(worrylevel)
                else:
                    monkeys[monkeys[m]['destiffalse']]['items'].append(worrylevel)
        if round in checkvals:
            print(round)
            itemcounts = list(reversed(sorted([m['itemcount'] for m in monkeys])))
            print(itemcounts)
    print(itemcounts[0] * itemcounts[1])











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