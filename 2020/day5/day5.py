def findrows(start,end,letters):
    # print(start,end,letters)
    if len(letters) == 0:
        return start
    else:
        if letters[0] in 'LF':
            return findrows(start,end-((end-start)//2)-1,letters[1:])
        elif letters[0] in 'RB':
            return findrows(((end-start)//2)+start+1,end,letters[1:])

def part1(filename):
    with open(filename) as f:
        seats = []
        for line in f:
            row = findrows(0,127,line[:7])
            col = findrows(0,7,line[7:10])
            seat = (row*8) + col
            seats.append(seat)
    print('Max Seat:',max(seats))
    for seat in range(min(seats),max(seats)+1):
        if seat + 1 in seats and seat - 1 in seats and seat not in seats:
            print("My Seat:",seat)
        


part1('input.txt')