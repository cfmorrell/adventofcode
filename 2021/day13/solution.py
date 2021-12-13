def part1(filename):
    with open(filename) as f:
        tempdots = {}
        folds = []
        for line in f:
            if ',' in line:
                col,row = [int(i) for i in line.strip().split(',')]
                if row in tempdots:
                    tempdots[row].add(col)
                else:
                    tempdots[row] = set([col])
            elif len(line) > 1:
                folds.append((line.split()[2][0],int(line.split('=')[1])))
        dots = [tempdots.get(i,set()) for i in range(max(tempdots.keys())+1)]
        # print(dots)        
        for fold in folds:
            start = fold[1]*2
            if fold[0] == 'y':
                for i in range(start,fold[1],-1):
                    dots[start-i] = dots[start-i].union(dots[i])
                    dots[i] = set()
            else:
                for row in dots:
                    # print(row)
                    thisrow = row.copy()
                    for v in thisrow:
                        if v > fold[1]:
                            row.add((fold[1]*2)-v)
                            row.discard(v)
                    # print(row)
            # print("After fold: {}\n{}".format(fold,dots))
            # break
        sumdots = 0
        for row in dots:
            sumdots += len(row)
        print(sumdots)

def part2(filename):
    with open(filename) as f:
        tempdots = {}
        folds = []
        for line in f:
            if ',' in line:
                col,row = [int(i) for i in line.strip().split(',')]
                if row in tempdots:
                    tempdots[row].add(col)
                else:
                    tempdots[row] = set([col])
            elif len(line) > 1:
                folds.append((line.split()[2][0],int(line.split('=')[1])))
        dots = [tempdots.get(i,set()) for i in range(max(tempdots.keys())+1)]
        for fold in folds:
            start = fold[1]*2
            if fold[0] == 'y':
                for i in range(start,fold[1],-1):
                    try:
                        dots[start-i] = dots[start-i].union(dots[i])
                        dots[i] = set()
                    except:
                        continue
            else:
                for row in dots:
                    thisrow = row.copy()
                    for v in thisrow:
                        if v > fold[1]:
                            row.add((fold[1]*2)-v)
                            row.discard(v)
        for row in dots:
            if len(row) > 0:
                for i in range(max(row)+1):
                    if i in row:
                        print('#',end='')
                    else:
                        print(' ',end='')
                print('')


# part1('sampleinput.txt')
# part1('input.txt')
# part2('sampleinput.txt')
part2('input.txt')