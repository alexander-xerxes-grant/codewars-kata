from collections import Counter


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        
        # check if the string is an anagram of the target
        # s and t must be the same length
        # create two dicts (hashmaps)
        # these will be the counts of the number of each
        # letter in each string
        
        # then iterate over the dicts and check
        # each count of each letter is equal
        
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}
        
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        for c in count_s:
            if count_s[c] != count_t.get(c, 0):
                return False
        return True