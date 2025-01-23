from typing import List

def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        has = set()
        for num in nums:
            has.add(num)
        for i in range(len(nums)):
            curr = nums[i]
            longest = 1
            if curr - 1 in has:
                continue
            while curr + 1 in has:
                curr += 1
                longest += 1
            res = max(res, longest)
        return res
            