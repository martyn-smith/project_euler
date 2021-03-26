"""
returns a maximum pathsum.
"""
import numpy as np
from pathsum import smartsum
FILENAME = "../data/18.dat"

def Euler_18():
    #data = np.genfromtxt("../18.dat", filling_values=0)
    data = [[int(i) for i in line.split()] for line in open(FILENAME)]
    #path = brute_force(data)
    result = smartsum(data)
    return result

def test_18():
    assert Euler_18() == 1074

if __name__ == "__main__":
    print(Euler_18())
