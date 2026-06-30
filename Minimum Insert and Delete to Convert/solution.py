import bisect as bi

class Solution:
    def minInsAndDel(self, a, b):
        # code here
        db = {b[i]: i for i in range(len(b))}
        ar = [db[i] for i in a if i in db]
        l = []
        for val in ar:
            i = bi.bisect_left(l, val)
            if i==len(l): l.append(val)
            else: l[i]=val
        return len(a)+len(b)-2*len(l)