from collections import defaultdict
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create an empty hashmap where the key:value will be letter counts like "e1, a1, t1": ["eat", "ate", "tea"]
      
        # iterate through the strings
     
            
            # create an array of 0's, one for each letter in the alphabet, this will be the counts of each letter that occurs
            # in a string
            count = [0] * 26
            
            # iterate through each character in each string
            for c in s:
                
                # increment the count for that character in the count array
                # ord returns the unicode point for a one-character string
                count[ord(c) - ord("a")] += 1
                
            # add count array and the anagrams to the hashmap
            # you must cast the count array to a tuple as lists are an unhashable type
            result[tuple(count)].append(s)
            
        return list(result.values())
    
        