class Solution:
    def maxCharGap(self, s):
        
        max_gap = -1
        
        for char in set(s):
            first = s.find(char)
            last = s.rfind(char)
            
            if first != last:
                gap = last - first - 1
                max_gap = max(max_gap, gap)
                
        return max_gap