from typing import List


def likes(array: List) -> str:
    result = "no one likes this" if len(array) == 0 else "" \
        f"{array[0]} likes this" if len(array) == 1 else "" \
        f"{array[0]} and {array[1]} like this" if len(array) == 2 else "" \
        f"{array[0]}, {array[1]} and {array[2]} like this" if len(array) == 3 else "" \
        f"{array[0]}, {array[1]} and {len(array)-2} others like this" if len(array) > 3 else ""
    return result
