from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        
        checked = {}
        
        for i, n in enumerate(nums):
            diff = (target - n)
            if diff in checked:
                return [checked[diff], i]
            checked[n] = i
        return