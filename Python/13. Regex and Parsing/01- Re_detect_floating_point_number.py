# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

import re
for _ in range(int(input())):
    n = input().strip()
    float = re.compile(r'^[+-]?[0-9]*\.[0-9]+$')
    if re.fullmatch(float, n):
        print (True)
    else:
        print (False)