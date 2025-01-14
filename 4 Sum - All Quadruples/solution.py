class Solution:
    def fourSum(self, arr, target):
        arr.sort()
        n = len(arr)
        quadruples = []
        
        for i in range(n - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]
                    if total == target:
                        quadruples.append([arr[i], arr[j], arr[left], arr[right]])
                        while left < right and arr[left] == arr[left + 1]:
                            left += 1
                        while left < right and arr[right] == arr[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruples


"""
Summary:
The solution sorts the array and uses two nested loops combined with a two-pointer technique to efficiently find all unique quadruples that sum up to the target. Duplicate quadruples are avoided by skipping repeated elements during iteration. The time complexity is O(n³), and the space complexity is O(1) (excluding the output list).
"""