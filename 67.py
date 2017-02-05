# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 21:18:48 2014

@author: martyn
"""

from pathsum import smartsum

def Euler_67():
	#data = np.genfromtxt("../18.dat", filling_values=0)
	data = [[int(i) for i in line.split()] for line in open("../67.dat")]
	#path = brute_force(data)
	result = smartsum(data)
	return result

print(Euler_67())
