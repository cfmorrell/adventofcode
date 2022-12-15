import string
import numpy as np
import json

def compare(left,right):
    # print("Compare {} vs {} - new recursion".format(left,right))
    for j in range(max(len(left),len(right))):
        try:
            lval = left[j]
        except (IndexError):
            # print("Out of items on left")
            return True
        try:
            rval = right[j]
        except (IndexError):
            # print("Out of items on right")
            return False
        # print("Compare {} vs {} - in loop".format(lval,rval))
        if type(lval) == int and type(rval) == int:
            # print('int,int')
            if lval < rval:
                return True
            elif lval > rval:
                return False
        elif type(lval) == list and type(rval) == list:
            # print('list,list')
            result = compare(lval,rval)
            if result == True or result == False:
                return result
        elif type(lval) == list and type(rval) == int:
            # print('list,int')
            result = compare(lval,[rval])
            if result == True or result == False:
                return result
        elif type(lval) == int and type(rval) == list:
            # print('int,list')
            result = compare([lval],rval)
            if result == True or result == False:
                return result

def part1():
    with open(filename) as f:
        numpairs = (len(f.readlines())//3) + 1
        f.seek(0)
        correctorder = []
        for i in range(1,numpairs+1):
            left = json.loads(f.readline().strip())
            right = json.loads(f.readline().strip())
            f.readline()
            print("Compare:",left,right)
            if compare(left,right):
                correctorder.append(i)
                print("Correct")
            else:
                print("Not Correct")
            print('-----------------------------')
        print(correctorder)
        print(sum(correctorder))


def part2():
    packets = []
    with open(filename) as f:
        for i,line in enumerate(f):
            if len(line.strip()) > 0:
                packets.append(json.loads(line.strip()))
            # if i == 10:
            #     break
    packets.append([[2]])
    packets.append([[6]])
    # print(packets)
    outoforder = True
    while outoforder:
        # print('New round of sorting')
        outoforder = False
        for i in range(len(packets)-1):
            # print("Compare {} vs {}".format(packets[i],packets[i+1]))
            if not compare(packets[i],packets[i+1]):
                # print('Rearranged',i)
                outoforder = True
                hold = packets[i+1]
                packets[i+1] = packets[i]
                packets[i] = hold
    # for packet in packets:
    #     print(packet)
    # print(packets.index([[2]])+1)
    # print(packets.index([[6]])+1)
    print((packets.index([[2]])+1) * (packets.index([[6]])+1))











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