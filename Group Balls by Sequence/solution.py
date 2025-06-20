from collections import Counter

class Solution:
    def validgroup(self, arr, k):
        if len(arr) % k != 0:
            return False  # Cannot divide into equal groups of size k
        
        count = Counter(arr)
        for num in sorted(count):
            if count[num] > 0:
                freq = count[num]
                for i in range(num, num + k):
                    if count[i] < freq:
                        return False  # Not enough of i to form a group
                    count[i] -= freq  # Use up `freq` number of each
        return True
