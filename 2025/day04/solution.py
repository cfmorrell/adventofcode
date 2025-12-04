import numpy as np

def part1():
    with open(filename) as f:
        lines = [list(line) for line in f.read().strip().split("\n")]
    arr = np.array(lines)
    padded = np.pad(arr, pad_width=1, mode='constant', constant_values=' ')

    # print(arr)
    numrolls = 0
    for r in range(arr.shape[0]):
        for c in range(arr.shape[1]):
            window = padded[r:r+3, c:c+3]
            count = np.sum(window == '@')
            if arr[r, c] == '@':
                count -= 1
            if count < 4 and arr[r, c] == '@':
                print(f"Found at {r},{c}")
                # print(window)
                numrolls += 1
    print(numrolls)

def part2():
    with open(filename) as f:
        lines = [list(line) for line in f.read().strip().split("\n")]
    arr = np.array(lines)
    numrolls = 0
    canremove = True
    while canremove:
        temparr = arr.copy()
        padded = np.pad(arr, pad_width=1, mode='constant', constant_values=' ')
        # print(arr)
        for r in range(arr.shape[0]):
            for c in range(arr.shape[1]):
                window = padded[r:r+3, c:c+3]
                count = np.sum(window == '@')
                if arr[r, c] == '@':
                    count -= 1
                if count < 4 and arr[r, c] == '@':
                    # print(f"Found at {r},{c}")
                    numrolls += 1
                    temparr[r, c] = '.'
        if np.array_equal(temparr, arr):
            canremove = False
        arr = temparr
        print(numrolls)












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