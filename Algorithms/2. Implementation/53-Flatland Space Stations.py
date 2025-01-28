# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/flatland-space-stations/problem?isFullScreen=true


# Language: Python

# ========================
#         Solution
# ========================

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
     sp = sorted(c)
     
     r = max(sp[0] - 0, n - 1 - sp[-1])

     for i in range(1, len(sp)):
        # le plus long chemin entre deux stations
        r = max(r, (sp[i] - sp[i - 1]) // 2)
     return r

    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
