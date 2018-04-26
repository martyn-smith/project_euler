"""
Finds the 10 001st prime number.  Actually just by using primegen
"""
from primegen import prime_by_trial

def Euler_7():
    #verified (104743)
    end_num = 10001
    pr = prime_by_trial()
    for n in range(0, (end_num - 1)):
        next(pr)
    return next(pr)

if __name__ == "__main__":
    print(Euler_7())
