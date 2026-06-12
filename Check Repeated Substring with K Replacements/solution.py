class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        # code here
        from collections import Counter
        n = len(s)
        q, r = divmod(n, k)
        
        if r:
            return False
            
        freqs = Counter(s[i:i + k] for i in range(0, n, k))
        
        fl = len(freqs)
        
        return fl == 1 or fl == 2 and [1, q - 1] == sorted(freqs.values())