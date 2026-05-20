class Solution:
    def isProduct(self, arr, target):
        seen = set()
        for num in arr:
            if (num and not target % num and (target // num) in seen) or (not num and not target):
                return True
            seen.add(num)
        return False