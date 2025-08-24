class Solution:
    def minDaysBloom(self, arr, k, m):
        n = len(arr)
        
        # Not enough flowers
        if n < m * k:
            return -1
        
        # Helper function: Can we make m bouquets by day 'day'?
        def canMake(day):
            bouquets = 0
            consecutive = 0
            for bloom in arr:
                if bloom <= day:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0
                if bouquets >= m:
                    return True
            return False
        
        # Binary search on days
        left, right = min(arr), max(arr)
        answer = -1
        
        while left <= right:
            mid = (left + right) // 2
            if canMake(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer
