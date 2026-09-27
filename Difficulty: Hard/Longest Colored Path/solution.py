from collections import defaultdict
class Solution:
    def longestPath(self, s, edges):
        # code here
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dp={}
        def fun(node, parent):
            if (node,parent) in dp:
                return dp[(node,parent)]
            ans = 0
            for nei in graph[node]:
                if nei == parent:
                    continue
                curr = s[nei-1]
                prev = s[node-1]
                if curr == 'R' and prev == 'B':
                    continue
                ans = max(ans, 1 + fun(nei, node))
            dp[(node,parent)]=ans
            return dp[(node,parent)]
        maxi=float('-inf')
        n=len(s)
        for node in range(1,n+1):
            maxi=max(maxi,1+fun(node,-1))
        return maxi
