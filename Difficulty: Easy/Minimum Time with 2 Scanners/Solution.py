class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        # code here
        res=float('inf')
        for i in range(n+1):
            time=max(i*s1,(n-i)*s2)
            res=min(res, time)
        return res
