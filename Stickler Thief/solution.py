from typing import List

class Solution:
    def findMaxSum(self, arr):
        n = len(arr)
        if n == 1:
            return arr[0]
        
        prev2 = 0
        prev1 = 0
        
        for money in arr:
            curr = max(money + prev2, prev1)
            prev2 = prev1
            prev1 = curr
        
        return prev1
