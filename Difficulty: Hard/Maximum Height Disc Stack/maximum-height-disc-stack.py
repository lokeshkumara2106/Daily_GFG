# class Solution:
#     def maxStackHeight(self, r, h):
#         n=len(r)
#         arr=sorted([r[i],h[i]] for i in range(len(h)))
#         dp=[[0]*(n+1) for _ in range(n+1)]
#         for ind in range(n-1,-1,-1):
#             for prev in range(n-1,-2,-1):
#                 take=0
#                 if prev!=-1:
#                     prad,phei=arr[prev]
#                 crad,chei=arr[ind]
#                 if prev==-1 or (crad>prad and chei>phei):
#                     take+=chei+dp[ind+1][ind+1]
#                 nott=dp[ind+1][prev+1]
#                 dp[ind][prev+1]= max(take,nott)
#         return dp[0][0]
class Solution:
    def maxStackHeight(self, r, h):
        n = len(r)
        discs = sorted(zip(r, h))

        vals = sorted(set(h))
        rank = {x: i + 1 for i, x in enumerate(vals)}

        bit = [0] * (len(vals) + 1)

        def query(i):
            res = 0
            while i > 0:
                res = max(res, bit[i])
                i -= i & -i
            return res

        def update(i, value):
            while i < len(bit):
                bit[i] = max(bit[i], value)
                i += i & -i

        ans = 0
        i = 0

        while i < n:
            j = i

            while j < n and discs[j][0] == discs[i][0]:
                j += 1

            temp = []

            for k in range(i, j):
                radius, height = discs[k]
                pos = rank[height]

                best = query(pos - 1) + height
                temp.append((pos, best))
                ans = max(ans, best)

            for pos, best in temp:
                update(pos, best)

            i = j

        return ans

