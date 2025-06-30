class Solution():
    def maxMinHeight(self, arr, k, w):
        def canAchieve(h):
            n = len(arr)
            operations = 0
            add = [0] * (n + 1)
            curr_add = 0

            for i in range(n):
                curr_add += add[i]
                current_height = arr[i] + curr_add

                if current_height < h:
                    needed = h - current_height
                    operations += needed
                    if operations > k:
                        return False
                    curr_add += needed
                    if i + w < n:
                        add[i + w] -= needed
            return True

        low = min(arr)
        high = low + k
        answer = low

        while low <= high:
            mid = (low + high) // 2
            if canAchieve(mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        return answer
