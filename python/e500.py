"""
Finds the smallest number with 2**500500 divisors,
modulo 500500507
"""
from numpy import product
from primegen import prime_by_trial

def Euler_500(num_divisors = 2**500500, mod_divisor = 500500507):
    divisors_prime_tree = get_prime_factors(num_divisors)
    return (product(i for i in divisors_prime_tree) % mod_divisor)

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
    print(Euler_500())