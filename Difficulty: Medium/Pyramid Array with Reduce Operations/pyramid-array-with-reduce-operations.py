class Solution:
    def formPyramid(self, arr):
        n = len(arr)

        # Maximum possible height considering the left side
        left = [0] * n
        left[0] = arr[0]

        for i in range(1, n):
            left[i] = min(arr[i], left[i - 1] + 1)

        # Maximum possible height considering the right side
        right = [0] * n
        right[n - 1] = arr[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = min(arr[i], right[i + 1] + 1)

        total = sum(arr)
        max_kept = 0

        for i in range(n):

            # Peak must satisfy:
            # 1. left side heights
            # 2. right side heights
            # 3. enough positions on left
            # 4. enough positions on right
            x = min(
                left[i],
                right[i],
                i + 1,
                n - i
            )

            # Complete pyramid with peak x
            kept = x * x

            max_kept = max(max_kept, kept)

        return total - max_kept