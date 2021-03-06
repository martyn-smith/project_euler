"""
Find the sum of all the multiples of 3 or 5 below 1000. (fizzbuzz++)
"""

def Euler_1(n = 1000, divisors=(3,5)):
    #verified.
    return sum(i for i in range(0, n)
                if any(i % d == 0 for d in divisors))

def test_1():
    assert Euler_1() == 233168

if __name__ == "__main__":
    print(Euler_1())


