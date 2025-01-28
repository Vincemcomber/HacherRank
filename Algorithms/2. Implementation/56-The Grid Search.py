# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/the-grid-search/problem?isFullScreen=true


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
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    # Write your code here
    i = 0
    while i <= len(G) - len(P):
        p0 = 0

        while True:
            j = 0
            i0 = i
            p = G[i0].find(P[j], p0)
            if p == -1:
                break

            while j < len(P) and i0 < len(G) and p == G[i0].find(P[j], p0):
                i0 += 1
                j += 1

            if j == len(P):
                return "YES"

            p0 = p + 1

        i += 1

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
