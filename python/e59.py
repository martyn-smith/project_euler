"""
returns The Gospel of John, chapter 1 with key "god".  Pffft.
"""

import numpy as np
from itertools import product
from string import ascii_lowercase
KEY_LENGTH = 3

def Euler_59():
    ciphertxt = np.loadtxt("../data/59.dat", dtype=int, delimiter=",")
    return E59_brute_force(ciphertxt)

def E59_brute_force(ciphertxt):
    """brute force does have one advantage - ability to search for long
    strings, e.g. 'the', which the quicker method does not.
    This probably does not make up for the m^n vs m*n time cost
    """
    trial_keys = product(ascii_lowercase, repeat = 3)
    for trial_key in trial_keys:
        #print("trialling... " + str(trial_key))
        trial_key = [ord(i) for i in trial_key]
        plaintxt = [(ciphertxt[i] ^ trial_key[i % 3]) for i in range(0, len(ciphertxt))]
        plaintxt = [str(chr(i)) for i in plaintxt]
        plaintxt = "".join(plaintxt)
        #print plaintxt
        if (" the " in plaintxt):
            return plaintxt

"""
def E59_smarter(ciphertxt):
    for i in range(1, KEY_LENGTH+1):
        subciphers = zip([],[])
     for j in range(0, len(ciphertxt)):
            for j in ascii_lowercase:
                j = ord(j)
                trial = []
                for k in :
                    trial.extend(str(unichr(j ^ k)))
"""

if __name__ == "__main__":
    print(Euler_59())
