class Solution:
    def activitySelection(self, start, finish):
        activities = sorted(zip(start, finish), key=lambda x: x[1])
        
        count = 0  
        last_end_time = 0 
        
        for s, f in activities:
            if s > last_end_time:
                count += 1
                last_end_time = f
        
        return count