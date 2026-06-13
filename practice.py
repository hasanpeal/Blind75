from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left = [0] * len(nums)
        right = [0] * len(nums)

        left[0] = 1
        right[len(nums) - 1] = 1


        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        for i in range(len(nums) - 2, -1, -1): # Middle val is -1 which represent 0 !!
            right[i] = nums[i+1] * right[i+1]
        for i in range(len(nums)):
            res[i] = left[i] * right[i]

        return res