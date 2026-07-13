from math import gcd

class Solution:
    def minOperations(self, permutation):
        MOD = 10**9 + 7
        size = len(permutation)

        seen = [False] * size
        answer_lcm = 1

        for start in range(size):
            if seen[start]:
                continue

            current = start
            cycle_length = 0

            while not seen[current]:
                seen[current] = True
                current = permutation[current] - 1
                cycle_length += 1

            answer_lcm = (answer_lcm * cycle_length) // gcd(answer_lcm, cycle_length)

        return answer_lcm % MOD