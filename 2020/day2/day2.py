def part1(filename):
    badPasswords = 0
    goodPasswords = 0
    with open(filename) as f:
        for line in f:
            occurences, letter, password = line.strip().split()
            minOccurrences = int(occurences.split('-')[0])
            maxOccurrences = int(occurences.split('-')[1])
            letter = letter[0]
            if password.count(letter) < minOccurrences or password.count(letter) > maxOccurrences:
                print('Bad password: ',password)
                badPasswords += 1
            else:
                goodPasswords += 1
    print('Good Passwords: ',goodPasswords)
    print('Bad Passwords: ',badPasswords)

def part2(filename):
    badPasswords = 0
    goodPasswords = 0
    with open(filename) as f:
        for line in f:
            positions, letter, password = line.strip().split()
            pos1 = int(positions.split('-')[0])
            pos2 = int(positions.split('-')[1])
            letter = letter[0]
            if password[pos1-1] == letter and password[pos2-1] == letter:
                print('Bad password: ',password)
                badPasswords += 1
            elif password[pos1-1] == letter or password[pos2-1] == letter:
                print('Good password: ',password)
                goodPasswords += 1
            else:
                print('Bad password: ',password)
                badPasswords += 1

    print('Good Passwords: ',goodPasswords)
    print('Bad Passwords: ',badPasswords)


# part1('input.txt')
part2('input.txt')
