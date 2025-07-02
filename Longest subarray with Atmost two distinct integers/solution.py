class Solution:
    def totalElements(self, arr):
        from collections import defaultdict
        
        left = 0
        max_len = 0
        count = defaultdict(int)
        
        for right in range(len(arr)):
            count[arr[right]] += 1

            # Shrink the window if more than 2 distinct integers
            while len(count) > 2:
                count[arr[left]] -= 1
                if count[arr[left]] == 0:
                    del count[arr[left]]
                left += 1

            # Update the maximum length
            max_len = max(max_len, right - left + 1)

        return max_len
