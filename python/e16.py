"""
prints the sum of digits of 2**1000
"""

def Euler_16(n = 2**1000):
    #gotta love python for making very long ints super easy
    result = 0
    #check old code, think a sum_of_digits() has been handled before...
    while (n >= 1):
        result += n % 10
        n //= 10
    return result

def test_16():
    assert Euler_16() == 1366

if __name__ == "__main__":
    print(Euler_16())
