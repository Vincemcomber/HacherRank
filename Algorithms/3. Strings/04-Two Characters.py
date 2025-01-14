# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/two-characters/problem?isFullScreen=true

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
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    m = 0
    st = set(s)
    length = len(st)
    if length > 1:
        from itertools import combinations
        for combos in combinations(st, length - 2):
            temp = s
            for c in combos:
                temp = temp.replace(c, '')
            if len([i for i in range(len(temp) - 1) if temp[i] == temp[i + 1]]) == 0:
                if len(temp) > m:
                    m = len(temp)
    return m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
