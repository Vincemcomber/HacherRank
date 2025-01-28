# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/lisa-workbook/problem?isFullScreen=true


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
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    res = 0
    page = 1
    
    for el in arr:
        pr_cur = 1
        for pr in range(pr_cur, pr_cur + el):
            if pr == page + pr//k - (1 if pr%k == 0 else 0):
                res += 1
            #print("problem = {} page = {} page% = {} res = {}".format(pr, page + pr//k - (1 if pr%k == 0 else 0), pr%k, res))
        
        #print()
        
        if el%k == 0:
            page += el//k
        else:
            page += 1 + el//k
        #print("page at end: {}".format(page))
        
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
