from typing import List

def maxProfit(self, prices: List[int]) -> int:
        pointer1, pointer2, res = 0, 1, 0
        while(pointer2 < len(prices)):
            profit = prices[pointer2] - prices[pointer1]
            res = max(res, profit)
            if(pointer2 == len(prices) - 1):
                pointer1 += 1
                pointer2 = pointer1 + 1
            else:
                pointer2 += 1
        return res