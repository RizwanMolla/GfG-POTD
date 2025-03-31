class Solution:
    def maxPartitions(self, s: str) -> int:
        last_seen = {}
        partitions = 0
        start = 0

        for i, char in enumerate(s):
            last_seen[char] = i

        end = 0
        for i, char in enumerate(s):
            end = max(end, last_seen[char])
            if i == end:
                partitions += 1
                start = i + 1

        return partitions