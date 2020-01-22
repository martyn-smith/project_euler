"""
Find the sum of even-numbered fibonacci terms below four million.
"""
from fibonaccigen import fibonacci

def Euler_2():
    #verified, integrated fibonacci() into this
    #remember f carries the value of f_prev[-1] in the while loop!
    max_num = 4e+6
    fb = fibonacci()
    f = 0
    result = 0

    while (f < max_num):
        f = next(fb)
        #test for even and sum
        if (f % 2) == 0:
            #print "found even f"
            result += f
    return result

if __name__ == "__main__":
    print(Euler_2())
