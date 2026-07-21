class Solution:
    def maxIndexDifference(self, s):
        # code here
        seen = {}
        ans = -1
        
        for i, e in enumerate(s):
            if e == 'a' and 'a' not in seen:
                seen[e] = (i, 0)
                ans = max(ans, 0)
                
            p = chr(ord(e)-1)
            if p in seen:
                idx, l = seen[p]
                l += i - idx 
                ans = max(ans, l)
                seen[e] = (i, l)
            
        return ans