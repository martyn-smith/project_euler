# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 10:57:53 2014

@author: c1346299
"""

def Euler_2():
	#verified, integrated fibonacci() into this
	#remember f carries the value of f_prev[-1] in the while loop!
	max_num = 4e+6
	f = 0
	sum = 0
	f_prev = []
	while (f < max_num):
		if (len(f_prev) >= 2):
			f += (f_prev[-2])
		elif (len(f_prev) == 1):
			f = 1
		else:
			f = 0
		print("f = {}".format(f))
		if (f % 2) == 0:
			#print "found even f"
			sum += f
		f_prev.extend([f])
	return sum

print(Euler_2())
