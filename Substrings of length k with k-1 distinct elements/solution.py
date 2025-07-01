class Solution:
    def substrCount(self, s, k):
        if k > len(s):
            return 0
        
        from collections import defaultdict

        count = 0
        freq = defaultdict(int)
        distinct = 0

        # Initialize the first window
        for i in range(k):
            if freq[s[i]] == 0:
                distinct += 1
            freq[s[i]] += 1
        
        if distinct == k - 1:
            count += 1

        # Slide the window
        for i in range(k, len(s)):
            # Remove the character going out of the window
            left_char = s[i - k]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                distinct -= 1

            # Add the new character coming into the window
            right_char = s[i]
            if freq[right_char] == 0:
                distinct += 1
            freq[right_char] += 1

            if distinct == k - 1:
                count += 1

        return count
