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
    return find_biggest_factor(primes, big_num)

def find_biggest_factor(primes, big_num):
    biggest_factor = 0
    for j in primes:
        if (big_num % j == 0):
            other_factor = big_num / j
            is_prime = True
            for k in primes:
                if (other_factor % k == 0):
                    #not prime
                    is_prime = False
                    break
            if (is_prime):
                j = max(other_factor, j)
            biggest_factor = max(j, biggest_factor)
    return biggest_factor

if __name__ == "__main__":
    print(Euler_3())
