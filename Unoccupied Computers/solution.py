class Solution:
    def solve(self, n, s):
        # code here
        states = [0]*26
        cnt = 0
        enough_compute = lambda states, n: sum(1 for e in states if e == 1) < n
    
        for e in s:
            idx = ord(e) - ord('A')
            if states[idx] == 2:
                continue
            elif states[idx] == 1:
                states[idx] += 1
            else:
                if enough_compute(states, n):
                    states[idx] = 1
                else:
                    states[idx] = 2
                    cnt += 1
        return cnt