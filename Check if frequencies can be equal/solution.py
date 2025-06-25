from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        char_freq = Counter(s)  # Frequency of each character
        freq_count = Counter(char_freq.values())  # Count of those frequencies

        if len(freq_count) == 1:
            return True  # All frequencies already equal

        if len(freq_count) == 2:
            freq1, freq2 = freq_count.keys()
            count1, count2 = freq_count[freq1], freq_count[freq2]

            # Case 1: one character has frequency 1, and appears once => can remove that char
            if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
                return True

            # Case 2: the higher frequency occurs once and is 1 more than the lower frequency
            if abs(freq1 - freq2) == 1:
                if (freq1 > freq2 and count1 == 1) or (freq2 > freq1 and count2 == 1):
                    return True

        return False
