class Solution:
    def cuts(self, s: str) -> int:
        def isPowerOfFive(binary: str) -> bool:
            if binary[0] == '0':
                return False
            num = int(binary, 2)
            while num % 5 == 0 and num != 0:
                num //= 5
            return num == 1

        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(i):
                if isPowerOfFive(s[j:i]):
                    dp[i] = min(dp[i], dp[j] + 1)

        return -1 if dp[n] == float('inf') else dp[n]
