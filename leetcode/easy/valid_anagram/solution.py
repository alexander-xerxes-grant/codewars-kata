class Solution:
    def is_anagram(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False

        a_map, b_map = {}, {}

        for i in range(len(a)):
            a_map[a[i]] = 1 + a_map.get(a[i], 0)
            b_map[b[i]] = 1 + b_map.get(b[i], 0)
            print(a_map)
            print(b_map)

        for i in a_map:
            if a_map[i] != b_map.get(i, 0):
                return False

        return True
