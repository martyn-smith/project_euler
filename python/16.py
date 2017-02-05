# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 15:00:28 2014

@author: c1346299
"""

def Euler_16():
	#gotta love python for making very long ints super easy
	big_num = (2 ** 1000)
	result = 0
	#check old code, think a sum_of_digits() has been handled before...
	while (big_num >= 1):
		result += big_num % 10
		big_num /= 10
	return result

print(Euler_16())
