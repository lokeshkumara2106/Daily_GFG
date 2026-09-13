class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        n = len(adj)
        def bfs(start):
            dist = [-1] * n
            dist[start] = 0
            q = deque([start])
            farthest = start
            while q:
                node = q.popleft()
                if dist[node] > dist[farthest]:
                    farthest = node
                for neighbor in adj[node]:
                    neighbor -= 1  # houses are numbered 1...n
                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[node] + 1
                        q.append(neighbor)
            return farthest, dist[farthest]
        # First BFS: find one endpoint of the diameter
        farthest_node, _ = bfs(0)

        # Second BFS: find the diameter length
        _, diameter = bfs(farthest_node)

        # Minimum possible maximum distance
        return (diameter + 1) // 2