

def count_duplicates(s):
    # s= s.lower()
    # result = 0
    # counts = {i:s.count(i) for i in s}
    # for value in counts.values():
    #     if value > 1:
    #         result += 1
    # return result

    return len([character for character in set(s.lower()) if s.lower().count(character) > 1])