class Solution:
    def combinationSum(self, arr, target):
        arr.sort()
        result = []
        
        def backtrack(start, path, current_sum):
            if current_sum == target:
                result.append(path.copy())
                return
            for i in range(start, len(arr)):
                if current_sum + arr[i] > target:
                    break
                path.append(arr[i])
                backtrack(i, path, current_sum + arr[i])
                path.pop()
        
        backtrack(0, [], 0)
        return result