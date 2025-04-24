#User function Template for python3
class Solution:
    def getSingle(self, arr):
        ones, twos = 0, 0
        for num in arr:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones