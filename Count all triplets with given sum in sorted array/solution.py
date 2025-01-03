class Solution:
    def countTriplets(self, arr, target):
        count = 0
        n = len(arr)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total_sum = arr[i] + arr[left] + arr[right]

                if total_sum == target:
                    left_val = arr[left]
                    right_val = arr[right]

                    if left_val == right_val:
                        num_left = right - left + 1
                        count += num_left * (num_left - 1) // 2
                        break
                    else:
                        left_count = 1
                        right_count = 1

                        while left + 1 < right and arr[left] == arr[left + 1]:
                            left_count += 1
                            left += 1

                        while right - 1 > left and arr[right] == arr[right - 1]:
                            right_count += 1
                            right -= 1

                        count += left_count * right_count
                        left += 1
                        right -= 1

                elif total_sum < target:
                    left += 1
                else:
                    right -= 1

        return count
