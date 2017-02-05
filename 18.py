# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 22:21:38 2014

@author: martyn
"""
import numpy as np
from pathsum import smartsum

def Euler_18():
	#data = np.genfromtxt("../18.dat", filling_values=0)
	data = [[int(i) for i in line.split()] for line in open("../18.dat")]
	#path = brute_force(data)
	result = smartsum(data)
	return result
	
print Euler_18()
	
