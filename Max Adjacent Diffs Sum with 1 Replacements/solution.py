class Solution:
    def maxDiffSum(self, arr):
       a = 0
       b = 0
    
       for i in range(1, len(arr)):
           x = max(
               a + abs(arr[i] - arr[i-1]),
               b + abs(arr[i] - 1)
           )
    
           y = max(
               a + abs(1 - arr[i-1]),
               b
           )
    
           a, b = x, y
    
       return max(a, b)