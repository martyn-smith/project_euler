"""
the sum of all primes up to two million.
"""
from primegen import primes_by_sieve

def Euler_10(n = 2e+6):
    #verified(2e+6)
    return sum(primes_by_sieve(n))

def test_Euler_10():
    assert Euler_10() == 142913828922

if __name__ == "__main__":
    print(Euler_10())
