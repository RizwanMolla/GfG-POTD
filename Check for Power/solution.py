import math

class Solution:
    def isPower(self, x, y):
        if x == 1:
            return y == 1
        
        res = math.log(y, x)
        return abs(res - round(res)) < 1e-10
