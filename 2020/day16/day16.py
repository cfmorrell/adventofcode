def part1(filename):
    with open(filename) as f:
        invalidvalues = []
        validranges = []
        for line in f:
            if 'or' in line:
                line = line.strip().split(': ')[1].split(' or ')
                for pair in line:
                    pair = [int(i) for i in pair.split('-')]
                    validranges.append(pair)
            elif line[0].isdigit():
                values = [int(i) for i in line.strip().split(',')]
                for value in values:
                    valid = False
                    for pair in validranges:
                        if min(pair) <= value <= max(pair):
                            valid = True
                            break
                    if not valid:
                        invalidvalues.append(value)
    print(invalidvalues,sum(invalidvalues))

def part2(filename):
    with open(filename) as f:
        invalidvalues = []
        validranges = []
        validtickets = []
        fields = {}
        for line in f:
            if 'or' in line:
                line = line.strip().split(': ')
                fieldtitle = line[0]
                fields[fieldtitle] = []
                line = line[1].split(' or ')
                for pair in line:
                    pair = [int(i) for i in pair.split('-')]
                    validranges.append(pair)
                    fields[fieldtitle].append(pair)
                print(fields)
            elif line[0].isdigit():
                ticketvalues = [int(i) for i in line.strip().split(',')]
                ticketisvalid = []
                for value in ticketvalues:
                    for pair in validranges:
                        if min(pair) <= value <= max(pair):
                            print("Ticket {} is valid because of value {} in pair {}".format(ticketvalues,value,pair))
                            ticketisvalid.append(True)
                        else:
                            ticketisvalid.append(False)
                print(ticketisvalid)
                if False not in ticketisvalid:
                    validtickets.append(ticketvalues)
    print(validtickets)

# part1('smallinput.txt')
# part1('input.txt')
part2('smallinput.txt')