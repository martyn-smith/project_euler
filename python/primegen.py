"""
various functions to generate primes
"""
def prime_by_trial():
    #by trial
    primes = [2]
    if len(primes) == 1:
            yield primes[-1]
    while True:
        x = primes[-1] + 1
        is_prime = False
        while not is_prime:
            is_prime = True
            for prime in primes:
                if (x % prime == 0):
                    is_prime = False
                    break
            if (is_prime):
                #print("Prime: {}\t length: {}\n".format(x, len(primes) + 1))
                primes.append(x)
            else:
                x += 1
        yield primes[-1]

def primes_by_sieve(max_num):
    #uses a sieve to find all primes below big_num, returns all primes
    #why it runs so slowly I'm not sure...
    nums = [True] * int(max_num)
    primes = []
    for i in range(2, len(nums)):
        if nums[i]:
            primes.append(i)
            j = 2
            while (j * i) < len(nums):
                nums[j * i] = False
                j += 1
    return primes
