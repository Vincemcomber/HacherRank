# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/mars-exploration/problem?isFullScreen=true

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
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    # Complete this function
    nb = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c != "SOS"[i % 3]:
            nb += 1
        i += 1
    return nb

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
