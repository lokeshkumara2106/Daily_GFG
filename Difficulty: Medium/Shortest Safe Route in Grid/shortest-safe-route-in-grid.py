from collections import deque
class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Mark safe cells
        safe = [[True] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    safe[i][j] = False

                    for dr, dc in directions:
                        nr = i + dr
                        nc = j + dc

                        if 0 <= nr < n and 0 <= nc < m:
                            safe[nr][nc] = False

        # BFS
        q = deque()
        visited = [[False] * m for _ in range(n)]

        # Start from every safe cell in the first column
        for i in range(n):
            if safe[i][0]:
                q.append((i, 0, 1))  # distance starts at 1
                visited[i][0] = True

        while q:
            r, c, dist = q.popleft()

            # Reached last column
            if c == m - 1:
                return dist

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < n and
                    0 <= nc < m and
                    safe[nr][nc] and
                    not visited[nr][nc]):

                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))

        return -1

