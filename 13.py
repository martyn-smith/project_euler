# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 15:14:50 2014

@author: c1346299
"""

import numpy as np

def Euler_13():
	#problematic, needs float datatype
	data = np.loadtxt("../13.dat")
	big_num = sum(data)
	#big_num /= (10 ** (np.log10(big_num) - 9))
	return big_num
	
print Euler_13()