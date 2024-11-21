# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

import re
m = re.search(r'([0-9a-zA-Z])\1+', input().strip())
print(m.group(1) if m else -1)
'''
if m:
    print(m.group(2))
else:
    print("-1")
'''