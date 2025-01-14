# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true


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

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    print(container)
    
    countByType=[0]* len(container[0])
    countByContainer=[sum(x) for x in container]
    for Ci in container: 
        print ("Ci=", Ci)
        for j in range(len(Ci)):
            print(" j=",j)
            countByType[j]+=Ci[j]

    countByContainer.sort()
    countByType.sort()
    print('Count By Types:',countByType)
    print('Count By Container:',countByContainer)
    return "Possible" if countByContainer==countByType else "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
