"""
finds the maximum product of four adjacent numbers in a 20x20 grid.
"""

from numpy import loadtxt, transpose

def Euler_11():
    #verified
    #diagonals are the tricky part, rest is easy
    data = loadtxt("../data/11.dat", dtype = int)
    big_num = max(find_max_in_rows(data), find_max_in_rows(transpose(data)), find_max_in_diagonals(data))
    return big_num

def find_max_in_rows(data, big_num = 0):
    for j in range(0, len(data[:,1])):
        for i in range(0, (len(data[:,0]) - 3)):
            num = (data[i][j] * data[i+1][j] * data[i+2][j] * data[i+3][j])
            big_num = max(big_num, num)
    return big_num

def find_max_in_diagonals(data, big_num = 0):
    for i in range(0, len(data[:,0]) - 3):
        for j in range(0, len(data[:,1]) - 3):
            num_right = (data[i][j] * data[i+1][j+1] * data[i+2][j+2] * data[i+3][j+3])
            num_left = (data[i][j] * data[i+1][j-1] * data[i+2][j-2] * data[i+3][j-3])
            big_num = max(big_num, num_right, num_left)
    return big_num

if __name__ == "__main__":
    print(Euler_11())
