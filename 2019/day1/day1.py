def day1(filename):
	f = open(filename,'r')
	total = 0
	for mass in f:
		fuel = int(int(mass)/3) - 2
		total += fuel
		while 1:
			fuel = int(fuel/3) - 2
			if fuel > 0:
				total += fuel
			else:
				break
	return total
