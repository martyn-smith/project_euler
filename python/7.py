"""
Finds the 10 001st prime number.  Actually just by using primegen
"""
import primegen

def Euler_7():
    #verified (104743)
    # It looks as though it's going to be worth it to write a
    # generate_primes() module
    return primegen.nth_prime_by_trial(10001)

if __name__ == "__main__":
    print(Euler_7())
