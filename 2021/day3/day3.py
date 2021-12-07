def part1(filename):
    with open(filename) as f:
        gamma = ''
        epsilon = ''
        l = [list(i) for i in f.read().split('\n')]
        d = {index:list(ele[0:]) for index,ele in enumerate(zip(*l))}
        for k,v in d.items():
            if v.count('1') > len(v)/2:
                gamma += '1'
                epsilon += '0'
            else:
                gamma += '0'
                epsilon += '1'
        print(int(gamma,2)*int(epsilon,2))

import numpy as np
def part2(filename):
    with open(filename) as f:
        a = np.array([list(i) for i in f.read().split('\n')])
        o2a = np.copy(a)
        i = 0
        while len(o2a) > 1:
            l = list(o2a[:,i])
            toremove = '0' if l.count('1') >= l.count('0') else '1'
            for index,value in reversed(list(enumerate(l))):
                if value == toremove:
                    o2a = np.delete(o2a,index,0)
            i += 1
        o2rating = int(''.join([str(i) for i in list(o2a[0])]),2)

        co2a = np.copy(a)
        i = 0
        while len(co2a) > 1:
            l = list(co2a[:,i])
            toremove = '0' if l.count('1') < l.count('0') else '1'
            for index,value in reversed(list(enumerate(l))):
                if value == toremove:
                    co2a = np.delete(co2a,index,0)
            i += 1
        co2rating = int(''.join([str(i) for i in list(co2a[0])]),2)

        print(o2rating * co2rating)




# part1('sampleinput.txt')
# part1('input.txt')
# part2('sampleinput.txt')
part2('input.txt')