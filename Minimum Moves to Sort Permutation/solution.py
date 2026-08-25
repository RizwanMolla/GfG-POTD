class Solution:
    def minMoves(self, arr):
        n = len(arr)
        atoi = [0] * (n + 1)
        for i in range(n):
            atoi[arr[i]] = i
        curr = lis = 1
        for i in range(1, n):
            if atoi[i] < atoi[i + 1]:
                curr += 1
                lis = max(lis, curr)
            else:
                curr = 1
        return n - lis