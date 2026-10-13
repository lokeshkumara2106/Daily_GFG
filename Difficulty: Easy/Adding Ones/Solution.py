class Solution:
    def update(self, n: int, updates: list[int]) -> list[int]:
        arr=[0]*n
        for i in range(len(updates)):
            arr[updates[i]-1]+=1
        for i in range(n):
            if i>0 and arr[i]==0:
                arr[i]=arr[i-1]
            elif i>0 and arr[i]!=0:
                arr[i]+=arr[i-1]
        return arr
