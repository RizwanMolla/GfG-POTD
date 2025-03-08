class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        start, max_length = 0, 1
        
        def expandAroundCenter(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1
        
        for i in range(len(s)):

            l1, len1 = expandAroundCenter(i, i)

            l2, len2 = expandAroundCenter(i, i + 1)
            
            if len1 > max_length:
                start, max_length = l1, len1
            if len2 > max_length:
                start, max_length = l2, len2
        
        return s[start:start + max_length]