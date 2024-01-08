from typing import List

nums = [1, 2, 3, 4]
# Output: [24,12,8,6]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # list of 1's to represent the result
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            print(f"Setting result[i] ({result[i]}) to prefix ({prefix})\n")
            prefix *= nums[i]
            print(
                f"Multiplying and setting prefix ({prefix}) equal to nums[i] ({nums[i]})\n"
            )

        print(result)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


solution = Solution().productExceptSelf(nums)
print(solution)
