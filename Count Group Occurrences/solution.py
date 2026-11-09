class Solution:
    def getCount (self, s, k):
        # code here
        cnt={}
        prv=''
        for c in s:
            if c==prv:
                continue
            cnt[c]=cnt.get(c,0)+1
            prv=c
        return sum(1 for c in cnt if cnt[c]==k)