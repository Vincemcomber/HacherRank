# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

from collections import Counter
import re

def isvalid(uid):
    if len(uid) != 10:
        return False
    if not uid.isalnum():
        return False
    if set(i for i in uid if uid.count(i)>1):
        return False
    #numbers
    num=[i for i,j in Counter(uid).items() if i.isdigit()]
    if len(num)<3:
        return False
    #capitals
    caps=[i for i,j in Counter(uid).items() if i.isupper()]
    if len(caps)<2:
        return False
    return True

def is_valid(uid):
    uid = ''.join(sorted(uid))
    has_2_or_more_upper = bool(re.search(r'[A-Z]{2,}', uid))
    has_3_or_more_digits = bool(re.search(r'\d{3,}', uid))
    has_10_proper_elements = bool(re.search(r'^[a-zA-Z0-9]{10}$', uid))
    no_repeats = not bool(re.search(r'(.)\1', uid))

    if has_2_or_more_upper and has_3_or_more_digits and has_10_proper_elements and no_repeats:
        return True
    else:
        return False


T = int(input())
for _ in range(T):
    l = input().strip()
    if is_valid(l):
        print("Valid")
    else:
        print("Invalid")