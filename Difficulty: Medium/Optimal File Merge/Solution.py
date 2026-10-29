import heapq
class Solution:
    def minComputation(self, files):
        # code here
        total=0
        l=[]
        for f in files:
            heapq.heappush(l,f)
        while len(l)>1:
            a=heapq.heappop(l)
            b=heapq.heappop(l)
            total+=(a+b)
            heapq.heappush(l,a+b)
        return total
