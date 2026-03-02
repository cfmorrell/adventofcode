import numpy as np

def part1():
    data = np.genfromtxt(filename, dtype=str)
    int_part = data[:-1].astype(int)
    last_row = data[-1]
    print(int_part)
    print(last_row)
    total = 0
    for index,operator in enumerate(last_row):
        if operator == '+':
            total += int_part[:,index].sum()
        elif operator == '*':
            total += int_part[:,index].prod()
        print(total)


def part2():
    with open(filename) as f:
        lines = [line.rstrip("\n") for line in f]
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]
    grid = np.array([list(row) for row in lines])
    cols = grid.T
    print(cols)
    total = 0
    firstrow = True
    rowvals = np.array([], dtype=int)
    for row in cols:
        if firstrow:
            operator = row[-1]
            firstrow = False
        if len(''.join(row).strip()) == 0:
            firstrow = True
            if operator == '+':
                total += rowvals.sum()
            elif operator == '*':
                total += rowvals.prod()
            print("Total so far:", total)
            rowvals = np.array([], dtype=int)

        else:
            rowvals = np.append(rowvals, int(''.join(row[:-1])))
            print(rowvals)
    if operator == '+':
        total += rowvals.sum()
    elif operator == '*':
        total += rowvals.prod()
    print("Total so far:", total)




            # data = np.genfromtxt(filename, dtype=str)
    # int_part = data[:-1]
    # last_row = data[-1]
    # print(int_part)
    # print(last_row)
    # total = 0
    # for index,operator in enumerate(last_row):
    #     col = int_part[:,index]
    #     char_grid = expand_strings_to_char_grid(col, pad=' ')
    #     print(char_grid)
    #     vals = np.array([], dtype=int)
    #     for col in char_grid.T:
    #         vals = np.append(vals,int(''.join(col)))
    #     if operator == '+':
    #         total += vals.sum()
    #     elif operator == '*':
    #         total += vals.prod()
    #     print(total)










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