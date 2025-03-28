class Solution:
    def eggDrop(self, n: int, k: int) -> int:
        dp = {}

        def solve(e, f):
            if f == 0 or f == 1:
                return f
            if e == 1:
                return f
            if (e, f) in dp:
                return dp[(e, f)]
            
            low, high, ans = 1, f, float('inf')
            while low <= high:
                mid = (low + high) // 2
                break_case = solve(e - 1, mid - 1)
                survive_case = solve(e, f - mid)
                worst = 1 + max(break_case, survive_case)
                
                if break_case > survive_case:
                    high = mid - 1
                else:
                    low = mid + 1

                ans = min(ans, worst)
            
            dp[(e, f)] = ans
            return ans
        
        return solve(n, k)
