#User function Template for python3
class Solution:
    def subsets(self, arr):
        res = []
        arr.sort()

        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(arr)):
                path.append(arr[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res