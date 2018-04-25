"""
Finds the largest prime factor of the number 600851475143.
"""
import numpy as np
import primes

def Euler_3():
    big_num = 600851475143
    #generate all the candidate primes
    max_num = int(np.sqrt(big_num))
    primes = primes.all_primes(max_num)
    return find_biggest_factor(primes, big_num)

"""
def E3_trial_by_division():
    #works, but deprecated
    big_num = 600851475143
    max_num = int(np.sqrt(big_num))
    primes = [2]
    for i in range(2, max_num):
        prime = True
        smaller_max_num = int(np.sqrt(i))
        for j in primes:
            if (j > smaller_max_num):
                break
            print "testing {} % {}".format(i, j)
            if (i % j == 0):
                #not a prime
                prime = False
                break
        if (prime):
            primes.extend([i])
    return find_biggest_factor(primes, big_num)
"""

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
