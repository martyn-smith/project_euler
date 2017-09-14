"""
Find the sum of even-numbered fibonacci terms below four million.
"""

def Euler_2():
    #verified, integrated fibonacci() into this
    #remember f carries the value of f_prev[-1] in the while loop!
    max_num = 4e+6
    f = 0
    sum = 0
    f_prev = []
    while (f < max_num):
        #generates the fibonacci sequence
        if (len(f_prev) >= 2):
            f += (f_prev[-2])
        #initial edge cases
        elif (len(f_prev) == 1):
            f = 1
        else:
            f = 0

        #test for even and sum
        if (f % 2) == 0:
            #print "found even f"
            sum += f
        f_prev.extend([f])
    return sum

if __name__ == "__main__":
    print(Euler_2())
