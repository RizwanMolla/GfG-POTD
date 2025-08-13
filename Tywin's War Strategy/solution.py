import math

class Solution:
    def minSoldiers(self, arr, k):
        n = len(arr)
        # Step 1: count already lucky troops
        lucky_count = sum(1 for x in arr if x % k == 0)
        
        required = math.ceil(n / 2) - lucky_count
        if required <= 0:
            return 0
        
        # Step 2: find costs to make unlucky troops lucky
        costs = []
        for x in arr:
            if x % k != 0:
                costs.append(k - (x % k))
        
        # Step 3: sort and sum smallest costs
        costs.sort()
        return sum(costs[:required])
