# Transpose

# We can generate the transposition of an array using the tool numpy.transpose. 
# It will not affect the original array, but it will create a new array.

# Flatten

# The tool flatten creates a copy of the input array flattened to one dimension.

# Task
# You are given a N X M integer array matrix with space separated elements (N = rows and M = columns). 
# Your task is to print the transpose and flatten results.

# Input Format
# The first line contains the space separated values of N and M. 
# The next N lines contains the space separated elements of M columns.

# Output Format
# First, print the transpose array and then print the flatten.


# Solution
import numpy

inp = input()
N, M = int(inp[0]), inp[1]
running_list = []
for i in range(0, N):
    line = input().split()
    running_list.append([c for c in line])

arr = numpy.array(running_list, int)
print((numpy.transpose(arr)), (arr.flatten()), sep='\n')
