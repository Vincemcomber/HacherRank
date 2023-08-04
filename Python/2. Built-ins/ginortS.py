### ginortS ###


##You are given a string S.
## S contains alphanumeric characters only.

##Your task is to sort the string  in the following manner:
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

##Input Format
#A single line of input contains the string .

##Constraints
#0<len(S)<1000

##Output Format
#Output the sorted string S.

#############CODE BELOW ########

s = input()
upper, lower,odd, even  = [], [], [], []

for char in s:
    if char.isnumeric():
        if int(char)%2 == 0:
            even.append(char)
        else:
            odd.append(char)
    else:
        if char.isupper():
            upper.append(char)
        else:
            lower.append(char)

print(''.join(sorted(lower))+''.join(sorted(upper))+''.join(sorted(odd))+''.join(sorted(even)))
