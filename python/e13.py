"""
just sums the numbers in the data file...
"""

import numpy as np
FILENAME = "../data/13.dat"

def Euler_13():
    #problematic, needs float datatype
    data = np.loadtxt(FILENAME)
    #big_num /= (10 ** (np.log10(big_num) - 9))
    return sum(data)

if __name__ == "__main__":
    print(Euler_13())
