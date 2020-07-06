"""
the data file contains a 1000-digit number.
Find the thirteen adjacent digits in the 1000-digit number that have
the greatest product.
"""
FILENAME = "../data/8.dat"

def Euler_8():
    #verified.  That was easy...
    with open(FILENAME) as f:
        big_num = f.read()
    big_product = 1
    for i in range(1, (len(big_num)-13)):
        product = 1
        num = big_num[i:(i+13)]
        for j in num:
            product *= int(j)
        big_product = max(product, big_product)
    return big_product

if __name__ == "__main__":
    print(Euler_8())
