from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We need this instead of {} because if we directly use res[count].append(s)
        # then it will give key error because no res[count] exist to append, using defaultdict(list) 
        # initialize an empty list key first then appends so no key error !!
        res = defaultdict(list) 
        for s in strs:
            count = [0] * 26 # Array of length 26, initialized each index's value to 0
            for c in s:
                count[ord(c) - ord('a')] += 1 # ord gives the ASCCI and the difference gives the index
            # We need to convert key from list to tuple the key must be IMMUTABLE, tuple is immutable
            res[tuple(count)].append(s) 
        return list(res.values()) # map.values() returns group of values in list form
            