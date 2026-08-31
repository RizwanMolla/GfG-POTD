from functools import lru_cache

class Solution:

    def minCost(self, n: int, i: int, d: int, c: int) -> int:
        @lru_cache(None)
        def f(x):
            if x == 0:
                return 0
            ans = x * i
            if x % 2 == 0:
                ans = min(ans, c + f(x // 2))
            else:
                ans = min(ans, i + c + f(x // 2))
                if x > 1:
                    ans = min(ans, d + c + f(x // 2 + 1))
            return ans
        return f(n)