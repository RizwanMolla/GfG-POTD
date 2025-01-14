class Solution:
    def closest3Sum(self, arr, target):
        arr.sort()
        n = len(arr)
        closest_sum = float('-inf')
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                if abs(current_sum - target) < abs(closest_sum - target) or (abs(current_sum - target) == abs(closest_sum - target) and current_sum > closest_sum):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        return closest_sum

"""
Summary:
The solution uses sorting and a two-pointer approach to efficiently find the closest sum to the target. By comparing both absolute differences and sum values, it ensures the maximum closest sum is returned in case of ties. The time complexity is O(n²), and the space complexity is O(1).
"""