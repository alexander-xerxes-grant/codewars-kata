from collections import Counter


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for c in s:
            s_map[c] = 1 + s_map.get(c, 0)
        for x in t:
            t_map[x] = 1 + t_map.get(x, 0)

        for a in t_map.keys():
            if t_map.get(a, 0) != s_map.get(a, 0):
                print(a)
                return False
            else:
                return True
