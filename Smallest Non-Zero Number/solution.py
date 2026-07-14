import math

class Solution:
    def find(self, arr):
        x = 0
        for i in arr[::-1]:
            x = math.ceil((x + i) / 2)
        return x