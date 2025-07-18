import math

class Solution:
    def lcmTriplets(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        
        if n % 2 != 0:
            return n * (n - 1) * (n - 2)
        
        if n % 3 == 0:
            return (n - 1) * (n - 2) * (n - 3)
        else:
            return n * (n - 1) * (n - 3)