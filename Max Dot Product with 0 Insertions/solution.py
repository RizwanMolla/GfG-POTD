class Solution:
    def maxDotProduct(self, a, b):
        n = len(a)
        m = len(b)
        
        prev = [0] * (m + 1)
        
        for i in range(1, n + 1):
        
            curr = [0] * (m + 1)
        
            for j in range(1, min(i, m) + 1):
                curr[j] = max(
                    prev[j], prev[j - 1] + a[i - 1] * b[j - 1]
        
                )
        
            prev = curr
        
        return prev[m]