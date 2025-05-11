from typing import List

class Solution:
    def kthLargest(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # List to store all possible subarray sums
        all_sums = []
        
        # Generate all possible subarrays and calculate their sums
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += arr[j]
                all_sums.append(curr_sum)
        
        # Sort the sums in descending order
        all_sums.sort(reverse=True)
        
        # Return the k-th largest sum
        return all_sums[k-1]