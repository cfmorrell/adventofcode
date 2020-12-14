
input_file_object = open("aoc16_input_9a.txt")
input_as_string = input_file_object.read()
input_file_object.close()
 
decompressed=[]
 
def findRightParen(current, left_index):
    for r in range(left_index+4, len(current)):
        if current[r] == ')':
            return r
 
#(AxB) take next A char and repeat B times
 
#input_as_string = input_as_string.replace(" ","")
#input_as_string = input_as_string.replace("\\n","")
 
example0 = 'ADVENT'
example1 = "A(1x5)BC"
example2 = '(3x3)XYZ'
 
exampleb = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
'''
x = 0
current = input_as_string
 
while x < len(current):
   if current[x] == '(':
       y = findRightParen(current,x)
       marker = current[x+1:y]
       marker_split = marker.split('x')
       #print(marker)
       characters = int(marker_split[0])
       repetitions = int(marker_split[1])
       temp = current[y+1:(y+1+characters)] * repetitions
       decompressed.append(temp)
       x+=(len(marker) + characters + 2)
   else:
       decompressed.append(current[x])
       x+=1
 
'''
 
def recursiveExpansion(some_string):
    if '(' not in some_string:
        return len(some_string)
   
    for x in range(len(some_string)):
        if some_string[x] !='(':
            pass
        else:
            y = findRightParen(some_string, x)
            marker = some_string[x+1:y]
            marker_split = marker.split('x')
            #print(x,y,marker,marker_split)
            #print(some_string)
            characters = int(marker_split[0])
            repetitions = int(marker_split[1])
            #print(some_string[:x])
            #print()
            #print(some_string[y+1:y+characters+1])
            #print()
            #print(some_string[y+characters+1:])
           
            return (recursiveExpansion(some_string[:x]) +
                    (recursiveExpansion(some_string[y+1:y+characters+1]) * repetitions) +
                    recursiveExpansion(some_string[(y+characters+1):]))
