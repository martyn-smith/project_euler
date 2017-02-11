# -*- coding: utf-8 -*-
"""
Find the sum of all the multiples of 3 or 5 below 1000. (fizzbuzz++)
"""

def Euler_1():
	#verified.
	max_num = 1000
	sum = 0
	for i in range(0, max_num):
		if ((i % 3) == 0) or ((i % 5) == 0):
			sum += i
	return sum

print(Euler_1())
