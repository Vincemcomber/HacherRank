# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

import re
n = int(input())
color_regex = re.compile(r'#[A-Fa-f0-9]{3,6}')
for _ in range(n):
    line = input()
    if re.match(color_regex, line):
        continue
    else:
        for m in re.findall(color_regex, line):
            print (m)