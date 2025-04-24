#User function Template for python3
class Solution:
    def subsetXORSum(self, arr):
        n = len(arr)
        total = 0
        for bit in range(31):
            count = 0
            for num in arr:
                if (num >> bit) & 1:
                    count += 1
            if count > 0:
                total += (1 << bit) * (1 << (n - 1))
        return total