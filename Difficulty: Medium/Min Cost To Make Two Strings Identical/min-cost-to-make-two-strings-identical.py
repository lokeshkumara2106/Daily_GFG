class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        # code here
        dp={}
        def fun(i,j):
            if i == len(s1):
                return (len(s2) - j) * costS2
            if j == len(s2):
                return (len(s1) - i) * costS1
            if (i,j) in dp:
                return dp[(i,j)]
            if s1[i]==s2[j]:
                return fun(i+1,j+1)
            delete_s1 = costS1 + fun(i + 1, j)
            delete_s2 = costS2 + fun(i, j + 1)
            dp[(i,j)] =min(delete_s1,delete_s2)
            return dp[(i,j)]
        # return fun(0,0)
        m=len(s1)
        n=len(s2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for j in range(n+1):
            dp[m][j]=(n-j)*costS2
        for i in range(m+1):
            dp[i][n]=(m-i)*costS1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s1[i]==s2[j]:
                    dp[i][j]= dp[i+1][j+1]
                    continue
                delete_s1 = costS1 + dp[i + 1][j]
                delete_s2 = costS2 + dp[i][j + 1]
                dp[i][j] =min(delete_s1,delete_s2)
        return dp[0][0]