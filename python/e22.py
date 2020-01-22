"""
Find the 'score' of all the names in the data file.
"""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Euler_22():
    with open("../data/names.txt") as f:
        names = f.read()[1:-1]
        names = names.split('","')
        names.sort()
        #print([nm for nm in names if any(ltr for ltr in nm if ltr not in alphabet)])
        score = sum(
                    sum((alphabet.index(letter) + 1) for letter in word) 
                    * (i + 1) for i, word in enumerate(names)
                )
    return score

if __name__ == "__main__":
    print(Euler_22())