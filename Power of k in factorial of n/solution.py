from collections import defaultdict

class Solution:
    def maxKPower(self, n, k):
        def prime_factors(x):
            factors = defaultdict(int)
            d = 2
            while d * d <= x:
                while x % d == 0:
                    factors[d] += 1
                    x //= d
                d += 1
            if x > 1:
                factors[x] += 1
            return factors

        def count_in_factorial(n, p):
            count = 0
            power = p
            while power <= n:
                count += n // power
                power *= p
            return count

        k_factors = prime_factors(k)
        min_power = float('inf')

        for prime, exp in k_factors.items():
            count = count_in_factorial(n, prime)
            min_power = min(min_power, count // exp)

        return min_power
