class Solution:
    def count(self, n: int, m: int) -> int:
        from functools import cache
        @cache
        def dfs(n=n,prv=None):
            nonlocal m
            if n==0:
                return 1
            ret=0
            for mm in range(1,m+1):
                if prv==None or mm%prv==0 or prv%mm==0:
                    ret+=dfs(n-1,mm)
            return ret
        return dfs()