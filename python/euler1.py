"""
Find the sum of all the multiples of 3 or 5 below 1000. (fizzbuzz++)
"""
divisors = (3,5)
max_num = 1000

def Euler_1():
    #verified.
    result = sum(i for i in range(0, max_num)
                if any(i % n == 0 for n in divisors))
    return result

if __name__ == "__main__":
    print(Euler_1())
