from collections import defaultdict
class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        # code here
        n=len(adj)
        res=set()
        graph=defaultdict(list)
        for u in range(n):
            for v in adj[u]:
                x,y=u,v
                if x>y:
                    x,y=y,x
                res.add((x,y))
        return len(res)
