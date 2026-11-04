class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        n = len(s)
        # Store the day on which each index becomes '?'
        days = [float('inf')] * n
        for i, idx in enumerate(p):
            days[idx] = i + 1
        def check(mid):
            for i in range(n - 1):
                if (s[i] == s[i+1]
                    and days[i] > mid
                    and days[i+1] > mid):
                    return False
            return True
        if check(0):
            return 0
        low = 1
        high = len(p)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
