import math

class Solution:
    def countNumbers(self, n):
        def sieve(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(math.sqrt(limit)) + 1):
                if is_prime[i]:
                    for j in range(i * i, limit + 1, i):
                        is_prime[j] = False
            return [i for i, val in enumerate(is_prime) if val]

        limit = int(n ** 0.5) + 1
        primes = sieve(limit)
        count = 0

        # Case 1: p^8
        for p in primes:
            if p ** 8 <= n:
                count += 1
            else:
                break

        # Case 2: p^2 * q^2 (p ≠ q)
        plen = len(primes)
        for i in range(plen):
            p2 = primes[i] ** 2
            if p2 > n:
                break
            for j in range(i + 1, plen):
                q2 = primes[j] ** 2
                num = p2 * q2
                if num <= n:
                    count += 1
                else:
                    break

        return count
