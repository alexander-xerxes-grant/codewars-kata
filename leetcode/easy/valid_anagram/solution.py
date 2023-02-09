class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}
        
        for c1, c2 in zip(s, t):
            if c1 in counts.keys():
                counts[c1] += 1
            else:
                counts[c1] = 1
            if c2 in counts.keys():
                counts[c2] -= 1
            else:
                counts[c2] = -1
                
        for val in counts.values():
            if val != 0:
                return False
        return True