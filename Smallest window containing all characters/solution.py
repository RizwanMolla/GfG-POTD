from collections import Counter

class Solution:
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return ""
        
        need = Counter(p)
        missing = len(p)
        left = start = end = 0
        min_len = float("inf")
        
        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            
            while missing == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start, end = left, right
                
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        
        return "" if min_len == float("inf") else s[start:end+1]
