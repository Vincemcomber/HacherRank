# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true


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
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    result = 0

    for i in range(max(a), min(b)+1):
        isFactorMultiple = True
        for num in a:
            if i % num !=0:
                isFactorMultiple = False
                break

        for num in b:
            if num % i != 0:
                isFactorMultiple = False
                break

        if isFactorMultiple == True:
            result += 1
    return result
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
