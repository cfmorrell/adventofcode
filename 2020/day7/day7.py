def buildDB(filename):
    db = dict()
    for l in open(filename).read().split("\n"):
        if l != '':
            l = l.replace(',','').split()
            # print(l)
            key = "{} {}".format(l[0],l[1])
            # print(key)
            t = list()
            l = l[4:]
            # print(l)
            if (l != ['no','other','bags.']):
                for i in range(len(l)):
                    if(i % 4 == 0):
                        t.append((int(l[i]),"{} {}".format(l[i+1],l[i+2])))
                if (key not in db):
                    db[key] = t
    return db

db = buildDB('input.txt')
# print(db)

def part1():
    search = ['shiny gold']
    outer,start = set(),0
    while True:
        for i in db.keys(): #
            for j in db[i]:
                if (j[1] in outer or j[1] in search):
                    outer.add(i)
        if (len(outer) > start):
            start = len(outer)
        else:
            break
    print(len(outer))

part1()

def part2():
    def getContent(bag):
        c = 1
        if (bag in db):
            for i in db[bag]:
                c += i[0]*getContent(i[1])
        return c
    print(getContent('shiny gold')-1)

part2()

# def part1(filename):
#     with open(filename) as f:
#         for line in f:
#             outsidebag = line.split(' bags')[0]
#             insidebags = line.split('contain')[1] #.strip().strip('.').strip('s')
#             insidebags = [i.split(' bag')[0].strip() for i in insidebags.split(', ') if 'no other' not in i]
#             print(outsidebag,insidebags)


# part1('smallinput.txt')