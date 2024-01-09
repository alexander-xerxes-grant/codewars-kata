class Solution:
    def is_anagram(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        
        count_a, count_b = {}, {}
        
        for i in range(len(a)):
            count_a[a[i]] = 1 + count_a.get(a[i], 0)
            count_b[b[i]] = 1 + count_b.get(b[i], 0)
            
        for c in count_a:
            if count_a[c] != count_b.get(c, 0):
                return False
        
        return True