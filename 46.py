# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:43:22 2015

@author: martyn
"""
from primegen import PrimesByTrial
import numpy as np

def Euler_46():
	i = 2
	primes = PrimesByTrial()
	while True:
		print i
		goldbach = False
		if ((primes.is_prime(i)) or (i % 2 == 0)):
			goldbach = True			
		for j in range(1, (int(np.sqrt((i - 2) / 2))+1)):
			if goldbach == True:
				break
			else:
				for k in primes.primes:
					if (i == 2*(j**2) + k):
						goldbach = True
						break
		if goldbach == True:
			i += 1
		else:
			return i

		
		
print Euler_46()
			