"""
Find the sum of the digits in the number 100!
"""
import math

def Euler_20(start_num = 100):
    #verified.  Once again, python makes this very easy.
    big_num = str(math.factorial(start_num))
    result = sum(int(chr) for chr in big_num)
    return result

if __name__ == "__main__":
    print(Euler_20())