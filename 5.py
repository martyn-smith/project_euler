# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 11:01:20 2014

@author: c1346299
"""
import itertools 
"""
 primes between 0 and 20: 2,3,5,7,11,13,17,19
 - if a number is divisible by these, it is divisible by
   all numbers between 0 and 20
"""

def Euler_5():
	#worked out by HAND.  bit crap really.
	answer = (2**4)*(3**2)*5*7*11*13*17*19
	primes = [2,3,5,7,11,13,17,19]
	powers = [0,0,0,0,0,0,0,0]
	for i in range (2,20):
		for prime in primes:
			if (i % prime == 0):
				x = i/prime
		
		
	
print Euler_5()
