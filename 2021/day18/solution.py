#!/usr/local/bin/python3

def part1(filename):
    with open(filename) as f:
        for line in f:
            l = eval(line.strip())
            print(l,type(l))

# def part2(filename):


part1('sampleinput.txt')
# part1('input.txt')
# part2('sampleinput.txt')
# part2('input.txt')