from typing import List

class Solution:
    def maxSkill(self, arr: List[int]) -> int:
        n = len(arr)
        arr = [1] + arr + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(1, n + 1):
            for l in range(1, n - length + 2):
                r = l + length - 1
                
                for k in range(l, r + 1):
                    skill = arr[l-1] * arr[k] * arr[r+1]
                    skill += dp[l][k-1] + dp[k+1][r]
                    dp[l][r] = max(dp[l][r], skill)
        
        return dp[1][n]