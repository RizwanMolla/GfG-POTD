class Solution:
    def balancePan(self, a, b):
        if a == 2:
            return True
        while b:
            r = b % a
            if r == 0 or r == 1:
                b //= a
            elif r == a - 1:
                b = (b + 1) // a
            else:
                return False
        return True