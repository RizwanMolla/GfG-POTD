from collections import defaultdict

class Solution:
    def sumOfModes(self, arr, k):
        n = len(arr)
        if k > n:
            return 0

        freq = defaultdict(int)         # number -> frequency
        count_map = defaultdict(set)    # frequency -> set of numbers
        max_freq = 0
        result = 0

        def add(x):
            nonlocal max_freq
            f = freq[x]
            if f > 0:
                count_map[f].remove(x)
                if not count_map[f]:
                    del count_map[f]
            freq[x] += 1
            count_map[f+1].add(x)
            max_freq = max(max_freq, f+1)

        def remove(x):
            nonlocal max_freq
            f = freq[x]
            count_map[f].remove(x)
            if not count_map[f]:
                del count_map[f]
                if f == max_freq:
                    max_freq -= 1
            freq[x] -= 1
            if freq[x] > 0:
                count_map[freq[x]].add(x)

        # initialize first window
        for i in range(k):
            add(arr[i])

        # process all windows
        for i in range(k, n+1):
            # pick mode = smallest element in max_freq bucket
            mode = min(count_map[max_freq])
            result += mode

            if i == n:   # last window
                break

            # slide window: remove left, add right
            remove(arr[i-k])
            add(arr[i])

        return result
