class Solution:
    def subarrayXor(self, arr):
        # code here 
        ans=0
        n=len(arr)
        if n%2==0:
            return 0
        for i in range(0,n,2):
            ans^=arr[i]
        return ans
