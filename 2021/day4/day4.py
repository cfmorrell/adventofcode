import numpy as np
def part1(filename):
    with open(filename) as f:
        numbers = [int(i) for i in f.readline().split(',')]
        boards = []
        flatboards = []
        tempboards = f.read().strip().split('\n\n')
        for boardnum,board in enumerate(tempboards):
            thisboard = []
            flatboards.append([int(i) for i in board.split()])
            for line in board.split('\n'):
                thisboard.append([int(i) for i in line.split()])
            boards.append([])
            thisboard = np.array(thisboard)
            for i in range(len(thisboard[:,0])):
                boards[boardnum].append(set(thisboard[:,i]))
                boards[boardnum].append(set(thisboard[i,:]))
        iswinner = False
        for i in range(5,len(numbers)):
            if iswinner:
                break
            thesenums = set(numbers[:i])
            for whichboard,board in enumerate(boards):
                if iswinner:
                    break
                for winner in board:
                    if winner.issubset(thesenums):
                        winnerboard = set(flatboards[whichboard])
                        iswinner = True
                        score = sum(list(winnerboard.difference(thesenums)))
                        print(numbers[i-1]*score)
                        break



def part2(filename):
    with open(filename) as f:
        numbers = [int(i) for i in f.readline().split(',')]
        boards = []
        flatboards = []
        tempboards = f.read().strip().split('\n\n')
        for boardnum,board in enumerate(tempboards):
            thisboard = []
            flatboards.append([int(i) for i in board.split()])
            for line in board.split('\n'):
                thisboard.append([int(i) for i in line.split()])
            boards.append([])
            thisboard = np.array(thisboard)
            for i in range(len(thisboard[:,0])):
                boards[boardnum].append(set(thisboard[:,i]))
                boards[boardnum].append(set(thisboard[i,:]))
        winnerslist = set()
        finished = False
        for i in range(5,len(numbers)):
            if finished:
                break
            thesenums = set(numbers[:i])
            for whichboard,board in enumerate(boards):
                if finished:
                    break
                for winner in board:
                    if winner.issubset(thesenums):
                        if len(winnerslist) == len(boards):
                            print('final winner')
                            finished = True
                        else:
                            winnerboard = set(flatboards[whichboard])
                            score = sum(list(winnerboard.difference(thesenums))) * numbers[i-1]
                            winnerslist.add(whichboard)
                            print('winner:',len(winnerslist),score)
                            break


# part1('sampleinput.txt')
# part1('input.txt')
# part2('sampleinput.txt')
part2('input.txt')