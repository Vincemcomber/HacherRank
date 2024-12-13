# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=true

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
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    while True:
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                s = s[:i-0] + s[i+2:]
                if len(s) == 0:
                    return "Empty String"
                break
            if i == len(s) - 2:
                return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
