# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 14:40:26 2014

@author: c1346299
"""
import primegen

def Euler_10():
	#verified
	primes = primegen.all_primes(2e+6)
	return sum(primes)

print(Euler_10())
