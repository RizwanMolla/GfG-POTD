class Solution:
    def noOfWays(self, m, n, x):
        # Edge cases
        # Minimum possible sum with n dice is n (all dice show 1)
        # Maximum possible sum with n dice is n*m (all dice show m)
        if x < n or x > n * m:
            return 0
        
        # dp[i][j] represents number of ways to get sum j using i dice
        # We need dp[n][x]
        dp = [[0 for _ in range(x + 1)] for _ in range(n + 1)]
        
        # Base case: 0 dice can make sum 0 in exactly 1 way
        dp[0][0] = 1
        
        # Fill the dp table
        for i in range(1, n + 1):  # for each number of dice from 1 to n
            for j in range(i, min(i * m + 1, x + 1)):  # for each possible sum
                # Try all possible face values (1 to m) for the current die
                for face in range(1, min(m + 1, j + 1)):
                    if j - face >= 0:
                        dp[i][j] += dp[i - 1][j - face]
        
        return dp[n][x]