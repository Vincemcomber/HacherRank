# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

import re
x = re.compile(r'[qwrtypsdfghjklzxcvbnm]([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', re.I)
m = re.findall(x, input().strip())
print('\n'.join(m or ['-1']))