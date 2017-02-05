# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 13:53:49 2014

@author: c1346299
"""

def Euler_9():
	#verified
	#and weirdly easy
	for a in range(1, 1000):
		for b in range(1, 1000-a):
			c = (1000 - (a + b))
			if ((a**2) == (b**2) + (c**2)):
				return (a*b*c)
			
print Euler_9()