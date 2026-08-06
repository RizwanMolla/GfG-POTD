class Solution:
    def countMinOperations(self, arr):
        # code here
        def op(n):
            div, inc = 0, 0
            while n > 0:
                if n&1 == 0:
                    n //= 2
                    div += 1
                else:
                    n -= 1
                    inc += 1
            return div, inc
            
        d, ans = 0, 0
        for e in arr:
            div, inc = op(e)
            d = max(d, div)
            ans += inc
        return ans + d