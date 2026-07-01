class Solution:
    def maxSumSubarray(self, arr):
        after_first_neg = False
        pos_s = 0
        s = 0
        lst = 0
        maxi = -sys.maxsize
        for i in arr:
            if i < 0:
                lst = min(i, lst)
                if after_first_neg and pos_s > s - lst + i:
                    s = pos_s
                    lst = i
                after_first_neg = True
            s += i
            pos_s += i
            maxi = max(maxi, s - lst)
            if pos_s < 0:
                pos_s = 0
        return max(arr) if maxi == 0 else maxi 