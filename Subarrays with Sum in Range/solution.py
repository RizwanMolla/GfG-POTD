class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        def lt(l):
            nonlocal arr
            ret=sm=lef=0
            for rig,ve in enumerate(arr):
                sm+=ve
                while sm>=l:
                    sm-=arr[lef]
                    lef+=1
                ret+=rig-lef+1
            return ret
        return lt(r+1)-lt(l)