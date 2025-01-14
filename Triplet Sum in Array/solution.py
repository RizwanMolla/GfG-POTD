class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()
        n = len(arr)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                total = arr[i] + arr[left] + arr[right]
                if total == target:
                    return True
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return False

"""
Summary:
The solution first sorts the array, then iterates through it while using a two-pointer approach to check for triplets that sum to the target. Sorting ensures the two-pointer traversal is efficient, giving the solution a time complexity of O(n²) and space complexity of O(1).
"""