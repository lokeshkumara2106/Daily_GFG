class Solution:
    def largestSubsquare(self, mat):
        # code here
        n=len(mat)
        right=[[0]*n for _ in range(n)]
        down=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n-1,-1,-1):
                if mat[i][j]=='X':
                    right[i][j]=1
                    if j+1<n:
                        right[i][j]+=right[i][j+1]
        for j in range(n):
            for i in range(n-1,-1,-1):
                if mat[i][j]=='X':
                    down[i][j]=1
                    if i+1<n:
                        down[i][j]+=down[i+1][j]
        ans=0
        for i in range(n):
            for j in range(n):
                max_k=min(right[i][j],down[i][j])
                for k in range(max_k,ans,-1):
                    if i+k>n or j+k>n:
                        continue
                    if right[i+k-1][j]<k:
                        continue
                    if down[i][j+k-1]<k:
                        continue
                    ans=k
                    break
        return ans