from typing import List

class Solution:
    def rob_linear(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for num in nums:
            temp = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = temp
        return prev1

    def maxValue(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        
        case1 = self.rob_linear(arr[:-1])
        case2 = self.rob_linear(arr[1:])
        
        return max(case1, case2)