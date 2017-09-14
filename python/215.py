"""
Consider the problem of building a wall out of 2×1 and 3×1 bricks (horizontal×vertical dimensions)
such that, for extra strength, the gaps between horizontally-adjacent bricks
never line up in consecutive layers, i.e. never form a "running crack".

There are eight ways of forming a crack-free 9×3 wall, written W(9,3) = 8.

Calculate W(32,10).
"""

def Euler_215(wall_length=9, wall_height=3, brick_lengths=[2,3]):
    pass
    #generate combinations of two and three that sum to wall_length
    #then combinations for which sum of elements are never equal until wall_length
