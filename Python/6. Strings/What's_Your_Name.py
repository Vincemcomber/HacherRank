# What's Your Name?

# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# Hello firstname lastname! You just delved into python.

# Input Format
# The first line contains the first name, and the second line contains the last name.

# Constraints
# The length of the first and last name ≤ 10.

# Output Format
# Print the output as mentioned above.

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Solutions
# Complete the 'print_full_name' function below.

# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(a, b):
    first_name = a
    last_name = b
        
    print("Hello", first_name, last_name + "!", "You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
