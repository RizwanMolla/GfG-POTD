#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from typing import List

class Solution:
    def minCandy(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        
        candies = [1] * n
        
        # Left to right pass
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Right to left pass
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)