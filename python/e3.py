"""
Finds the largest prime factor of the number 600851475143.
"""
import numpy as np
from primegen import primes_by_sieve

def Euler_3():
    big_num = 600851475143
    #generate all the candidate primes
    max_num = int(np.sqrt(big_num))
    primes = primes_by_sieve(max_num)
    return find_biggest_factor_functional(primes, big_num)

def find_biggest_factor_reversed(primes, big_num):
    while True:
        for prime in primes[::-1]:
            if big_num % prime ==0:
                return prime

def find_biggest_factor_functional(primes, big_num):
    return max(p for p in primes if big_num % p == 0)

if __name__ == "__main__":
    print(Euler_3())
