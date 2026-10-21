class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        mini=arr[0]
        prev=arr[0]
        for i in range(1,len(arr)):
            curr=min(prev+arr[i],arr[i])
            mini=min(mini,curr)
            prev=curr
        return mini
