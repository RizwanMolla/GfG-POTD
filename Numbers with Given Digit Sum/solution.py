class Solution:
    def countWays(self, n, sum):
        from functools import cache
        @cache
        def dfs(n=n,sm=sum):
            if n<=0 or sm<=0:
                return n==0 and sm==0
            ret=0
            for nn in range(1 if n==1 else 0,10):
                ret+=dfs(n-1,sm-nn)
            return ret
        ret=dfs()
        return ret if ret>0 else -1