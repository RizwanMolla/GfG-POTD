import math

class Solution:
    def cntCoprime(self, arr):
        actual_max_val = 0
        if arr:
            actual_max_val = max(arr)
        
        current_max_val_for_arrays = actual_max_val 
        
        if current_max_val_for_arrays == 0 and len(arr) > 0:
             current_max_val_for_arrays = 1


        mu = [0] * (current_max_val_for_arrays + 1)
        min_prime_factor = [0] * (current_max_val_for_arrays + 1)
        
        primes = []

        mu[1] = 1
        for i in range(2, current_max_val_for_arrays + 1):
            if min_prime_factor[i] == 0:
                min_prime_factor[i] = i
                primes.append(i)
                mu[i] = -1
            
            for p in primes:
                if p > min_prime_factor[i] or i * p > current_max_val_for_arrays:
                    break
                min_prime_factor[i * p] = p
                if p == min_prime_factor[i]:
                    mu[i * p] = 0
                else:
                    mu[i * p] = -mu[i]

        freq = [0] * (current_max_val_for_arrays + 1)
        for x in arr:
            if x <= current_max_val_for_arrays:
                freq[x] += 1

        cnt_divisible = [0] * (current_max_val_for_arrays + 1)
        for d in range(1, current_max_val_for_arrays + 1):
            for multiple in range(d, current_max_val_for_arrays + 1, d):
                cnt_divisible[d] += freq[multiple]

        total_coprime_pairs = 0
        for d in range(1, current_max_val_for_arrays + 1):
            if mu[d] == 0:
                continue
            
            k = cnt_divisible[d]
            if k >= 2:
                pairs_divisible_by_d = k * (k - 1) // 2
                total_coprime_pairs += mu[d] * pairs_divisible_by_d
        
        return total_coprime_pairs