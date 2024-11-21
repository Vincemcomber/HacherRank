# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/re-split/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

regex_pattern = r"[,.]"    # Do not delete 'r'.


import re
print("\n".join(re.split(regex_pattern, input())))