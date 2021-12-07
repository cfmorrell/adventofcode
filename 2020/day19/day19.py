# import re
# def part1(filename):
#     rules = {}
#     messages = []
#     with open(filename) as f:
#         for line in f:
#             if line[0].isdigit():
#                 line = line.strip().split(': ')
#                 rules[line[0]] = line[1].replace('"','').replace(' ','')
#             else:
#                 messages.append(line.strip())
#     print('Finished Reading file')
#     rule0 = [rules['0'].replace(' ','')]
#     count = 0
#     while [re.search('^[ab]*$',i) for i in rule0].count(None) > 0:# and count <= 5:
#         for r in range(len(rule0)):
#             for c in rule0[r]:
#                 if c in 'ab':
#                     continue
#                 if '|' in rules[c]:
#                     thisrulelist = rules[c].split('|')
#                     thisrule = rule0[r]
#                     rule0[r] = rule0[r].replace(c,thisrulelist[0])
#                     for rl in thisrulelist[1:]:
#                         rule0.append(thisrule.replace(c,rl))
#                 else:
#                     rule0[r] = rule0[r].replace(c,rules[c])
#     print('Finished expanding rules')
#     matchcount = 0
#     for message in messages:
#         match = [1 for i in rule0 if i == message]
#         if sum(match) > 0:
#             print('Matched',message)
#             matchcount += 1
#     print(matchcount)

import regex
# import sys

def parse(f):
    rules = {}
    for line in f:
        if line == '\n':
            break
        ident, rule = line.rstrip().split(': ')
        rules[int(ident)] = rule.replace('"', '')
    return rules, f.read().splitlines()

def match(rules, messages):
    def expand(word):
        return group(int(word)) if word.isdigit() else word
    def group(ident):
        return '(?:' + ''.join(map(expand, rules[ident].split())) + ')'
    reg = regex.compile(group(0))
    return sum(reg.fullmatch(m) is not None for m in messages)

with open('input.txt') as f:
    rules, messages = parse(f)
print(match(rules, messages))

rules[8] = '42 +'
rules[11] = '(?P<group> 42 (?&group)? 31 )'
print(match(rules, messages))