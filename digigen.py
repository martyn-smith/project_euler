# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 12:11:44 2014

@author: c1346299
"""

"""
returns leading and trailing digits of an integer (whilst keeping it an integer)
"""

def leading_digit(i):
	while (i > 10):
		i /= 10
		#print i
	if (i % 10 == 0):
		return 1
	else:
		return (i % 10)
	
