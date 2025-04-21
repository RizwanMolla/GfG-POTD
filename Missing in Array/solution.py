class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1
        total_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        return total_sum - actual_sum