def part1():
    with open(filename) as f:
        content = f.read()
    rules,updates = content.split('\n\n')
    rules = [[int(i) for i in rule.split('|')] for rule in rules.split()]
    updates = [[int(i) for i in update.split(',')] for update in updates.split()]
    total = 0
    for update in updates:
        badupdate = False
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) >= update.index(rule[1]):
                    badupdate = True
                    break
        if not badupdate:
            total += update[len(update)//2]
    print(total)

def checkbadupdate(update,rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) >= update.index(rule[1]):
                return True
    return False


def part2():
    with open(filename) as f:
        content = f.read()
    rules,updates = content.split('\n\n')
    rules = [[int(i) for i in rule.split('|')] for rule in rules.split()]
    updates = [[int(i) for i in update.split(',')] for update in updates.split()]
    badupdates = []
    for update in updates:
        badupdate = checkbadupdate(update,rules)
        if badupdate:
            badupdates.append(update)
    total = 0
    for badupdate in badupdates:
        print(badupdate)
        stillBad = True
        while stillBad:
            print('anotherlap')
            stillBad = False
            for rule in rules:
                # print(rule)
                if rule[0] in badupdate and rule[1] in badupdate:
                    if badupdate.index(rule[0]) >= badupdate.index(rule[1]):
                     
                        badupdate.insert(badupdate.index(rule[0]),badupdate.pop(badupdate.index(rule[1])))
                        stillBad = True
        print('Fixed',badupdate)
        total += badupdate[len(badupdate)//2]
    print(total)











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