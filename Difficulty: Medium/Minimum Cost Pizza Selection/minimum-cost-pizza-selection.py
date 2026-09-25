class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        # code here
        INF = float('inf')

        # We only need to consider areas up to x + l - 1,
        # because adding one large pizza can take us past x.
        dp = [INF] * (x + l)
        dp[0] = 0

        for area in range(1, x + l):
            if area >= s:
                dp[area] = min(dp[area], dp[area - s] + cs)

            if area >= m:
                dp[area] = min(dp[area], dp[area - m] + cm)

            if area >= l:
                dp[area] = min(dp[area], dp[area - l] + cl)

        return min(dp[x:])