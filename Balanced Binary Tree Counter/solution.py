class Solution:
    def countBT(self, h: int) -> int:
        MODULO = 10 ** 9 + 7
        a = b = 1
        for _ in range(h - 1):
            a, b = b, b * (2 * a + b) % MODULO
        return b