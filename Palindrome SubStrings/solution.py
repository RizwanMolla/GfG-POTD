#User function Template for python3
class Solution:
    def countPS(self, s: str) -> int:
        def countPalindromes(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= 2:
                    count += 1
                l -= 1
                r += 1
            return count
        
        n = len(s)
        total_count = 0
        
        for i in range(n):
            total_count += countPalindromes(i, i)
            total_count += countPalindromes(i, i+1)
        
        return total_count