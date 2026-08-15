class Solution:
    def countWithout(self, n: int, d: int) -> int:
        if n == 0:
            return 0
    
        digits = str(n)
    
        from functools import lru_cache
    
        @lru_cache(None)
        def dp(pos, tight, started):
            if pos == len(digits):
                return 1 if started else 0
    
            limit = int(digits[pos]) if tight else 9
            ans = 0
    
            for digit in range(limit + 1):
                new_tight = tight and (digit == limit)
    
                if not started and digit == 0:
                    ans += dp(pos + 1, new_tight, False)
                elif digit != d:
                    ans += dp(pos + 1, new_tight, True)
    
            return ans
    
        return dp(0, True, False)