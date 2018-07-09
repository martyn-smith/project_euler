"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import itertools

def Euler_4():
    #verified
    big_palindrome = 0
    for i, j in itertools.combinations(range(100,999), 2): #gives 403651 results?
        candidate = (i*j)
        #we're doing it the hard way, damnit - no tostring() method!
        etadidnac = reverse(candidate)
        #print(f"{candidate}\t{etadidnac}")
        if (etadidnac == candidate):
            big_palindrome = max(big_palindrome, candidate)
    return big_palindrome
            #print "{}, {} = {} | {}".format(i, j, candidate, etadidnac)

def reverse(num):
    i = 0
    mun = 0
    while num:
        #print "num = {}".format(num)
        digit = num % 10
        mun *= 10
        mun += digit
        num //= 10
        i += 1
    return mun

if __name__ == "__main__":
    print(Euler_4())
