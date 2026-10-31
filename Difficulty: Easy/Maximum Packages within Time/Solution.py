class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        # code here
        maxi=0
        n=len(arr)
        total=0
        left=0
        for right in range(n):
            total+=arr[right]
            while right-left+1>totalTime:
                total-=arr[left]
                left+=1
            maxi=max(maxi,total)
        return maxi
