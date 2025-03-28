from typing import List

class Solution:
    def maxProfit(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0
        
        hold = -float('inf')
        cash = 0

        for price in arr:
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - k)
        
        return cash