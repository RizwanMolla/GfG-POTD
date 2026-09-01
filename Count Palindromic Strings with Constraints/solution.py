import math
class Solution:
    def palindromicStrings(self, n, k):
        # code here
        res = 0
        mod = 10**9 + 7
        def per(k, v):
            return math.factorial(k) // (math.factorial(k-v))
        for l in range(1, n+1):

            v = l//2
            if v > k:
                continue
            if l % 2 == 0:
                res += per(k, v)
            else:

                res += (k-v) * per(k, v)
        return res % mod