class Solution:
    def smallestSubWithSum(self, arr, x):
        # code here 
        left=0
        total=0
        maxii=float('inf')
        for right in range(len(arr)):
            total+=arr[right]
            while total>x:
                maxii=min(maxii,right-left+1)
                total-=arr[left]
                left+=1
        return maxii if maxii!=float('inf') else 0
