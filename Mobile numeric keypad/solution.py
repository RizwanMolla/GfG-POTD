class Solution:
    def getCount(self, n: int) -> int:
        if n == 1:
            return 10
        
        # Keypad layout
        neighbors = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }
        
        # Initialize dp table
        dp = [[0] * (n + 1) for _ in range(10)]
        
        # Base case: length 1, each digit has 1 sequence
        for digit in range(10):
            dp[digit][1] = 1
        
        # Fill the table for lengths 2 to n
        for length in range(2, n + 1):
            for digit in range(10):
                for neighbor in neighbors[digit]:
                    dp[digit][length] += dp[neighbor][length - 1]
        
        # Total sequences of length n from all starting digits
        return sum(dp[d][n] for d in range(10))
