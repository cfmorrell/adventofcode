def dostuff(a,m):
    result = ''
    for i in range(len(a)):
        if m[i] == 'X':
            result += a[i]
        elif m[i] == '1':
            result += '1'
        elif m[i] == '0':
            result += '0'
    return result

def part1(filename):
    with open(filename) as f:
        memory = {}
        mask = ''
        for line in f:
            line = line.strip().split(' = ')
            if line[0] == 'mask':
                mask = line[1]
                print(mask)
            else:
                memloc = int(line[0].replace('mem[','')[:-1])
                memval = str(bin(int(line[1])))[2:].zfill(36)
                memval = int(dostuff(memval,mask),base=2)
                print(memloc,memval)
                memory[memloc] = memval
        print(sum(memory.values()))

def part2(filename):
    with open(filename) as f:
        memory = {}
        mask = ''
        for line in f:
            line = line.strip().split(' = ')
            if line[0] == 'mask':
                mask = line[1]
                print(mask)
            else:
                memloc = str(bin(int(line[0].replace('mem[','')[:-1])))[2:].zfill(36)
                memval = int(line[1])
                




part1('smallinput.txt')
part1('input.txt')
part2('smallinput2.txt')