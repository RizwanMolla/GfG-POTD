#User function Template for python3
class Solution:
    def nCr(self, n, r):
        if r > n:
            return 0
        r = min(r, n - r)
        res = 1
        for i in range(r):
            res = res * (n - i) // (i + 1)
        return res