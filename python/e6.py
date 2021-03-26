
"""
Finds the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

NOTE: the problem ACTUALLY wants the difference between the square of the sum
and the sum of the squares.
"""

def Euler_6_easy_way():
    sum_of_squares = sum([(i**2) for i in range (1,101)])
    square_of_sum = (sum([i for i in range (1,101)]))**2
    return square_of_sum - sum_of_squares

def Euler_6_better_way():
    # uses S_n = n(a_1 + a_n)/2 for square of sums
    # to be honest... I can't quite remember how sum_of_squares works.  But it does.
    sum_of_squares = int((1e+6)/3 + (1e+4)/2 + 100/6)
    square_of_sum = int((100*101/2)**2)
    return square_of_sum - sum_of_squares

if __name__ == "__main__":
    print(f"easy way: {Euler_6_easy_way()}")
    print(f"better way: {Euler_6_better_way()}")
