def solution(s):
    result = ""

    for char in s:
        if char.isupper() and char != s[0]:
            result += " " + char
        else:
            result += char
    return result
