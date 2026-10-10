class Solution:
    def minOperation(self, n):
        return n.bit_length() + n.bit_count() - 1