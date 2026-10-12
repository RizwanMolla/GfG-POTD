class Solution:
    def minSquares(self, n, m):
        def dfs(m=m,n=n):
            if m==0 or n==0:
                return 0
            if m==1 or n==1:
                return max(m,n)
            if n<m:
                m,n=n,m
            return dfs(m,n%m)+n//m
        return dfs()