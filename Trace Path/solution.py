class Solution:
    def isPossible(self, n: int, m: int, s: str) -> bool:
        # code here
        mx_r = 0
        mn_r = 0
        mx_c = 0
        mn_c = 0

        curr_x = 0
        curr_y = 0
        for i in s:
            if i == 'L':
                curr_y -= 1
            elif i == 'R':
                curr_y += 1
            elif i == 'D':
                curr_x -= 1
            else:
                curr_x += 1

            mx_r = max(mx_r, curr_x)
            mn_r = min(mn_r, curr_x)
            mx_c = max(mx_c, curr_y)
            mn_c = min(mn_c, curr_y)

        pn = mx_r - mn_r + 1
        pm = mx_c - mn_c + 1

        return pn <= n and pm <= m