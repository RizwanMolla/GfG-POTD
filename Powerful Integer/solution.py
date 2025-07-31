class Solution:
    def powerfulInteger(self, intervals, k):
        from collections import defaultdict
        
        events = defaultdict(int)
        
        for start, end in intervals:
            events[start] += 1
            events[end + 1] -= 1
        
        sorted_points = sorted(events.items())
        
        current_count = 0
        prev_point = -1
        max_powerful = -1
        
        for point, delta in sorted_points:
            if current_count >= k:
                max_powerful = max(max_powerful, point - 1)
            
            current_count += delta
        
        return max_powerful
