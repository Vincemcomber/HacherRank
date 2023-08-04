"""
ABC is a right angled triangle.
∠ABC = 90 degree.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC. 
Your task is to find ∠MBC in degrees.

Input Format
The first line contains the length of side AB.
The second line contains the length of side BC.

Output Format
Output ∠MBC in degrees. 
Note: Round the angle to the nearest integer.

Sample Input
10
10

Sample Output
45°
"""

# SOLUTION

# importing the module
import math

# taking the input from user
ab = float(input())
bc = float(input())

# finding the distance 
ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0
mc = bm

# equalizing the sides 
b = mc
c = bm
a = bc

# where b=c
# finding the angle in radian
angel_b_radian = math.acos(a / (2*b))

# converting the radian to degree
angel_b_degree = int(round((180 * angel_b_radian) / math.pi))

# printing with degree
print(angel_b_degree,'\u00B0',sep='')
