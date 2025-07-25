class Solution:
    def maxCircularSum(self, arr):
        def kadane(nums):
            max_ending = max_so_far = nums[0]
            for num in nums[1:]:
                max_ending = max(num, max_ending + num)
                max_so_far = max(max_so_far, max_ending)
            return max_so_far
        
        def min_kadane(nums):
            min_ending = min_so_far = nums[0]
            for num in nums[1:]:
                min_ending = min(num, min_ending + num)
                min_so_far = min(min_so_far, min_ending)
            return min_so_far

        total_sum = sum(arr)
        max_normal = kadane(arr)
        min_subarray = min_kadane(arr)

        if max_normal < 0:
            return max_normal
        
        return max(max_normal, total_sum - min_subarray)
