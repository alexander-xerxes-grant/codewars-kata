# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns True
# solution('abc', 'd') # returns False
# (solution('abcde', '')) # returns True
import re

def solution(string, ending):
    if string.endswith(ending):
        return True
    return False

def solution(string, ending):
    escaped = re.escape(ending)
    if re.search(fr"{escaped}$", string) is not None:
        return True
    return False

# print(solution('abc', 'bc')) 
# print(solution('abc', 'd'))
# print(solution('abcde', ''))
print(solution('!@#$%^&*() :-)', ':-)'))
print(solution('abc\n', 'abc'))