class Solution:
    def findKthSmall(self, arr, k):
        # code here
        n=len(arr)
        arr.sort()
        for i in range(n):
            missing=arr[i]-(i+1)
            if missing>=k:
                return arr[i]-(missing-k+1)
        return arr[-1]+(k-(arr[-1]-n))
