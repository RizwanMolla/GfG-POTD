class Solution:
    def countSubstring(self, s):
        count = 0
        
        char_freq = {}
        
        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        for freq in char_freq.values():
            count += (freq * (freq + 1)) // 2
        
        return count