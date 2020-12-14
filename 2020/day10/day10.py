# def part1(filename):
#     with open(filename) as f:
#         data = sorted([int(i) for i in f.read().split()])
#     data.insert(0,0)
#     data.append(max(data)+3)
#     onediff = 0
#     threediff = 0
#     for i in range(len(data)-1):
#         if data[i+1] - data[i] == 1:
#             onediff += 1
#         elif data[i+1] - data[i] == 3:
#             threediff += 1
#     print(onediff,threediff,onediff*threediff)

# part1('input.txt')




f = open('input.txt')
numbers = sorted([int(l.split()[0]) for l in f.readlines()])

def findDif(last_number):
    dif = []
    for n in numbers:
        dif.append(n-last_number)
        last_number = n
    dif.append(3)
    return dif

def findArrs(dif):
    temp_list = []
    mult_list = []
    for n in dif:
        if n != 3:
            temp_list.append(n)
        
        elif n == 3:
            if len(temp_list) > 3:
                mult_list.append((len(temp_list)-1)*2+(len(temp_list)-3))
            elif len(temp_list) > 1:
                mult_list.append((len(temp_list)-1)*2)
            temp_list = []
            
    r2 = 1
    for x in mult_list:
            r2 = r2 * x 
    return r2

dif = findDif(0)
r1 = dif.count(1)*(dif.count(3))
print("Result part 1: ", r1)

print("Result part 2: ", findArrs(dif))