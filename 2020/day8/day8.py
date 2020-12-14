import copy

def part1(filename):
    with open(filename) as f:
        l = [[i.split()[0],int(i.split()[1])] for i in f.read().split('\n')]
    # print(l)

    for i,v in enumerate(l):
        # print(l)
        l2 = copy.deepcopy(l)        
        if v[0] == 'nop':
            l2[i][0] = 'jmp'
        elif v[0] == 'jmp':
            l2[i][0] = 'nop'
        else:
            continue
        # print(l)

        executed = []
        accumulator = 0
        cmd = 0
        while 1:#cmd <= len(l2):
            # print(executed,accumulator,cmd,l2[cmd])
            if cmd in executed:
                print('Infinite Loop',accumulator)
                break
            elif cmd >= len(l2):
                print('Ended Gracefully',accumulator)
                break
            elif l2[cmd][0] == 'nop':
                executed.append(cmd)
                cmd += 1
            elif l2[cmd][0] == 'acc':
                executed.append(cmd)
                accumulator += l2[cmd][1]
                cmd += 1
            elif l2[cmd][0] == 'jmp':
                executed.append(cmd)
                cmd += l2[cmd][1]            


part1('input.txt')