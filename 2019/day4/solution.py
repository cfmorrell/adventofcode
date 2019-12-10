#!/usr/bin/python

# import sys


def func():
    start = 372304
    end = 847060
    good = 0
    for guess in range(start,end+1):
        guess = str(guess)
        test1 = False
        test2 = False
        if guess[0] == guess[1] or guess[1] == guess[2] or guess[2] == guess[3] or guess[3] == guess[4] or guess[4] == guess[5]:
            test1 = True
        if int(guess[0]) <= int(guess[1]) <= int(guess[2]) <= int(guess[3]) <= int(guess[4]) <= int(guess[5]):
            test2 = True
        if test1 and test2:
            good += 1
            print(guess)
    print(good)

if __name__ == "__main__":
    # filename = str(sys.argv[1])
    print(func())
