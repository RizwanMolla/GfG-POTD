class Solution:
    def farMin(self, arr):
        n = len(arr)
        if n == 0:
            return []

        min_idx_suffix = [0] * n
        min_idx_suffix[n-1] = n-1
        for i in range(n-2, -1, -1):
            if arr[i] <= arr[min_idx_suffix[i+1]]:
                min_idx_suffix[i] = i
            else:
                min_idx_suffix[i] = min_idx_suffix[i+1]

        ans = [-1] * n
        for i in range(n):
            j = i + 1
            current_ans = -1
            while j < n:
                k = min_idx_suffix[j]
                if arr[k] < arr[i]:
                    current_ans = k
                    j = k + 1
                else:
                    j = k + 1
                    break
            ans[i] = current_ans

        return ans