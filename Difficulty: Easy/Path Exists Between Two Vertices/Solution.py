from collections import defaultdict
class Solution:
    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:
        graph=defaultdict(list)
        for x in range(len(adj)):
            for y in adj[x]:
                graph[x].append(y)
                graph[y].append(x)
        def dfs(u, graph, visited):
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v, graph, visited)
        visited = set()
        dfs(u, graph, visited)
        return v in visited
