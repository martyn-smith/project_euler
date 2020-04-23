"""
Finds the 10 001st prime number.  Actually just by using primegen
"""
from primegen import prime_by_trial

def Euler_7(n = 10_001):
    #verified (104743)
    pr = prime_by_trial()
    for _ in range(0, (n - 1)):
        next(pr)
    return next(pr)

def test_7():
    assert Euler_7() == 104743

if __name__ == "__main__":
    print(Euler_7())
