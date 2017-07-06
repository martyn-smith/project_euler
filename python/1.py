"""
Find the sum of all the multiples of 3 or 5 below 1000. (fizzbuzz++)
"""

def Euler_1():
	#verified.
	max_num = 1000
	result = sum([i for i in range(0, max_num) if ((i % 3) == 0) or ((i % 5) == 0)])
	return result

if __name__ == "__main__":
	print(Euler_1())
