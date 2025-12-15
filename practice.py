from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i], 0)
        # Creating [[],[],[],[]........]
        # Where each index represent the occurence and each [] holds the values with that occurence
        # This is similar to bucket sort, however in bucket sort each index represent the [], and val
        # is the occurence
        count = [[] for i in range(len(nums) + 1)] # +1 because len ignore 0 index
        for key, val in map.items():
            count[val].append(key)
        res = []
        for i in range(len(count) - 1, -1, -1): # Loop depends on len of count not nums!
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res
        # Running time O(n), we could have used sorting or heap but runtime would be O(nlogn), 0(nlogk)
                