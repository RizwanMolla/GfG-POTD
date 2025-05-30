class Solution:
    def minCoins(self, coins, total):
        dp = [float('inf')] * (total + 1)
        dp[0] = 0  

        for coin in coins:
            for amount in range(coin, total + 1):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

        return dp[total] if dp[total] != float('inf') else -1