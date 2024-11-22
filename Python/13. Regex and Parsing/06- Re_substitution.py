# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

import re

for _ in range(int(input())):
    l = input()
    l = re.sub(r" &&(?= )", " and", l)
    l = re.sub(r" \|\|(?= )", " or", l)
    print(l)