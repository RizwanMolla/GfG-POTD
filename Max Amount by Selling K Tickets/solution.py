import heapq

class Solution:
    def maxAmount(self, arr, k):
        MOD = 10**9 + 7

        # Max heap using negative values
        heap = [-x for x in arr]
        heapq.heapify(heap)

        ans = 0

        while k > 0 and heap:
            cur = -heapq.heappop(heap)
            ans = (ans + cur) % MOD

            if cur > 1:
                heapq.heappush(heap, -(cur - 1))

            k -= 1

        return ans