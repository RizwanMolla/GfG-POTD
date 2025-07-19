from collections import defaultdict
from math import factorial

class Solution:
    def vowelCount(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_positions = defaultdict(list)

        for ch in s:
            if ch in vowels:
                vowel_positions[ch].append(ch)

        unique_vowels = list(vowel_positions.keys())
        
        if not unique_vowels:
            return 0

        selection_count = 1
        for v in unique_vowels:
            selection_count *= len(vowel_positions[v])

        permutation_count = factorial(len(unique_vowels))

        return selection_count * permutation_count
