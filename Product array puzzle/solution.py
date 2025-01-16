class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        res = [1] * n
        left = 1
        for i in range(n):
            res[i] = left
            left *= arr[i]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= arr[i]
        return res

"""
Overview: The solution uses two passes to calculate the result efficiently without division. In the first pass, it computes the product of all elements to the left of each index and stores it in the result array. In the second pass, it multiplies the result array with the product of all elements to the right of each index. This approach ensures O(n) time complexity and O(1) extra space complexity (excluding the result array).
"""