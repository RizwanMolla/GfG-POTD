#User function Template for python3
class Solution:
    def findSubString(self, s):
        # Step 1: Find all unique characters in the string
        unique_chars = set(s)
        n_unique = len(unique_chars)
        
        # Step 2: Initialize variables for sliding window approach
        n = len(s)
        if n <= n_unique:  # If string length is already equal to or less than unique chars
            return n
        
        # Initialize a frequency counter for characters in current window
        freq = {}
        
        # Start with a window size of the entire string
        start = 0
        min_length = n  # Maximum possible window size initially
        count = 0  # Count of unique characters found in current window
        
        # Step 3: Use sliding window technique to find smallest window
        for end in range(n):
            # Add current character to window
            if s[end] not in freq:
                freq[s[end]] = 1
                count += 1
            else:
                freq[s[end]] += 1
            
            # If we found all unique characters, try to minimize the window
            while count == n_unique:
                # Update minimum length if current window is smaller
                min_length = min(min_length, end - start + 1)
                
                # Try to shrink window from left
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                    count -= 1
                start += 1
        
        return min_length