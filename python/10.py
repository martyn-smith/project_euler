"""
the sum of all primes up to two million.
"""
import primes

def Euler_10():
    #verified
    primes = primes.all_primes(2e+6)
    return sum(primes)

if __name__ == "__main__":
    print(Euler_10())
