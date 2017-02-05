# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 12:55:11 2014

@author: c1346299
"""
FILENAME = "../8.dat"

def Euler_8():
	#verified.  That was easy...
	with open(FILENAME) as f:
		big_num = f.read()
	big_product = 1
	for i in range(1, (len(big_num)-13)):
		product = 1
		num = big_num[i:(i+13)]
		for j in num:
			product *= int(j)
		big_product = max(product, big_product)
	return big_product

print(Euler_8())
