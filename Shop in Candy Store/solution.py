class Solution:
    def minMaxCandy(self, prices, k):
        prices.sort()
        
        min_cost = 0
        start, end = 0, len(prices) - 1
        while start <= end:
            min_cost += prices[start]
            start += 1
            end -= k
        
        max_cost = 0
        start, end = 0, len(prices) - 1
        while start <= end:
            max_cost += prices[end]
            end -= 1
            start += k
        
        return [min_cost, max_cost]
