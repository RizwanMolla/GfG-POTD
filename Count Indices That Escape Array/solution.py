class Solution:
    def goodIndices(self, arr):
        # code here
        n=len(arr)
        good=[None]*n
        def dfs(ind):
            if ind>=n or ind<0:
                return 1
            if ind in visited:
                return 0
            visited.add(ind)

            good[ind]=dfs(ind+arr[ind])
            return good[ind]

        for i in range(n):
            if good[i] is None:
                visited=set()
                dfs(i)
        return sum(good)