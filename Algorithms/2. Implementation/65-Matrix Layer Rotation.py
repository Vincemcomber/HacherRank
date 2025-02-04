# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matrix-rotation-algo/problem?isFullScreen=true

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
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Write your code here
    n = len(matrix)
    m = len(matrix[0])
    lowerit = math.floor(min(n, m)/2)
    
    n -= 1
    m -= 1
    for i in range(lowerit):
        arr = []
        endl = n - i
        endr = m - i
        for j in range(i, endl+1):
            arr.append(matrix[j][i])
        for j in range(i + 1, endr+1):
            arr.append(matrix[endl][j])
        for j in range(endl-1, i-1, -1):
            arr.append(matrix[j][endr])
        for j in range(endr-1, i, -1):
            arr.append(matrix[i][j])
            
        bigrcheck =  r % len(arr)
        
        nwarr = arr[len(arr)-bigrcheck:] + arr[:len(arr)-bigrcheck] 
        
        counter = 0
        for j in range(i, endl+1):
            matrix[j][i] = nwarr[counter]
            counter += 1
        for j in range(i + 1, endr+1):
            matrix[endl][j] = nwarr[counter]
            counter += 1
        for j in range(endl-1, i-1, -1):
            matrix[j][endr] = nwarr[counter]
            counter += 1
        for j in range(endr-1, i, -1):
            matrix[i][j] = nwarr[counter]
            counter += 1
    for line in matrix:
        print(*line)
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
