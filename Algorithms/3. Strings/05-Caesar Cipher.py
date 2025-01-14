# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem?isFullScreen=true

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
import functools

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    # Complete this function
    def caesar():
        for c in s:
            c = ord(c)
            if 97 <= c <= 122:
                c = 97 + ((c - 97) + k) % 26
            elif 65 <= c <= 90: 
                c = 65 + ((c - 65) + k) % 26
            yield chr(c) 
    
    return ''.join(caesar())
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
