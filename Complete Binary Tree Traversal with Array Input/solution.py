class Solution:
    def levelSort(self, arr):
        lth=len(arr)
        ret=[]
        q=[1]
        while q:
            ret.append(sorted([arr[ix-1] for ix in q]))
            nq=[]
            for cur in q:
                if cur*2<=lth:
                    nq.append(cur*2)
                if cur*2+1<=lth:
                    nq.append(cur*2+1)
            q=nq
        return ret