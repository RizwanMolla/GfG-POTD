#User function Template for python3
class Solution:
    def countWays(self, digits: str) -> int:
        if not digits or digits[0] == '0':
            return 0

        prev2, prev1 = 1, 1  

        for i in range(1, len(digits)):
            curr = 0  

            if digits[i] != '0':
                curr += prev1  

            two_digit = int(digits[i-1:i+1]) 
            if 10 <= two_digit <= 26:
                curr += prev2  

            prev2, prev1 = prev1, curr

        return prev1