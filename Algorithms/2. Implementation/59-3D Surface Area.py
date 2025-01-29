# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true


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
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    H, W = len(A), len(A[0])
    area = 2*H*W
    #print("H = {} W = {} area = {}".format(len(A), len(A[0]), area))
    
    for ind in range(H):
        for jnd in range(W):
            #print("i = {} j = {} A = {}".format(ind, jnd, A[ind][jnd]))
            # ind-1, jnd
            if ind-1 >= 0:
                #print("adding part {}".format(max(0, A[ind][jnd] - A[ind-1][jnd])))
                area += max(0, A[ind][jnd] - A[ind-1][jnd])
            else:
                #print("adding full {}".format(A[ind][jnd]))
                area += A[ind][jnd]
            # ind, jnd-1
            if jnd-1 >= 0:
                #print("adding part {}".format(max(0, A[ind][jnd] - A[ind][jnd-1])))
                area += max(0, A[ind][jnd] - A[ind][jnd-1])
            else:
                #print("adding full {}".format(A[ind][jnd]))
                area += A[ind][jnd]
            # ind+1, jnd
            if ind+1 < H:
                #print("adding part {}".format(max(0, A[ind][jnd] - A[ind+1][jnd])))
                area += max(0, A[ind][jnd] - A[ind+1][jnd])
            else:
                #print("adding full {}".format(A[ind][jnd]))
                area += A[ind][jnd]
            # ind, jnd+1
            if jnd+1 < W:
                #print("adding part {}".format(max(0, A[ind][jnd] - A[ind][jnd+1])))
                area += max(0, A[ind][jnd] - A[ind][jnd+1])
            else:
                #print("adding full {}".format(A[ind][jnd]))
                area += A[ind][jnd]
    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
