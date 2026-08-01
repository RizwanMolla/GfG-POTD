class Solution:
    def findMax(self, n, a, b, k):
        # code here
        arr = [0] * (n + 1)
        for x, y, z in zip(a, b, k):
            arr[x] += z
            arr[y+1] -= z
            
        t = 0
        mx = 0
        for i in arr:
            t += i
            mx = max(mx, t)
        return mx