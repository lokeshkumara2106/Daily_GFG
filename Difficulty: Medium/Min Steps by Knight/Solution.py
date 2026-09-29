from collections import deque

class Solution:
    def minStepToReachTarget(
        self,
        knightPos: list[int],
        targetPos: list[int],
        n: int
    ) -> int:

        directions = [
            (-2, -1), (-1, -2),
            (1, -2), (2, -1),
            (2, 1), (1, 2),
            (-2, 1), (-1, 2)
        ]

        sx, sy = knightPos
        tx, ty = targetPos

        if [sx, sy] == [tx, ty]:
            return 0

        q = deque([(sx, sy, 0)])
        visited = {(sx, sy)}

        while q:
            x, y, steps = q.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                # 1-based board
                if 1 <= nx <= n and 1 <= ny <= n:

                    if (nx, ny) == (tx, ty):
                        return steps + 1

                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny, steps + 1))

        return -1
