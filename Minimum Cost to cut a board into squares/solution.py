class Solution:
    def minCost(self, n: int, m: int, x: list[int], y: list[int]) -> int:
        totalCost = 0
        horizontal_pieces = 1
        vertical_pieces = 1

        # Sort cut costs in descending order
        x.sort(reverse=True)
        y.sort(reverse=True)

        i, j = 0, 0  # pointers

        # Iterate while there are still cuts to be made
        while i < len(x) and j < len(y):
            if x[i] >= y[j]:
                totalCost += x[i] * horizontal_pieces
                vertical_pieces += 1
                i += 1
            else:
                totalCost += y[j] * vertical_pieces
                horizontal_pieces += 1
                j += 1

        # Remaining vertical cuts
        while i < len(x):
            totalCost += x[i] * horizontal_pieces
            vertical_pieces += 1
            i += 1

        # Remaining horizontal cuts
        while j < len(y):
            totalCost += y[j] * vertical_pieces
            horizontal_pieces += 1
            j += 1

        return totalCost
