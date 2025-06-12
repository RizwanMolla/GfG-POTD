class Solution:
    def printKClosest(self, arr, k, x):
        filtered = [a for a in arr if a != x]
        sorted_by_closeness = sorted(filtered, key=lambda a: (abs(a - x), -a))
        result = sorted_by_closeness[:k]
        return result
