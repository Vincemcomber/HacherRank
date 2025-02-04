# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/fair-rations/problem?isFullScreen=true

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
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

# Complete the fairRations function below.
def fairRations(B):
    ret = 0

    for i in range(len(B)-1, 0, -1):
        if B[i] % 2 == 1:
            B[i] += 1
            B[i-1] += 1
            ret += 2

    if B[0] % 2 == 1:
        return "NO"
        
    return ret  
    
       
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result))

    fptr.close()
