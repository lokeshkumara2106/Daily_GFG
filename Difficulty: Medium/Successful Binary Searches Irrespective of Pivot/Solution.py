class Solution:
    def countAlwaysFound(self, arr):
        n = len(arr)

        # Build suffix minimum array
        suffix_min = [0] * n
        suffix_min[n - 1] = arr[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(arr[i], suffix_min[i + 1])

        prefix_max = float('-inf')
        count = 0

        for i in range(n):
            if (arr[i] > prefix_max and
                (i == n - 1 or arr[i] < suffix_min[i + 1])):
                count += 1

            prefix_max = max(prefix_max, arr[i])

        return count
