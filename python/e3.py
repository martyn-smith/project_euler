"""
Finds the largest prime factor of the number 600851475143.
"""
import numpy as np
from primegen import primes_by_sieve

def Euler_3(n = 600851475143):
    #generate all the candidate primes
    max_num = int(np.sqrt(n))
    primes = primes_by_sieve(max_num)
    return find_biggest_factor_functional(primes, n)

def find_biggest_factor_reversed(primes, n):
    while True:
        for prime in primes[::-1]:
            if n % prime == 0:
                return prime

def find_biggest_factor_functional(primes, n):
    return max(p for p in primes if n % p == 0)

def test_3():
    assert Euler_3() == 6857

if __name__ == "__main__":
    print(Euler_3())
