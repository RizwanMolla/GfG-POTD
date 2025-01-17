from typing import List
class Solution:
    def zeroSumSubmat(self, mat: List[List[int]]) -> int:
        def max_zero_sum_subarray(arr):
            prefix_sum = 0
            prefix_map = {0: -1}
            max_len = 0

            for i, val in enumerate(arr):
                prefix_sum += val
                if prefix_sum in prefix_map:
                    max_len = max(max_len, i - prefix_map[prefix_sum])
                else:
                    prefix_map[prefix_sum] = i

            return max_len

        rows, cols = len(mat), len(mat[0])
        max_area = 0

        for top in range(rows):
            col_sum = [0] * cols
            for bottom in range(top, rows):
                for col in range(cols):
                    col_sum[col] += mat[bottom][col]

                height = bottom - top + 1
                width = max_zero_sum_subarray(col_sum)
                max_area = max(max_area, height * width)

        return max_area
