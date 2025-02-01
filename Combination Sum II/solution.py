class Solution:
    def uniqueCombinations(self, arr, target):
        arr.sort()
        result = []
        
        def backtrack(start, path, current_sum):
            if current_sum == target:
                result.append(path.copy())
                return
            for i in range(start, len(arr)):
                if i > start and arr[i] == arr[i - 1]:
                    continue
                if current_sum + arr[i] > target:
                    break
                path.append(arr[i])
                backtrack(i + 1, path, current_sum + arr[i])
                path.pop()
        
        backtrack(0, [], 0)
        return result