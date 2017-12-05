#!/usr/bin/python

import sys
import math

num = int(sys.argv[1])

i = 1
while 1:
	if i**2 >= num:
		break
	i += 2

#i is the width and height of the square
distance_to_center = (i-1)/2
if num >= (i**2)-i + 1:
	print abs(num-(i**2-distance_to_center))+distance_to_center
elif num > (i-1)**2:
	print abs(num - ((i-1)**2+1) - distance_to_center) + distance_to_center
elif num > ((i-2)**2) + i - 1:
	print abs(num - ((i-2)**2 + i - 1 + distance_to_center)) + distance_to_center
else:
	print abs(num - ((i-2)**2 + i - 1 - distance_to_center)) + distance_to_center