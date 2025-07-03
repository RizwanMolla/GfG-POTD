class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        if n == 0 or k == 0:
            return -1

        char_count = {}
        max_len = -1
        start = 0

        for end in range(n):
            # Add character to dictionary
            char_count[s[end]] = char_count.get(s[end], 0) + 1

            # Shrink window until we have at most k unique characters
            while len(char_count) > k:
                char_count[s[start]] -= 1
                if char_count[s[start]] == 0:
                    del char_count[s[start]]
                start += 1

            # Check if window has exactly k unique characters
            if len(char_count) == k:
                max_len = max(max_len, end - start + 1)

        return max_len
