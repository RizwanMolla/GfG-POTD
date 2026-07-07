class Solution:
    def largestArea(self, n, m, arr):
        blocked_rows = sorted(r for r, c in arr)
        blocked_cols = sorted(c for r, c in arr)

        max_rows = 0
        prev = 0
        for r in blocked_rows:
            max_rows = max(max_rows, r - prev - 1)
            prev = r
        max_rows = max(max_rows, n - prev)

        max_cols = 0
        prev = 0
        for c in blocked_cols:
            max_cols = max(max_cols, c - prev - 1)
            prev = c
        max_cols = max(max_cols, m - prev)

        return max_rows * max_cols
