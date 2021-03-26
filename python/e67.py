"""
Another pathsum, but with more data.
"""

from pathsum import smartsum

def Euler_67():
    #data = np.genfromtxt("../18.dat", filling_values=0)
    data = [[int(i) for i in line.split()] for line in open("../data/67.dat")]
    #path = brute_force(data)
    result = smartsum(data)
    return result

if __name__ == "__main__":
    print(Euler_67())
