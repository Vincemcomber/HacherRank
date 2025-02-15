# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/big-sorting/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

#!/bin/python3

import os
import math
import random
import sys
import re


# Complete the bigSorting function below.
def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x), x))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()