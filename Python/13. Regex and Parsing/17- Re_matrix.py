# ========================
#       Information
# ========================

# Direct Link: https://github.com/akiselev1/hackerrank-solutions/blob/master/re_matrix.py

# Language: Python

# ========================
#         Solution
# ========================

#!/bin/python3
import re
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

lst = [list(i) for i in zip(*matrix)]
txt = "".join(str(r) for v in lst for r in v)
txt = re.split(r"(?<=\w)[^\w]+(?=\w)", txt)
text = " ".join(str(e) for e in txt)
print(text)
