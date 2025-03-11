class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        prev, curr = cost[0], cost[1]  
        
        for i in range(2, n):
            next_step = cost[i] + min(prev, curr)  
            prev, curr = curr, next_step  
        return min(prev, curr)
