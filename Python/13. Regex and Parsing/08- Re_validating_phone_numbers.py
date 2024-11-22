# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

import re
def is_valid(num):
    if re.search(r'^[7-9][0-9]{9}$', num):
        return "YES"
    else:
        return "NO"


N = int(input())
for _ in range(N):
    l = input().strip()
    print(is_valid(l))