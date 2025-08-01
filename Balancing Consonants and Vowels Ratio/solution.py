from collections import defaultdict

class Solution:
    def countBalanced(self, arr):
        def get_balance(s):
            vowels = set('aeiou')
            return sum(1 if c in vowels else -1 for c in s)

        prefix_sum = 0
        count_map = defaultdict(int)
        count_map[0] = 1  # Base case: zero balance at start
        result = 0

        for s in arr:
            prefix_sum += get_balance(s)
            result += count_map[prefix_sum]
            count_map[prefix_sum] += 1

        return result
