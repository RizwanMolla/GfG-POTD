class Solution:
    def prefixStrings(self, n: int) -> int:
        
        MOD = 10**9 + 7
    
        fact = [1] * (2 * n + 1)
        for i in range(1, 2 * n + 1):
            fact[i] = fact[i - 1] * i % MOD
    
        inv_fact_n = pow(fact[n], MOD - 2, MOD)
    
        comb = fact[2 * n] * inv_fact_n % MOD
        comb = comb * inv_fact_n % MOD
    
        ans = comb * pow(n + 1, MOD - 2, MOD) % MOD
    
        return ans