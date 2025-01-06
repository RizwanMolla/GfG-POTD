class Solution:
    def sumClosest(self, arr, target):
        arr.sort()
        n = len(arr)
        if n < 2:
            return []
        
        left, right = 0, n - 1
        closest_sum = float('inf')
        result = []
        
        while left < right:
            current_sum = arr[left] + arr[right]
            diff = abs(current_sum - target)
            
            if diff < abs(closest_sum - target) or (diff == abs(closest_sum - target) and arr[right] - arr[left] > result[1] - result[0]):
                closest_sum = current_sum
                result = [arr[left], arr[right]]
            
            if current_sum < target:
                left += 1
            else:
                right -= 1
                
        return result


"""
Overview:
The algorithm sorts the array and uses the two-pointer technique to find the pair whose sum is closest to the target. If multiple pairs have the same sum difference, the pair with the maximum absolute difference is selected. This ensures O(n log n) complexity due to sorting and O(n) for the two-pointer traversal.
"""