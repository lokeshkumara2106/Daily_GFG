from collections import deque
class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:
        # code here
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            # Original direction: cost 0
            graph[u].append((v, 0))

            # Reverse direction: cost 1
            graph[v].append((u, 1))

        dist = [float('inf')] * (n + 1)
        dist[src] = 0

        dq = deque([src])

        while dq:

            node = dq.popleft()

            for nei, cost in graph[node]:

                if dist[node] + cost < dist[nei]:

                    dist[nei] = dist[node] + cost

                    if cost == 0:
                        dq.appendleft(nei)
                    else:
                        dq.append(nei)

        if dist[dst] == float('inf'):
            return -1

        return dist[dst]