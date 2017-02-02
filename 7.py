# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 17:46:39 2014

@author: c1346299
"""
import primegen

def Euler_7():
	#verified (104743)
	# It looks as though it's going to be worth it to write a 
	# generate_primes() module
	return primegen.nth_prime_by_trial(10001)
	
print Euler_7()