class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        # code here
        arr.sort()
        count = start = 0
        for end in range(1, len(arr)):
            while arr[end] - arr[start] >= k:
                start += 1
            count += end - start
        return count