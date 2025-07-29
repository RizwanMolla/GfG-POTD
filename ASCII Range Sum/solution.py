class Solution:
    def asciirange(self, s):
        first = {}
        last = {}
        
        # Step 1: Record first and last occurrences
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i  # last will get updated every time
        
        result = []
        
        # Step 2: For each character with different first and last occurrence
        for ch in first:
            if first[ch] != last[ch]:
                start = first[ch] + 1
                end = last[ch]
                ascii_sum = sum(ord(s[i]) for i in range(start, end))
                if ascii_sum > 0:
                    result.append(ascii_sum)
        
        return result
