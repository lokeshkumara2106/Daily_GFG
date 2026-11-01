class Solution:
    def maximumSubarray(self, arr: list[int]) -> int:
        """ code here """
        normal=arr[0]
        squared=arr[0]**2
        ans=max(normal,squared)
        for num in arr[1:]:
            new_squared=max(num*num, squared+num, normal + num*num)
            new_normal=max(num,normal+num)
            normal=new_normal
            squared=new_squared
            ans=max(ans,normal,squared)
        return ans
