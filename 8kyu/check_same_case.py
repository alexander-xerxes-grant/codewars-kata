# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/python
# Write a function that will check if two given characters are the same case.

# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0
# Examples
# 'a' and 'g' returns 1

# 'A' and 'C' returns 1

# 'b' and 'G' returns 0

# 'B' and 'g' returns 0

# '0' and '?' returns -1

import string


alphabet = string.ascii_letters

print(alphabet)

def same_case(a, b): 
    if a not in alphabet or b not in alphabet:
        return -1
    elif a.isupper() == b.isupper():
        return 1
    else:
        return 0


print(same_case('C', 'B') )
print(same_case('b', 'a'))
print(same_case('H', ':'))
print(same_case('\t', 'Z'))
print(same_case('b', 'Z'))