from bisect import bisect_left

def isPossible(arr, target, k):
    n = len(arr)
    if n % 2 == 1:
        # for odd-sized array, consider elements from middle to end
        for i in range(n // 2, n):
            if arr[i] < target:
                k -= target - arr[i]
    else:
        # for even-sized array, handle two middle elements separately
        if arr[n // 2] <= target:
            k -= target - arr[n // 2]
            k -= target - arr[n // 2 - 1]
        else:
            k -= 2 * target - (arr[n // 2] + arr[n // 2 - 1])

        # process remaining elements to the right
        for i in range(n // 2 + 1, n):
            if arr[i] < target:
                k -= target - arr[i]

    return k >= 0


class Solution:
    def maximizeMedian(self, arr, k):
        arr.sort()
        n = len(arr)

        # compute initial median floor if even length
        iniMedian = arr[n // 2]
        if n % 2 == 0:
            iniMedian += arr[n // 2 - 1]
            iniMedian //= 2

        low, high = iniMedian, iniMedian + k
        bestMedian = iniMedian

        # binary search to find maximum achievable median
        while low <= high:
            mid = (low + high) // 2
            if isPossible(arr, mid, k):
                bestMedian = mid
                low = mid + 1
            else:
                high = mid - 1

        return bestMedian
