class Solution:
    def lexicographicallySmallest(self, s, k):
        n = len(s)
        
        # Correct power-of-2 check with proper parentheses
        if (n & (n - 1)) == 0:
            k = k // 2
        else:
            k = k * 2
        
        # If k >= n, impossible to have non-empty result
        if k >= n:
            return "-1"
        
        stack = []
        
        # Build lexicographically smallest string using stack
        for ele in s:
            while stack and k > 0 and stack[-1] > ele:
                stack.pop()
                k -= 1
            stack.append(ele)
        
        # Remove remaining characters from end if k > 0
        while k > 0:
            stack.pop()
            k -= 1
        
        # Return -1 if result is empty, otherwise return the string
        return ''.join(stack) if stack else "-1"   