# Sum and Prod

# Task
# You are given a 2-D array with dimensions N X M. 
# Your task is to perform the sum tool over axis 0 and then find the product of that result.

# Input Format
# The first line of input contains space separated values of N and M. 
# The next N lines contains M space separated integers.

# Output Format
# Compute the sum along axis 0. Then, print the product of that sum.


import numpy

N, M = tuple(map(int, input().split()))
running_list = []
for i in range(0, N):
    running_list.append(input().split())
    
my_array = numpy.array(running_list, int)
print(numpy.prod(numpy.sum(my_array, axis=0), axis=None))
