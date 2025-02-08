from typing import List

def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maximum = 0

        while (left < right):
            currMax = (right - left) * min(heights[left], heights[right])
            maximum = max(currMax, maximum)
            if(heights[left] <= heights[right]):
                left += 1
            else:
                right -= 1
        return maximum
