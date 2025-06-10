class Solution:
    def countStrings(self, s):
        """
        Ultra-optimized O(n) solution.
        """
        from collections import defaultdict
        
        # Count character frequencies and positions
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)
        
        chars = list(pos.keys())
        result = 0
        
        # All characters the same
        if len(chars) == 1:
            return 1
        
        # Count pairs of different characters
        for i in range(len(chars)):
            for j in range(i + 1, len(chars)):
                result += len(pos[chars[i]]) * len(pos[chars[j]])
        
        # Add original string if any character repeats
        if any(len(positions) > 1 for positions in pos.values()):
            result += 1
        
        return result