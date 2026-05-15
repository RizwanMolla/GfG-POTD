from functools import lru_cache

class Solution:

    def optimalKeys(self, n: int) -> int:
        count = 0
        @lru_cache(None)
        def recurse(j = n):
            if j in {0, 1, 2, 3, 4, 5, 6}: return j
            else:
                maxVal = 0
                for i in range(j-3, 0, -1):
                    maxVal = max(maxVal, recurse(i) * (j-i-1))
                return maxVal
            
        
        return recurse()
