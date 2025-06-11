from typing import List

def findMin(self, nums: List[int]) -> int:
        l, r, res = 0, len(nums) - 1, nums[0]
        # It's '<=' because what if we have [2] here l val = 2 r val = 2, it would skip loop for '<'
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res