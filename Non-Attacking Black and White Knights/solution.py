class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        total_squares = n * m

        total_ways = total_squares * (total_squares - 1)

        attacking = 4 * (
            (n - 1) * max(0, m - 2) +
            (n - 2) * max(0, m - 1)
        )

        return total_ways - attacking