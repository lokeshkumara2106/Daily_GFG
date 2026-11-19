class Solution:
    def sortIt(self, arr):
        n = len(arr)
        for i in range(n):
            if arr[i]%2:
                arr[i]=-arr[i]
        arr.sort()
        for i in range(n):
            if arr[i]<0:
                arr[i]=-arr[i]
        return arr
