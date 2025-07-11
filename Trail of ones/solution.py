class Solution:
    def countConsec(self, n: int) -> int:
        if n < 2:
            return 0
        
        a = [0] * (n + 1)
        b = [0] * (n + 1)
        
        a[1] = 1  # "0"
        b[1] = 1  # "1"
        
        for i in range(2, n + 1):
            a[i] = a[i - 1] + b[i - 1]
            b[i] = a[i - 1]
        
        no_consec = a[n] + b[n]
        
        # Total binary strings of length n
        total = 2 ** n
        
        return total - no_consec
