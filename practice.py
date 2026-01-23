from typing import List

def twoSum(self, numbers: List[int], target: int) -> List[int]:
        has = {}
        for i, v in enumerate(numbers):
            has[v] = i
        for i in range(len(numbers)):
            key = target - numbers[i]
            if key in has and has.get(key) != i:
                return [min(i+1, has.get(key) + 1), max(i+1, has.get(key) + 1)]
        