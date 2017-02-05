# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 15:07:26 2014

@author: c1346299
"""
import digigen

def Euler_17():
	#verified
	result = 0
	for i in range(1,1001):
		number = make_number_into_words(i)
		number = number.replace(" ", "")
		result += len(number)
	return result

def make_number_into_words(i, string = ""):
	#valid between 1 and 1000
	numbers = [" ",
		"one",
		"two",
		"three",
		"four",
		"five",
		"six",
		"seven",
		"eight",
		"nine",
		"ten",
		"eleven",
		"twelve",
		"thirteen",
		"fourteen",
		"fifteen",
		"sixteen",
		"seventeen",
		"eighteen",
		"nineteen",
		"twenty",
		"thirty",
		"forty",
		"fifty",
		"sixty",
		"seventy",
		"eighty",
		"ninety",
		"hundred",
		"thousand",
		"and"]
	if i in range(1,20):
		string += numbers[i]
	elif i in range(20,100):
		string += numbers[digigen.leading_digit(i) + 18] + numbers[0]
		string += make_number_into_words(i % 10)
	elif i in range(100,1000):
		string += numbers[digigen.leading_digit(i)] + numbers[0] + numbers[28]
		if not (i % 100 == 0):
			string += numbers[0] + numbers[30] + numbers[0]
			string += make_number_into_words(i % 100)
	elif i == 1000:
		string += numbers[digigen.leading_digit(i)] + numbers[0] + numbers[29]
	return string
	
print Euler_17()