class Solution:
    def splitArray(self, arr, k):
        def canSplit(maxSumAllowed):
            count = 1
            currentSum = 0
            for num in arr:
                if currentSum + num > maxSumAllowed:
                    count += 1
                    currentSum = num
                else:
                    currentSum += num
            return count <= k

        low = max(arr)
        high = sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if canSplit(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
