class Solution:
    def maximumWeight(self, n, edges, queries):
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            pu = find(u)
            pv = find(v)

            if pu == pv:
                return 0

            # Number of new paths formed between the components
            paths = size[pu] * size[pv]

            # Union by size
            if size[pu] < size[pv]:
                pu, pv = pv, pu

            parent[pv] = pu
            size[pu] += size[pv]

            return paths

        # Sort edges by weight
        edges.sort(key=lambda x: x[2])

        # Sort queries while preserving their original indices
        sorted_queries = sorted(
            [(q, i) for i, q in enumerate(queries)]
        )

        ans = [0] * len(queries)
        total = 0
        j = 0

        for q, idx in sorted_queries:
            while j < len(edges) and edges[j][2] <= q:
                u, v, w = edges[j]
                total += union(u, v)
                j += 1

            ans[idx] = total

        return ans
