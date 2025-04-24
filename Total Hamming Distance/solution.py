class Solution:
    def totHammingDist(self, arr):
        total = 0
        n = len(arr)
        
        for i in range(32):
            count_ones = sum((num >> i) & 1 for num in arr)
            count_zeros = n - count_ones
            total += count_ones * count_zeros
        
        return total
