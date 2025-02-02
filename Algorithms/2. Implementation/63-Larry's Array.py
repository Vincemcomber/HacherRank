# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/larrys-array/problem?isFullScreen=true


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
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    # Write your code here
    inv = 0
    for ctr1 in range(len(A) - 1, -1, -1):
        for ctr2 in range(ctr1 - 1, -1, -1):
            if A[ctr2] > A[ctr1]:
                inv += 1
    if (inv % 2) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
