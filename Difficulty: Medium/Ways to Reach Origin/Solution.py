class Solution:
    def ways(self, x: int, y: int) -> int:
        endx = x
        endy = y
        dp = {}
        MOD = 10**9 + 7

        def fun(x, y):
            if x == 0 and y == 0:
                return 1

            if (x, y) in dp:
                return dp[(x, y)]

            ans = 0

            for dx, dy in [(-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx <= endx and 0 <= ny <= endy:
                    ans = (ans + fun(nx, ny)) % MOD

            dp[(x, y)] = ans
            return ans

        # return fun(x, y)
        dp = [[0] * (y + 1) for _ in range(x + 1)]

        dp[0][0] = 1

        # First column
        for i in range(1, x + 1):
            dp[i][0] = 1

        # First row
        for j in range(1, y + 1):
            dp[0][j] = 1

        # Remaining cells
        for i in range(1, x + 1):
            for j in range(1, y + 1):
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1])%MOD

        return dp[x][y]
