import math

class Solution:
    def smallestDivisor(self, arr, k):
        left, right = 1, max(arr)
        result = right  # initialize with max possible value

        while left <= right:
            mid = (left + right) // 2
            total = sum(math.ceil(num / mid) for num in arr)

            if total <= k:
                result = mid  # mid is a valid divisor, try smaller
                right = mid - 1
            else:
                left = mid + 1  # mid too small, try bigger

        return result
