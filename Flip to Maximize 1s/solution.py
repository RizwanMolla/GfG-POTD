class Solution:
    def maxOnes(self, arr):
        # code here
        onescount=0
        ans=0
        for i in range(len(arr)):
            if arr[i]==1:
                onescount+=1
        curr=0
        for r in range(len(arr)):
            
            if arr[r]==0:
                curr+=1
            else:
                curr-=1
            if curr < 0:
                curr = 0

            ans=max(ans,curr)
        return ans+onescount
        