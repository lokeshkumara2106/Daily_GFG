class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        # code here
        n = len(arr)
        mid = n // 2

        left = sorted(arr[:mid])
        right = sorted(arr[mid:])

        ans = 0
        j = 0

        for x in left:
            while j < mid and 5 * right[j] <= x:
                j += 1

            ans += j

        return ans