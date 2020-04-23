"""
Find the sum of the digits in the number 100!
"""
import math

def Euler_20(n = 100):
    #verified.  Once again, python makes this very easy.
    big_num = str(math.factorial(n))
    result = sum(int(chr) for chr in big_num)
    return result

def test_20():
    assert Euler_20() == 648

if __name__ == "__main__":
    print(Euler_20())