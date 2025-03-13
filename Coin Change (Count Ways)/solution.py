class Solution:
    def count(self, coins, targetSum):
        dp = [0] * (targetSum + 1)
        dp[0] = 1  

        for coin in coins:
            for amount in range(coin, targetSum + 1):
                dp[amount] += dp[amount - coin]

        return dp[targetSum]