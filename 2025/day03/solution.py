def part1():
    with open(filename) as f:
        joltage = 0
        for battery_bank in f.read().split('\n'):
            battery_bank = [int(x) for x in battery_bank]
            sub_bank = battery_bank[0:-1]
            first_digit = max(sub_bank)
            sub_bank = battery_bank[battery_bank.index(first_digit)+1:]
            second_digit = max(sub_bank)
            joltage += int(str(first_digit) + str(second_digit))
        print("Total Joltage:", joltage)

def part2():
    with open(filename) as f:
        joltage = 0
        for battery_bank in f.read().split('\n'):
            battery_bank = [int(x) for x in battery_bank]
            digits = []
            for i in range(12,0,-1):
                if i == 1:
                    sub_bank = battery_bank[:]
                else:
                    sub_bank = battery_bank[:-i+1]
                digits.append(max(sub_bank))
                battery_bank = battery_bank[battery_bank.index(max(sub_bank))+1:]
            joltage += int(''.join([str(x) for x in digits]))
        print("Total Joltage:", joltage)

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