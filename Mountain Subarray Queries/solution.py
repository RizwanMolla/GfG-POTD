class Solution:
    def processQueries(self, nums, queries):
        size = len(nums)

        right_end = [0] * size
        left_start = [0] * size

        idx = size - 1
        right_end[idx] = idx

        for idx in range(size - 2, -1, -1):
            if nums[idx] <= nums[idx + 1]:
                right_end[idx] = right_end[idx + 1]
            else:
                right_end[idx] = idx

        left_start[0] = 0

        for idx in range(1, size):
            if nums[idx] <= nums[idx - 1]:
                left_start[idx] = left_start[idx - 1]
            else:
                left_start[idx] = idx

        result = []

        for start, end in queries:
            if right_end[start] >= left_start[end]:
                result.append(True)
            else:
                result.append(False)

        return result