class Solution:
    def insertInterval(self, intervals, newInterval):
        res = []
        i = 0
        n = len(intervals)
        newStart, newEnd = newInterval

        while i < n and intervals[i][1] < newStart:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newEnd:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i += 1
        res.append([newStart, newEnd])

        while i < n:
            res.append(intervals[i])
            i += 1

        return res
