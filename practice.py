from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for i in range(len(nums)):
            has[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in has and has.get(diff) != i:
                return [i, has.get(diff)]
        return []
