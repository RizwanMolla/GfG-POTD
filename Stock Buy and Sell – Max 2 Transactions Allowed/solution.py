class Solution:
    def maxProfit(self, prices):
        
        if not prices or len(prices) < 2:
            return 0

        n = len(prices)
        
        profit_left = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            profit_left[i] = max(profit_left[i - 1], prices[i] - min_price)
        
        profit_right = [0] * n
        max_price = prices[-1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            profit_right[i] = max(profit_right[i + 1], max_price - prices[i])
        
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, profit_left[i] + (profit_right[i + 1] if i + 1 < n else 0))
        
        return max_profit