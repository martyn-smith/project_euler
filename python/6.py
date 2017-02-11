# -*- coding: utf-8 -*-
"""
Finds the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""

def Euler_6_easy_way():
	#this works...except it's the wrong way round?
	sum_of_squares = sum([(i**2) for i in range (1,101)])
	square_of_sum = (sum([i for i in range (1,101)]))**2
	return (sum_of_squares - square_of_sum)

def Euler_6_better_way():
	#uses S_n = n(a_1 + a_n)/2
	sum_of_squares = ((1e+6)/3) + ((1e+4)/2) + (100/6)
	square_of_sum = (100*101/2)**2
	return (sum_of_squares - square_of_sum)

print("easy way: {}\n".format(Euler_6_easy_way()))
print("better way: {}".format(Euler_6_better_way()))
