class Solution:
    def power(self, b: float, e: int) -> float:
        if e == 0:
            return 1.0
        if e < 0:
            return 1.0 / self.power(b, -e)
        res = 1.0
        while e > 0:
            if e % 2 == 1:
                res *= b
            b *= b
            e = e // 2
        return res