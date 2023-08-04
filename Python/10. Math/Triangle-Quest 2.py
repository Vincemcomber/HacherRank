"""
You are given a positive integer N. 
Your task is to print a palindromic triangle of size N.
For example, a palindromic triangle of size 5 is:
1
121
12321
1234321
123454321
You can't take more than two lines. The first line (a for-statement) is already written for you. 
You have to complete the code using exactly one print statement.

Note: 
Using anything related to strings will give a score of 0. 
Using more than one for-statement will give a score of 0.

Input Format
A single line of input containing the integer N.

Output Format
Print the palindromic triangle of size N as explained above.

Sample Input
5

Sample Output
1
121
12321
1234321
123454321
"""

# SOLUTION
# Reading number of rows
row = int(input('Enter how many lines? '))

# Generating pattern
for i in range(1,row+1):
    
    # for space
    for j in range(1, row+1-i):
        print(' ', end='')
    
    # for increasing pattern
    for j in range(1,i+1):
        print(j, end='')
    
    # for decreasing pattern 
    for j in range(i-1,0,-1):
        print(j, end='')
    
    # Moving to next line
    print()
