class Solution:
    def countFriendsPairings(self, n: int) -> int:
        from functools import cache
        @cache
        def dp(ix=n):
            if ix<=0:
                return 1
            return dp(ix-1)+(ix-1)*dp(ix-2)
        return dp()