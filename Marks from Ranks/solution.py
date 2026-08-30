class Solution:
    def getMarks(self, l, r, rank):
        r2m={}
        rk=1
        for ll,rr in zip(l,r):
            r2m[rk]=ll
            rk+=rr-ll+1
        lst=list(r2m)
        from bisect import bisect_right
        ret=[]
        for rk in rank:
            ix=bisect_right(lst,rk)
            ret.append(rk-lst[ix-1]+r2m[lst[ix-1]])
        return ret