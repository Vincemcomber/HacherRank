# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem?isFullScreen=true

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
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    n = len(s)
    i = 1
    while i <= n // 2:
        j = i
        a = int(s[:i])
        flag = 1
        while j < n:
            b = str(a + 1)
            if s[j:j + len(b)] != b:
                flag = 0
                break
            j += len(b)
            a = int(b)
        if flag:
            print('YES ' + s[:i])
            return
        i += 1
    print('NO')
    return

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
