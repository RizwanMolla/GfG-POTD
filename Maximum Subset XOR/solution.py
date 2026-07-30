class Solution:
    def maxSubsetXOR(self, arr):
        n = len(arr)
        index = 0

        # Step 1 is to Build Linear Basis
        for bit in range(31, -1, -1):
            pivot = -1

            # Step 2 is Finding element with current bit set
            for i in range(index, n):
                if arr[i] & (1 << bit):
                    pivot = i
                    break

            if pivot == -1:
                continue

            # Step 3 to Bring pivot to current position
            arr[index], arr[pivot] = arr[pivot], arr[index]

            # step 4 is to Remove current bit from all other numbers
            for i in range(n):
                if i != index and (arr[i] & (1 << bit)):
                    arr[i] ^= arr[index]

            index += 1

        # final Step: Find maximum XOR
        ans = 0
        for i in range(index):
            ans = max(ans, ans ^ arr[i])

        return ans