class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            d = {}

            for j in range(i, n):
                d[s[j]] = d.get(s[j], 0) + 1

                maxi = max(d.values())
                mini = min(d.values())

                count += maxi - mini

        return count
