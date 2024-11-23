# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

import re
from itertools import groupby

def is_valid(cid):
    #cid = ''.join(sorted(cid))
    start_456 = bool(re.search(r'^[4-6]', cid))
    #print("start_456 = ", start_456)
    has_16_digits = bool(re.search(r'(?:[0-9]{4}-){3}[0-9]{4}|[0-9]{16}', cid))
    #print("has_16_digits = ", has_16_digits)
    cid = cid.replace('-', '')
    has_16_digits1 = bool(len(cid) == 16)
    no_more_than_4repeats = bool(max(len(list(g)) for _, g in groupby(cid)) < 4)
    #print("no_more_than_4repeats = ", no_more_than_4repeats)

    if start_456 and has_16_digits and no_more_than_4repeats and has_16_digits1:
        return "Valid"
    else:
        return "Invalid"


N = int(input())
for _ in range(N):
    l = input().strip()
    print(is_valid(l))

"""
import re
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")
    
"""