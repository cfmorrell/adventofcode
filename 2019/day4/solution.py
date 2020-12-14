#!/usr/bin/python

# import sys


def func():
    start = 372304
    end = 847060
#    start = 111122
#    end = 111122
    good = 0
    for guess in range(start,end+1):

        guess = [int(i) for i in str(guess)]
        test1 = False
        test2 = False
        test3 = False
        if guess[0] == guess[1] or guess[1] == guess[2] or guess[2] == guess[3] or guess[3] == guess[4] or guess[4] == guess[5]:
            test1 = True
            # print('Test 1 Good')
        if guess[0] <= guess[1] <= guess[2] <= guess[3] <= guess[4] <= guess[5]:
            test2 = True
            # print('Test 2 Good')
        if guess.count(guess[0]) == 2 or guess.count(guess[1]) == 2 or guess.count(guess[2]) == 2 or guess.count(guess[3]) == 2 or guess.count(guess[4]) == 2 or guess.count(guess[5]) == 2:
            test3 = True
            # print('Test 3 Good')
        if test1 and test2 and test3:
            good += 1
            # print(guess)
    print(good)

if __name__ == "__main__":
    # filename = str(sys.argv[1])
    print(func())
