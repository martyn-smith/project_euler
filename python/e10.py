"""
the sum of all primes up to two million.
"""
from primegen import primes_by_sieve

def Euler_10():
    #verified(2e+6)
    max_num = 2e+6
    return sum(primes_by_sieve(max_num))

if __name__ == "__main__":
    print(Euler_10())
