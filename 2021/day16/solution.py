def parsepacket(packet: str) -> str:
    global versionsum, operators, operands
    print('parse packet: {}'.format(packet))
    if '1' not in packet:
        return
    version = int(packet[:3],2)
    versionsum += version
    type = int(packet[3:6],2)
    packet = packet[6:]
    if type == 0:
        operators.append('sum')
    elif type == 1:
        operators.append('product')
    elif type == 2:
        operators.append('minimum')
    elif type == 3:
        operators.append('maximum')
    elif type == 5:
        operators.append('gt')
    elif type == 6:
        operators.append('lt')
    elif type == 7:
        operators.append('eq')
    print(operators)
    if type == 4:
        print('Literal packet: Version {}, Type {}, Data {}'.format(version, type, packet))
        realvalue = ''
        while 1:
            thischunk = packet[:5]
            packet = packet[5:]
            realvalue += thischunk[1:]
            if thischunk[0] == '0':
                break
        print("Packet Value: {}, {}".format(int(realvalue,2),realvalue))
        operands.append(int(realvalue,2))
        print(operands)
        parsepacket(packet)
    else:
        print('Operator packet: Version {}, Type {}, Data {}'.format(version, type, packet))
        lengthtype = int(packet[0],2)
        print('Length Type: {}'.format(lengthtype))
        packet = packet[1:]
        if lengthtype == 0:
            subpacketlength = int(packet[:15],2)
            print('15 bit length: {} from {}'.format(subpacketlength,packet[:15]))
            parsepacket(packet[15:])
        else:
            print("Numsubpackets in binary: {}".format(packet[:11]))
            numsubpackets = int(packet[:11],2)
            print("{} Subpackets".format(numsubpackets))
            parsepacket(packet[11:])

def part1(filename):
    global versionsum, operators, operands
    versionsum = 0
    with open(filename) as f:
        h = f.readline().strip()
        print(h)
        b = bin(int('1'+h, 16))[3:]
        print("Starting packet: {}".format(b))
        print(parsepacket(b))
    print(versionsum)

def part2(filename):
    global operators, versionsum, operands
    operators = []
    operands = []
    versionsum = 0
    with open(filename) as f:
        h = f.readline().strip()
        print(h)
        b = bin(int('1'+h, 16))[3:]
        print("Starting packet: {}".format(b))
        print(parsepacket(b))
        print(operators,operands)


# part1('sampleinput.txt')
# part1('input.txt')
part2('sampleinput.txt')
# part2('input.txt')