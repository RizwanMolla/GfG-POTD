class Solution:
    def minDifference(self, arr):
        # Convert time to seconds
        seconds = []
        for time in arr:
            h, m, s = map(int, time.split(":"))
            total = h * 3600 + m * 60 + s
            seconds.append(total)
        
        # Sort the time values
        seconds.sort()
        
        # Initialize min_diff with a large number
        min_diff = float('inf')
        
        # Compare adjacent times
        for i in range(1, len(seconds)):
            diff = seconds[i] - seconds[i - 1]
            min_diff = min(min_diff, diff)
        
        # Wrap around difference between last and first time
        wrap_around_diff = 86400 - seconds[-1] + seconds[0]
        min_diff = min(min_diff, wrap_around_diff)
        
        return min_diff
