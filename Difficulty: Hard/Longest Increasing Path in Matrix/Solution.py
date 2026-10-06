class Solution:
    def longIncPath(self, matrix, n, m):

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        # (value, row, column)
        cells = []

        for i in range(n):
            for j in range(m):
                cells.append((matrix[i][j], i, j))

        # Larger values first
        cells.sort(reverse=True)

        dp = [[1] * m for _ in range(n)]

        answer = 1

        for value, i, j in cells:

            for dx, dy in directions:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < n and 0 <= nj < m:

                    if matrix[ni][nj] > matrix[i][j]:
                        dp[i][j] = max(
                            dp[i][j],
                            1 + dp[ni][nj]
                        )

            answer = max(answer, dp[i][j])

        return answer
