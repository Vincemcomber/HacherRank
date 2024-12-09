# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true


# Language: Python

# ========================
#         Solution
# ========================

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    tmp = [
        s[0] + s[1] + s[2],
        s[3] + s[4] + s[5],
        s[6] + s[7] + s[8],
        s[0] + s[3] + s[6],
        s[1] + s[4] + s[7],
        s[2] + s[5] + s[8],
        s[0] + s[4] + s[8],
        s[2] + s[4] + s[6],
    ]
    return all(x == tmp[0] for x in tmp)

def cost(s1, s2):
    return sum(abs(a - b) for a, b in zip(s1, s2))

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    s = sum(s, [])  # flaten s

    #  All possible magic squares of 3x3 order
    magic_squares = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
    ]

    costs = []  # this variable will contain all possible costs

    for magic_square in magic_squares:
        costs.append(sum([abs(magic_square[i] - s[i]) for i in range(9)]))

    return min(costs) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
