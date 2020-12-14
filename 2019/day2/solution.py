import sys

def func(filename):
	"""
	>>> func("test1.txt")
	[2, 0, 0, 0, 99]
	>>> func("test2.txt")
	[2, 3, 0, 6, 99]
	>>> func("test3.txt")
	[2, 4, 4, 5, 99, 9801]
	>>> func("test4.txt")
	[30, 1, 1, 4, 2, 5, 6, 0, 99]
	"""
	for noun in range(100):
		for verb in range(100):
			f = open(filename,'r')
			codes = [int(i) for i in f.read().strip().split(",")]
			f.close()
			codes[1] = noun
			codes[2] = verb
			print(codes[0:5],end=", ")
			curpos = 0
			curcode = codes[curpos]
			while 1:
				pos1 = codes[curpos + 1]
				pos2 = codes[curpos + 2]
				destpos = codes[curpos + 3]
				if curcode == 1:
					newval = codes[pos1] + codes[pos2]
				elif curcode == 2:
					newval = codes[pos1] * codes[pos2]
				codes[destpos] = newval
				curpos += 4
				if curpos > len(codes) or codes[curpos] == 99:
					break
				curcode = codes[curpos] 
			print(codes[0:5])
			if codes[0] == 19690720 and codes[curpos] == 99:
				return((noun,verb))
				

if __name__ == "__main__":
	filename = str(sys.argv[1])
	n,v = func(filename)
	print(n,v,(100 * n + v))
