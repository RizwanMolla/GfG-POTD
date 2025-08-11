class Solution:
    def maxSum(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        # 1) Manacher odd-length palindromes: d1[i] = radius count (length = 2*d1[i]-1)
        d1 = [0] * n
        l = 0; r = -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l = i - (k - 1)
                r = i + (k - 1)

        # 2) For each right endpoint j we want minimal center i (i <= j <= i + d1[i]-1).
        # Use DSU next-pointer to assign each j at most once.
        parent_next = list(range(n + 1))  # 0..n, parent_next[n] = n sentinel

        def find_next(x):
            # smallest unassigned index >= x (or n if none)
            while parent_next[x] != x:
                parent_next[x] = parent_next[parent_next[x]]
                x = parent_next[x]
            return x

        def union_next(x, y):
            parent_next[find_next(x)] = find_next(y)

        best_start_center_for_right = [-1] * n
        for i in range(n):
            R = i + d1[i] - 1
            j = find_next(i)
            while j <= R and j < n:
                best_start_center_for_right[j] = i
                union_next(j, j + 1)
                j = find_next(j)

        best_left = [0] * n
        for j in range(n):
            if best_start_center_for_right[j] != -1:
                best_left[j] = 2 * (j - best_start_center_for_right[j]) + 1

        # 3) Symmetrically, for each left endpoint k we want maximal center i (i - d1[i]+1 <= k <= i).
        # Use DSU prev-pointer by mapping indices to 1..n with 0 as sentinel.
        parent_prev = list(range(n + 1))  # indices 0..n, 0 reserved as sentinel (none)

        def find_prev(x):
            # x in 1..n, returns largest unassigned index <= x in 1..n, or 0 if none
            while parent_prev[x] != x and parent_prev[x] != 0:
                parent_prev[x] = parent_prev[parent_prev[x]]
                x = parent_prev[x]
            return parent_prev[x] if parent_prev[x] != 0 else 0

        def union_prev(x, y):
            rx = find_prev(x)
            ry = find_prev(y)
            if rx != 0:
                parent_prev[rx] = ry

        best_center_for_left = [-1] * n
        for i in range(n - 1, -1, -1):
            L = i - (d1[i] - 1)
            j = find_prev(i + 1)  # map index i -> i+1
            while j != 0 and (j - 1) >= L:
                idx = j - 1
                best_center_for_left[idx] = i
                union_prev(j, j - 1)
                j = find_prev(j)

        best_right = [0] * n
        for k in range(n):
            if best_center_for_left[k] != -1:
                best_right[k] = 2 * (best_center_for_left[k] - k) + 1

        # 4) prefix/suffix maxima and check splits
        for i in range(1, n):
            if best_left[i] < best_left[i - 1]:
                best_left[i] = best_left[i - 1]
        for i in range(n - 2, -1, -1):
            if best_right[i] < best_right[i + 1]:
                best_right[i] = best_right[i + 1]

        ans = 0
        for i in range(n - 1):
            ans = max(ans, best_left[i] + best_right[i + 1])
        return ans
