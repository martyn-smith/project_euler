"""
just sums the numbers in the data file...
"""

import numpy as np

def Euler_13():
    #problematic, needs float datatype
    data = np.loadtxt("../data/13.dat")
    big_num = sum(data)
    #big_num /= (10 ** (np.log10(big_num) - 9))
    return big_num

if __name__ == "__main__":
    print(Euler_13())
