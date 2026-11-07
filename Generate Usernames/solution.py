class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        lth=len(arr)
        res={}
        for ix in range(lth-1,-1,-1):
            ve=arr[ix]
            res[ve]=ix
        ret=arr[:]
        apx=1
        for ix,ve in enumerate(arr):
            if ve in res and res[ve]==ix:
                continue
            tmp=ve+f'{apx}'
            while tmp in res:
                apx+=1
                tmp=ve+f'{apx}'
            ret[ix]=tmp
            res[tmp]=ix
            apx=1
        return ret