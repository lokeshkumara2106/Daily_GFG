class Solution:
    def largestSumCycle(self, edges):
        n = len(edges)
        visited = [0] * n
        ans = -1

        def dfs(node, path, position):
            nonlocal ans

            visited[node] = 1
            position[node] = len(path)
            path.append(node)

            nei = edges[node]

            if nei != -1:
                if visited[nei] == 0:
                    dfs(nei, path, position)

                elif visited[nei] == 1:
                    # Cycle found
                    start = position[nei]
                    cycle_sum = sum(path[start:])
                    ans = max(ans, cycle_sum)

            # Mark completely processed
            visited[node] = 2

        for i in range(n):
            if visited[i] == 0:
                dfs(i, [], {})

        return ans
