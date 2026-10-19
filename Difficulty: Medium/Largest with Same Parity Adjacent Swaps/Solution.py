class Solution:
    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        # code here
        n=len(arr)
        i=0
        while i<n:
            j=i
            while j<n and arr[j]%2==arr[i]%2:
                j+=1
            arr[i:j]=sorted(arr[i:j],reverse=True)
            i=j
        return arr
        # while True:
        #     found=False
        #     for i in range(n-1,0,-1):
        #         if arr[i]>arr[i-1] and (arr[i-1]+arr[i])%2==0:
        #             arr[i],arr[i-1]=arr[i-1],arr[i]
        #             found=True
        #     if not found:
        #         break
        # return arr
        
