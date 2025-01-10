class Solution:
    def countDistinct(self, arr, k):
        from collections import defaultdict
        result = []
        freq_map = defaultdict(int)
        distinct_count = 0

        for i in range(k):
            if freq_map[arr[i]] == 0:
                distinct_count += 1
            freq_map[arr[i]] += 1

        result.append(distinct_count)

        for i in range(k, len(arr)):
            start_element = arr[i - k]
            freq_map[start_element] -= 1
            if freq_map[start_element] == 0:
                distinct_count -= 1

            new_element = arr[i]
            if freq_map[new_element] == 0:
                distinct_count += 1
            freq_map[new_element] += 1

            result.append(distinct_count)

        return result
