class Solution:
    def find(self, lst, num):
        ans = -1
        low, high = 0, len(lst) - 1

        while low <= high:
            mid = (low + high) // 2
            if lst[mid] >= num:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def minDeletions(self, arr):
        n = len(arr)
        lst = []

        for i in range(n):
            num = arr[i]

            if len(lst) == 0 or lst[-1] < num:
                lst.append(num)
            else:
                idx = self.find(lst, num)
                lst[idx] = num

        return n - len(lst)
