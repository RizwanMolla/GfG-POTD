class Solution:
    def sortBySetBitCount(self, arr):
        # code here
        def countSetBit(n):
            cnt=0
            while n:
                n=n&(n-1)
                cnt+=1
            return cnt
        res=sorted(arr,reverse=True,key=lambda a:countSetBit(a))
        return res