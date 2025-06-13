class Solution:
    def kokoEat(self, arr, k):
        def canFinish(speed):
            """Check if Koko can finish all piles within k hours at given speed"""
            total_hours = 0
            for pile in arr:
                # Calculate hours needed for this pile: ceil(pile/speed)
                hours_needed = (pile + speed - 1) // speed  # This is ceil division
                total_hours += hours_needed
                if total_hours > k:  # Early termination if already exceeded
                    return False
            return total_hours <= k
        
        # Binary search on eating speed
        left, right = 1, max(arr)
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if canFinish(mid):
                result = mid  # This speed works, try to find smaller
                right = mid - 1
            else:
                left = mid + 1  # Need faster speed
        
        return result