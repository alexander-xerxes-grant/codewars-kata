def find_shortest_word(s):
    return min(len(word) for word in s.split())
