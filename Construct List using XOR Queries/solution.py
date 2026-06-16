class Solution:
    def constructList(self, queries):
        xor=0
        ans=[0]
        for q,x in queries:
            if q==0:
                ans.append(x^xor)
            else:
                xor^=x
        n=len(ans)
        for i in range(n):
            ans[i]^=xor
        ans.sort()
        return ans