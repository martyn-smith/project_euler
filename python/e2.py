"""
Find the sum of even-numbered fibonacci terms below four million.
"""
from fibonaccigen import fibonacci

def Euler_2(n = 4e+6):
    #verified, integrated fibonacci() into this
    #remember f carries the value of f_prev[-1] in the while loop!
    fb = fibonacci()
    f = 0
    result = 0 #sum(f for f in fb if f % 2 == 0)

    while (f < n):
        f = next(fb)
        #test for even and sum
        if (f % 2) == 0:
            result += f
    return result

def test_2():
    assert Euler_2() == 4613732

if __name__ == "__main__":
    print(Euler_2())
