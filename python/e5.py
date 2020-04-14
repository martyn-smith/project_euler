"""
Finds the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20.
"""
"""
 primes between 0 and 20: 2,3,5,7,11,13,17,19
 - if a number is divisible by these, it is divisible by
   all numbers between 0 and 20
"""

def Euler_5(n = 20):
    #answer by hand - the product of maximum powers of each prime
    #answer = (2**4)*(3**2)*5*7*11*13*17*19
    primes, powers = [2], [0]
    for num in range(2, n+1):
        for i, p in enumerate(primes):
            power = 0
            while num % p == 0:
                power += 1
                num //= p
            powers[i] = max(power, powers[i])
        if num > 1: #is prime
            primes.append(num)
            powers.append(1)
    answer = 1
    for base, power in zip(primes, powers):
        answer *= base**power
    return answer

def test_5():
    assert Euler_5() == 232792560

if __name__ == "__main__":
    print(Euler_5())