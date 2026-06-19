class Solution:
    def optimalArray(self, arr):
        res = [0]
        for i in range(1, len(arr)):
            res.append(res[-1] + (arr[i] - arr[i//2]))
        return res