class Solution:
    def largestSubset(self, arr):
        if not arr:
            return []
        
        n = len(arr)
        arr.sort()  # Sort the array first
        
        # dp[i] represents the length of the longest divisible subset ending at index i
        dp = [1] * n
        # Store the actual subset ending at each index
        subsets = [[arr[i]] for i in range(n)]
        
        max_length = 1
        result = [arr[0]]
        
        # Fill dp array using dynamic programming
        for i in range(1, n):
            for j in range(i):
                # If arr[i] is divisible by arr[j], we can extend the chain
                if arr[i] % arr[j] == 0:
                    new_length = dp[j] + 1
                    if new_length > dp[i]:
                        dp[i] = new_length
                        subsets[i] = subsets[j] + [arr[i]]
                    elif new_length == dp[i]:
                        # Compare lexicographically and choose the greater one
                        new_subset = subsets[j] + [arr[i]]
                        if new_subset > subsets[i]:
                            subsets[i] = new_subset
            
            # Update the result if we found a longer subset
            if dp[i] > max_length:
                max_length = dp[i]
                result = subsets[i]
            elif dp[i] == max_length:
                # If same length, choose lexicographically greater
                if subsets[i] > result:
                    result = subsets[i]
        
        return result