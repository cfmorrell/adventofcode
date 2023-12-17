from collections import Counter
cardstrength = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

class Card(object):

    def __init__(self,line):
        self.bet = int(line.strip().split()[1])
        self.hand = line.strip().split()[0]
        print('Checking:',self.hand)
        counter = Counter(self.hand)
        if len(counter) == 1:
            print("Five of a kind")
            self.type='5K'
            self.strength=7
        elif max(counter.values()) == 4:
            print("Four of a kind")
            self.type='4K'
            self.strength=6
        elif max(counter.values()) == 3 and min(counter.values()) == 2:
            print("Full House")
            self.type="FH"        
            self.strength=5
        elif max(counter.values()) == 3:
            print("Three of a kind")
            self.type="3K"
            self.strength=4
        elif sorted(counter.values())[1] == 2 and sorted(counter.values())[2] == 2:
            print("Two Pair")
            self.type="2P"
            self.strength=3
        elif max(counter.values()) == 2:
            print("One Pair")
            self.type="PR"
            self.strength=2
        else:
            print("High Card")
            self.type="HC"
            self.strength=1
        
    def __repr__(self):
        return("{}, {}, {}".format(self.hand,self.type, self.bet))

    def __str__(self):
        return("{}, {}, {}".format(self.hand,self.type, self.bet))
    
    def __gt__(self,other):
        if self.strength > other.strength:
            return True
        elif self.strength < other.strength:
            return False
        else:
            for index in range(len(self.hand)):
                if cardstrength[self.hand[index]] > cardstrength[other.hand[index]]:
                    return True
                elif cardstrength[self.hand[index]] < cardstrength[other.hand[index]]:
                    return False
        return False

    def __lt__(self,other):
        if self.strength < other.strength:
            return True
        elif self.strength > other.strength:
            return False
        else:
            for index in range(len(self.hand)):
                if cardstrength[self.hand[index]] < cardstrength[other.hand[index]]:
                    return True
                elif cardstrength[self.hand[index]] > cardstrength[other.hand[index]]:
                    return False
        return False

    def __eq__(self,other):
        if self.strength != other.strength:
            return False
        if self.hand[::] == other.hand[::]:
            return True
        else:
            return False

def part1():
    with open(filename) as f:
        cards = []
        for line in f:
            cards.append(Card(line))
    cards = sorted(cards)
    print(cards)
    winnings = 0
    for index,card in enumerate(cards):
        winnings += (index+1)*card.bet
    print(winnings)
        


def part2():
    with open(filename) as f:
        pass







import sys,time,string
try:
    if sys.argv[1] not in ['T','F']:
        raise
    filename = 'sampleinput.txt' if sys.argv[1] == 'T' else 'input.txt'
    part = int(sys.argv[2])
except:
    print('Usage: solution.py [T|F] [1|2] (Testing & Part)')
    exit()


start = time.perf_counter()
if part == 1:
    part1()
else:
    part2()
end = time.perf_counter()
ms = (end-start)# * 10**6
print(f"Elapsed {ms:.03f} seconds.")
print(f"Elapsed {ms*10**3:.03f} milliseconds.")
print(f"Elapsed {ms*10**6:.03f} microsecondss.")