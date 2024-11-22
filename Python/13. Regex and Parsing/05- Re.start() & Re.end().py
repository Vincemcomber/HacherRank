# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

import re
S = input()
k = "(?=({}))".format(input().strip())
matches = list(re.finditer(k, S))
if matches:
    print('\n'.join(str((m.start(1), m.end(1)-1)) for m in matches))
else:
    print('(-1, -1)')