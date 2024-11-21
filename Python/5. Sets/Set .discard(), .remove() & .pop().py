# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/default-arguments/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================


n = input()
elements = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()
    operation = command[0]
    args = command[1:]

    if operation != 'pop':
        operation += '(' + ','.join(args) + ')'
        eval('elements.' + operation)
    else:
        elements.pop()
print(sum(elements))