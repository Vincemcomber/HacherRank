# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true

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
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    special_characters = "!@#$%^&*()-+"

    chars_to_add = int(not any(x.isupper() for x in password)) + int(not any(x.islower() for x in password)) + \
        int(not any(x.isdigit() for x in password)) + \
        int(not any(sc in password for sc in special_characters))

    if n + chars_to_add < 6:
        chars_to_add += 6 - (n + chars_to_add)

    return chars_to_add
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
