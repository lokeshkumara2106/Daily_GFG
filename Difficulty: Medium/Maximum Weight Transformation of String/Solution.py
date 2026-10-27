class Solution:
    def getMaxWeight(self, s):
        n = len(s)
        # dp[i] stores the max additional weight obtainable up to index i
        dp = [0] * (n + 1)

        for i in range(n):
            # Option 1: Leave s[i] unpaired
            dp[i + 1] = max(dp[i + 1], dp[i])

            # Option 2: Form a pair with s[i] and s[i+1]
            if i + 1 < n:
                gain = 2 if s[i] != s[i + 1] else 1
                dp[i + 2] = max(dp[i + 2], dp[i] + gain)

        return n + dp[n]
