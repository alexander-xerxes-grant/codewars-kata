from collections import defaultdict
from typing import List


class Solution:
    
    def group_anagrams(self, strs: List[str])-> List[List[str]]:
        # define a hashmap, using defaultdict(list)
        # iterate through the list of strs
        # for each
        # create an array with 26 0's that will be the count
        # of each occurrence of letters in each string
        # then, iterate through each character in each str
        
        result = defaultdict(list)
        
        for s in strs:
            
            count = [0] * 26
            
            for c in s:
                
                count[ord(c) - ord("a")] += 1
                print(count)
            
            result[tuple(count)].append(s)
            
        return result.values()
    
    
if 