# Incorrect Regex

# You are given a string S. 
# Your task is to find out whether S is a valid regex or not.

# Input Format
# The first line contains integer T, the number of test cases. 
# The next T lines contains the string S.

# Constraints
# 0 < T < 100

# Output Format
# Print "True" or "False" for each test case without quotes.


# Enter your code here. Read input from STDIN. Print output to STDOUT

# SOLUTION
import re

T = int(input())
for i in range(0, T):
    regex_raw = input()
    try:
        regex = re.compile(regex_raw)
    except re.error:
        print(False)
    else:
        print(True)
