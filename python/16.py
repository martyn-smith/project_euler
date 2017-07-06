"""
prints the sum of digits of 2**1000
"""

def Euler_16():
	#gotta love python for making very long ints super easy
	big_num = (2 ** 1000)
	result = 0
	#check old code, think a sum_of_digits() has been handled before...
	while (big_num >= 1):
		result += big_num % 10
		big_num /= 10
	return result

if __name__ == "__main__":
	print(Euler_16())
