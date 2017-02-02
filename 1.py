# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 10:57:08 2014

@author: c1346299
"""

def Euler_1():
	#verified, no point optimising
	max_num = 1000
	sum = 0
	for i in range(0, max_num):
		if ((i % 3) == 0) or ((i % 5) == 0):
			sum += i
	return sum

print(Euler_1())
