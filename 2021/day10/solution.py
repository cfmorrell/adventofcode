def part1(filename):
    with open(filename) as f:
        left = '([{<'
        right = ')]}>'
        scoredict = {')':3,']':57,'}':1197,'>':25137}
        score = 0
        for line in f:
            stack = []
            for c in line:
                if c == '\n':
                    break
                elif c in left:
                    stack.append(c)
                elif c in right and stack[-1] == left[right.find(c)]:
                    stack.pop()
                else:
                    score += scoredict[c]
                    print(score, c, stack)
                    break

def part2(filename):
    with open(filename) as f:
        left = '([{<'
        right = ')]}>'
        scoredict = {')':1,']':2,'}':3,'>':4}
        allscores = []
        for line in f:
            stack = []
            for c in line:
                if c == '\n':
                    # print("Line to complete: {}".format(line))
                    # print(stack)
                    score = 0
                    for i in stack[::-1]:
                        score = (score * 5) + scoredict[right[left.find(i)]]
                        # print(score,i)
                    allscores.append(score)
                    break
                elif c in left:
                    stack.append(c)
                elif c in right and stack[-1] == left[right.find(c)]:
                    stack.pop()
                else:
                    # print("Line to throw out: {}".format(line))
                    break
        print(sorted(allscores))
        print(sorted(allscores)[int((len(allscores)/2))])



# part1('sampleinput.txt')
# part1('input.txt')
# part2('sampleinput.txt')
part2('input.txt')