# Min and Max

# Task
# You are given a 2-D array with dimensions NxM. 
# Your task is to perform the min function over axis 1 and then find the max of that.

# Input Format
# The first line of input contains the space separated values of N and M. 
# The next N lines contains M space separated integers.

# Output Format
# Compute the min along axis 1 and then print the max of that result.


import numpy

N, M = map(int, input().split())
running_list = []
for i in range(0, N):
    running_list.append([x for x in input().split()])

my_array = numpy.array(running_list, int)
print(numpy.max(numpy.min(my_array, axis=1), axis=None))
