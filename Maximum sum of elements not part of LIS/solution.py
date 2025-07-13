class Solution:
    def nonLisMaxSum(self, arr):
        n = len(arr)
        total = sum(arr)
        maxlen = 1
        LisSum = float('inf')
        
        length = [1] * n
        sum_arr = [0] * n

        for i in range(n):
            sum_arr[i] = arr[i]
            for j in range(i):
                if arr[j] < arr[i] and length[j] + 1 >= length[i]:
                    length[i] = length[j] + 1
                    sum_arr[i] = sum_arr[j] + arr[i]
            maxlen = max(maxlen, length[i])

        for i in range(n):
            if length[i] == maxlen:
                LisSum = min(LisSum, sum_arr[i])

        return total - LisSum
