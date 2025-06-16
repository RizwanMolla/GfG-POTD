class Solution:
    def minCost(self, heights, cost):
        """
        Single-pass solution using weighted median property.
        """
        # Pair heights with costs and sort
        pairs = sorted(zip(heights, cost))
        
        # Find weighted median in one pass
        total_weight = sum(cost)
        target_weight = (total_weight + 1) // 2
        
        cumulative_weight = 0
        for height, weight in pairs:
            cumulative_weight += weight
            if cumulative_weight >= target_weight:
                target_height = height
                break
        
        # Calculate total cost
        return sum(abs(h - target_height) * c for h, c in zip(heights, cost))