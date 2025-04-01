#User function Template for python3

class Solution:
    def largestSwap(self,s):
        #code here
        s = list(s)
        n = len(s)
        
        last_pos = {ch: i for i, ch in enumerate(s)}
        
        for i in range(n):
            for d in range(9, int(s[i]), -1):
                d = str(d)
                if d in last_pos and last_pos[d] > i:
                    s[i], s[last_pos[d]] = s[last_pos[d]], s[i]
                    return "".join(s)
        
        return "".join(s)