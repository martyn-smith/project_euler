# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 17:51:49 2014

@author: c1346299
"""
	
	
class PrimesByTrial:
	primes = []
	
	def is_prime(self, x):
		is_prime = True
		for prime in self.primes:
			if (x % prime == 0):
				is_prime = False
				break
		if (is_prime):
			self.primes.append(x)
		return is_prime
		

def nth_prime_by_trial(n):
	#by trial
	primes = [2]
	x = 3
	while len(primes) < n:
		#print "trying {}".format(x)
		is_prime = True
		for prime in primes:
			if (x % prime == 0):
				is_prime = False
				break
		if (is_prime):
			#print "PRIME: {}".format(x)
			primes.append([x])
			#print len(primes)
		x += 2
	return primes[-1]
	
def all_primes(max_num):
	#uses a sieve to find all primes below big_num, returns all primes
	#why it runs so slowly I'm not sure...
	nums = [True] * int(max_num)
	primes = []
	#primes[2:3] = [False, False]
	for i in range(2, len(nums)):
		if (nums[i] == True):
			primes.append(i)
			j = 2 
			while (j * i) < len(nums):
				nums[j * i] = False
				j += 1
	return primes