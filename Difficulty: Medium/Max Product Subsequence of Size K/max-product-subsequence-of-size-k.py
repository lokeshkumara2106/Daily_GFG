class Solution:
    def maxProduct(self, arr: list[int], k: int) -> int:
        # code here
        n=len(arr)
        arr.sort()
        maxii=float('-inf')
        for i in range(k+1):
            val=1
            for j in range(i):
                val*=arr[j]
            for j in range(n-1,n-(k-i)-1,-1):
                val*=arr[j]
            maxii=max(maxii,val)
        return maxii