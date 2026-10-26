class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        n = len(arr)

        if k == 0:
            return max(arr) - min(arr)

        prefix_min = [0] * n
        prefix_max = [0] * n
        suffix_min = [0] * n
        suffix_max = [0] * n

        # Prefix minimum and maximum
        prefix_min[0] = prefix_max[0] = arr[0]

        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], arr[i])
            prefix_max[i] = max(prefix_max[i - 1], arr[i])

        # Suffix minimum and maximum
        suffix_min[n - 1] = suffix_max[n - 1] = arr[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])
            suffix_max[i] = max(suffix_max[i + 1], arr[i])

        ans = float('inf')

        # Try removing each subarray of size k
        for i in range(n - k + 1):
            left = i - 1
            right = i + k

            mn = float('inf')
            mx = float('-inf')

            # Remaining elements on the left
            if left >= 0:
                mn = min(mn, prefix_min[left])
                mx = max(mx, prefix_max[left])

            # Remaining elements on the right
            if right < n:
                mn = min(mn, suffix_min[right])
                mx = max(mx, suffix_max[right])

            ans = min(ans, mx - mn)

        return ans
