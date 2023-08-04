# Lists

# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

# Input Format
# The first line contains an integer, n, denoting the number of commands. 
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints
# The elements added to the list must be integers.

# Output Format
# For each command of type print, print the list on a new line.


# Enter your code here. Read input from STDIN. Print output to STDOUT

# Solution
if __name__ == '__main__':
    L = []
    N = int(input())
    for _ in range(N):
        input_string = input().split()
        # The input will consist of a command first, followed by the arguments
        command = input_string[0]
        arguments = input_string[1:]
        if (command != "print"):
            command += "("+ ",".join(arguments) +")"
            eval("L." + command)
        else:
            print(L)
