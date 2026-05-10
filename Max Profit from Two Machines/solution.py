class Solution:
    def maxProfit(self, x, y, a, b):
        n = len(a)

        tasks = []
        for i in range(n):
            tasks.append((abs(a[i] - b[i]), i))

        tasks.sort(reverse=True)

        profit = 0

        for _, i in tasks:
            if (a[i] >= b[i] and x > 0) or y == 0:
                profit += a[i]
                x -= 1
            else:
                profit += b[i]
                y -= 1

        return profit