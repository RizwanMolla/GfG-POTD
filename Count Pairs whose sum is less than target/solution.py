class Solution:
    def countPairs(self, arr, target):
        arr.sort()
        count = 0
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] + arr[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count


"""
Overview:
The array is sorted, and two pointers are used to count all pairs whose sum is less than the target. The pointer adjustments minimize redundant calculations, ensuring optimal performance with O(n log n) for sorting and O(n) for traversal.
"""